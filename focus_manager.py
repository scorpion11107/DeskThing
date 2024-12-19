from core_classes import CoreGrid

from kivy.uix.widget import Widget

class FocusManager (Widget):
    def __init__(self, screen_manager, **kwargs):
        self.sm = screen_manager
        super().__init__(**kwargs)