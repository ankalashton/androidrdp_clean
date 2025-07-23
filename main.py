from kivy.app import App
from kivy.uix.label import Label

class AndroidRDP(App):
    def build(self):
        return Label(text="Hello, Android — clean build!")

AndroidRDP().run()
