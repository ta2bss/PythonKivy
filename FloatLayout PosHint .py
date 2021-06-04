import time
from kivy.base import runTouchApp
from kivy.lang import Builder

runTouchApp(Builder.load_string
("""
FloatLayout
    Button:
        text: "B1"
        size_hint: 0.1,0.2
        pos_hint:{"x":0.2, "y":0.3}
"""))

