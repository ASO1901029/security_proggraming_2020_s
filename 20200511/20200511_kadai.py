def calc_time(t):
    MINUTE = 60
    HOUR = MINUTE * 60
    s = t % MINUTE
    m = t % HOUR // MINUTE
    h = t // HOUR
    print(f"{str(h).zfill(2)}:{str(m).zfill(2)}:{str(s).zfill(2)}")


def calc_time2(t):
    print(f"{t // 60 // 60}:{t // 60 % 60}:{t % 60}")


t = 45296
calc_time(t)
calc_time2(t)
