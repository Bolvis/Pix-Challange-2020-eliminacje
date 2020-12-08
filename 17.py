import math
for step in range(0,360,6):
	arrow.angle = step
	arrow.pen.on= False
	arrow.position = Vector(20*math.cos(math.radians(step)),20*math.sin(math.radians(step)))
	arrow.pen.on= True
	for i in range(3):
		arrow.move(30)
		arrow.angle += 45
