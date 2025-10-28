from datetime import datetime, timedelta, UTC
from calendar import timegm
from jose import jwt
current_time = datetime.now(UTC)
offset = timedelta(hours=5)
payload = {"ola":"153", "exp":(current_time+offset)}
token = jwt.encode(payload, "ajhfasushfasufhas7yafuba", algorithm="HS256")
content = jwt.decode(token, "ajhfasushfasufhas7yafuba", algorithms="HS256")
print(int(content["exp"])>timegm(datetime.now(UTC).utctimetuple()))

async def delta_between_dates():
    
    return