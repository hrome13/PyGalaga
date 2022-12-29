class Enemy:
    def __init__(self, pos, width, height, speed):
        self._pos = pos
        self._left = pos[0]
        self._right = pos[0] + width
        self._top = pos[1]
        self._bottom = pos[1] + height
        self._speed = speed

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