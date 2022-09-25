from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.stacklayout import StackLayout

class Stack(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for i in range(30):
            b1 = Button(text=str(i+1), size_hint=(None, None), size=(100, 100))
            self.add_widget(b1)



# App Creation
class TestApp(App):
    def Build(self):
        return Satck()


TestApp().run()
