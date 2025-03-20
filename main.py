from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivy.core.window import Window

Window.size = (350, 610)
class MainApp(MDApp):
    def build(self):
        return MDLabel(text="Hello, Humans", halign="center")


MainApp().run()