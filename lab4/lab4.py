# Jeff Powell
# CSC295
# 10/4/23
# Program reads in student grades and reports various statistics regarding the
# grade distribution

import lab4_table_header as th


# Main function is responsible for calling other logic in the program to
# assemble the data
def main():
    student_list = load_info()
    print("Student Grade Data\n")
    sort_info(student_list)
    print_info(student_list)
    print()
    min_idx = places_to_skip(student_list)
    print("Stats for Exams Taken:")
    print(f"Minimum = {student_list[-min_idx - 1][0]:.1f}")
    print(f"Maximum = {student_list[0][0]:.1f}")
    print(f"Mean = {get_mean(student_list):.1f}")
    print(f"Median = {get_median(student_list):.1f}")


# Determines if there is any student with identical IDs in the student list
# already
def check_for_duplicate(student_list, student):
    for s in student_list:
        if s[1] == student[1]:
            return True
    return False


# Maximum printable length of an ID
MAX_ID_LEN = 7


# Formats a student ID to be MAX_ID_LEN digits for printing
def format_num(num):
    digits = len(str(num))
    while digits > MAX_ID_LEN:
        num /= 10
        digits -= 1
    s = (MAX_ID_LEN - digits) * '0' + str(num)
    return s


# Prints the list of accumulated student data out
def print_info(student_list):
    th.lab4_table_header()
    for s in student_list:
        id = format_num(s[1])
        if s[0] == -1:
            print(f"{s[2]:<16} {id:>10}     N/A")
        else:
            print(f"{s[2]:<16} {id:>10} {s[0]:>7}")


# Sorts info by grade from highest to lowest
def sort_info(student_list):
    student_list.sort(reverse=True)


# Returns the median grade of the student list
def get_median(student_list):
    sort_info(student_list)
    l2 = student_list.copy()
    l2.sort()
    real_len = len(student_list) - places_to_skip(student_list)
    if real_len % 2 == 0:
        idx = real_len // 2
        return (student_list[idx][0] + student_list[idx - 1][0]) / 2
    else:
        return student_list[real_len // 2][0]


# Determines how many invalid grades were read in by the program, and returns
# the number of places to skip
def places_to_skip(student_list):
    l1 = student_list.copy()
    l1.sort()
    invalid = 0
    for idx in range(len(l1)):
        if l1[idx][0] != -1:
            return invalid
        invalid += 1
    return invalid


# Returns average grade of the distribution
def get_mean(student_list):
    sum = 0
    l1 = student_list.copy()
    l1.sort()
    real_len = len(student_list) - places_to_skip(student_list)
    for s in l1:
        if s[0] == -1:
            continue
        sum += s[0]
    return sum / real_len


# Reads info from an input file given by user into a list of students
def load_info():
    while True:
        try:
            file_name = input("Input a file name: ")
            with open(file_name, "r") as file:
                data = file.readlines()
            student_list = []
            for i in range(0, len(data), 3):
                if len(student_list) >= 30:
                    break
                student = data[i:i + 3]
                name = student[0].strip('\n')
                try:
                    id = int(student[1])
                    grade = int(student[2])
                    if grade < 1 or grade >= 110:
                        grade = -1
                except Exception:
                    return student_list
                student = (grade, id, name)
                if not check_for_duplicate(student_list, student):
                    student_list.append(student)

            return student_list
        except FileNotFoundError:
            continue


if __name__ == "__main__":
    main()
