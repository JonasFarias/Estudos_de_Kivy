from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.stacklayout import StackLayout

#interface
class Interface(FloatLayout):
    pass


class scroller():
    pass

class stack(StackLayout):
    def __int__(self, **kwargs):
        super().__init__(**kwargs)
        for i in range(30):
            b1 = Button(text=str(i+1), sice_hint=(None, None), size=(100, 100))
            self.add_widget(b1)

#App Creation
class TestApp(App):
    pass
TestApp().run()