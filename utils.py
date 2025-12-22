def mp_to_minutes(mp):
    """
    Convert Basketball-Reference MP values (MM:SS) to float minutes.
    Returns None for DNP / inactive / malformed values.
    """
    if isinstance(mp, str) and ":" in mp:
        mins, secs = mp.split(":")
        return int(mins) + int(secs) / 60
    return None