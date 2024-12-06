###    Imports    ###

from module_manager import load_modules
from core_classes import CoreButton

from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager, SlideTransition

from kivy.clock import Clock

from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView

from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.graphics import *

from kivy.config import Config
Config.set("graphics", "fullscreen", "auto")

from kivy.core.window import Window
window_size = Window.size

###    Logic functions    ###

modules = load_modules()

def select_module(instance):
    global current_screen
    current_screen.manager.switch_to(modules[instance.i].run())

def show_cursor():
    Window.show_cursor = True

def hide_cursor():
    Window.show_cursor = False

###    Graphic classes    ###

class MainScreen (Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        global current_screen
        current_screen = HomeScreen()

        layout = FloatLayout()

        sm = ScreenManager(transition = SlideTransition(duration=0.2),
                           size_hint = (1, 0.96),
                           pos_hint = {"x": 0, "y": 0.04})
        sm.add_widget(current_screen)
        layout.add_widget(sm)

        footer = Footer(size_hint = (1, 0.04))
        layout.add_widget(footer)

        self.add_widget(layout)

class Footer (GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        with self.canvas:
            Color(0.15, 0.15, 0.15)
            Rectangle(pos = [0, 0], size = [window_size[0], window_size[1]*0.045])
        
        self.cols = 3
        self.spacing = 10

        self.add_widget(CloseButton(function = exit, text = "Close"))
        self.add_widget(SwitchModeButton(function = lambda button: hide_cursor(),
                                         text = "Switch mode"))
        self.add_widget(StatusLabel())

class SwitchModeButton (CoreButton):
    def __init__(self, function, **kwargs):
        super().__init__(function, **kwargs)

class CloseButton (CoreButton):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class StatusLabel (GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.cols = 1

        Clock.schedule_interval(lambda dt: self.update(), 10)
        self.update()
    
    def update(self):
        from psutil import sensors_battery
        from datetime import datetime

        battery = sensors_battery()
        percent = battery.percent
        plugged = "Plugged" if battery.power_plugged else "Unplugged"
        battery_text = (str(percent) + '% | ' + str(plugged))
        self.add_widget(Label(text = battery_text))

        date_time = datetime.now()
        time_text = (date_time.strftime("%H") + ":" +
                     date_time.strftime("%M") + " - " +
                     date_time.strftime("%x"))
        self.add_widget(Label(text = time_text))

class HomeScreen (Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        view = ScrollView(do_scroll_x = False, do_scroll_y = True)
        layout = GridLayout(cols = 2, spacing = 10, padding = 10, size_hint_y = None)
        layout.bind(minimum_height=layout.setter('height'))

        for j in range(100):
            for i in range(len(modules)):
                info = modules[i].get_info()
                button = ModuleSelectButton(function = select_module,
                    ind = i,
                    text = (info[1] + ": " + info[2]),
                    size_hint_y = None)
                layout.add_widget(button)
        
        view.add_widget(layout)
        self.add_widget(view)
        self.add_widget(MyKeyboardListener())

class ModuleSelectButton (CoreButton):
    def __init__(self, ind, **kwargs):
        self.i = ind
        super().__init__(**kwargs)

        self.background_normal = ""
        if self.i%2 == 0:
            self.background_color = (0.35, 0.35, 0.35, 1)
        else:
            self.background_color = (0.4, 0.4, 0.4, 1)

class MyKeyboardListener(Widget):

    def __init__(self, **kwargs):
        super(MyKeyboardListener, self).__init__(**kwargs)
        self._keyboard = Window.request_keyboard(
            self._keyboard_closed, self, 'text')
        if self._keyboard.widget:
            # If it exists, this widget is a VKeyboard object which you can use
            # to change the keyboard layout.
            pass
        self._keyboard.bind(on_key_down=self._on_keyboard_down)

    def _keyboard_closed(self):
        print('My keyboard have been closed!')
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        print('The key', keycode, 'have been pressed')
        print(' - text is %r' % text)
        print(' - modifiers are %r' % modifiers)

        # Keycode is composed of an integer + a string
        # If we hit escape, release the keyboard
        if keycode[1] == 'escape':
            keyboard.release()

        # Return True to accept the key. Otherwise, it will be used by
        # the system.
        return True

class DeskThing (App):
    def build(self):

        window = MainScreen()
        return window

if __name__ == "__main__":
    DeskThing().run()

