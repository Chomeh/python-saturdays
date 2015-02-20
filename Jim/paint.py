from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse

# Simple paint application.
# Draws yellow circles wherever that screen is touched
# See http://kivy.org/docs/tutorials/firstwidget.html

class MyPaintWidget(Widget):
    def on_touch_down(self, touch):
        print(touch)
        d = 30.
        self.canvas.add(Color(1, 1, 0))
        self.canvas.add(Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d)))

class MyPaintApp(App):
    def build(self):
        return MyPaintWidget()

MyPaintApp().run()





