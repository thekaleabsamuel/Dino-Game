from ursina import *
app = Ursina()

window.color = color.white

dino = Entity(model='quad', texture='assets/dino.png', collider='box', x=-5)

ground1 = Entity(model='quad', texture="assets/ground.gif", scale=(50,1))

camera.orthographic = True
camera.fov = 10

app.run()