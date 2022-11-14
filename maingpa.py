from kivy.core.window import Window
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen


class HomePage(MDScreen):
    pass
        

class MainApp(MDApp):
    def build(self):
        Window.size = [300, 600]
        self.theme_cls_primary_palette = "LightBlue"
        Builder.load_file('ScreensDesign.kv')
        return HomePage()


if __name__ == "__main__":
    MainApp().run()
