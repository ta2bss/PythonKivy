from kivy.base import runTouchApp
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout


runTouchApp(Builder.load_string("""
Label:
    Button:
        text:"Okay"

        
    Button:
        text:"Alp"
        
        
"""))

