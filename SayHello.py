import time

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class Benimesajla(App):
    def build(self):
        self.pencere = GridLayout()
        self.pencere.cols = 1
        self.pencere.add_widget(Image(source = "logo.png"))
        self.mesaj = Label(text="Lutfen adinizi giriniz")
        self.pencere.add_widget(self.mesaj)

        self.giris = TextInput(multiline=False)
        self.pencere.add_widget(self.giris)

        self.dugme = Button(text="tikla")
        self.dugme.bind(on_press=self.cagir)
        self.pencere.add_widget(self.dugme)
        return self.pencere


    def cagir (self, olay):
        if self.giris.text == "Okay" :
            self.mesaj.text = "Selamlar " + self.giris.text+" !!!"
        else:
            self.mesaj.text = "KİMSİN LAN SEN " + self.giris.text + " !!!"



if __name__ == "__main__":
    Benimesajla().run()

