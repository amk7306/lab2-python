# Author: amk7306@psu.edu
# Collaborator: ZhihongJiang  zbj5088@psu.edu
# Collaborator: Prajnay Kataria pmk5429@psu.edu
# Collaborator: Travis Stauffer tcs5399@psu.edu 
# Section: 1
# Breakout: 12

def run():
  grade = float(input("Enter your CMPSC 131 grade: "))
  g = getLetterGrade(grade) 
  print(f"Your letter grade for CMPSC 131 is {g}.")
def getLetterGrade(grade):
  if 93<=grade and grade>100: 
    return "A"
  elif 90<=grade and grade<93:
    return "A-"
  elif 87<=grade and grade<90:
    return "B+"
  elif 83<=grade and grade<87:
    return "B"
  elif 80<=grade and grade<83:
    return "B-"
  elif 77<=grade and grade<80:
    return "C+"
  elif 70<=grade and grade<=77:
    return "C"
  elif 60<=grade and grade<70:
    return "D"
  else: 
    return "F"
if __name__ == "__main__":
  run()