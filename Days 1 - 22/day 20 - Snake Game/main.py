from screen import CreateScreen
from snake import CreateSnake
import time
screen = CreateScreen()
snake = CreateSnake()


    


screen.screen.listen()
screen.screen.onkey(snake.up , "Up")    
screen.screen.onkey(snake.down , "Down")    
screen.screen.onkey(snake.left , "Left")    
screen.screen.onkey(snake.right , "Right")    

is_game_on = True
while is_game_on:
    screen.screen.update()
    time.sleep(0.1)
    snake.moveSnake()

screen.screen.exit_on_click()
