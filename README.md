# ShotClock


## Objective & Rules

The objective of ShotClock is to make as many shots as possible in the alloted 60 seconds countdown. 

* A Shot in ShotClock is defined as a falling object, the balls, making contact with the hoop.
    
* A shot is registed as a point, +1 to the player's score. 

The hoop is fixed on the x axis, can only move from left to right.

* Left right movement is controlled by keyboard inputs
    
    * A controls movement to the left
        
    * D controls movement to the right

The player has no control over the falling objects

## Falling Objects(Balls) Logic

```python
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
                new_ball(i

```

The logic behind the falling objects is the result of a few simple steps (Note: WIDTHxHEIGHT is the window size):

1. At the start, spawn (n) number of balls, from a list of balls, at the top of the screen, y = 0, with random x values on the screen accounting for ball size, x = {20,WIDTH-20}.

2. Each ball is spawned with its own speed, and its Y position is updated to make the ball 'fall', ball.y += speed

3. The ball continues to fall unless it:
    * (a) Makes contact with the hoop and is a shot (+1 to score).
    
    * (b) Goes off screen, ball.y > HEIGHT.

4. After the ball is registered as a made shot or goes off screen it is not cleared from the display, but is respawned at the top of the screen as a 'new' ball.
    

What this means is that the falling balls effect is created by the continues looping of the same (n) number of balls.
For this project n = 4 for a screen of size 600x400, so list of game balls only as has a length of n, 4.

    * n < 4 doesnt fill up the screen enough 
    
    * n > 4  clutters the screen and results in a more overlapping.
    
    * n is dependant on screen size

This is method works well, but begins to fall apart when the screen/window size is increased—resulting in more balls, which results in a longer list. 
