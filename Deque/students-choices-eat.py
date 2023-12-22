# https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/description/

from collections import deque


def countStudents(students, sandwiches):
    # using deque to pop from the left
    students_queue = deque(students)
    sandwiches_queue = deque(sandwiches)

    while students_queue:
        # if the items at the starting of both queue match,
        # then we pop the queue
        if students_queue[0] == sandwiches_queue[0]:
            students_queue.popleft()
            sandwiches_queue.popleft()
        # in case if the top item do not match of both the queu
        # and we see all the students are 1 and top sandwhich is 0, then we return
        # students length
        elif students_queue[0] != sandwiches_queue[0] and (
                len(students_queue) == sum(students_queue) and sandwiches_queue[0] == 0):
            return len(students_queue)
        # if we see all the students are 0 and top sandwich is 1
        # then we return the length of students as they will never eat top sandwich
        elif students_queue[0] != sandwiches_queue[0] and (sum(students_queue) == 0
                                                           and sandwiches_queue[0] == 1):
            return len(students_queue)
        else:
            # otherwise move the top student to last in the queue
            front_student = students_queue.popleft()
            students_queue.append(front_student)
    # this is the total number of students unable to eat
    return len(students_queue)


students = [1, 1, 0, 0]
sandwiches = [0, 1, 0, 1]

students = [1, 1, 1, 0, 0, 1]
sandwiches = [1, 0, 0, 0, 1, 1]

print(countStudents(students, sandwiches))
