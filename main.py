import time
from turtle import Screen
from snake import Snake
from food import SnakeFood
from snakescore import Score

chopa = Score()
robin = SnakeFood()
nami = Screen()
luffy = Snake()


nami.bgcolor("black")
nami.setup(width=600, height=600)
#nami.textinput(title="Welcome to snake game", prompt="Do you want play snake game")
nami.title("The snake game")
nami.tracer(0)

nami.listen()
nami.onkey(luffy.up, "Up")
nami.onkey(luffy.down, "Down")
nami.onkey(luffy.right, "Right")
nami.onkey(luffy.left, "Left")
is_move = True
while is_move:
    nami.update()
    time.sleep(0.1)
    luffy.move()
    # detect collosion with food
    if luffy.head.distance(robin) < 15:
        robin.refresh()
        chopa.increase_score()
        luffy.extent()
    # detect collosion with wall
    if luffy.head.xcor() > 280 or luffy.head.xcor() < -280 or luffy.head.ycor() > 280 or luffy.head.ycor() < -280:
        chopa.increase_high_score()
        luffy.reset()
    for segment in luffy.segment[1:]:
        if luffy.head.distance(segment) < 10:
            chopa.increase_high_score()
            luffy.reset()

nami.exitonclick()
