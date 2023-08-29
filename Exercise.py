class Exercise:
    name = ""
    weight = 0
    comment = ""

    def __init__(self, name, weight=None, comment=None):
        self.name = name
        self.weight = weight
        self.comment = comment

    def change_name(self, name):
        self.name = name

    def change_weight(self, weight):
        self.weight = weight

    def change_comment(self, comment):
        self.comment = comment

    def get_name(self):
        return self.name

    def get_weight(self):
        return self.weight

    def get_comment(self):
        return self.comment

    def print_exercise(self):
        print("Name: " + self.name)
        print("Weight: " + self.weight)
        print("Comment: " + self.comment)

