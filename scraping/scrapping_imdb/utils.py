def time_to_minutes(time):
    """
    Convertit la durée du film en minutes.
    
    Args:
        time (str): Durée du film.
    
    Returns:
        int: Durée du film en minutes.
    """
    # Vérifie si la chaîne 'time' n'est pas vide
    if time:
        # Initialise la durée en minutes à zéro
        duration = 0
        
        # Si 'h' est présent dans 'time', extrait le nombre d'heures
        if 'h' in time:
            hours = int(time.split('h')[0].strip())  # Extrait les heures
            duration += hours * 60                  # Convertit les heures en minutes et ajoute à la durée

        # Si 'm' est présent dans 'time', extrait le nombre de minutes
        if 'm' in time:
            minutes = int(time.split('m')[0].split()[-1].strip())  # Extrait les minutes
            duration += minutes                                    # Ajoute les minutes à la durée

    # Si 'time' est vide, retourne None
    else:
        duration = None

    return duration