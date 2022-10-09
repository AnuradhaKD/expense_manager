from kivymd.app import MDApp
from kivy.core.window import Window

class MainApp(MDApp):
    def __init__(self, **kwargs):
            Window.size = (400,600)
            super().__init__()
            
MainApp().run()
            