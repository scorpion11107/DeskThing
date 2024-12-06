from kivy.uix.button import Button

class CoreButton (Button):
    def __init__(self, function, **kwargs):
        super().__init__(**kwargs)
        self.bind(on_press = function)