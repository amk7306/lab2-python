# Author: amk7306@psu.edu
# Collaborator: ZhihongJiang  zbj5088@psu.edu
# Collaborator: Prajnay Kataria pmk5429@psu.edu
# Collaborator: Travis Stauffer tcs5399@psu.edu 
# Section: 1
# Breakout: 12

import main
def getLetterGrade(grade):
  grade = float(grade)
  #grade = input("Enter your CMPSC 131 grade: ")
  if grade == 100:
    return "A+"
  if 93<=grade and grade<100: 
    return "A"
  if 90<=grade and grade<93:
    return "A-"
  if 87<=grade and grade<90:
    return "B+"
  if 83<=grade and grade<87:
    return "B"
  if 80<=grade and grade<83:
    return "B-"
  if 76<=grade and grade<80:
    return "C+"
  if 70<=grade and grade<77:
    return "C"
  if 60<=grade and grade<70:
    return "D"
  if  60 > grade: 
    return "F"
  #print(f"Your letter grade for CMPSC 131 is: {grade}")
if __name__ == "__main__":
  getLetterGrade()