
from kivy.animation import Animation
from kivy.properties import StringProperty, NumericProperty
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
class Clock(Label):
    a = NumericProperty(5)
    def start(self):
        self.anim = Animation(a=0, duration=self.a)
        def finish_callback(animation, clock):
            clock.text = "FINISHED"
        self.anim.bind(on_complete=finish_callback)
        self.anim.start(self)
    def on_a(self, instance, value):
        self.text = str(round(value, 1))
    
class Timer(App):
    def build(self):
        self.clock = GridLayout(cols=1)
        Header = Label(text="TIMER V. 0.1", font_size="70sp")
        self.clock.add_widget(Header)
        self.MessageLine = Label(text="Input Time in secs")
        self.clock.add_widget(self.MessageLine)
        self.inputsec = TextInput(multiline=False)
        self.clock.add_widget(self.inputsec)
        Click = Button(text="Click")
        Click.bind(on_press=self.event)
        self.clock.add_widget(Click)
        Crono = Clock()
        self.clock.add_widget(Crono)
        Crono.start()
        return self.clock

    def event(self, number):
        try:
            global secint
            secint = int(self.inputsec.text)
            self.MessageLine.text = "Count Down From : " + self.inputsec.text
            print (self.inputsec.text)
            print (type(self.inputsec.text))
        except:
            self.MessageLine.text = "Input a Number"
if __name__ == "__main__":
    Timer().run()
