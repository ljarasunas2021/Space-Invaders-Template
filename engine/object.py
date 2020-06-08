import pygame


class Object:

    img = None
    pos_x = 0
    pos_y = 0
    render_order = 0

    def __init__(self, engine, img_path, x, y, render_order=0):
        self.engine = engine
        self.img = pygame.image.load(img_path)
        self.width = self.img.get_rect()[2]
        self.height = self.img.get_rect()[3]
        self.pos_x = x
        self.pos_y = y
        self.hidden = False
        self.render_order = render_order

        engine.add_object(self)

    def render(self, screen):
        # if not self.hidden:
        screen.blit(self.img, (self.pos_x, self.pos_y))

    def check_collision(self, obj):
        selfRect = self.img.get_rect().copy()
        selfRect = selfRect.move(self.pos_x, self.pos_y)
        objRect = obj.img.get_rect().copy()
        objRect = objRect.move(obj.pos_x, obj.pos_y)
        return selfRect.colliderect(objRect)

    def hide(self):
        self.hidden = True

    def show(self):
        self.hidden = False

    def destroy(self):
        self.engine.remove_object(self)
        self = None
