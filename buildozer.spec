[app]
title = MyApp
package.name = myapp
package.domain = org.test
version = 0.1
source.dir = .
source.include_exts = py
requirements = python3,kivy==2.3.0,pyjnius==1.6.1
orientation = portrait
fullscreen = 0

android.api = 34
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True
android.permissions = INTERNET

[buildozer]
log_level = 2
warn_on_root = 1
