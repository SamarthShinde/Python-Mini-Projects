import pygame
import random

# Initialize pygame
pygame.init()

# Set up display
width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Fashionable Snake Game")

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Snake class
class Snake:
    def __init__(self):
        self.body = [(width//2, height//2)]
        self.direction = (1, 0)

    def move(self):
        head = self.body[-1]
        new_head = (head[0] + self.direction[0]*10, head[1] + self.direction[1]*10)
        self.body.append(new_head)
        self.body.pop(0)

    def grow(self):
        tail = self.body[0]
        new_tail = (tail[0] - self.direction[0]*10, tail[1] - self.direction[1]*10)
        self.body.insert(0, new_tail)

    def draw(self):
        for segment in self.body:
            pygame.draw.rect(window, GREEN, (*segment, 10, 10))
            pygame.draw.ellipse(window, GREEN, (*segment, 10, 10))

# Food class
class Food:
    def __init__(self):
        self.position = (random.randrange(0, width, 10), random.randrange(0, height, 10))

    def draw(self):
        pygame.draw.rect(window, RED, (*self.position, 10, 10))

# Initialize game objects
snake = Snake()
food = Food()

clock = pygame.time.Clock()
score = 0

font = pygame.font.Font(None, 36)

def display_score(score):
    score_text = font.render("Score: " + str(score), True, GREEN)
    window.blit(score_text, (10, 10))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.direction = (0, -1)
            elif event.key == pygame.K_DOWN:
                snake.direction = (0, 1)
            elif event.key == pygame.K_LEFT:
                snake.direction = (-1, 0)
            elif event.key == pygame.K_RIGHT:
                snake.direction = (1, 0)

    snake.move()

    if snake.body[-1] == food.position:
        food = Food()
        snake.grow()
        score += 10

    if (snake.body[-1][0] < 0 or snake.body[-1][0] >= width or
        snake.body[-1][1] < 0 or snake.body[-1][1] >= height):
        display_score(score)
        pygame.display.update()
        pygame.time.wait(2000)
        pygame.quit()
        quit()

    for segment in snake.body[:-1]:
        if segment == snake.body[-1]:
            display_score(score)
            pygame.display.update()
            pygame.time.wait(2000)
            pygame.quit()
            quit()

    window.fill(WHITE)
    snake.draw()
    food.draw()
    display_score(score)
    pygame.display.update()
    clock.tick(15)

