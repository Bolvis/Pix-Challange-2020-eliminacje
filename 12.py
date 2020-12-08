for y in range(-90,110,20):
	for x in range(-90,110,20):
		sprite = Sprite()
		if x <= y:
			sprite.color = Color(0,255,0)
			sprite.image = 2
		else:
			sprite.color = Color(255,0,0)
			sprite.image = 3
		sprite.size = 10
		sprite.position = Vector(x,y)
		game.add(sprite)