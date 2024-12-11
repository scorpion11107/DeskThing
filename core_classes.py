from kivy.uix.button import Button

class CoreButton (Button):
    def __init__(self, function, **kwargs):
        super().__init__(**kwargs)
        self.bind(on_press = function)
    
    def on_gain_focus(self):
        print("focus")
    
    def on_lose_focus(self):
        print("unfocus")