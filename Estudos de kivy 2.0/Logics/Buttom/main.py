from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout


class LogicalInterface(BoxLayout):
    def OnPressing(self):
        print('Oi')
    def OnRelease(self):
        print('ah')




class TestApp(App):
    pass

TestApp().run()