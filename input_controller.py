from kivy.uix.widget import Widget

class InputController (Widget):
    def __init__(self, window, **kwargs):
        super().__init__(**kwargs)

        window.bind(on_key_down = self.on_key_down)
        window.bind(on_joy_button_down = self.on_button_down)
        window.bind(on_joy_axis = self.on_axis)

    def on_button_down(self, window, stickid, buttonid):
        print(f"Button {buttonid} on stick {stickid} pressed.")
    
    def on_axis(self, window, stickid, axisid, value):
        print(f"Axis {axisid} on stick {stickid} moved to {value:.2f}")

    def on_key_down(self, window, keyboard, keycode, text, modifiers):
        print("Keycode:", keycode, "\tKey:", chr(keycode))