from kivy.app import App
from kivy.core.window import Window
from kivy.uix.widget import Widget

Window.size = (375, 560)


class MyInterface(Widget):
    def Start_pressing(self, start_img, SM):
        start_img.source = 'imagens/Pressed_Start_Btn.png'
        if(SM.current == "backgroung_2" or SM.current == "backgroung_3"):
            SM.transition.direction = "right"
        SM.current = "background_1"


    def Start_release(self, start_img):
        start_img.source = 'imagens/Start_Btn.png'



    def Stats_pressing(self, stats_img, SM):
        stats_img.source = 'imagens/Pressed_Stats_Btn.png'
        if (SM.current == "backgroung_1"):
            SM.transition.direction = "left"
        if (SM.current == "backgroung_3"):
            SM.transition.direction = "right"
        SM.current = "background_2"


    def Stats_release(self, stats_img):
        stats_img.source = 'imagens/Stats_Btn.png'


    def Likes_pressing(self, likes_img, SM):
        likes_img.source = 'imagens/Pressed_Likes_Btn.png'
        if(SM.current == "backgroung_1" or SM.current == "backgroung_2"):
            SM.transition.direction = "left"
        SM.current = "background_3"


    def Likes_release(self, likes_img):
        likes_img.source = 'imagens/Likes_Btn.png'


class CustomApp(App):
    pass


CustomApp().run()

