class RectangularCordinates:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def get_coardinate(self):
        return (self.x, self.y)
    
    def on_axis(self) -> bool:
        if self.x == 0 or self.y == 0:
            return True
        else:
            return False
        
    def quardrant_check(self):
        if self.on_axis():
            return None
        if self.x > 0 and self.y > 0:
            return 1
        elif self.x < 0 and self.y > 0:
            return 2
        elif self.x < 0 and self.y < 0:
            return 3
        else:
            return 4
    
    def distance_x(self):
        return abs(self.y)
    
    def distance_y(self):
        return abs(self.x)
