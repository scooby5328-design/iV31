package com.chili.iv31

import android.app.Activity
import android.content.Context
import com.android.billingclient.api.AcknowledgePurchaseParams
import com.android.billingclient.api.BillingClient
import com.android.billingclient.api.BillingClientStateListener
import com.android.billingclient.api.BillingFlowParams
import com.android.billingclient.api.BillingResult
import com.android.billingclient.api.PendingPurchasesParams
import com.android.billingclient.api.ProductDetails
import com.android.billingclient.api.Purchase
import com.android.billingclient.api.PurchasesUpdatedListener
import com.android.billingclient.api.QueryProductDetailsParams
import com.android.billingclient.api.QueryPurchasesParams

class Billing(
    context: Context,
    private val forcedTier: String?,
    private val onChange: (Boolean, String?) -> Unit,
) : PurchasesUpdatedListener {
    private val prefs = context.getSharedPreferences("iv31", Context.MODE_PRIVATE)
    private val client = BillingClient.newBuilder(context)
        .setListener(this)
        .enablePendingPurchases(PendingPurchasesParams.newBuilder().enableOneTimeProducts().build())
        .enableAutoServiceReconnection()
        .build()
    @Volatile private var details: ProductDetails? = null
    @Volatile private var formattedPrice: String = prefs.getString(KEY_PRICE, "") ?: ""
    @Volatile private var ready = false

    fun isPro(): Boolean = when (forcedTier) {
        "pro" -> true
        "free" -> false
        else -> prefs.getBoolean(KEY_PRO, false)
    }

    fun price(): String = formattedPrice

    fun start() {
        client.startConnection(object : BillingClientStateListener {
            override fun onBillingSetupFinished(result: BillingResult) {
                if (result.responseCode != BillingClient.BillingResponseCode.OK) return
                ready = true
                loadDetails()
                checkOwned(null)
            }

            override fun onBillingServiceDisconnected() {
                ready = false
            }
        })
    }

    fun refresh() {
        if (ready) checkOwned(null)
    }

    fun restore() {
        if (!ready) {
            onChange(isPro(), "Couldn't reach Google Play. Check your connection and try again.")
            return
        }
        checkOwned { owned -> onChange(owned, if (owned) "Purchase restored. iv31 Full is unlocked." else "No iv31 Full purchase was found on this Google account.") }
    }

    fun buy(activity: Activity) {
        val product = details
        if (!ready || product == null) {
            onChange(isPro(), "Google Play isn't ready yet. Check your connection and try again.")
            if (ready) loadDetails()
            return
        }
        val params = BillingFlowParams.newBuilder()
            .setProductDetailsParamsList(
                listOf(BillingFlowParams.ProductDetailsParams.newBuilder().setProductDetails(product).build())
            )
            .build()
        client.launchBillingFlow(activity, params)
    }

    fun end() = client.endConnection()

    private fun loadDetails() {
        val params = QueryProductDetailsParams.newBuilder()
            .setProductList(
                listOf(
                    QueryProductDetailsParams.Product.newBuilder()
                        .setProductId(PRODUCT_ID)
                        .setProductType(BillingClient.ProductType.INAPP)
                        .build()
                )
            )
            .build()
        client.queryProductDetailsAsync(params) { result, productResult ->
            if (result.responseCode != BillingClient.BillingResponseCode.OK) return@queryProductDetailsAsync
            val product = productResult.productDetailsList.firstOrNull { it.productId == PRODUCT_ID } ?: return@queryProductDetailsAsync
            details = product
            val price = product.oneTimePurchaseOfferDetails?.formattedPrice ?: ""
            if (price.isNotEmpty() && price != formattedPrice) {
                formattedPrice = price
                prefs.edit().putString(KEY_PRICE, price).apply()
                onChange(isPro(), null)
            }
        }
    }

    private fun checkOwned(done: ((Boolean) -> Unit)?) {
        val params = QueryPurchasesParams.newBuilder().setProductType(BillingClient.ProductType.INAPP).build()
        client.queryPurchasesAsync(params) { result, purchases ->
            if (result.responseCode != BillingClient.BillingResponseCode.OK) {
                done?.invoke(isPro())
                return@queryPurchasesAsync
            }
            val owned = purchases.filter { PRODUCT_ID in it.products && it.purchaseState == Purchase.PurchaseState.PURCHASED }
            owned.forEach { acknowledge(it) }
            val was = isPro()
            setPro(owned.isNotEmpty())
            if (done != null) done(isPro()) else if (was != isPro()) onChange(isPro(), null)
        }
    }

    override fun onPurchasesUpdated(result: BillingResult, purchases: MutableList<Purchase>?) {
        when (result.responseCode) {
            BillingClient.BillingResponseCode.OK -> purchases.orEmpty().forEach { handle(it) }
            BillingClient.BillingResponseCode.ITEM_ALREADY_OWNED -> checkOwned { owned ->
                onChange(owned, if (owned) "You already own iv31 Full. It's unlocked." else null)
            }
            BillingClient.BillingResponseCode.USER_CANCELED -> onChange(isPro(), null)
            else -> onChange(isPro(), "The purchase didn't go through. Nothing was charged. Try again in a moment.")
        }
    }

    private fun handle(purchase: Purchase) {
        if (PRODUCT_ID !in purchase.products) return
        when (purchase.purchaseState) {
            Purchase.PurchaseState.PURCHASED -> {
                acknowledge(purchase)
                setPro(true)
                onChange(true, "Thanks! iv31 Full is unlocked.")
            }
            Purchase.PurchaseState.PENDING -> onChange(isPro(), "Your payment is pending. iv31 Full unlocks as soon as Google Play confirms it.")
            else -> Unit
        }
    }

    private fun acknowledge(purchase: Purchase) {
        if (purchase.isAcknowledged) return
        val params = AcknowledgePurchaseParams.newBuilder().setPurchaseToken(purchase.purchaseToken).build()
        client.acknowledgePurchase(params) { }
    }

    private fun setPro(pro: Boolean) {
        prefs.edit().putBoolean(KEY_PRO, pro).apply()
    }

    companion object {
        const val PRODUCT_ID = "iv31_full"
        private const val KEY_PRO = "pro"
        private const val KEY_PRICE = "price"
    }
}
