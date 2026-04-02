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
android.ndk = 27b  # Updated from 25b

[buildozer]
log_level = 2
warn_on_root = 1

[app:permissions]
android.permissions = INTERNET

[app:android]
android.api = 34
android.minapi = 21
android.ndk = 27b  # Updated from 25b
android.accept_sdk_license = True
