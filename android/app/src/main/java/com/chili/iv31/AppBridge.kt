package com.chili.iv31

import android.webkit.JavascriptInterface

class AppBridge(private val activity: MainActivity, private val billing: Billing) {
    @JavascriptInterface
    fun isPro(): Boolean = billing.isPro()

    @JavascriptInterface
    fun price(): String = billing.price()

    @JavascriptInterface
    fun buy() = activity.launchPurchase()

    @JavascriptInterface
    fun restore() = billing.restore()
}
