from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.properties import (
    NumericProperty, ReferenceListProperty, ObjectProperty
)
from kivy.core.window import Window

class Element(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Window.bind(mouse_pos = self.on_mouseover)

    def on_mouseover(self, *args):
        print("enter")

class PeriodicTable(Widget):
    helium = ObjectProperty(None)

    pass


class TableApp(App):
    def build(self):
        return PeriodicTable()

if __name__ == "__main__":
    TableApp().run()

# Colors !!
# green  : 0.46, 0.42, 0.03
# yellow : 0.85, 0.62, 0.09
# white  : 0.91, 0.91, 0.91