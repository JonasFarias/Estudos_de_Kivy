from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout


class My_ScreenManager(BoxLayout):

    def FirstBtn(self, SM):
        SM.current = 'second'

    def SecondBtn(self, SM):
        SM.current = 'first'


class TestApp(App):
    pass


TestApp().run()
