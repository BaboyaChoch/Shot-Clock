#ShotClock

## Inspiration

ShotClock is simple game based on 'catching' falling objects with increasing speeds.

This game was inspired by a catching the fruit flash game. 
This flash game featured falling fruits that had to be caught with a basket.

ShotClock is a basketball take on this old flash game. 
In ShotClock the fruits are basketballs and the basket is a basketball hoop. 

## Objective/Rules

The objective of ShotClock is to make as many shots as possible in the alloted 60 seconds countdown. 
    * A Shot in ShotClock is defined as a falling object, the balls, making contact with the hoop.  
    * A shot is registed as a point, +1 to the player's score. 

The hoop is fixed on the x axis, can only move from left to right.
    * Left right movement is controlled by keyboard inputs
        * A controls movement to the left
        * D controls movement to the right

The player has no control over the falling objects

## Falling Objects(Balls) Logic

Falling objects logic is the result of a few simple steps(WIDTHxHEIGHT is the window size):
    * 1: At the start, spawn (n) number of balls, from a list of balls, at the top of the screen, y = 0, with random x values on the screen accounting for ball size, x = {20,WIDTH-20}.

    * 2: Each ball is spawned with its own speed, and its Y position is updated to make the ball 'fall', ball.y += speed

    * 3: The ball continues to fall unless it:
        * (a) Makes contact with the hoop and is a shot (+1 to score).
        * (b) Goes off screen, ball.y > HEIGHT.

    * 4: After the ball is a made shot or goes off screen it is not cleared from the display, but is respawned at the top of the screen as a 'new' ball.
    
What this means is that the falling balls effect is created by the continues looping of the same (n) number of balls.

For this project n = 4 for a screen of size 600x400, so list of game balls only as has a length of n, 4. 
    * n < 4 doesnt fill up the screen enough 
    * n > 4  clutters the screen and results in a more overlapping.
    * n is dependant on screen size

This is methodworks well, nut begins to fall apart when the screen/window size is increased—resulting in more balls, which results in a longer list. 