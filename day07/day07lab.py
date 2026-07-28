print("welcome to my course");

# list in python
students = [
    "Abel",
    "Sara",
    "John"
]
for student in students:
    print(student)

acc1="cbe-1"
acc2="cbe-100"
# 
class Node:
 def __init__(self, data):
  self.data = data
  self.next = None # points to next node
head = Node(acc1)
head.next = Node(acc2)
print(head)
print(head.next)
