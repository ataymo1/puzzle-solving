class CountSquares:

    def __init__(self):
        self.points = {}
        self.point_list = []
        

    def add(self, point: List[int]) -> None:
        point = tuple(point)

        if point in self.points:
            self.points[point] += 1
        else:
            self.points[point] = 1

        

    def count(self, point: List[int]) -> int:
        # print(self.points)
        x, y = point
        total = 0

        for other_x, other_y in self.points:

            add = self.points[(other_x, other_y)]
            if x == other_x and y == other_y:
                continue

            if abs(x - other_x) == abs(y - other_y):
                corner_one = (x, other_y)
                corner_two = (other_x, y)
                if corner_one in self.points and corner_two in self.points:
                    total += add * self.points[corner_two] * self.points[corner_one]
        # print(total)
        return total


            

        
