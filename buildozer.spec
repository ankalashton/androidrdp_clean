[app]
title = AndroidRDP
package.name = androidrdp
package.domain = org.ankalashton
source.dir = .
version = 1.0.0
requirements = python3,kivy
orientation = portrait
fullscreen = 1
android.permissions = INTERNET
android.minapi = 21
android.ndk_api = 21
android.build_tools_version = 34.0.0
target = android

[p4a]
bootstrap = sdl2
source_dir = external/p4a
ndk_dir = $ANDROID_NDK_HOME

[buildozer]
warn_on_root = 1
log_level = 2
