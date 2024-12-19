from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import Screen

class CoreButton (Button):
    def __init__(self, function, **kwargs):
        super().__init__(**kwargs)
        self.bind(on_press = function)
    
    def on_gain_focus(self):
        print("focus")
    
    def on_lose_focus(self):
        print("unfocus")

class CoreGrid (GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def get_info(self):
        self.lines = len(self.children) // self.cols
        if len(self.children) % self.cols != 0:
            self.lines += 1
        
        return [self.lines, self.cols]