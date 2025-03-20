std_Name = []
while True:
  print('ËNTER NAME OF STUDENT ' + str(len(std_Name * 1 ))+ ('   ENETR NOTHING TO STOP'))
  name = input()
  if name == "":
   break
  std_Name = std_Name+ [name]
  print("The student name are:")
  for name in std_Name:
   print(" " + name)
   