[app]
title = MyApp
package.name = myapp
package.domain = org.test
version = 0.1
source.dir = .
source.include_exts = py
requirements=python==3.10.11,kivy==2.1.0,pyjnius==1.5.1
orientation = portrait
fullscreen = 0

android.api = 34
android.minapi = 21
android.ndk = 27b
android.ndk_path = ~/.buildozer/android/platform/android-sdk/ndk/27.0.12077973

[buildozer]
log_level = 2
warn_on_root = 1

[app:permissions]
android.permissions = INTERNET

[app:android]
android.api = 34
android.minapi = 21
android.ndk = 27b
android.ndk_path = ~/.buildozer/android/platform/android-sdk/ndk/27.0.12077973
android.accept_sdk_license = True
