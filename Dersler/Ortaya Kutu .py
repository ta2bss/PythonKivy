from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.uix.button import Button

class Class3():
    print ("Okay Alp")

class Class1(BoxLayout):
    def __init__(self,**kwargs):
        super(Class1,self).__init__(**kwargs)

        self.padding=100

        button = Button(text="button")
        self.add_widget(button)


class Class2(App):
    def build(self):
        return Class1()

if __name__ == "__main__":

    Class2().run()

