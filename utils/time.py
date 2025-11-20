from datetime import datetime, timedelta, UTC

async def delta_between_dates(start_time: datetime) -> str:
    # Si el datetime es naive (tzinfo = None), interpretarlo como local time
    if start_time.tzinfo is None:
        # Interpreta que la hora naive estaba en la zona local del sistema
        start_time = start_time.astimezone()

    # Convertir de zona local a UTC
    start_time = start_time.astimezone(UTC)

    current_time = datetime.now(UTC)
    delta: timedelta = current_time - start_time

    if delta.days >= 365:
        return f"{delta.days/365:.1f} y"
    if delta.days >= 30:
        return f"{delta.days/30:.1f} m"
    if delta.days >= 1:
        return f"{delta.days} d"

    seconds = int(delta.total_seconds())
    if seconds >= 60:
        return f"{seconds // 60} min"
    if seconds >= 1:
        return f"{seconds} sec"

    return "0 sec"
