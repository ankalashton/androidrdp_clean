[app]
title = AndroidRDP
package.name = androidrdp
package.domain = org.ankalashton
source.dir = .
version = 1.0.0
requirements = python3,kivy
android.permissions = INTERNET
android.minapi = 21
android.sdk = 31
android.ndk = 27.3.13750724
android.ndk_api = 21
android.build_tools_version = 34.0.0
target = android
orientation = portrait
fullscreen = 1

# (опционально) отключить logcat
log_level = 2

# (опционально) задать иконку приложения
# icon.filename = %(source.dir)s/data/icon.png

[p4a]
bootstrap = sdl2
python-for-android.url = https://github.com/ankalashton/python-for-android.git
# libffi больше не используется
# можно указать вручную список рецептов при необходимости:
# recipes = kivy

[buildozer]
warn_on_root = 1
log_level = 2
