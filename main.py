import pygame
pygame.init()
from class_ball import Ball
from class_paddle import Paddle
from class_bot import Bot

WIDTH,HEIGHT=700,500
PADDLE_HEIGHT,PADDLE_WIDTH=100,20
BALL_RADIUS=7
WIN=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Pong")
FPS=60
SCORE_FONT=pygame.font.SysFont("comicsans",30)

WHITE=(255,255,255)
BLACK=(0,0,0)

    
def draw(win,paddles,ball,left,right):
    win.fill(BLACK)
    lefttxt=SCORE_FONT.render(f'{left}',1,WHITE)
    righttxt=SCORE_FONT.render(f'{right}',1,WHITE)
    win.blit(lefttxt, (WIDTH//4-lefttxt.get_width()//2,20))
    win.blit(righttxt, (WIDTH*(3/4)-righttxt.get_width()//2,20))


    for paddle in paddles:
        paddle.draw(win)
    ball.draw(win)
    pygame.display.update()

def handle_collision(ball,left_paddle,right_paddle):
    if ball.y+ball.radius>=HEIGHT:
        ball.y_vel*=-1
    elif ball.y-ball.radius<=0:
        ball.y_vel*=-1
    
    if ball.x_vel<0:
        if ball.y>=left_paddle.y and ball.y<=left_paddle.y+left_paddle.height:
            if ball.x-ball.radius<=left_paddle.x+left_paddle.width:
                ball.x_vel*=-1
                
                middle_y=left_paddle.y+left_paddle.height/2
                difference_in_y=middle_y-ball.y
                reduction_factor=(left_paddle.height/2)/ball.MAX_VEL
                ball.y_vel=difference_in_y/reduction_factor*-1
    else:
        if ball.y>=right_paddle.y and ball.y<=right_paddle.y+right_paddle.height:
            if ball.x+ball.radius>=right_paddle.x:
                ball.x_vel*=-1

                middle_y=right_paddle.y+right_paddle.height/2
                difference_in_y=middle_y-ball.y
                reduction_factor=(right_paddle.height/2)/ball.MAX_VEL
                ball.y_vel=difference_in_y/reduction_factor*-1

def handle_paddle_movement(keys,left_paddle,right_paddle,ball_y):
    left_paddle.move(ball_y)

    if keys[pygame.K_UP] and right_paddle.y-right_paddle.VEL>=0:
        right_paddle.move(up=True)

    if keys[pygame.K_DOWN] and right_paddle.y+right_paddle.VEL+right_paddle.height<=HEIGHT:
        right_paddle.move(up=False)

def main():
    run=True
    clock=pygame.time.Clock()
    left_paddle=Bot(10,HEIGHT//2-PADDLE_HEIGHT//2,PADDLE_WIDTH,PADDLE_HEIGHT)
    right_paddle=Paddle(WIDTH-10-PADDLE_WIDTH,HEIGHT//2-PADDLE_HEIGHT//2,PADDLE_WIDTH,PADDLE_HEIGHT)
    ball=Ball(WIDTH//2,HEIGHT//2,BALL_RADIUS)

    left_score=0
    right_score=0
    while run:
        clock.tick(FPS)
        draw(WIN,[left_paddle,right_paddle],ball,left_score,right_score)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
                break
        keys=pygame.key.get_pressed()
        handle_paddle_movement(keys,left_paddle,right_paddle,ball.y)
        ball.move()
        handle_collision(ball,left_paddle,right_paddle)
        if ball.x<0:
            right_score+=1
            ball.reset()

        elif ball.x>WIDTH:
            left_score+=1
            ball.reset()

    
    pygame.quit()


if __name__=='__main__':
    main()