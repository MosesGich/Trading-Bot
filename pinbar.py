def pinbar(hist):
    i=-2
    high = hist.High.iloc[i]
    low = hist.Low.iloc[i]
    opened = hist.Open.iloc[i]
    closed = hist.Close.iloc[i]
    height = high - low
    print(closed)
    bar = closed - opened
    bar = abs(bar)
    if height < 0.0009:
        return [0, 0]
    else:
        result = []
        result = direction(closed, opened, high, low)
        wick = result[0]
        ratio = wick / bar
        ratio = abs(ratio)
        if ratio > 0.9:
            print("pinbar present")
            return [result[1], 1]
        else:
            print("pinbar is not present")
            return [result[1], 0]


def direction(closed, opened, high, low):
    wick = 0
    global bearish
    if closed > opened:
        x = high - closed
        y = opened - low
    else:
        x = high - opened
        y = closed - low
    if x > y:
        bearish = 1
        if y != 0:
            z = x / y
            if z >= 1.5:
                wick = x
        else:
            wick = x
    elif y > x:
        bearish = 0
        if x != 0:
            z = y / x
            if z >= 1.5:
                wick = y
        else:
            wick = y
    return [wick, bearish]
