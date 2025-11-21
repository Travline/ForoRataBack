from datetime import datetime, timedelta, UTC

async def delta_between_dates(start_date: datetime) -> str:
  end_date = int(datetime.now(UTC).timestamp())
  start_date = int(start_date.timestamp())
  delta = end_date - start_date
  if delta > 31536000:
    return f"{int(delta/31536000)}y"
  if delta > 2592000:
    return f"{int(delta/2592000)}m"
  if delta > 86400:
    return f"{int(delta/86400)}d"
  if delta > 3600:
    return f"{int(delta/3600)}h"
  if delta > 60:
    return f"{int(delta/60)}min"
  if delta > 0:
    return f"{int(delta)}s"