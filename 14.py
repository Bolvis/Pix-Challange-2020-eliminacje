for y in range(-90,110,20):
	for x in range(-90,110,20):
		sprite = Sprite()
		sprite.color = Color(255,0,0)
		sprite.size = 10
		sprite.image = 66
		sprite.position = Vector(x,y)
		sprite.angle= x - y
		game.add(sprite)