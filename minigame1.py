import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 500, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dodge IT!")

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (200,0,0)
BLUE = (0,0,200)

player_size = 50
player = pygame.Rect(WIDTH/2, HEIGHT-60, player_size, player_size)
 
enemy_size = 50
enemy = pygame.Rect(random.randint(0, WIDTH-enemy_size), 0, enemy_size, enemy_size)
enemy_speed = 15

clock = pygame.time.Clock()

score = 0
font = pygame.font.SysFont("Arial", 30)

while True:
  screen.fill(WHITE)

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()

  keys = pygame.key.get_pressed()
  if keys[pygame.K_LEFT] and player.right < WIDTH:
    player.move_ip(-7,0)
  if keys[pygame.K_RIGHT] and player.right < WIDTH:
    player.move_ip(7,0)

  enemy.move_ip(0, enemy_speed)
  if enemy.top > HEIGHT:
    enemy.x = random.randint(0, WIDTH-enemy_size)
    enemy.y = 0
    score += 1
  
  if player.colliderect(enemy):
    print("GAME OVER! FINAL SCORE: ", score)
    pygame.quit()
    sys.exit()
  
  pygame.draw.rect(screen, BLUE, player)
  pygame.draw.rect(screen, RED, enemy)
  
  score_text = font.render(f"Score: {score}", True, BLACK)
  screen.blit(score_text, (10,10))

  pygame.display.flip()
  clock.tick(30)