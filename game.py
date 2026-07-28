import pygame
import random

pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("CRAFT")

RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

paddle_width = 120
paddle_height = 15

paddle_y = HEIGHT - 50
paddle_x = (WIDTH - paddle_width) // 2
paddle_speed = 10

ball_x = random.randint(80, WIDTH - 80)
ball_y = 50
ball_speed = 6
ball_radius = 25

score = 0
font = pygame.font.Font(None, 30)

clock = pygame.time.Clock()
running = True

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        paddle_x = paddle_x - paddle_speed

    if keys[pygame.K_RIGHT]:
        paddle_x = paddle_x + paddle_speed

    if paddle_x < 0:
        paddle_x = 0

    if paddle_x > WIDTH - paddle_width:
        paddle_x = WIDTH - paddle_width

    # Move ball downward
    ball_y = ball_y + ball_speed

    # Ball caught by paddle
    if (ball_y + ball_radius >= paddle_y and
        ball_y - ball_radius <= paddle_y + paddle_height and
        paddle_x <= ball_x <= paddle_x + paddle_width):

        score += 1
        ball_x = random.randint(80, WIDTH - 80)
        ball_y = 50

    # Ball missed
    if ball_y - ball_radius > HEIGHT:
        score -= 1
        ball_x = random.randint(80, WIDTH - 80)
        ball_y = 50

    # End game if score becomes negative
    if score < 0:
        running = False

    screen.fill(BLACK)

    pygame.draw.rect(
        screen,
        BLUE,
        (paddle_x, paddle_y, paddle_width, paddle_height)
    )

    pygame.draw.circle(
        screen,
        RED,
        (int(ball_x), int(ball_y)),
        ball_radius
    )

    s_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(s_text, (30, 30))

    pygame.display.update()

# Game Over Screen
screen.fill(BLACK)

game_over_text = font.render(
    f"Game Over! Final Score: {score}",
    True,
    WHITE
)

screen.blit(
    game_over_text,
    (WIDTH // 2 - 120, HEIGHT // 2)
)

pygame.display.update()
pygame.time.delay(3000)

pygame.quit()