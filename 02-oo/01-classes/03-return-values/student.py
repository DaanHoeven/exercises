class Wall:
    armor = 10
    height = 5

    # write your code here
    def get_cost(self):
        cost = self.armor * self.height
        return cost

    # don't touch below this line

    def fortify(self):
        self.armor *= 2
