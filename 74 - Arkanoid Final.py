import pygame
from random import randrange as rnd

pygame.init()

#Screen settings
WIDTH, HEIGHT = 1200, 600
fps = 60
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
bg = pygame.image.load("stars_bg_pexel.jpg").convert()

#Paddle settings
paddle_width = 150
paddle_height = 30
paddle_vel = 10
paddle = pygame.Rect(WIDTH // 2 - paddle_width // 2, HEIGHT - paddle_height - 10, paddle_width, paddle_height)

#Ball settings
ball_radius = 15
ball_vel = 5
ball_rect = int(ball_radius * 2 ** 0.5)
ball = pygame.Rect(rnd(ball_rect, WIDTH - ball_rect), HEIGHT // 2, ball_rect, ball_rect)
vel_x, vel_y = 1, -1

#Block settings
block_list = [pygame.Rect(10 + 120 * i, 10 + 60 * j, 100, 35) for i in range(10) for j in range(8)]
colors = [(rnd(30, 256), rnd(30, 256), rnd(30, 256)) for i in range(10) for j in range(8)]


def detect_collision(vel_x, vel_y, ball, rect):
    if vel_x > 0:
        vel_x_new = ball.right - rect.left
    else:
        vel_x_new = rect.right - ball.left

    if vel_y > 0:
        vel_y_new = ball.bottom - rect.top
    else:
        vel_y_new = rect.bottom - ball.top

    if abs(vel_x_new - vel_y_new) < 10:
        vel_x, vel_y = -vel_x, -vel_y

    elif vel_x_new > vel_y_new:
        vel_y = -vel_y

    elif vel_y_new > vel_x_new:
        vel_x = -vel_x

    return vel_x, vel_y


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    screen.blit(bg, (0, 0))

    #Draw world

    [pygame.draw.rect(screen, colors[color], block) for color, block in enumerate(block_list)]
    pygame.draw.rect(screen, pygame.Color("white"), paddle)
    pygame.draw.circle(screen, pygame.Color("blue"), ball.center, ball_radius)
    

    #Ball movement
    ball.x += ball_vel * vel_x
    ball.y += ball_vel * vel_y

    #Side collision
    if ball.centerx < ball_radius or ball.centerx > WIDTH - ball_radius:
        vel_x = -vel_x

    #Vertical collision
    if ball.centery < ball_radius:
        vel_y = -vel_y

    #Paddle collision
    if ball.colliderect(paddle) and vel_y > 0:
        vel_x, vel_y = detect_collision(vel_x, vel_y, ball, paddle)

    #Collision blocks
    hit_index = ball.collidelist(block_list)
    if hit_index != -1:
        hit_rect = block_list.pop(hit_index)
        hit_color = colors.pop(hit_index)
        vel_x, vel_y = detect_collision(vel_x, vel_y, ball, hit_rect)

        #Special effect
        hit_rect.inflate_ip(ball.width * 2, ball.height * 2)
        pygame.draw.rect(screen, hit_color, hit_rect)
        fps += 1

    #Controls
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and paddle.left > 0:
        paddle.left -= paddle_vel

    if key[pygame.K_RIGHT] and paddle.right < WIDTH:
        paddle.right += paddle_vel

    #Win or Lose
    if ball.bottom > HEIGHT:
        print("GAME OVER!")
        exit()
        
    elif not len(block_list):
        print("YOU HAVE WON!")
        exit()
    
    #Update screen
    pygame.display.flip()
    clock.tick(fps)

