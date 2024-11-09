if __name__ == '__main__':
    import yfinance as yf
    import time as tm
    from email_send import email_send
    import schedule
    from datetime import time, datetime
    from pinbar import pinbar
    from functions import trade, green, market_level
    times = ["30m", "1h"]
    markets = ["USDCAD=X", "EURCAD=X", "GBPCAD=X", "EURUSD=X", "AUDUSD=X"]


    def checker():
        for t in times:
            for m in markets:
                print(m, t)
                levels = market_level(m)
                d = []
                hist = yf.download(m,start="2024-10-16", end="2024-10-17", interval= t)
                d = pinbar(hist)
                if d[1] == 1:
                    level = trade(d[0], levels, hist)
                    res = green(hist, level, d[0])
                    if res[0] == 1:
                        email_send(m, t, res[1])
                else:
                    print("no opportunity")


    def trial():
        try:
            checker()
        except:
            trial()


    schedule.every().hour.at(":30").do(trial)
    schedule.every().hour.at(":00").do(trial)
    while True:
        schedule.run_pending()
        tm.sleep(10)