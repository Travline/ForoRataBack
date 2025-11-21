from datetime import datetime, timedelta, UTC

async def delta_between_dates(start_date: datetime) -> str:
  end_date = int(datetime.now(UTC).timestamp())
  start_date = int(start_date.timestamp())
  delta = end_date - start_date
  return f"{delta} secs"