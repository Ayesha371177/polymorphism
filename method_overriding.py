class graduatestudent:
 def display(self):
  print("graduate student")
class student(graduatestudent):
 def display(self):
  print("student")
s=student()
s.display()