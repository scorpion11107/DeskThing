from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

class NavigationApp(App):
    def build(self):
        # Layout with some buttons
        self.layout = BoxLayout(orientation='vertical', spacing=10, padding=10)
        self.buttons = []

        for i in range(5):
            btn = Button(text=f"Button {i + 1}")
            btn.bind(on_press=self.on_button_press)
            self.layout.add_widget(btn)
            self.buttons.append(btn)
        
        # Initially focus the first button
        self.current_index = 0
        self.update_focus()
        
        # Bind keyboard events
        Window.bind(on_key_down=self.on_key_down)
        
        return self.layout
    
    def update_focus(self):
        """Update the focus style for buttons."""
        for i, btn in enumerate(self.buttons):
            if i == self.current_index:
                btn.background_color = [0, 1, 0, 1]  # Highlight the focused button
            else:
                btn.background_color = [1, 1, 1, 1]  # Default button color

    def on_key_down(self, window, key, scancode, codepoint, modifiers):
        """Handle keyboard navigation."""
        if key == 273:  # Up arrow key
            self.current_index = (self.current_index - 1) % len(self.buttons)
        elif key == 274:  # Down arrow key
            self.current_index = (self.current_index + 1) % len(self.buttons)
        elif key == 13:  # Enter key
            self.buttons[self.current_index].trigger_action(0.1)  # Trigger button press
        self.update_focus()
    
    def on_button_press(self, instance):
        """Handle button press events."""
        print(f"{instance.text} clicked!")

if __name__ == '__main__':
    NavigationApp().run()
