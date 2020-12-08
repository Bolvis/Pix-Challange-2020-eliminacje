for y in range(-90,100,10):
	for x in range(-90,100,10):
		ball = Sprite()
		ball.size = 10
		ball.image = 51
		ball.position = Vector(x,y)
		game.add(ball)