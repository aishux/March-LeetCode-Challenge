class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius 
        self.x_center = x_center
        self.y_center = y_center

    def randPoint(self) -> List[float]:
        radius = self.radius*sqrt(random.random()) # sample radius as r*sqrt(x) 
        theta = 2*pi*random.random() # sample angle as unif [0, 2*pi) 
        return self.x_center + radius*cos(theta), self.y_center + radius*sin(theta)
