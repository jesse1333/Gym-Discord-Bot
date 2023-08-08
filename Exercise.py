class Exercise:
    weight = 0
    comment = ""

    def __init__(self):
        weight = 0
        comment = ""

    def change_weight(self, weight):
        self.weight = weight

    def change_comment(self, comment):
        self.comment = comment

    def get_weight(self):
        return self.weight

    def get_comment(self):
        return self.comment

    def print_exercise(self):
        print("Weight: " + self.weight)
        print("Comment: " + self.comment)

