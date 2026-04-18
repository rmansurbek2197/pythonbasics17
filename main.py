class Student:
    def __init__(self, name, surname, student_id):
        self.name = name
        self.surname = surname
        self.student_id = student_id
        self.exams = []

    def add_exam(self, exam):
        self.exams.append(exam)

class Exam:
    def __init__(self, name, questions):
        self.name = name
        self.questions = questions

class Question:
    def __init__(self, question, options, correct_option):
        self.question = question
        self.options = options
        self.correct_option = correct_option

class Result:
    def __init__(self, student, exam, score):
        self.student = student
        self.exam = exam
        self.score = score

class OnlineExamSystem:
    def __init__(self):
        self.students = []
        self.exams = []

    def add_student(self, student):
        self.students.append(student)

    def add_exam(self, exam):
        self.exams.append(exam)

    def get_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None

    def get_exam(self, exam_name):
        for exam in self.exams:
            if exam.name == exam_name:
                return exam
        return None

    def start_exam(self, student, exam):
        score = 0
        for question in exam.questions:
            answer = input(question.question + " " + str(question.options) + " ")
            if answer == question.correct_option:
                score += 1
        result = Result(student, exam, score)
        student.add_exam(exam)
        return result

system = OnlineExamSystem()

student1 = Student("John", "Doe", "12345")
exam1 = Exam("Math", [
    Question("What is 2 + 2?", ["1", "2", "3", "4"], "4"),
    Question("What is 5 * 5?", ["20", "25", "30", "35"], "25"),
    Question("What is 10 - 5?", ["3", "4", "5", "6"], "5")
])

system.add_student(student1)
system.add_exam(exam1)

result = system.start_exam(student1, system.get_exam("Math"))
print("Exam Name: " + result.exam.name)
print("Student Name: " + result.student.name + " " + result.student.surname)
print("Score: " + str(result.score))