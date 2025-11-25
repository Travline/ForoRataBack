from datetime import datetime, timezone

async def delta_between_dates(start_date: datetime) -> str:
    # Obtener la hora actual en UTC
    end_date = datetime.now(timezone.utc)  # Hora actual en UTC
    
    # Si start_date no tiene zona horaria, asignarle UTC
    if start_date.tzinfo is None:  # Si la fecha no tiene zona horaria asignada
        start_date = start_date.replace(tzinfo=timezone.utc)  # Asignar UTC
    
    # Calcular la diferencia entre las dos fechas en segundos
    delta = end_date - start_date
    delta_seconds = int(delta.total_seconds())  # Convertir la diferencia a segundos

    # Convertir el delta a unidades más legibles
    if delta_seconds > 31536000:  # Más de un año (en segundos)
        return f"{int(delta_seconds / 31536000)}y"
    if delta_seconds > 2592000:  # Más de un mes (en segundos)
        return f"{int(delta_seconds / 2592000)}m"
    if delta_seconds > 86400:  # Más de un día (en segundos)
        return f"{int(delta_seconds / 86400)}d"
    if delta_seconds > 3600:  # Más de una hora (en segundos)
        return f"{int(delta_seconds / 3600)}h"
    if delta_seconds > 60:  # Más de un minuto (en segundos)
        return f"{int(delta_seconds / 60)}min"
    if delta_seconds > 0:  # Menos de un minuto (en segundos)
        return f"{int(delta_seconds)}s"
    
    return "0s"  # Si no hay diferencia significativa
