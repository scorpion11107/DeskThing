###    Imports    ###

from module_manager import load_modules

from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager, SlideTransition

from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView

from kivy.uix.button import Button
from kivy.graphics import Color

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
        view = ScrollView(do_scroll_x = False, do_scroll_y = True)
        layout = GridLayout(cols = 1, spacing = 10, padding = 10, size_hint_y = None)
        layout.bind(minimum_height=layout.setter('height'))

        for i in range(len(modules)):
            info = modules[i].get_info()
            button = ModuleSelectButton(ind = i,
                text = (info[0] + ": " + info[1]),
                size_hint_y = None)
            button.bind(on_press = select_module)
            layout.add_widget(button)
        
        view.add_widget(layout)
        self.add_widget(view)

class ModuleSelectButton (Button):
    def __init__(self, ind, **kwargs):
        self.i = ind
        super().__init__(**kwargs)
        self.bind(on_press = select_module)

        self.background_normal = ""
        if self.i%2 == 0:
            self.background_color = (0.35, 0.35, 0.35, 1)
        else:
            self.background_color = (0.4, 0.4, 0.4, 1)

class DeskThing (App):
    def build(self):
        global screen
        sm = ScreenManager(transition = SlideTransition(duration=0.2))
        screen = MainAppScreen()
        sm.add_widget(screen)
        return sm

if __name__ == "__main__":
    DeskThing().run()

