from curses import ACS_GEQUAL
from unicodedata import name


class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks=[], score):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score

    def changeName (self, NewName):
        self.name = NewName

    def changeAge (self, NewAge):
        self.age = int(NewAge)

    def addTrack (self, NewTrack):
        self.tracks.append(NewTrack)

    def getScore (self):
        return self.score

    def __repr__ (self):
         return f'name: {self.name} age: {self.age} tracks: {self.tracks} score: {self.score}

Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()
