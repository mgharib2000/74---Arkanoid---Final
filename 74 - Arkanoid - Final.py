import pygame
from random import randrange as rnd

WIDTH, HEIGHT = 1200, 600

#paddle settings
paddle_width = 150
paddle_height = 30
paddle_speed = 10
paddle = pygame.Rect(WIDTH // 2 - paddle_width // 2, HEIGHT - paddle_height - 10, paddle_width, paddle_height)

#ball settings
ball_radius = 15
ball_speed = 5
ball_rect = int(ball_radius * 2 ** 0.5)
vel_x, vel_y = 1, -1

#block settings
block_list = [pygame.Rect(10 + 120 * i, 10 + 70 * j, 100, 35) for i in range(10) for j in range(8)]
colors = [(rnd(30, 256), rnd(30, 256), rnd(30, 256)) for i in range(10) for j in range(8)]


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

#background
bg = pygame.image.load("stars_bg_pexel.jpg").convert()



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    screen.blit(bg, (0, 0))

    # Draw world

    [pygame.draw.rect(bg, colors[color], block) for color, block in enumerate(block_list)]
    pygame.draw.rect(bg, pygame.Color("white"), paddle)
    #pygame.draw.circle(bg, pygame.Color("blue"), ball.center, ball.radius)
    """

    # Ball movement
    ball.x += ball_vel * vel_x
    ball.y += ball_vel * vel_y

    # Side collision
    if ball.center_x < ball_radius or ball_center_x > WIDTH - ball_radius:
        vel_x = -vel_x

    # Vertical collision
    if ball.center_y < ball_radius:
        vel_y = -vel_y

    # Paddle collision
    if ball.colliderect(paddle) and vel_y > 0:
        vel_x, vel_y = detect_collision(vel_x, vel_y, ball, paddle)

    # Collision blocks

    # Win, Game Over
    if ball.bottom > HEIGHT:
        print("GAME OVER!")
        exit()

    elif not len(block_list):
        print("YOU HAVE WON!")
        exit()
    """

    # Controls

    # Update screen
    pygame.display.flip()
    clock.tick(60)
    
