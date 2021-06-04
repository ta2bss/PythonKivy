from kivy.base import runTouchApp
from kivy.lang import Builder

runTouchApp(Builder.load_string
("""
FloatLayout
    Button:
        text: "B1"
        size_hint: 0.1,0.3
"""))