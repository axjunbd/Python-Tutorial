class Student:
    def __init__(self, name, number_of_scores):
        self.name = name
        self.test_scores = [0] * number_of_scores
        
    def getName(self):
        return self.name
        
    def getScore(self, position):
        if 0 <= position < len(self.test_scores):
            return self.test_scores[position]
        raise IndexError("Score position is out of bounds")
        
    def setScore(self, position, value):
        if 0 <= position < len(self.test_scores):
            self.test_scores[position] = value
        else:
            raise IndexError("Score position is out of bounds")
            
    def getHighestScore(self):
        if not self.test_scores:
            return 0
        return max(self.test_scores)
        
    def getAverageScore(self):
        if not self.test_scores:
            return 0
        return sum(self.test_scores) / len(self.test_scores)
        
    def __str__(self):
        return f"Student: {self.name}\nScores: {self.test_scores}\nAverage: {self.getAverageScore():.2f}\nHighest Score: {self.getHighestScore()}"

if __name__ == "__main__":
    student = Student("John Doe", 3)
    
    print("Initial Student Status:")
    print(student)
    
    student.setScore(0, 85)
    student.setScore(1, 92)
    student.setScore(2, 78)
    
    print("\nAfter Setting Scores:")
    print(f"Name: {student.getName()}")
    print(f"Score 1: {student.getScore(0)}")
    print(f"Score 2: {student.getScore(1)}")
    print(f"Score 3: {student.getScore(2)}")
    print(f"Highest Score: {student.getHighestScore()}")
    print(f"Average Score: {student.getAverageScore():.2f}")
    print("\nFinal String Representation:")
    print(student)
