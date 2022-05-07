from random import randint

def randchance(perc1, perc2):
    r = randint(0, perc1)
    r1 = randint(perc1, perc2)
    r2 = randint(0, 100)

    output = 0

    if r < r1:
        output = r1 - r
    elif r > r1:
        output = r - r1

    if output < r2:
        output += r2
    elif output > r2:
        output -= r2

    if output > perc1:
        return perc2

    elif output < perc1:
        return perc1
