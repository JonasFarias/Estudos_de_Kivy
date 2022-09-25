from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout


class LogicalInterface(BoxLayout):
    def OnPressing(self, ID, input):
        print('Oi')
        ID.text = input.text

    def OnRelease(self, ID, input):
        print('ah')




class TestApp(App):
    pass

TestApp().run()