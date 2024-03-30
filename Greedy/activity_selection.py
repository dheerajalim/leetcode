"""
The idea is to get the maximum number of activities that can be done
Given that no two activities can overlap

The idea here is to sort the activities based on the end time.
Why we sort on the end timeof the activity:
>> Dekh bhai , agar koi activity jaldi khatam ho hyegi tho bache hue time me
aur zada activity accomadate kr legi

example: [[1,10], [2,4], [5,6], [7,9]]
Agar is case me start time ke basis pe sort kiya tho
sabse pehle [1,10] activity lenge and 10 second tak block ho jynge: total sirf ek activity kr paye

Agat humne end time ke basis pe sort kiya hota tho kya hota:
sabse pehle [2,4] > [5,7] > [7,9] : tho total 3 activity krte and jab [1,10] pe atte tho yhe tho
already past activity hai, no use

Hence sorting on the ned time is better and optimal
"""


def activity_selection(activities):
    # sorting the activities based on the end time
    activities = sorted(activities, key=lambda x: x[1])

    # since the first activity will always be taken, hence we set res = 1
    res = 1

    # store the end time of the first activity
    end_taken = activities[0][1]
    # iterate over the activities from the second activity as 1st activity is already considered
    for start, end in activities[1:]:
        # if the start time of current activity is >= end time of previous activity
        # this means that these activities do not overall and can be considered
        if start >= end_taken:
            res += 1
            # update the end_take time to be the time of the last activity that happened
            # since we can only consider activities which will happen on or after this end time
            end_taken = end

    return res


activities = [[2, 4], [1, 3], [10, 11], [3, 8]]
# activities = [[2, 3], [1, 4], [5, 8], [6, 10]]
# activities = [[1,10], [2,4], [5,6], [7,9]]
activities =[[2,1]]
print(activity_selection(activities))
