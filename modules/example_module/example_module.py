from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label

def get_main_screen():
    return MainScreen()

class MainScreen (Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.add_widget(Label(text="Welcome to the Example Module"))