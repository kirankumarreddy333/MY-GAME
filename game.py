import pygame
import random

pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("MY GAME")

RED = (255, 0, 0)
BLACK = (20, 20, 20)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

paddle_width = 120
paddle_height = 15

paddle_speed = 10
ball_speed = 6
ball_radius = 25

font = pygame.font.Font(None, 35)
title_font = pygame.font.Font(None, 70)
score_font = pygame.font.Font(None, 45)
small_font = pygame.font.Font(None, 35)

clock = pygame.time.Clock()

running = True

while running:

    # Reset Game
    paddle_x = (WIDTH - paddle_width) // 2
    paddle_y = HEIGHT - 50

    ball_x = random.randint(80, WIDTH - 80)
    ball_y = 50

    score = 0

    game = True

    # ---------------- GAME LOOP ----------------
    while game:

        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                game = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            paddle_x -= paddle_speed

        if keys[pygame.K_RIGHT]:
            paddle_x += paddle_speed

        if paddle_x < 0:
            paddle_x = 0

        if paddle_x > WIDTH - paddle_width:
            paddle_x = WIDTH - paddle_width

        # Move Ball
        ball_y += ball_speed

        # Catch Ball
        if (
            ball_y + ball_radius >= paddle_y
            and ball_y - ball_radius <= paddle_y + paddle_height
            and paddle_x <= ball_x <= paddle_x + paddle_width
        ):

            score += 1

            ball_x = random.randint(80, WIDTH - 80)
            ball_y = 50

        # Miss Ball
        if ball_y - ball_radius > HEIGHT:
            game = False

        # Draw Screen
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

        score_text = font.render(f"Score : {score}", True, WHITE)
        screen.blit(score_text, (20, 20))

        pygame.display.update()

    if not running:
        break

    # ---------------- GAME OVER SCREEN ----------------
    waiting = True

    while waiting:

        screen.fill(BLACK)

        title = title_font.render("GAME OVER", True, RED)
        final_score = score_font.render(f"Final Score : {score}", True, WHITE)
        play_again = small_font.render("Press SPACE to Play Again", True, GREEN)
        quit_game = small_font.render("Press ESC to Quit", True, YELLOW)

        screen.blit(title, title.get_rect(center=(WIDTH // 2, 170)))
        screen.blit(final_score, final_score.get_rect(center=(WIDTH // 2, 250)))
        screen.blit(play_again, play_again.get_rect(center=(WIDTH // 2, 340)))
        screen.blit(quit_game, quit_game.get_rect(center=(WIDTH // 2, 390)))

        pygame.display.update()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                waiting = False
                running = False

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_SPACE:
                    waiting = False

                if event.key == pygame.K_ESCAPE:
                    waiting = False
                    running = False

pygame.quit()