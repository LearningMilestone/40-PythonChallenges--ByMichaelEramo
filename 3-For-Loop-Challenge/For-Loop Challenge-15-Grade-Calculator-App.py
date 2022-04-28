#Reference : The Art of Doing Computer Science Through Python Application udemy course by Michael P. Eramo
#For Loops Challenge 15: Grade Point Average Calculator App

print("Welcome to the Grade Point Average Calculator App")

#Get user input
name = input("What is your name: ").title().strip()
grade_num = int(input("How many grades would you like to enter: "))

#Get the user's grades
grades = []
for i in range(grade_num):
    grades.append(int(input("Enter grade: ")))

#Sort the grades and print them to the screen
grades.sort(reverse=True)
print("\nGrades Highest to Lowest:")
for grade in grades:
    print("\t" + str(grade))

#Calculate the average
average = sum(grades)/len(grades)
average = round(average, 2)

#Print a grade summary
print("\n" + name + "'s Grade Summary:")
print("\tTotal Number of Grades: " + str(len(grades)))
print("\tSum of Grades: " + str(sum(grades)))
print("\tHighest Grade: " + str(max(grades)))
print("\tLowest Grade: " + str(min(grades)))
print("\tAverage: " + str(average))

#Get the user's desired average and calculate what they need to get on the next assignment
desired_avg = float(input("\nWhat is your desired average: "))
grade_req = desired_avg*(len(grades)+1) - sum(grades)
grade_req = round(grade_req, 2)

#Print a summary
print("\nGood luck " + name + "!")
print("You will need to get a " + str(grade_req))
#
# #Make a copy of the original grades and swap out one of the grades
# 41 new_grades = grades[:]
# 42 print("\nLets see what you average could have been if you did better/worse on an
# assignment.")
# 43 grade_change = int(input("What grade would you like to change: "))
# 44 new_grades.remove(grade_change)
# 45 new_grade = int(input("What grade would you like to change " + str(grade_change)
#                          + " to: "))
# 46 new_grades.append(new_grade)
# 47
# 48 #Sort the new grades and print them to the screen
# 49 new_grades.sort(reverse=True)
# 50 print("\nNew Grades Highest to Lowest:")
# 51 for grade in new_grades:
#     52 print("\t" + str(grade))
# 53
# 54 #Calculate the new average
# 55 new_average = sum(new_grades)/len(new_grades)
# 56 new_average = round(new_average, 2)
# 57
# 58 #Print a new grade summary
# 59 print("\n" + name + "'s New Grade Summary:")
# 60 print("\tTotal Number of Grades: " + str(len(new_grades)))
#
# print("\tHighest Grade: " + str(max(new_grades)))
# 62 print("\tLowest Grade: " + str(min(new_grades)))
# 63 print("\tAverage: " + str(new_average))
# 64
# 65 #Print a summary on how the average changed
# 66 print("\nYour new average would be a " + str(new_average) + " compared to your
# real average of " + str(average) + "!")
# 67 average_change = new_average - average
# 68 average_change = round(average_change, 2)
# 69 print("That is a change of " + str(average_change) + " points!")
# 70
# 71 #Too bad the original grades are still intact!
# 72 print("\nToo bad your original grades are still the same!")
# 73 print(grades)
# 74 print("You should go ask for extra credit!")