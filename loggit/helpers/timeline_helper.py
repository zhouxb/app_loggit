import datetime

ONE_DAY = datetime.timedelta(seconds=60*60*24)

def day_on_num(start_day, num):
    current_time = start_day
    yield current_time.strftime('%Y%m%d')

    for i in range(0, num):
        current_time = current_time - ONE_DAY
        yield current_time.strftime('%Y%m%d')

