# PingPong

This is a basic implementation of the Atari Pong game, but it's missing a few things intentionally and they're left as further exploration for the reader.
## Further Exploration
### Score
When a ball goes past a paddle, the other player should score a point. After every frame score is updated for both the player. Geometry and co-ordinates are important characterstics of the movement of the ball. It natigates the ball which direction should be choosen and some restriction code, so that ball moves back whenever it touches any of the paddle.
### Ball trajectory
The ball should change trajectory based on where it hit the paddle. For example, if it hit the topmost part of the paddle it should have a sharp angle upward, whereas if it hit the direct middle of the paddle it should move completely flat towards the other payer.
### Paddles
There are two paddles placed at left and right side, the player can move them by using keyboard. When one player reaches the winning score the game ends. Now, the paddles can no longer be moved.
## Library Used
Tkinter library is one the best python library to implement GUI. In this project, Interface is provided by using the same library and logics are all coded in python programming language. 
