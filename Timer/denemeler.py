from kivy.uix.colorpicker import ColorWheel

class AutonomousColorWheel(ColorWheel):
    def __init__(self, **kwarg):
        super(AutonomousColorWheel, self).__init__(**kwarg)
        self.init_wheel(dt = 0)

    def on__hsv(self, instance, value):
        super(AutonomousColorWheel, self).on__hsv(instance, value)
        print(self.rgba)     #Or any method you want to trigger