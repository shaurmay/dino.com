from ursina import *
import random
app = Ursina()

window.color = color.white

dino = Animation("dino/dinoo.gif", collider = "box", scale = (1,1,1), x = -5)

ground1 = Entity(model = "quad", texture = "dino/ground.gif", scale = (50, 0.5, 10), z = 1)
ground2 = duplicate(ground1, x=50)
pair = [ground1, ground2]

cactus = Entity(model="quad", texture = "dino/cactuss.png", scale = (0.8, 1, 0.8), x=20, collider = "box")
cacti = []

def NewCactus():
    new = duplicate(cactus, x = 10+random.randint(0,5))
    cacti.append(new)
    invoke(NewCactus, delay = 2)

NewCactus()

label = Text(text = f"Points: {0}", color = color.black, position = (-0.6, 0.4))
points = 0

def update():
    global points
    points += 1
    label.text = f"Points: {points}"
    
    for ground in pair:
        ground.x -= 6*time.dt 
        if ground.x < -35:
            ground.x += 100
    for c in cacti:
        c.x -= 6*time.dt 
    if dino.intersects().hit:
        application.pause()

def input(key):
    if key == "space":
        if dino.y < 0.01:
            dino.animate_y(2, duration = 0.4, curve = curve.out_sine)
            dino.animate_y(0, duration = 0.4, delay = 0.4, curve = curve.out_sine)


camera.orthographic = True
camera.fov = 10

app.run()