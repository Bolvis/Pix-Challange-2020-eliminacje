import math
for step in range(90,432,36):
	sprite = Sprite()
	sprite.size = 25
	sprite.image = 24
	sprite.angle = step - 90
	sprite.position = Vector(50*math.cos(math.radians(step)),50*math.sin(math.radians(step)))
	game.add(sprite)