index = 1
for y in range(90,-110,-20):
	for x in range(-90,110,20):
		sprite = Sprite()
		if index % 3 == 0:
			sprite.color = Color(255,0,0)
		sprite.size = 10
		sprite.text = str(index)
		sprite.position = Vector(x,y)
		index += 1
		game.add(sprite)