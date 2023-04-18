def time_to_minutes(time):
    if time and 'h' in time and 'm' in time:
        hours, minutes = time.strip().split('h')
        hours = int(hours.strip())
        minutes = int(minutes.strip()[:-1])
        duration = hours * 60 + minutes
    else:
        duration = None
    return duration