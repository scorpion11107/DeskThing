from focus_manager import FocusManager

from kivy.uix.widget import Widget

class InputController (Widget):
    def __init__(self, window, **kwargs):
        super().__init__(**kwargs)

        window.bind(on_key_down = self.on_key_down)
        window.bind(on_motion = self.on_motion)
        window.bind(on_joy_button_down = self.on_button_down)
        window.bind(on_joy_axis = self.on_axis)
        window.bind(on_joy_hat=self.on_hat)

        self.has_trig = False

        self.focus = FocusManager(window = window)

    def on_key_down(self, window, keyboard, kc, text, modifiers):
        """ Handle keyboard key press input """
        if kc == 82:
            self.focus.on_up()
            return True
        elif kc == 79:
            self.focus.on_right()
            return True
        elif kc == 81:
            self.focus.on_down()
            return True
        elif kc == 80:
            self.focus.on_left()
            return True
        elif kc == 40:
            self.focus.on_select()
            return True
        print("Keycode:", kc)
    
    def on_motion(self, window, etype, me):
        """ Handle mouse movement input """
        self.focus.on_movement()
        return True

    def on_button_down(self, window, stickid, buttonid):
        """ Handle controller button input """
        if buttonid == 0:
            self.focus.on_select()
            return True
        print(f"Button {buttonid} on stick {stickid} pressed.")
    
    def on_axis(self, window, stickid, axisid, value):
        """ Handle controller joystick or trigger input """
        print(f"Axis {axisid} on stick {stickid} moved to {value}")

    def on_hat(self, window, stickid, hatid, val):
        """ Handle controller D-pad input """
        if val == (0, 1):
            self.focus.on_up()
            return True
        elif val == (1, 0):
            self.focus.on_right()
            return True
        elif val == (0, -1):
            self.focus.on_down()
            return True
        elif val == (-1, 0):
            self.focus.on_left()
            return True