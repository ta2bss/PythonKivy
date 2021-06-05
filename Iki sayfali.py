from kivy.animation import Animation
from kivy.properties import StringProperty, NumericProperty
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

def pageone():
    class FirstPage(App):
        def build(self):
            self.window1 = GridLayout()
            self.window1.cols = 1

            Header = Label(text="TIMER V. 0.1", font_size="70sp")
            self.window1.add_widget(Header)

            self.message = Label(text="Input Timer Seconds")
            self.window1.add_widget(self.message)

            self.entry = TextInput(multiline=False)
            self.window1.add_widget(self.entry)

            self.dugme = Button(text="Click here after input")
            self.dugme.bind(on_press=self.callit)
            self.window1.add_widget(self.dugme)
            return self.window1

        def callit(self, event):
            try:
                global a
                a = (self.entry.text)
                pagetwo()
            except:
                self.message.text = "THIS IS NOT A NUMBER " + self.entry.text + " !!!"

    if __name__ == "__main__":
        FirstPage().run()


def pagetwo():
    class Cronoanimation(Label):
        Seconds = NumericProperty(a)

        def start(self):
            Animation.cancel_all(self)
            self.anim = Animation(Seconds=0, duration=self.Seconds)

            def finish_callback(animation, window2):
                window2.text = "FINISHED"

            self.anim.bind(on_complete=finish_callback)
            self.anim.start(self)

        def on_Seconds(self, instance, value):
            self.text = str(round(value, 1))

    class Timer(App):
        def build(self):
            cronometer = Cronoanimation()
            self.window2 = GridLayout(cols=1)

            Header = Label(text="TIMER V. 0.1", font_size="70sp")
            self.window2.add_widget(Header)

            #self.MessageLine = Label(text="Input Time in secs")
            #self.window2.add_widget(self.MessageLine)

            #self.inputsec = TextInput(multiline=False)
            #self.window2.add_widget(self.inputsec)

            #Click = Button(text="Click")
            #Click.bind(on_press=self.event)
            #self.window2.add_widget(Click)

            self.window2.add_widget(cronometer)
            cronometer.start()

            return self.window2

        def event(self, number):
            try:
                global secint
                secint = int(self.inputsec.text)
                self.MessageLine.text = "Count Down From : " + self.inputsec.text
                print(type(secint))
            except:
                self.MessageLine.text = "Input a Number"

    if __name__ == "__main__":
        Timer().run()


pageone()
