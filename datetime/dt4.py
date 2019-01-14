import datetime
import pytz
dt_utcnow=datetime.datetime.now(tz=pytz.UTC)
print(dt_utcnow)
dt_mtn=dt_utcnow.astimezone(pytz.timezone('Asia/Kolkata'))
print(dt_mtn)
dt=datetime.datetime.now()   #as on the system
print(dt)
dt_east=dt.astimezone(pytz.timezone('Asia/Kolkata'))
print(dt_east)

td=pytz.timezone('US/Mountain')
dt=td.localize(dt)
print(dt)


#for dispaying all timezones 
for tz in pytz.all_timezones:
	pass
	#print(tz)