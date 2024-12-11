from kivy.uix.widget import Widget

class FocusManager (Widget):
    def __init__(self, window, **kwargs):
        super().__init__(**kwargs)

        self.window = window

        self.c_mode = 0 # Current mode, 0 is mouse, 1 is keyboard / controller
        self.c_focused = None # Current focused element
        self.p_focused = None # Previous focused element
    
    def on_up(self):
        print("up")
        self.switch_mode(1)
    
    def on_right(self):
        print("right")
    
    def on_down(self):
        print("down")
    
    def on_left(self):
        print("left")
    
    def on_select(self):
        print("select")
    
    def on_movement(self):
        print("movement")
        self.switch_mode(0)
    

    def switch_mode(self, mode):
        """ Switch between mouse and keyboard / controller mode """
        if mode != self.c_mode:
            self.c_mode = mode
            self.manage_cursor()
            if mode == 0:
                self.p_focused = self.c_focused
                self.c_focused = None
            else:
                self.c_focused = self.p_focused
            
            self.window.children[0].children[1].children[0].children[-1].on_gain_focus()

    def manage_cursor(self):
        """ Show cursor if mode = 0, else hide it"""
        self.window.show_cursor = not(self.c_mode)