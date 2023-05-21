def largestAltitude(gain) -> int:
    altitudes = [0, gain[0]]

    for i in range(1, len(gain)):
        x = altitudes[-1]
        altitudes.append(altitudes[-1] + gain[i])

    return max(altitudes)

gain = [-5,1,5,0,-7]
print(largestAltitude(gain))

