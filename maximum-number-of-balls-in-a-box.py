def countBalls( lowLimit: int, highLimit: int) -> int:

    # create a dict with low to high values as the key
    # if the key does not exists add that to the dict
    # later max of values is the answer

    ball_box_dict = {}

    for i in range(lowLimit, highLimit+1):
        if i > 9:
            box = 0
            while i != 0:
                remainder = i %10
                i = i //10
                box += remainder

            if ball_box_dict.get(box):
                ball_box_dict[box] += 1
            else:
                ball_box_dict[box] = 1

        else:
            ball_box_dict[i] = 1

    return max(ball_box_dict.values())



print(countBalls(19,28))
