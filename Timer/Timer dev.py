from kivy.animation import Animation
from kivy.properties import NumericProperty
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
            self.Header1 = Label(text="TIMER V. 0.1", font_size="70sp")
            self.Header2 = Label(text=" " )
            self.window1.add_widget(self.Header1)
            self.window1.add_widget(self.Header2)

            self.message1 = Label(text="Input Countdown Duration in Seconds")
            self.window1.add_widget(self.message1)
            self.entry1 = TextInput(multiline=False)
            self.window1.add_widget(self.entry1)

            self.message2 = Label(text="Input Interval Duration in Seconds")
            self.window1.add_widget(self.message2)
            self.entry2 = TextInput(multiline=False)
            self.window1.add_widget(self.entry2)

            self.message3 = Label(text="Input Number of Sets ")
            self.window1.add_widget(self.message3)
            self.entry3 = TextInput(multiline=False)
            self.window1.add_widget(self.entry3)

            self.butt1 = Button(text="Click here after input")
            self.butt1.bind(on_press=self.callit)
            self.window1.add_widget(self.butt1)
            return self.window1

        def callit(self, event):
            try:
                global a
                global b
                global c
                a = (self.entry1.text)
                b = (self.entry2.text)
                c = (self.entry3.text)
                a = int(a)
                b = int(b)
                c = int(c)
                self.window1.clear_widgets()
                FirstPage().stop()
                return pagetwo()

            except:
                self.Header2.text = "THIS IS NOT A NUMBER "

    if __name__ == "__main__":
        FirstPage().run()


def pagetwo():
    class Cronoanimation(Label):
        Secondsa = NumericProperty(a)

        def start(self):
            Animation.cancel_all(self)
            self.anim = Animation(Secondsa=0, duration=self.Secondsa)

            def finish_callback(animation, window2):
                window2.text = "FINISHED"

            self.anim.bind(on_complete=finish_callback)
            self.anim.start(self)

        def on_Secondsa(self, instance, value):
            self.text = str(round(value, 1))

    class Timer(App):
        def build(self):
            cronometer = Cronoanimation()
            self.window2 = GridLayout(cols=1)
            Header = Label(text="TIMER V. 0.1", font_size="70sp")
            self.window2.add_widget(Header)
            self.window2.add_widget(cronometer)
            cronometer.start()
            return self.window2

    if __name__ == "__main__":
        Timer().run()


pageone()
