
def convertVal(card):
    if card[0] == 'T':
        val = 10
    elif card[0] == 'J':
        val = 11
    elif card[0] == 'Q':
        val = 12
    elif card[0] == 'K':
        val = 13
    elif card[0] == 'A':
        val = 14
    else:
        val = int(card[0], 10)
    return val


def minCardVal(card1, card2):
    val1 = convertVal(card1)
    val2 = convertVal(card2)
    if val1 < val2:
        return 0
    else:
        return 1


def maxCardVal(card1, card2):
    val1 = convertVal(card1)
    val2 = convertVal(card2)
    if val1 > val2:
        return 0
    else:
        return 1


def findLowest(hand):
    min = minCardVal(hand[0], hand[1])
    lastmin = min
    min = minCardVal(hand[min], hand[2])
    if min == 0:
        min = minCardVal(hand[lastmin], hand[3])
    else:
        lastmin = 2
        min = minCardVal(hand[2], hand[3])
    if min == 0:
        min = minCardVal(hand[lastmin], hand[4])
    else:
        lastmin = 3
        min = minCardVal(hand[3], hand[4])
    if min == 0:
        return lastmin
    else:
        return 4


def findHighest(hand):
    max = maxCardVal(hand[0], hand[1])
    lastmax = max
    max = maxCardVal(hand[max], hand[2])
    if max == 0:
        max = maxCardVal(hand[lastmax], hand[3])
    else:
        lastmax = 2
        max = maxCardVal(hand[2], hand[3])
    if max == 0:
        max = maxCardVal(hand[lastmax], hand[4])
    else:
        lastmax = 3
        max = maxCardVal(hand[3], hand[4])
    if max == 0:
        return lastmax
    else:
        return 4


def findLowest2(hand):
    min = minCardVal(hand[0], hand[1])
    lastmin = min
    min = minCardVal(hand[min], hand[2])
    if min == 0:
        min = minCardVal(hand[lastmin], hand[3])
    else:
        lastmin = 2
        min = minCardVal(hand[2], hand[3])
    if min == 0:
        return lastmin
    else:
        return 3


def straight(hand):
    low = findLowest(hand)
    lowNum = convertVal(hand[low])
    orig = lowNum
    while lowNum < (orig + 4):
        if convertVal(hand[0]) == (lowNum + 1) or convertVal(hand[1]) == (lowNum + 1)\
                or convertVal(hand[2]) == (lowNum + 1) or convertVal(hand[3]) == (lowNum + 1)\
                or convertVal(hand[4]) == (lowNum + 1):
            lowNum = lowNum + 1
        else:
            return False
    return True


def flush(hand):
    suit = hand[0][1]
    if suit == hand[1][1] and suit == hand[2][1] and suit == hand[3][1] and suit == hand[4][1]:
        return True
    else:
        return False


def pair(hand):
    val1 = convertVal(hand[0])
    val2 = convertVal(hand[1])
    val3 = convertVal(hand[2])
    val4 = convertVal(hand[3])
    val5 = convertVal(hand[4])
    if val1 == val2 or val1 == val3 or val1 == val4 or val1 == val5:
        return val1
    elif val2 == val3 or val2 == val4 or val2 == val5:
        return val2
    elif val3 == val4 or val3 == val5:
        return val3
    elif val4 == val5:
        return val4
    else:
        return -1


def multiple(hand):
    val0 = pair(hand)
    val1 = convertVal(hand[0])
    val2 = convertVal(hand[1])
    val3 = convertVal(hand[2])
    val4 = convertVal(hand[3])
    val5 = convertVal(hand[4])
    matchNum = 0
    if val0 == -1:
        return 5 #no pairs
    if val0 == val1:
        card1 = hand.pop(0)
        matchNum = matchNum + 1
    if val0 == val2:
        if(matchNum == 1):
            card2 = hand.pop(0)
        else:
            card1 = hand.pop(1)
        matchNum = matchNum + 1
    if val0 == val3:
        if matchNum == 2:
            card3 = hand.pop(0)
        elif matchNum == 1:
            card2 = hand.pop(1)
        else:
            card1 = hand.pop(2)
        matchNum = matchNum + 1
    if val0 == val4:
        if matchNum == 3:
            card4 = hand.pop(0)
        elif matchNum == 2:
            card3 = hand.pop(1)
        elif matchNum == 1:
            card2 = hand.pop(2)
        else:
            card1 = hand.pop(3)
        matchNum = matchNum + 1
    if val0 == val5:
        if matchNum == 3:
            card4 = hand.pop(1)
        elif matchNum == 2:
            card3 = hand.pop(2)
        else:
            card2 = hand.pop(3)
        matchNum = matchNum + 1
    if matchNum == 4:
        hand.append(card1)
        hand.append(card2)
        hand.append(card3)
        hand.append(card4)
        return 0 #4 of a kind
    elif matchNum == 3:
        hand.append(card1)
        hand.append(card2)
        hand.append(card3)
        if convertVal(hand[0]) == convertVal(hand[1]):
            return 1 #full house
        else:
            return 2 #3 of a kind
    elif matchNum == 2:
        hand.append(card1)
        hand.append(card2)
        if convertVal(hand[0]) == convertVal(hand[1]) or convertVal(hand[0]) == convertVal(hand[2])\
                or convertVal(hand[1]) == convertVal(hand[2]):
            return 3 #2 pairs
        else:
            return 4 #1 pair


def almostFlush(hand):
    suit = hand[0][1]
    if suit == hand[1][1]:
        if suit == hand[2][1] and suit == hand[3][1]:
            return 4
        elif suit == hand[2][1] and suit == hand[4][1]:
            return 3
        elif suit == hand[3][1] and suit == hand[4][1]:
            return 2
    else:
        if suit == hand[2][1] and suit == hand[3][1] and suit == hand[4][1]:
            return 1
        else:
            suit = hand[1][1]
            if suit == hand[2][1] and suit == hand[3][1] and suit == hand[4][1]:
                return 0
            else:
                return -1


def almostStraight(hand):
    low = findLowest(hand)
    lowNum = convertVal(hand[low])
    high = findHighest(hand)
    highNum = convertVal(hand[high])
    orig = lowNum
    card = hand.pop(high)
    while lowNum < (orig + 3):
        if convertVal(hand[0]) == (lowNum + 1) or convertVal(hand[1]) == (lowNum + 1)\
                or convertVal(hand[2]) == (lowNum + 1) or convertVal(hand[3]) == (lowNum + 1):
            lowNum = lowNum + 1
        else:
            lowNum = orig + 4
    hand.append(card)
    if lowNum == (orig + 3):
        return 4
    else:
        low = findLowest(hand)
        high = findHighest(hand)
        orig = highNum
        card = hand.pop(low)
        while highNum > (orig - 3):
            if convertVal(hand[0]) == (highNum - 1) or convertVal(hand[1]) == (highNum - 1) \
                    or convertVal(hand[2]) == (highNum - 1) or convertVal(hand[3]) == (highNum - 1):
                highNum = highNum - 1
            else:
                highNum = orig - 4
        hand.append(card)
        if highNum == (orig - 3):
            return 4
        else:
            return -1


class MarleeBryant:
    student_Name = ""
    student_Hand = []

    def student_function(self):
        a = self.student_Hand
        multVal = multiple(a)
        i1 = True
        i2 = True
        i3 = True
        i4 = True
        i5 = True
        if flush(a) or straight(a) or multVal == 0 or multVal == 1:
            return [False, False, False, False, False]
        elif multVal == 3:
            i1 = False
            i2 = False
            i3 = False
            i4 = False
            i5 = False
            compVal = convertVal(a[0])
            if compVal != convertVal(a[1]) and compVal != convertVal(a[2])\
                    and compVal != convertVal(a[3]) and compVal != convertVal(a[4]):
                i1 = True
            else:
                compVal = convertVal(a[1])
                if compVal != convertVal(a[0]) and compVal != convertVal(a[2]) \
                        and compVal != convertVal(a[3]) and compVal != convertVal(a[4]):
                    i2 = True
                else:
                    compVal = convertVal(a[2])
                    if compVal != convertVal(a[0]) and compVal != convertVal(a[1]) \
                            and compVal != convertVal(a[3]) and compVal != convertVal(a[4]):
                        i3 = True
                    else:
                        compVal = convertVal(a[3])
                        if compVal != convertVal(a[0]) and compVal != convertVal(a[1]) \
                                and compVal != convertVal(a[2]) and compVal != convertVal(a[4]):
                            i4 = True
                        else:
                            i5 = True
            return [i1, i2, i3, i4, i5]
        elif multVal == 2 or multVal == 4:
            valfor3 = pair(a)
            if convertVal(a[0]) == valfor3:
                i1 = False
            if convertVal(a[1]) == valfor3:
                i2 = False
            if convertVal(a[2]) == valfor3:
                i3 = False
            if convertVal(a[3]) == valfor3:
                i4 = False
            if convertVal(a[4]) == valfor3:
                i5 = False
            return [i1, i2, i3, i4, i5]
        elif multVal == 5:
            i1 = False
            i2 = False
            i3 = False
            i4 = False
            i5 = False
            i = almostFlush(a)
            if i >= 0:
                if i == 0:
                    i1 = True
                elif i == 1:
                    i2 = True
                elif i == 2:
                    i3 = True
                elif i == 3:
                    i4 = True
                else:
                    i5 = True
                return [i1, i2, i3, i4, i5]
            i = almostStraight(a)
            if i >= 0:
                i5 = True
                return [i1, i2, i3, i4, i5]
            i = findHighest(a)
            i1 = True
            i2 = True
            i3 = True
            i4 = True
            i5 = True
            if i >= 0:
                if i == 0:
                    i1 = False
                elif i == 1:
                    i2 = False
                elif i == 2:
                    i3 = False
                elif i == 3:
                    i4 = False
                else:
                    i5 = False
                return [i1, i2, i3, i4, i5]
        else:
            return [True, True, True, True, True]














