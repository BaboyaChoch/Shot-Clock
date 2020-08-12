import pygame
from random import randint

pygame.init()

#game window
WIDTH = 600
HEIGHT = 400
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shot Clock")
pygame.display.set_icon(pygame.image.load('icon.png'))

#gmae font
pygame.font.init()
GAME_FONT = pygame.font.Font('gamera.TTF', 35)

#game start and timing variables
game_start = False  # boolean that controls main loop
start_time = 0  # Start time for game timer
TIME_ALLOWED = 60  # amount of time player has (1 minute)


#ball properties
MAX_BALL_SPEED = 17
MIN_BALL_SPEED = 4

#game colors
BLACK = (0, 0, 0)
ORANGE = (252, 102, 0)

#sprites
HOOP = pygame.image.load('hoop.png')
BASKETBALL = pygame.image.load('ball.png')

class Ball:
    def __init__(self,x, y,vel):
        self.x = x
        self.y = y
        self.vel = vel

    def draw_ball(self, surface):
        surface.blit(BASKETBALL,(self.x, self.y))

    def update_position(self):
        self.y += self.vel

    def is_off_screen(self):
        return self.y > 420


# game start loop
def start_game():
    global game_start
    global start_time

    line1 = GAME_FONT.render("Make Shots! You Have 60s!!", True, ORANGE)
    line2 = GAME_FONT.render("Press SPACE To Start!!", True, ORANGE)
    line3 = GAME_FONT.render("ESC to Exit  R to Reset", True, ORANGE)
    line4 = GAME_FONT.render("A:Left   D:Right", True, ORANGE)

    win.blit(line1, (50, 50))
    win.blit(line2, (80, 130))
    win.blit(line3, (80, 210))
    win.blit(line4, (150, 290))

    pygame.display.update()

    while not game_start:

        if game_start:
            break

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_start = True
                    start_time = pygame.time.get_ticks()
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()


def is_time_left():
    return TIME_ALLOWED > int((pygame.time.get_ticks() - start_time) / 1000)

game_balls = [
    Ball(randint(30, 570), 0, randint(1, MAX_BALL_SPEED)),
    Ball(randint(30, 570), 0, randint(1, MAX_BALL_SPEED)),
    Ball(randint(30, 570), 0, randint(1, MAX_BALL_SPEED)),
    Ball(randint(30, 570), 0, randint(1, MAX_BALL_SPEED))
]

def new_ball(index):
    global MAX_BALL_SPEED
    global MIN_BALL_SPEED

    game_balls[index].x = randint(30, 570)
    game_balls[index].y = 0
    game_balls[index].vel = randint(MIN_BALL_SPEED, MAX_BALL_SPEED)

    if MIN_BALL_SPEED < MAX_BALL_SPEED:
        MIN_BALL_SPEED += 1

def main():

    global game_start
    global start_time
  
    hoop_x = 260
    hoop_y = 360

    hitbox_x = 280
    hitbox_y = 380

    clock = pygame.time.Clock()
    SCORE = 0  # player score
    
    start_game()
    if not game_start:
        print("\nYou Didn't Press Space :( ")
    else:
        print("\nGame starting....")

    while game_start and is_time_left():
        TIME_LEFT = TIME_ALLOWED -  int((pygame.time.get_ticks() - start_time) / 1000)
        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_start = False

        keys = pygame.key.get_pressed()

        # if press left(A):
        # move the basket to left (-1 to y value)
        if keys[pygame.K_a]:
            hoop_x -= 40
            hitbox_x -= 40
            # after moving the platform. if its x or y match those of the platform
            # they have collided/touched (the ball is caught) add one

        # if press right(D):
        # move the basket to the right(+1 to y value)
        if keys[pygame.K_d]:
            hoop_x += 30
            hitbox_x += 30

        # if press escape(ESC)
        # quit game
        if keys[pygame.K_ESCAPE]:
            print("Exiting Game......")
            game_start = False

        # if press reset(R)
        # resets timer to 60s
        if keys[pygame.K_r]:
            start_time = pygame.time.get_ticks()
            SCORE = 0

        win.fill((0, 0, 0))

        # basket/hoop
        win.blit(HOOP, (hoop_x,hoop_y))


        # balls
        # Loop the same (4) balls with a new speed and position each time they come back.
        # ball is looped after it registers as a point or falls off screen
        for i in range(4):

            if game_balls[i].is_off_screen():
                new_ball(i)

            game_balls[i].draw_ball(win)
            game_balls[i].update_position()

            # if any part of the hoop/platform is touched by a ball as a collision
            # ball is cleared from the display and new ball appears
            if (hitbox_y) < game_balls[i].y < (hitbox_y + 20) and (hitbox_x) < \
                    game_balls[i].x < (hoop_x + 120):
                    # hitbox is simplified to be 120x20 rectangle starting from the top left corner of the rim
                    # if a ball falls within this region it is considered a score.
                SCORE += 1
                new_ball(i)

        # prints time on screen
        time_tracker = GAME_FONT.render(F"Time:{TIME_LEFT}", True, ORANGE)
        win.blit(time_tracker, (455, 0))

        # prints score on screen
        score_tracker = GAME_FONT.render(F"Score:{SCORE}", True, ORANGE)
        win.blit(score_tracker, (0, 0))

        pygame.display.update()

    # End Game Loop
    # End screen lasts for 10 secs and exits automatically
    close_window = False
    while not close_window:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    close_window = True

                if event.key == pygame.K_r:
                    win.fill(BLACK)
                    main()

        win.fill(BLACK)

        game_over = GAME_FONT.render("Game Over!", True, ORANGE)
        win.blit(game_over, (215, 80))

        final_score = GAME_FONT.render(F"Final Score: {SCORE} ", True, ORANGE)
        win.blit(final_score, (185, 170))

        new_game = GAME_FONT.render("Press R to Start New Game", True, ORANGE)
        win.blit(new_game, (50,240))

        exit_game = GAME_FONT.render("Press ESC to Close Game", True, ORANGE)
        win.blit(exit_game, (50, 270))

        pygame.display.update()

    # gg
    pygame.quit()


if __name__ == "__main__":
     main()