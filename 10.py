arrow.pen.on = False
arrow.pen.size = 0.5
arrow.pen.color = Color(0,255,0)
for i in range(-11,1):
	arrow.pen.on = False
	arrow.position = Vector(0,-i*10)
	arrow.pen.on = True
	arrow.position = Vector(-110+(-i*10),0)
arrow.pen.color = Color(0,0,255)
for i in range(-11,1):
	arrow.pen.on = False
	arrow.position = Vector(0,i*10)
	arrow.pen.on = True
	arrow.position = Vector(-110+(-i*10),0)
arrow.pen.color = Color(0,0,0)
for i in range(-11, 1):
	arrow.pen.on = False
	arrow.position = Vector(0,i*10)
	arrow.pen.on = True
	arrow.position = Vector(110+(i*10),0)
arrow.pen.color = Color(255,0,0)
for i in range(-11,1):
	arrow.pen.on = False
	arrow.position = Vector(0,-i*10)
	arrow.pen.on = True
	arrow.position = Vector(110+(i*10),0)