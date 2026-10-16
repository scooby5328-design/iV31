Unicode true
!define APPNAME "iv31"
!define VERSION "0.0.0"
!define UNKEY "Software\Microsoft\Windows\CurrentVersion\Uninstall\iv31"
!define WV2KEY "SOFTWARE\WOW6432Node\Microsoft\EdgeUpdate\Clients\{F3017226-FE2A-4295-8BDF-00C3A9A7E4C5}"
!define WV2KEY32 "SOFTWARE\Microsoft\EdgeUpdate\Clients\{F3017226-FE2A-4295-8BDF-00C3A9A7E4C5}"

!include "MUI2.nsh"

Name "${APPNAME}"
OutFile "dist\iv31-Setup-${VERSION}.exe"
InstallDir "$LOCALAPPDATA\Programs\iv31"
InstallDirRegKey HKCU "Software\iv31" "InstallDir"
RequestExecutionLevel user
SetCompressor /SOLID lzma
BrandingText "iv31 ${VERSION}"

VIProductVersion "${VERSION}.0"
VIAddVersionKey "ProductName" "iv31"
VIAddVersionKey "CompanyName" "Chili"
VIAddVersionKey "FileDescription" "iv31 Setup"
VIAddVersionKey "FileVersion" "${VERSION}"
VIAddVersionKey "ProductVersion" "${VERSION}"
VIAddVersionKey "LegalCopyright" "© 2026 Chili"

!define MUI_ICON "pkg\icon.ico"
!define MUI_UNICON "pkg\icon.ico"
!define MUI_ABORTWARNING
!define MUI_FINISHPAGE_RUN "$INSTDIR\iv31.exe"
!define MUI_FINISHPAGE_RUN_TEXT "Launch iv31"

!insertmacro MUI_PAGE_WELCOME
!insertmacro MUI_PAGE_COMPONENTS
!insertmacro MUI_PAGE_DIRECTORY
!insertmacro MUI_PAGE_INSTFILES
!insertmacro MUI_PAGE_FINISH
!insertmacro MUI_UNPAGE_CONFIRM
!insertmacro MUI_UNPAGE_INSTFILES
!insertmacro MUI_LANGUAGE "English"

Function .onInit
  IfSilent done
  ReadRegStr $0 HKLM "${WV2KEY}" "pv"
  StrCmp $0 "" 0 done
  ReadRegStr $0 HKLM "${WV2KEY32}" "pv"
  StrCmp $0 "" 0 done
  ReadRegStr $0 HKCU "${WV2KEY32}" "pv"
  StrCmp $0 "" 0 done
  MessageBox MB_YESNO|MB_ICONINFORMATION "iv31 needs the Microsoft Edge WebView2 Runtime, which doesn't seem to be installed.$\r$\n$\r$\nOpen Microsoft's download page now?$\r$\n(You can still continue installing.)" IDNO done
  ExecShell "open" "https://developer.microsoft.com/microsoft-edge/webview2/"
  done:
FunctionEnd

Section "iv31 (required)" SecMain
  SectionIn RO
  nsExec::Exec 'taskkill /F /IM iv31.exe'
  SetOutPath "$INSTDIR"
  File "pkg\iv31.exe"
  File "pkg\resources.neu"
  File "pkg\icon.ico"
  WriteUninstaller "$INSTDIR\Uninstall iv31.exe"
  CreateShortcut "$SMPROGRAMS\iv31.lnk" "$INSTDIR\iv31.exe" "" "$INSTDIR\icon.ico"
  WriteRegStr HKCU "Software\iv31" "InstallDir" "$INSTDIR"
  WriteRegStr HKCU "${UNKEY}" "DisplayName" "iv31"
  WriteRegStr HKCU "${UNKEY}" "DisplayVersion" "${VERSION}"
  WriteRegStr HKCU "${UNKEY}" "Publisher" "Chili"
  WriteRegStr HKCU "${UNKEY}" "DisplayIcon" "$INSTDIR\icon.ico"
  WriteRegStr HKCU "${UNKEY}" "InstallLocation" "$INSTDIR"
  WriteRegStr HKCU "${UNKEY}" "UninstallString" '"$INSTDIR\Uninstall iv31.exe"'
  WriteRegStr HKCU "${UNKEY}" "QuietUninstallString" '"$INSTDIR\Uninstall iv31.exe" /S'
  WriteRegDWORD HKCU "${UNKEY}" "NoModify" 1
  WriteRegDWORD HKCU "${UNKEY}" "NoRepair" 1
  WriteRegDWORD HKCU "${UNKEY}" "EstimatedSize" 3300
SectionEnd

Section "Desktop shortcut" SecDesktop
  CreateShortcut "$DESKTOP\iv31.lnk" "$INSTDIR\iv31.exe" "" "$INSTDIR\icon.ico"
SectionEnd

!insertmacro MUI_FUNCTION_DESCRIPTION_BEGIN
  !insertmacro MUI_DESCRIPTION_TEXT ${SecMain} "The iv31 app."
  !insertmacro MUI_DESCRIPTION_TEXT ${SecDesktop} "Put an iv31 shortcut on your desktop."
!insertmacro MUI_FUNCTION_DESCRIPTION_END

Section "Uninstall"
  nsExec::Exec 'taskkill /F /IM iv31.exe'
  Delete "$INSTDIR\iv31.exe"
  Delete "$INSTDIR\resources.neu"
  Delete "$INSTDIR\icon.ico"
  Delete "$INSTDIR\Uninstall iv31.exe"
  RMDir /r "$INSTDIR\.tmp"
  RMDir "$INSTDIR"
  Delete "$SMPROGRAMS\iv31.lnk"
  Delete "$DESKTOP\iv31.lnk"
  DeleteRegKey HKCU "${UNKEY}"
  DeleteRegKey HKCU "Software\iv31"
SectionEnd
