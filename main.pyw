###    Imports    ###

from module_manager import load_modules

from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView

from kivy.uix.button import Button

from kivy.config import Config
Config.set("graphics", "fullscreen", "auto")

###    Logic functions    ###

modules = load_modules()

def select_module(instance):
    global screen
    screen.manager.switch_to(modules[instance.i].run())

###    Graphic classes    ###

class MainAppScreen (Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        view = ScrollView()
        layout = BoxLayout(orientation='vertical', spacing = 10, padding = 15)

        for i in range(len(modules)):
            button = ModuleSelectButton(ind = i, text = modules[i].get_info()[0])
            button.bind(on_press = select_module)
            layout.add_widget(button)
        
        view.add_widget(layout)
        self.add_widget(view)

class ModuleSelectButton (Button):
    def __init__(self, ind, **kwargs):
        self.i = ind
        super().__init__(**kwargs)
        self.bind(on_press = select_module)

class DeskThing (App):
    def build(self):
        sm = ScreenManager()
        global screen
        screen = MainAppScreen()
        sm.add_widget(screen)
        return sm

if __name__ == "__main__":
    DeskThing().run()

