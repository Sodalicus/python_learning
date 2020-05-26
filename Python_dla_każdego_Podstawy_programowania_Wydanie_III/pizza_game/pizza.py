#!/usr/bin/env python3

from livewires import games, color
import random



games.init(screen_width = 640, screen_height = 480, fps = 50)

class Game():
    difficult = 0
    def __init__(self):
        pass
    def main(self):
        wall_image = games.load_image("sciana.jpg", transparent = False)
        games.screen.background = wall_image


        the_pan = Pan()
        games.screen.add(the_pan)

        games.mouse.is_visible = False

        games.screen.event_grab = True
        games.screen.mainloop()
        



class Pan(games.Sprite):
    image = games.load_image("patelnia.bmp")
    def __init__(self):
        super(Pan, self).__init__(image = Pan.image,
                                x = games.mouse.x,
                                bottom = games.screen.height)
        self.seconds = 0
        self.time_to_display = 0
        self.chefs_number = 0
        self.display_values()
        self.spawn_chef()

    def display_values(self):

        self.time = games.Text(value = self.seconds, size = 25, color = color.black,
                top = 5, left = 10)
        games.screen.add(self.time)

        self.score = games.Text(value = 0, size = 25, color = color.black,
                top = 5, right = games.screen.width - 10)
        games.screen.add(self.score)

        self.difficulty = games.Text(value = Game.difficult, size = 25, color = color.black,
                top = 25, left = 10)
        games.screen.add(self.difficulty)

    def update(self):
        self.x = games.mouse.x
        if self.left < 0: self.left = 0
        if self.right > games.screen.width: self.right = games.screen.width

        self.seconds += 1/50
        self.time_to_display = "Time: "+str(int(self.seconds))
        self.time.value = self.time_to_display
        self.time.left = 10

        self.check_catch()
        self.set_difficulty()
        if Game.difficult == 3 and self.chefs_number <2:
            self.spawn_chef()

    def set_difficulty(self):
        if int(self.seconds) > 10: 
            Game.difficult = 1
            self.difficulty.value = "Difficulty: "+str(Game.difficult)
            self.difficulty.left = 10 
        if int(self.seconds) > 15:
            Game.difficult = 2
            self.difficulty.value = "Difficulty: "+str(Game.difficult)
            self.difficulty.left = 10
        if int(self.seconds) > 20:
            Game.difficult = 3
            self.difficulty.value = "Difficulty: "+str(Game.difficult)
            self.difficulty.left = 10


    def check_catch(self):
        for pizza in self.overlapping_sprites:
            self.score.value += 10
            self.score.right = games.screen.width - 10
            pizza.handle_caught()

    def spawn_chef(self):
            games.screen.add(Chef())
            self.chefs_number +=1



class Pizza(games.Sprite):
    image = games.load_image("pizza.bmp")

    def __init__(self, x , dy, y = 90):
        super(Pizza, self).__init__(image = Pizza.image,x = x,
                y = y, dy = dy)
    def update(self):
        if self.bottom > games.screen.height:
            self.end_game()
            self.destroy()

    def handle_caught(self):
        self.destroy()

    def end_game(self):
        end_message = games.Message(value = "Koniec gry",
                                            size = 90,
                                            color = color.red,
                                            x = games.screen.width/2,
                                            y = games.screen.height/2,
                                            lifetime = 5*games.screen.fps,
                                            after_death = games.screen.quit)
        games.screen.add(end_message)

class Chef(games.Sprite):
    image = games.load_image("kucharz.bmp")

    def __init__(self, y = 55, speed = 2, odds_change = 200):
        super(Chef, self).__init__(image = Chef.image, 
                                    x = games.screen.width/2,
                                    y = y,
                                    dx = speed)
        self.odds_change = odds_change
        self.time_til_drop = 0
        self.pizza_speed = 1
        self.pizza_height = 90
    
    def update(self):
        if self.left < 0 or self.right > games.screen.width:
            self.dx = -self.dx
        elif random.randrange(self.odds_change) == 0:
            self.dx = -self.dx

        self.check_drop()
        if Game.difficult >= 1:
            self.pizza_speed = 2
        if Game.difficult >= 2:
            self.pizza_height = 180
            

    def check_drop(self):
        if self.time_til_drop > 0:
            self.time_til_drop -= 1
        else:
            new_pizza = Pizza(x = self.x, dy = self.pizza_speed, y = self.pizza_height)
            games.screen.add(new_pizza)
            #self.time_til_drop = int(new_pizza.height*1.3/self.pizza_speed)+1
            self.time_til_drop = int(new_pizza.height*1.3/1)+1


game = Game()
game.main()

