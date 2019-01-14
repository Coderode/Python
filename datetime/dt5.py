import datetime
import pytz
dt_kol=datetime.datetime.now(tz=pytz.timezone('Asia/Kolkata'))
print(dt_kol.isoformat())
print(dt_kol.strftime('%B %d,%Y')) #January 04,2019
#we can see these types using documentation of python
dt_str='July 26,2016'
dt=datetime.datetime.strptime(dt_str,'%B %d,%Y')
print(dt)
#strftime->datetime to string
#strptime->string to datetime
