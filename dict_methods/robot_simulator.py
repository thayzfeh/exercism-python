# Globals for the directions
# Change the values as you see fit
EAST = (1,0)
NORTH = (0,1)
WEST = (-1,0)
SOUTH = (0,-1)

TURN_LEFT = {EAST: NORTH, NORTH: WEST, WEST: SOUTH, SOUTH: EAST}
TURN_RIGHT = {EAST: SOUTH, SOUTH: WEST, WEST: NORTH, NORTH: EAST}

class Robot:
    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):

        self.direction = direction
        self.coordinates = (x_pos,y_pos)

    def move(self,commands):
        for command in commands:
            match command:
                case "L":
                    self.change_direction(left=True)
                case "R":
                    self.change_direction(right=True)
                case "A":
                    self.advance()
                case _:
                    raise ValueError("Invalid Command.")
                
    def change_direction(self,right=False,left=False):
        if right:
            self.direction = TURN_RIGHT[self.direction]
        elif left:
            self.direction = TURN_LEFT[self.direction]
    
    def advance(self):
        x, y = self.coordinates
        x += self.direction[0]
        y += self.direction[1]
        self.coordinates = (x,y)


robot = Robot(NORTH, 0, 0)
robot.move("A")
