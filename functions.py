def trade(bearish, levels, hist):
    i=-2
    opened = hist.Open.iloc[i]
    closed = hist.Close.iloc[i]
    for level in levels:
        if bearish == 1:
            if closed > opened:
                pivot = closed
            else:
                pivot = opened
            if pivot > level:
                if pivot - level > 0.0007:
                    print("pin bar too far")
                else:
                    print(level)
                    return level
            else:
                if level - pivot > 0.0005:
                    print("pin bar too far")
                else:
                    print(level)
                    return level
        elif bearish == 0:
            if closed > opened:
                pivot = opened
            else:
                pivot = closed
            if pivot > level:
                if pivot - level > 0.0005:
                    print("pin bar too far")
                else:
                    print(level)
                    return level
            else:
                if level - pivot > 0.0007:
                    print("pin bar too far")
                else:
                    print(level)
                    return level
    else:
        return 0


def green(hist, light, bearish):
    i = -2
    bar0 = [hist.High.iloc[i-2],hist.Low.iloc[i-2], hist.Open.iloc[i-2], hist.Close.iloc[i-2]]
    bar1 = [hist.High.iloc[i-3],hist.Low.iloc[i-3], hist.Open.iloc[i-3], hist.Close.iloc[i-3]]
    bar2 = [hist.High.iloc[i-4],hist.Low.iloc[i-4], hist.Open.iloc[i-4], hist.Close.iloc[i-4]]
    bar3 = [hist.High.iloc[i-5],hist.Low.iloc[i-5], hist.Open.iloc[i-5], hist.Close.iloc[i-5]]
    bararray = [bar0, bar1, bar2, bar3]
    if light is None or light == 0:
        print('market not on level')
        return [0, ""]
    else:
        if bearish == 0:
            for bar in bararray:
                if bar[2] > bar[3]:
                    higher = bar[2]
                else:
                    higher = bar[3]
                if bar[1] <= light:
                    print("too many touches")
                    return [1, "cautious buy"]
                elif higher - light >= 0.0019:
                    print(light)
                    print('Possible Buy')
                    return [1, "Buy"]
        elif bearish == 1:
            for bar in bararray:
                if bar[2] > bar[3]:
                    lower = bar[3]
                else:
                    lower = bar[2]
                if bar[0] >= light:
                    print("too many touches")
                    return [1, "Cautious sell"]
                elif light - lower >= 0.0019:
                    print("Possible Sell")
                    return [1, "Sell"]
        print('not 20 pips high')


def market_level(market):
    level_usdcad = [1.38416, 1.38032, 1.37640, 1.38736]
    level_eurcad = [1.46641, 1.46976, 1.47555, 1.47831, 1.45960]
    level_gbpcad = [1.69129, 1.67846, 1.68216, 1.68669]
    level_eurusd = [1.06579, 1.06360, 1.06685, 1.07108]
    level_audusd = [0.63713, 0.63984, 0.63281, 0.62932]
    if market == "USDCAD=X":
        level = level_usdcad
    elif market == "EURCAD=X":
        level = level_eurcad
    elif market == "GBPCAD=X":
        level = level_gbpcad
    elif market == "EURUSD=X":
        level = level_eurusd
    elif market == "AUDUSD=X":
        level = level_audusd
    return level

