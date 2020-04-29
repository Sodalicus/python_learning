#!/usr/bin/env python3

from livewires import games,color
import random

games.init()
class Application():
    aliens = 0
    def __init__(self):
        background = games.load_image("background.bmp", transparent=False)
        games.screen.background = background


    def main(self):
        player = Player()
        games.screen.add(player)
        alien = Alien()
        games.screen.add(alien)
        games.mouse.is_visible = False
        games.screen.event_grab = True
        games.screen.mainloop()


class Player(games.Sprite):
    image = games.load_image("ball.bmp")
    def __init__(self):
        super(Player, self).__init__(image = Player.image,
                                    x = games.screen.width/2,
                                    y = games.screen.height/2)
        Application.aliens = 1
        self.time = 0
        self.lost = 0

        self.timex = games.Text(value = self.time,
                            size = 50,
                            color = color.black,
                            top = 5,
                            left = 10)
        games.screen.add(self.timex)

    def update(self):
        self.x = games.mouse.x
        self.y = games.mouse.y
        if Application.aliens < 50:
            games.screen.add(Alien())
            Application.aliens +=1
        if self.overlapping_sprites and not self.lost:
            self.lost = 1
            text = "Przegrałeś! " + str(self.timex.value)
            end_message = games.Message(value = text,
                                        size = 90,
                                        color = color.black,
                                        x = games.screen.width/2,
                                        y = games.screen.height/2,
                                        lifetime = games.screen.fps,
                                        after_death = games.screen.quit)
            games.screen.add(end_message)
        self.time += 1/50
        self.timex.value = int(self.time)
        self.timex.left = 10


class Alien(games.Sprite):
    image = games.load_image("alien.bmp")
    def __init__(self):
        super(Alien, self).__init__(image = Alien.image,
                                    x = random.randrange(games.screen.width),
                                    y = 0,
                                    dy = random.randrange(1,6))

    def update(self):
        if self.bottom >= games.screen.height-1: 
            self.destroy()
            Application.aliens -=1

app = Application()
app.main()

