from kivy.app import App
from kivy.uix.widget import Widget


class myAppGUI(Widget):
    pass



class myApp(App):
    def build(self):
        return myAppGUI()


if __name__ == "__main__":
    myApp().run()