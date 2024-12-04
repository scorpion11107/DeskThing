###    Imports    ###

from module_manager import load_modules

from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager, SlideTransition

from kivy.clock import Clock

from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView

from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.graphics import *

from kivy.config import Config
Config.set("graphics", "fullscreen", "auto")
Config.set("kivy", "log_level", "warning")

from kivy.core.window import Window
window_size = [Window.size[i] for i in range(2)]

###    Logic functions    ###

modules = load_modules()

def select_module(instance):
    global screen
    screen.manager.switch_to(modules[instance.i].run())

###    Graphic classes    ###

class SelectModuleScreen (Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = FloatLayout()

        global screen
        sm = ScreenManager(transition = SlideTransition(duration=0.2), size_hint = (1, 0.96), pos_hint = {"x": 0, "y": 0.04})
        screen = MainAppScreen()
        sm.add_widget(screen)
        layout.add_widget(sm)

        footer = Footer(size_hint = (1, 0.04))

        layout.add_widget(footer)

        self.add_widget(layout)

class Footer (FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        with self.canvas:
            Color(0, 0, 0)
            Rectangle(pos = [0, 0], size = [window_size[0], window_size[1]*0.045])
        
        layout = GridLayout(cols = 2, spacing = 10)

        layout.add_widget(CloseButton(text = "Close"))
        layout.add_widget(BatteryLabel())

        self.add_widget(layout)
        

class CloseButton (Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind(on_press = exit)

class BatteryLabel (Label):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        Clock.schedule_interval(lambda dt: self.display_battery(), 10)
        self.display_battery()

    def display_battery(self):
        import psutil
        battery = psutil.sensors_battery()
        percent = battery.percent
        plugged = "Plugged" if battery.power_plugged else "Unplugged"
        self.text = (str(percent) + ' | ' + str(plugged))

class MainAppScreen (Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        view = ScrollView(do_scroll_x = False, do_scroll_y = True)
        layout = GridLayout(cols = 2, spacing = 10, padding = 10, size_hint_y = None)
        layout.bind(minimum_height=layout.setter('height'))

        for j in range(100):
            for i in range(len(modules)):
                info = modules[i].get_info()
                button = ModuleSelectButton(ind = i,
                    text = (info[0] + ": " + info[1]),
                    size_hint_y = None)
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

        window = SelectModuleScreen()
        return window

if __name__ == "__main__":
    DeskThing().run()

