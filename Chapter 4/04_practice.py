# Write a program to get 7 input fruit names and store it to list
inp_1 = input("Enter fruit 1: ")
inp_2 = input("Enter fruit 2: ")
inp_3 = input("Enter fruit 3: ")
inp_4 = input("Enter fruit 4: ")
inp_5 = input("Enter fruit 5: ")
inp_6 = input("Enter fruit 6: ")
inp_7 = input("Enter fruit 7: ")

fruit_list = [inp_1, inp_2, inp_3, inp_4, inp_5, inp_6, inp_7]
print(fruit_list)

# Write a program to accept marks of 6 students and display them in sorted manner
marks_1 = int(input("Enter marks 1: "))
marks_2 = int(input("Enter marks 2: "))
marks_3 = int(input("Enter marks 3: "))
marks_4 = int(input("Enter marks 4: "))
marks_5 = int(input("Enter marks 5: "))
marks_6 = int(input("Enter marks 6: "))

marks_list = [marks_1, marks_2, marks_3, marks_4, marks_5, marks_6]
marks_list.sort()
print(marks_list)

# Check tha a type cannot be changed in Python
# marks_list[0] = "50"
# print(marks_list)

# Write a program to sum a list with 4 numbers
number_list = [1, 2, 3, 4]
print(sum(number_list))

# Write a program to count the number of zeros in the following tuple
tuple_example = (7, 0, 8, 0, 0, 9)
print(tuple_example.count(0))

