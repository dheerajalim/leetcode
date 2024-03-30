"""
The idea is that we can return either 5 or 10
so we maintian the count of 5 and 10
And by greedy approach,
if we  get $10 bill we return 5 and store 10 with us
if we get $20 bill we return 10 and 5 , no need to store 20 as we will never return 20 currency
if we have $20 bill and we do not have $10, then we check if we have atleast 3 $5, then we return
else: we return False

"""


def lemonade_change(bills):
    # handle edge case
    if bills[0] != 5:
        return False
    # keep this to maintain the count of 5's and 10's coin
    fives, tens = 0, 0

    # iterate opver the bills
    for bill in bills:

        # if we get a 5 bill, we just take  the curreny no need to return
        # any coin back, hence fives += 1
        if bill == 5:
            fives += 1

        # if we get 10 $ bill, we need to return 5
        # and we now have 10 with us
        elif bill == 10 and fives:
            fives -= 1
            tens += 1
        # if we have 20 bill, then we need to think greedly
        # we return 10 first and then 5
        elif bill == 20 and tens and fives:
            tens -= 1
            fives -= 1
        # if we do not have 10 and we have atleast 3 5's, then we return
        elif bill == 20 and fives >= 3:
            fives -= 3
        # else there is no scope we can serve the change
        else:
            return False

    return True


bills = [5, 5, 5, 10, 20]
# bills = [5,5,10,10,20]
bills = [5, 5, 5, 5, 10, 20, 10]
bills = [5, 5, 5, 10, 5, 20, 5, 10, 5, 20]
bills = [5, 5, 5, 10, 5, 5, 10, 20, 20, 20]
print(lemonade_change(bills))
