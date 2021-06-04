from kivy.base import runTouchApp
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout


runTouchApp(Builder.load_string("""
Label:
    Button:
        text:"Okay"
        font_size:32
        color:.8,.9,0,1
        size: 200,200
        pos: 50,100
        
    Button:
        text:"Alp"
        font_size:32
        color:.8,.9,0,1
        size: 200,200
        pos: 250,100
        
        
"""))

