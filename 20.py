index = 0
for y in range(95,-100,-5):
	index += 1 if y >= 0 else -1
	for x in range(index):
		sprite = Sprite()
		sprite.image = 63
		sprite.size = 5
		if y % 2 == 1:
			sprite.position = Vector((x * -5) -5,y) if x % 2 == 0 else Vector(x * 5,y)
		else:
			sprite.position = Vector((x * -5) -5,y) if x % 2 == 1 else Vector(x * 5,y)
		game.add(sprite)