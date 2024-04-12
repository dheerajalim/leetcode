"""
https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/?envType=daily-question&envId=2024-04-08
"""

from collections import deque


def count_students(students, sandwiches):
    # store the result in dequeu to pop from both ends
    students = deque(students)
    sandwiches = deque(sandwiches)

    # iterate until we have students available to eat sandwich
    while students:
        # this store the current length of the students queue
        # who still need to have breakfast
        student_queue = len(students)
        # this is a count to know we are at which position in the student queue
        count = 0
        # we keep on moving the students to end if the sandwich is not my choice
        while students[0] != sandwiches[0]:
            # if we move all students in queue, and we reach the same student
            # that means none of the student is having the required sandwich available
            # hence we return the count which is the count of students who did not eat
            if count == student_queue:
                return count

            # we keep on moving the student to the back of the queue
            # and increasing the count which tells us how many students are moved
            front_student = students.popleft()
            students.append(front_student)
            count += 1

        # else if the choice matches, we just give the sandwich to student
        students.popleft()
        sandwiches.popleft()

    # this means everyone ate ,and we return hunger count as 0
    return 0


students = [1, 1, 1, 0, 0, 1]
sandwiches = [1, 0, 0, 0, 1, 1]

print(count_students(students, sandwiches))
