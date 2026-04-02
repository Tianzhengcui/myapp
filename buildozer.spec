[app]
title = MyApp
package.name = myapp
package.domain = org.example

[buildozer]
# Log level (0 = error, 1 = info, 2 = debug)
log_level = 2
warn_on_root = 1

[app:permissions]
android.permissions = INTERNET

[app:android]
# Use specific, known-working versions
android.api = 31
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True
