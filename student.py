"""
File: student.py
Resources to manage a student's name and test scores.
"""

class Student(object):
    """Represents a student."""

    def __init__(self, name, number):
        """All scores are initially 0."""
        self.name = name
        self.scores = []
        for count in range(number):
            self.scores.append(0)

    def getName(self):
        """Returns the student's name."""
        return self.name
  
    def setScore(self, i, score):
        """Resets the ith score, counting from 1."""
        self.scores[i - 1] = score

    def getScore(self, i):
        """Returns the ith score, counting from 1."""
        return self.scores[i - 1]
   
    def getAverage(self):
        """Returns the average score."""
        return sum(self.scores) / len(self._scores)
    
    def getHighScore(self):
        """Returns the highest score."""
        return max(self.scores)
    def __eq__(self, student):
        return self.name == student.name 
    
    def __ge__(self, student):
        return self.name == self.name or self.name>student.name
    
    def __lt__(self, student):
        return self.name<student.name
 
    def __str__(self):
        """Returns the string representation of the student."""
        return "Name: " + self.name  + "\nScores: " + \
               " ".join(map(str, self.scores))

def main():
    """A simple test."""
    student = Student("Ken", 5)
    print(student)
    for i in range(1, 6):
        student.setScore(i, 100)
    print(student)

    print("\nSecond student")
student2 = Student("Ken", 5)
print(student2)

print("\nThird student")
student3 = Student("Lia", 5)
print(student3)

print("\nChecking equal student 1 and student 2")
print(student2.__eq__(student2))

print("\nChecking equal student 1 and student 3")
print(student3.__eq__(student3))

print("\nChecking greater than equal student 1 and student 3")
print(student3.__ge__(student3))

print("\nChecking less than student 1 and student 3")
print(student3.__lt__(student3))

if __name__ == "__main__":
    main()


