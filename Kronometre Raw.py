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

class Timer(App):
    def build(self):

        self.clock=GridLayout(cols=1)
        Header=Label(text="TIMER V. 0.1", font_size="70sp")
        self.clock.add_widget(Header)
        MessageLine = Label(text="Input Time in secs")
        self.clock.add_widget(MessageLine)
        inputsec=TextInput(multiline=False)
        self.clock.add_widget(inputsec)
        Click = Button(text="Tikla")
        self.clock.add_widget(Click)

        Crono=Clock()
        self.clock.add_widget(Crono)
        Crono.start()
        return self.clock


class Clock(Label):
    a = NumericProperty(3)  # seconds
    def start(self):
        self.anim = Animation(a=0, duration=self.a)
        def finish_callback(animation, clock):
            playsound ("bip.mp3")
            clock.text = "FINISHED"
        self.anim.bind(on_complete=finish_callback)
        self.anim.start(self)
    def on_a(self, instance, value):
        self.text = str(round(value, 1))

if __name__ == "__main__":
    Timer().run()