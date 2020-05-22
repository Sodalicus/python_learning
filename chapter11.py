#!/usr/bin/env python 

from livewires import games, color

games.init(screen_width = 640, screen_height = 480, fps = 50)

wall_image = games.load_image("sciana.jpg", transparent = False)

games.screen.background = wall_image

score = games.Text(value = 544877,
        size = 60,
        color = color.black,
        x = 550,
        y = 30)

games.screen.add(score)

pizza_image = games.load_image("pizza.bmp")

pizza = games.Sprite(image = pizza_image, x = 320, y = 240)

games.screen.add(pizza)

games.screen.mainloop()
