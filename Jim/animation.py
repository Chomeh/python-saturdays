from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse
from kivy.clock import Clock

# A very simple animation example

#Create widget object
widget = Widget()

#Program variables
diameter=30
x=100.
y=100.

#Create drawing objects and add to the widget's canvas
color = Color(1,0,0)
ellipse = Ellipse(size=(diameter, diameter))
widget.canvas.add(color)
widget.canvas.add(ellipse)

#represents one animation iteration
def animation(deltaTime):
    global x
    global y

    x = x + 1
    y = y + 1
    ellipse.pos=(x - diameter / 2, y - diameter / 2)

#ask kivy to call the 'animation' function 60 times a second
Clock.schedule_interval(animation, 1.0/60.0)

myApp = App()
myApp.root = widget
myApp.run()