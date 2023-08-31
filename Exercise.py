class Exercise:
    name = ""
    weight = 0
    comment = ""

    def __init__(self, *args):                                 # args is basically how many parameters are passed in
        if len(args) == 1:
            self.name = args[0]
            self.weight = 0
            self.comment = ""
        elif len(args) == 2:
            self.name = args[0]
            self.weight = args[1]
            self.comment = ""
        elif len(args) == 3:
            self.name = args[0]
            self.weight = args[1]
            self.comment = args[2]

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
        print("Weight: " + str(self.weight))
        print("Comment: " + self.comment)

