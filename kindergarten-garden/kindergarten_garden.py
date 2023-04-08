class Garden:
    STUDENTS = [
        'Alice', 'Bob', 'Charlie', 'David',
        'Eve', 'Fred', 'Ginny', 'Harriet',
        'Ileana', 'Joseph', 'Kincaid', 'Larry',
    ]
    PLANTS = {
        "G": "Grass",
        "C": "Clover",
        "R": "Radishes",
        "V": "Violets",
    }
    def __init__(self, diagram, students=STUDENTS):
        self.diagram = diagram
        self.students = sorted(students)

    def plants(self, student):
        pos = self.students.index(student) * 2
        return [self.PLANTS[letter] 
                for line in self.diagram.splitlines() 
                for letter in line[pos:pos+2]]

