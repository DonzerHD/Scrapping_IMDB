def time_to_minutes(time):
    """
    Convertit la durée du film en minutes.
    
    Args:
        time (str): Durée du film.
    
    Returns:
        int: Durée du film en minutes.
    """
    if time:
        duration = 0
        if 'h' in time:
            hours = int(time.split('h')[0].strip())
            duration += hours * 60
        if 'm' in time:
            minutes = int(time.split('m')[0].split()[-1].strip())
            duration += minutes
    else:
        duration = None

    return duration