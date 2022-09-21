from multiprocessing import Pipe
import pygame 
import os


WIDTH, HEIGHT= 600, 600
Title = "AI Flappy Bird"
MAX_ROTATION = 25
VELOCITY = 20
TIME = 5
#make the image bigger then load it
Bird = [ 
        pygame.transform.scale2x(pygame.image.load(
            os.path.join("/Users/hamzaboualam/Downloads/Projects/Flappy Bird/AI-Flappy-bird/imgs", "bird1.png"))),
        pygame.transform.scale2x(pygame.image.load(
            os.path.join("/Users/hamzaboualam/Downloads/Projects/Flappy Bird/AI-Flappy-bird/imgs", "bird2.png"))),
        pygame.transform.scale2x(pygame.image.load(
            os.path.join("/Users/hamzaboualam/Downloads/Projects/Flappy Bird/AI-Flappy-bird/imgs", "bird3.png")
            ))
        ]

pipe = pygame.transform.scale2x(pygame.image.load(os.path.join("/Users/hamzaboualam/Downloads/Projects/Flappy Bird/AI-Flappy-bird/imgs", "pipe.png")))
base = pygame.transform.scale2x(pygame.image.load(os.path.join("/Users/hamzaboualam/Downloads/Projects/Flappy Bird/AI-Flappy-bird/imgs", "base.png")))
background = pygame.transform.scale2x(pygame.image.load(os.path.join("/Users/hamzaboualam/Downloads/Projects/Flappy Bird/AI-Flappy-bird/imgs", "bg.png")))