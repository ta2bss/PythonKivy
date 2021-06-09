from kivy.animation import Animation
from kivy.properties import NumericProperty
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ListProperty
from kivy.lang import Builder
from kivy.core.window import Window

counter = 1
counterstr = str(counter)


def pageone():
    global counter

    class FirstPage(App):
        def build(self):
            self.window1 = BoxLayout(orientation="vertical")
            self.horizontalbox1 = BoxLayout(orientation="horizontal")
            self.horizontalbox2 = BoxLayout(orientation="horizontal")
            self.horizontalbox3 = BoxLayout(orientation="horizontal")
            self.horizontalbox4 = BoxLayout(orientation="horizontal")

            self.Header1 = Label(text="Very Simple Timer", font_size="40sp")
            self.Header2 = Label(text=" ")
            self.message1 = Label(text="Rest in Seconds", font_size="20sp", size_hint=(.7, 1))
            self.entry1 = TextInput(multiline=False, font_size="30sp", size_hint=(.3, .9),halign='center')
            self.message2 = Label(text="Work in Seconds", font_size="20sp", size_hint=(.7, 1))
            self.entry2 = TextInput(multiline=False, font_size="30sp", size_hint=(.3, .9),halign='center')
            self.message3 = Label(text="Number of Sets ", font_size="20sp", size_hint=(.7, 1))
            self.entry3 = TextInput(multiline=False, font_size="30sp", size_hint=(.3, .9),halign='center')
            self.message4 = Label(text="Initial in Seconds -Def.(5)", font_size="20sp", size_hint=(.7, 1))
            self.entry4 = TextInput(multiline=False, font_size="30sp", size_hint=(.3, .9),halign='center')
            self.butt1 = Button(text="RUN", font_size="40sp", background_color = [0/255,35/255,255/255,1])
            self.butt1.bind(on_press=self.callit)

            self.window1.add_widget(self.Header1)
            self.window1.add_widget(self.Header2)
            self.horizontalbox1.add_widget(self.message2)
            self.horizontalbox1.add_widget(self.entry2)
            self.horizontalbox2.add_widget(self.message1)
            self.horizontalbox2.add_widget(self.entry1)
            self.horizontalbox3.add_widget(self.message3)
            self.horizontalbox3.add_widget(self.entry3)
            self.horizontalbox4.add_widget(self.message4)
            self.horizontalbox4.add_widget(self.entry4)

            self.window1.add_widget(self.horizontalbox1)
            self.window1.add_widget(self.horizontalbox2)
            self.window1.add_widget(self.horizontalbox3)
            self.window1.add_widget(self.horizontalbox4)

            self.window1.add_widget(self.butt1)

            return self.window1

        def callit(self, event):
            try:
                global d
                global dstr
                d = (self.entry4.text)
                d = int(d)
                dstr = str(d)
            except:
                d = 5
                d = int(d)
                dstr = str(d)

            try:
                global a
                global b
                global c

                global counter
                global astr
                global bstr
                global cstr

                a = (self.entry1.text)
                b = (self.entry2.text)
                c = (self.entry3.text)

                a = int(a)
                b = int(b)
                c = int(c)

                astr = str(a)
                bstr = str(b)
                cstr = str(c)

                self.window1.clear_widgets()
                FirstPage().stop()
                return pagetwo()

            except:
                self.Header2.text = "PLEASE INPUT ONLY NUMBERS "

    if __name__ == "__main__":
        FirstPage().run()


def pagetwo():
    class Cronoanimation(Label):
        if counter == 1:
            Secondsa = NumericProperty(d)
        else:
            Secondsa = NumericProperty(a)

        def start(self):
            Animation.cancel_all(self)
            self.anim = Animation(Secondsa=0, duration=self.Secondsa)

            def finish_callback(animation, window2):
                Timer().stop()

            self.anim.bind(on_complete=finish_callback)
            self.anim.start(self)

        def on_Secondsa(self, instance, value):
            self.text = str(round(value, 1))

    class Timer(App):
        def build(self):
            cronometer = Cronoanimation()
            self.window2 = GridLayout(cols=1)
            if counter != 1:
                Header = Label(text="REST", font_size="70sp",color=[1,1,0,1])
                SetInfo = Label(text="Set:" + counterstr + " of " + cstr)
            else:
                Header = Label(text="GET SET", font_size="70sp",color=[1,1,0,1])
                SetInfo = Label(text="Set:" + counterstr + " of " + cstr)
            self.window2.add_widget(Header)
            self.window2.add_widget(SetInfo)
            self.window2.add_widget(cronometer)
            cronometer.start()
            return self.window2

    if __name__ == "__main__":
        Timer().run()

    pagethree()


def pagethree():
    class Pauseranimation(Label):
        Secondsb = NumericProperty(b)

        def start(self):
            Animation.cancel_all(self)
            self.anim = Animation(Secondsb=0, duration=self.Secondsb)

            def finish_callback(animation, window3):
                Pauser().stop()

            self.anim.bind(on_complete=finish_callback)
            self.anim.start(self)

        def on_Secondsb(self, instance, value):
            self.text = str(round(value, 1))

    class Pauser(App):
        def build(self):
            Pausermeter = Pauseranimation()
            self.window3 = GridLayout(cols=1)
            Header = Label(text="WORK", font_size="70sp",color= [0,0,1,1])
            SetInfo = Label(text="Set:" + counterstr + " of " + cstr)
            self.window3.add_widget(Header)
            self.window3.add_widget(SetInfo)
            self.window3.add_widget(Pausermeter)
            Pausermeter.start()

            return self.window3

    class finished(App):
        def build(self):
            self.window4 = GridLayout()
            self.window4.clear_widgets()
            self.window4.cols = 1

            self.Header1 = Label(text="FINISHED", font_size="70sp", color= [1,0,0,1])
            self.Header2 = Label(text=" ")
            self.window4.add_widget(self.Header1)
            self.window4.add_widget(self.Header2)

            self.butt1 = Button(text="Main")
            self.butt1.bind(on_press=self.tomainscreen)
            self.window4.add_widget(self.butt1)

            self.butt2 = Button(text="Restart")
            self.butt2.bind(on_press=self.torepeate)
            self.window4.add_widget(self.butt2)

            self.butt3 = Button(text="Exit")
            self.butt3.bind(on_press=self.toexit)
            self.window4.add_widget(self.butt3)

            return self.window4

        def tomainscreen(self, event):
            self.window4.clear_widgets()
            finished().stop()
            global counter
            global counterstr
            counter = 1
            counterstr = str(counter)
            pageone()

        def torepeate(self, event):
            self.window4.clear_widgets()
            finished().stop()
            global counter
            global counterstr
            counter = 1
            counterstr = str(counter)
            pagetwo()

        def toexit(self, event):
            self.window4.clear_widgets()
            finished().stop()
            exit()

    if __name__ == "__main__":
        Pauser().run()
    global counter
    counter = counter + 1
    global counterstr
    counterstr = str(counter)
    if counter != c + 1:
        pagetwo()
    else:
        finished().run()


pageone()
