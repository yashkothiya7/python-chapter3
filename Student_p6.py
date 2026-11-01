class Student:
    def __init__(self):
        self.id = None
        self.name = None
        self.marks = None

    def set_id(self, student_id):
        self.id = student_id

    def set_name(self, name):
        self.name = name

    def set_marks(self, marks):
        self.marks = marks

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_marks(self):
        return self.marks

 