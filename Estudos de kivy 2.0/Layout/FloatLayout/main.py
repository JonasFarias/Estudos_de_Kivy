from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button

#interface
class Int(FloatLayout):
    def __int__(self, **kwargs):
        super().__init__(**kwargs)
        b1 = Button(text='Oi')
        self.add_widget(b1)






#App Creation
class TestApp(App):
    pass

TestApp().run()