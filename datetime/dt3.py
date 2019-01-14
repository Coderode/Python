import datetime
import pytz
dt=datetime.datetime(2019,1,4,12,23,12,tzinfo=pytz.UTC)  #with time zone
print(dt)

dt_now=datetime.datetime.now(tz=pytz.UTC)  #with time zone(1)
print(dt_now)

dt_utcnow=datetime.datetime.utcnow().replace(tzinfo=pytz.UTC) #(2)
print(dt_utcnow)
#(1) and (2) are same
#(1) is easy to understand so use it as utcnow