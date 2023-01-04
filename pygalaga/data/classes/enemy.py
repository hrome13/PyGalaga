from math import sin, cos

class Enemy:
    def __init__(self, pos, width, height, speed, t):
        self._pos = pos
        self._left = pos[0]
        self._right = pos[0] + width
        self._top = pos[1]
        self._bottom = pos[1] + height
        self._speed = speed
        self._t = t
        self._prev_x = 0
        self._prev_y = 0

    @property
    def pos(self):
        return self._pos

    @property
    def left(self):
        return self._left

    @property
    def right(self):
        return self._right

    @property
    def top(self):
        return self._top

    @property
    def bottom(self):
        return self._bottom

    @property
    def speed(self):
        return self._speed

    @property
    def t(self):
        return self._t

    @property
    def prev_x(self):
        return self._prev_x

    @property
    def prev_y(self):
        return self._prev_y

    @pos.setter
    def pos(self, pos):
        self._pos = pos

    @left.setter
    def left(self, left):
        self._left = left

    @right.setter
    def right(self, right):
        self._right = right

    @top.setter
    def top(self, top):
        self._top = top

    @bottom.setter
    def bottom(self, bottom):
        self._bottom = bottom

    @t.setter
    def t(self, new_t):
        self._t = new_t

    @prev_x.setter
    def prev_x(self, new_x):
        self._prev_x = new_x

    @prev_y.setter
    def prev_y(self, new_y):
        self._prev_y = new_y

    def update_t(self):
        self.t += self.speed

    def move(self, screen_width):
        # Move along the lemniscate:
        #       r^2 = a^2 cos(2 theta)

        a = screen_width // 3

        x = a * cos(self.t) / (1 + sin(self.t) ** 2)
        y = a * sin(self.t) * cos(self.t) / (1 + sin(self.t) ** 2)
        dx = self.prev_x - x
        dy = self.prev_y - y
        self.prev_x = x
        self.prev_y = y
        
        self.pos = [self.pos[0] + dx, self.pos[1] + dy]
        self.left += dx
        self.right += dx
        self.top += dy
        self.bottom += dy

        self.update_t()