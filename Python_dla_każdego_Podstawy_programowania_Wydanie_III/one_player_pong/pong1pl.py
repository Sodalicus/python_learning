#!/usr/bin/env python3


#Solution to excercise 3 from chapter 11, from the book
#"Python programming for absolute beginner, 3rd edition"
#Author: Paweł Krzemiński
from livewires import games, color
games.init(screen_width = 640, screen_height = 480, fps = 50)

class Application():
    def __init__(self):
        pass
        background_image = games.load_image("background.bmp", transparent = False)
        games.screen.background = background_image

    def main(self):
        ball = Ball() 
        games.screen.add(ball)
        paddle = Paddle() 
        games.screen.add(paddle)
        games.mouse.is_visible = False

        games.screen.event_grab = True
 
        games.screen.mainloop()

class Ball(games.Sprite):
    image = games.load_image("ball.bmp")
    def __init__(self):
        super(Ball, self).__init__(image = Ball.image, x = games.screen.width/2,
                y = games.screen.height/2, dx = 1, dy = 1)

    def update(self):
        if self.top < 0 or self.bottom > games.screen.height: self.dy = -self.dy
        if self.left < 0 or self.right > games.screen.width: self.dx = -self.dx
        for sprite in games.screen.get_all_objects():
            if sprite !=  self:
                if self.right >= sprite.left and self.left <= sprite.right:
                    if self.bottom == sprite.top:
                        self.dy = -self.dy 
                if self.top >= sprite.top:
                    self.end_game()

    def end_game(self):
        end_message = games.Message(value = "Koniec gry",
                                    size = 90,
                                    color = color.black,
                                    x = games.screen.width/2,
                                    y = games.screen.height/2,
                                    lifetime = 5*games.screen.fps,
                                    after_death = games.screen.quit)
        games.screen.add(end_message)


class Paddle(games.Sprite):
    image = games.load_image("paddle.bmp")
    def __init__(self):
        super(Paddle, self).__init__(image = Paddle.image, 
                x = games.screen.width/2,
                y = games.screen.height - 40)

    def update(self):
        self.x = games.mouse.x
        if self.left < 0: self.left = 0
        if self.right > games.screen.width: self.right = games.screen.width

app = Application()
app.main()
