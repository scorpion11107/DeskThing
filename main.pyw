from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button


class MainScreen (Widget):
    pass

class DeskThingApp (App):
    def build (self):
        return MainScreen()


if __name__ == "__main__":
    DeskThingApp().run()

