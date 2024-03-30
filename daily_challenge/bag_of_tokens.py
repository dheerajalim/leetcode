def token_score(tokens, power):
    # edge case when we have no token give
    if len(tokens) == 0:
        return 0

    # sort the tokens based on the value in ascending order
    tokens = sorted(tokens)

    score = 0
    # if the first token is itself greater than the power
    # then we can never increase the score hence we return 0
    if tokens[0] > power:
        return 0

    # position the i and j pointers
    i, j = 0, len(tokens) - 1

    # iterate until i <= j
    while i <= j:
        # if the token at ith position is < power, then we can use power and increase score
        # and move the ith index
        if tokens[i] <= power:
            score += 1
            power -= tokens[i]
            i += 1
        # else if we cannot use power to consume token
        # we try to lose score to increase power and see if we can satisfy
        # the other tokens
        elif tokens[j] > power and score > 0:
            # this is a case where [example : [100, 200]] i and j are equal but
            # if we consume token , it will reduce score and we cannot further move
            # so better keep the score which it was earlier
            if i == j:
                return score

            score -= 1
            power += tokens[j]
            j -= 1

    return score


tokens = [10, 20, 30, 40, 100, 200]
power = 50

print(token_score(tokens, power))
