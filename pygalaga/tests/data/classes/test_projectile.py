import unittest
from pygalaga.data.classes.projectile import Projectile

class TestProjectile(unittest.TestCase):
    def test_move(self):
        pos = [20,20]
        width, height = 5, 5
        speed = 2
        projectile = Projectile(pos, width, height, speed)
        
        projectile.move()
        self.assertEqual(projectile.pos, [20, 18])
        self.assertEqual(projectile.left, 20)
        self.assertEqual(projectile.right, 25)
        self.assertEqual(projectile.top, 18)
        self.assertEqual(projectile.bottom, 23)
        
if __name__ == '__main__':
    unittest.main()