import pygame
import random

# Initialize pygame
pygame.init()

# Game constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PADDLE_WIDTH = 100
PADDLE_HEIGHT = 15
BALL_RADIUS = 10
CUP_RADIUS = 30
BALL_SPEED_X = 5
BALL_SPEED_Y = -5

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Initialize the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Cup Pong")

# Font for score
font = pygame.font.SysFont("Arial", 30)

# Ball class
class Ball:
    def __init__(self):
        self.x = SCREEN_WIDTH // 2
        self.y = SCREEN_HEIGHT // 2
        self.radius = BALL_RADIUS
        self.speed_x = BALL_SPEED_X
        self.speed_y = BALL_SPEED_Y

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

        # Bounce off walls
        if self.x <= 0 or self.x >= SCREEN_WIDTH:
            self.speed_x = -self.speed_x
        if self.y <= 0:
            self.speed_y = -self.speed_y

    def draw(self, screen):
        pygame.draw.circle(screen, WHITE, (self.x, self.y), self.radius)

# Paddle class
class Paddle:
    def __init__(self):
        self.width = PADDLE_WIDTH
        self.height = PADDLE_HEIGHT
        self.x = (SCREEN_WIDTH - self.width) // 2
        self.y = SCREEN_HEIGHT - 50

    def move(self, x):
        self.x = x - self.width // 2
        # Make sure the paddle stays within the screen
        if self.x < 0:
            self.x = 0
        elif self.x > SCREEN_WIDTH - self.width:
            self.x = SCREEN_WIDTH - self.width

    def draw(self, screen):
        pygame.draw.rect(screen, GREEN, (self.x, self.y, self.width, self.height))

# Cup class
class Cup:
    def __init__(self):
        self.x = random.randint(100, SCREEN_WIDTH - 100)
        self.y = 50
        self.radius = CUP_RADIUS

    def draw(self, screen):
        pygame.draw.circle(screen, RED, (self.x, self.y), self.radius)

# Game loop
def game_loop():
    paddle = Paddle()
    ball = Ball()
    cup = Cup()

    score = 0
    running = True
    clock = pygame.time.Clock()

    while running:
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Get mouse position to move the paddle
        mouse_x, _ = pygame.mouse.get_pos()
        paddle.move(mouse_x)

        # Move the ball
        ball.move()

        # Check for ball hitting the cup
        if (cup.x - cup.radius < ball.x < cup.x + cup.radius) and (cup.y - cup.radius < ball.y < cup.y + cup.radius):
            score += 1
            ball = Ball()  # Reset the ball after scoring
            cup = Cup()  # Move the cup to a new location

        # Draw everything
        paddle.draw(screen)
        ball.draw(screen)
        cup.draw(screen)

        # Draw score
        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()

# Start the game
game_loop()
