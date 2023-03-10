import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, width, height, starting_x, starting_y):
        super().__init__()
        self.image = pygame.image.load(
            "toppng.com-white-penguin-flying-club-penguin-flying-pengui-962x768.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (width, height))
        self.image.set_colorkey((246, 246, 246))
        self.player_group = pygame.sprite.Group()
        self.player_group.add(self)
        self.rect = self.image.get_rect()
        self.rect.y = starting_y
        self.rect.x = starting_x
        self.velocity_x = 0
        self.velocity_y = 0
        self.control = True
        self.current_health = 1000
        self.maximum_health = 1000
        self.health_bar_length = 350
        self.health_ratio = self.maximum_health / self.health_bar_length

    def movement(self, key_input):
        self.rect.x += self.velocity_x
        self.rect.y += self.velocity_y

        if key_input[(ord("d"))] and self.control is True:
            self.velocity_x = 10
        else:
            if self.velocity_x > 0:
                self.velocity_x -= 0.5

        if key_input[(ord("a"))] and self.control is True:
            self.velocity_x = -10
        else:
            if self.velocity_x < 0:
                self.velocity_x += 0.5

        if key_input[(ord("s"))]:
            self.velocity_y = 10
        else:
            if self.velocity_y > 0:
                self.velocity_y -= 0.5

        if key_input[(ord("w"))]:
            self.velocity_y = -10
        else:
            if self.velocity_y < 0:
                self.velocity_y += 0.5

    def collisions(self):
        if self.rect.x < -40:
            self.velocity_x = 10

        if self.rect.x + self.rect.width > 740:
            self.velocity_x = -10
            self.control = False
        else:
            self.control = True

        if self.rect.y < -40:
            self.velocity_y = 10

        if self.rect.y + self.rect.height > 940:
            self.velocity_y = -10

    def get_damage(self, amount):
        if self.current_health > 0:
            self.current_health -= amount
        else:
            self.current_health = 0

    def get_health(self, amount):
        if self.current_health < self.maximum_health:
            self.current_health += amount
        else:
            self.current_health = self.maximum_health

    def collisions_with(self, sprite_group):
        if pygame.sprite.spritecollide(self, sprite_group, True):
            self.get_damage(100)
