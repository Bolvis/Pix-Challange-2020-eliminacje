arrow.pen.on = False
arrow.position = Vector(100,-100)
arrow.pen.on = True
top_y = 100
bot_y = -100
left_x = - 100
right_x = 100
for index in range(20):
	top_y -= 5
	arrow.position = Vector(right_x,top_y)
	left_x += 5
	arrow.position = Vector(left_x,top_y)
	bot_y += 5
	arrow.position = Vector(left_x,bot_y)
	right_x -= 5
	arrow.position = Vector(right_x,bot_y)