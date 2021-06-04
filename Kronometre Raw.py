from inspect import currentframe, getframeinfo

import kivy
from kivy.base import runTouchApp
from playsound import playsound
from kivy.lang import Builder
from kivy.app import App
from kivy.uix.label import Label
from kivy.animation import Animation
from kivy.properties import StringProperty, NumericProperty
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput




frameinfo = getframeinfo(currentframe());print("Satır", frameinfo.lineno)
class Timer(App):
    frameinfo = getframeinfo(currentframe()) ;print("Satır", frameinfo.lineno)
    def build(self):
        frameinfo = getframeinfo(currentframe()) ;print("Satır", frameinfo.lineno)

        self.clock=GridLayout(cols=1)
        Header=Label(text="TIMER V. 0.1", font_size="70sp")
        frameinfo = getframeinfo(currentframe());print("Satır", frameinfo.lineno)
        self.clock.add_widget(Header)
        self.MessageLine = Label(text="Input Time in secs")
        self.clock.add_widget(self.MessageLine)
        frameinfo = getframeinfo(currentframe());print("Satır", frameinfo.lineno)
        self.inputsec=TextInput(multiline=False)
        self.clock.add_widget(self.inputsec)
        Click = Button(text="Tikla")
        Click.bind(on_press=self.cagir)
        self.clock.add_widget(Click)
        frameinfo = getframeinfo(currentframe()) ; print("Satır", frameinfo.lineno)
        Crono=Clock()
        self.clock.add_widget(Crono)
        Crono.start()
        frameinfo = getframeinfo(currentframe());print("Satır", frameinfo.lineno)
        return self.clock

    def cagir (self, olay):
        frameinfo = getframeinfo(currentframe()) ;print("Satır", frameinfo.lineno)
        print(type(self.inputsec.text))
        global secint
        secint = int (self.inputsec.text)
        print (type(secint))
        frameinfo = getframeinfo(currentframe()) ;print("Satır", frameinfo.lineno)
        if self.inputsec.text == "Okay" :
            self.MessageLine.text = "Selamlar " + self.inputsec.text+" !!!"
        else:
            self.MessageLine.text = "KİMSİN LAN SEN " + self.inputsec.text + " !!!"

class Clock(Label):
    frameinfo = getframeinfo(currentframe()) ;print("Satır", frameinfo.lineno)
    a = NumericProperty(0)  # seconds
    frameinfo = getframeinfo(currentframe()) ;print("Satır", frameinfo.lineno)
    def start(self):
        Timer()
        frameinfo = getframeinfo(currentframe()) ;print("Satır", frameinfo.lineno)
        self.anim = Animation(a=0, duration=self.a)
        def finish_callback(animation, clock):
            playsound ("bip.mp3")
            clock.text = "FINISHED"
        self.anim.bind(on_complete=finish_callback)
        self.anim.start(self)
        frameinfo = getframeinfo(currentframe()) ; print("Satır", frameinfo.lineno)
    def on_a(self, instance, value):
        self.text = str(round(value, 1))

if __name__ == "__main__":
    frameinfo = getframeinfo(currentframe()) ;print("Satır", frameinfo.lineno)
    Timer().run()