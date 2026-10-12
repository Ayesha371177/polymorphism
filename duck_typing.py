class car:
 def start(self):
  print("car started")
class bike:
 def start(self):
  print("bike started")
c=car()
b=bike()
def select_vehicle(obj):
 obj.start()
 select_vehicle(c)