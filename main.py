# from curses import ACS_GEQUAL
# from unicodedata import name


class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, score, tracks=[]):
        self.name = name
        self.age = age
        self.score = score
        self.tracks = tracks
    def change_name (self, NewName):
        self.name = NewName
    def change_age (self, NewAge):
        self.age = int(NewAge)
    def get_score (self):
        return self.score
    def add_track (self, NewTrack):
        self.tracks.append(NewTrack)
    def __repr__ (self):
         return f"name: {self.name} age: {self.age} score: {self.score} tracks: {self.tracks}"
Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)
# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()
print(Bob)