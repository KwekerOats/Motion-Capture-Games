import pygame
import random
import sys
import time
        
def pong_game():
    
    height = 400
    width = 1000

    
    class paddle(pygame.Rect):
        def __init__(self, velocity, up_key, down_key, *args, **kwargs):
            self.velocity = velocity
            self.up_key = up_key
            self.down_key = down_key
            super().__init__(*args, **kwargs)

        def move_paddle(self, board_height):
            keys_pressed = pygame.key.get_pressed()

            if keys_pressed[self.up_key]:
                if self.y - self.velocity > 0:
                    self.y -= self.velocity

            if keys_pressed[self.down_key]:
                if self.y + self.velocity < board_height - self.height:
                    self.y += self.velocity

    class ball(pygame.Rect):
        def __init__(self, velocity, *args, **kwargs):
            self.velocity = velocity
            self.angle = 0
            super().__init__(*args, **kwargs)

        def move_ball(self):
            self.x += self.velocity
            self.y += self.angle


    class pong:

        height = 400
        width = 1000

        p1_score = 0
        p2_score = 0

        paddle_width = 10
        paddle_height = 100

        ball_width = 10
        ball_velocity = 10

        colour = (255,255,255)
        
        def wall_hit_check(self):
            for ball in self.balls:
                if ball.x > self.width:
                    self.p2_score += 1
                    #self.game_loop()
                elif ball.x < 0:
                    self.p1_score += 1
                    #self.game_loop()
                if ball.y > self.height - self.ball_width or ball.y <0:
                    ball.angle = -ball.angle

        def paddle_hit_check(self):
            for ball in self.balls:
                for paddle in self.paddles:
                    if ball.colliderect(paddle):
                        ball.velocity = -ball.velocity
                        ball.angle = random.randint(-10, 10)
                        break

        def __init__(self):
            pygame.init()

            self.screen = pygame.display.set_mode((self.width, self.height))
            self.clock = pygame.time.Clock()

            self.paddles = []
            self.balls = []
            self.paddles.append(paddle(
                self.ball_velocity,
                pygame.K_w,
                pygame.K_s,
                0,
                self.height / 2 - self.paddle_height / 2,
                self.paddle_width,
                self.paddle_height
            ))

            self.paddles.append(paddle(
                self.ball_velocity,
                pygame.K_UP,
                pygame.K_DOWN,
                self.width - self.paddle_width,
                self.height / 2 - self.paddle_height / 2,
                self.paddle_width,
                self.paddle_height
            ))

            self.balls.append(ball(
                self.ball_velocity,
                self.width / 2 - self.ball_width / 2,
                self.height / 2 - self.ball_width / 2,
                self.ball_width,
                self.ball_width
            ))



        def game_loop(self):

            #pong game window setup
            basicfont = pygame.font.SysFont(None, 48)
            KP = basicfont.render('Kwong Pong', True, (255, 255, 255), (0, 0, 0))
            KPr = KP.get_rect()
            KPr.centerx = self.screen.get_rect().centerx
            KPr.centery = 30

            p1gi = basicfont.render(str(self.p1_score), True, (255, 255, 255), (0, 0, 0))
            p1gir = p1gi.get_rect()
            p1gir.centerx = 30
            p1gir.centery = 30
            p2gi = basicfont.render(str(self.p1_score), True, (255, 255, 255), (0, 0, 0))
            p2gir = p2gi.get_rect()
            p2gir.centerx = 970
            p2gir.centery = 30            
              
            #main game loop for basic pong
            while True:
                for event in pygame.event.get():
                    if event in pygame.event.get():
                        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                            return

                self.screen.fill((0, 0, 0))


                self.wall_hit_check()
                self.paddle_hit_check()
                self.screen.blit(KP, KPr)
                self.screen.blit(p1gi, p1gir)
                self.screen.blit(p2gi, p2gir)

                for ball in self.balls:
                    ball.move_ball()
                    pygame.draw.rect(self.screen, self.colour, ball)

                for paddle in self.paddles:
                    paddle.move_paddle(self.height)
                    pygame.draw.rect(self.screen, self.colour, paddle)

                pygame.display.flip()
                self.clock.tick(60)

    if __name__ == '__main__':
        pong = pong()
        pong.game_loop()
pong_game()
