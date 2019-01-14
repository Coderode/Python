#datetime module
import datetime

#using date functions
d=datetime.date(2016,7,24)  #not 07 put 7 
print(d)

tday=datetime.date.today()
print(tday)#default format 2019-01-04=(year,month,day)
print(tday.year)
print(tday.month)
print(tday.day)
# or print(datetime.date.today().year)
print(tday.weekday())  #in numbers
print(tday.isoweekday())

##using weekday()=>  monday=0 ... sunday=6
##using isoweekday()=> monday=1 ... sunday=7


#timedelta()  =>difference
tdelta=datetime.timedelta(days=7) 
print(tday+tdelta)  #date after 7 days ->future
print(tday-tdelta)   #date before 7 days ->past

#or
print(datetime.date.today()+datetime.timedelta(days=7))

#date2=date1+timedelta
#timedelta=date1-date2


#no. of days from bday to today
bday=datetime.date(1997,1,31)

till_bday=tday-bday
print(till_bday)
print(till_bday.days)
print(till_bday.total_seconds())


#using time functions
print()
t=datetime.time(9,30,45,10000)  #  h:m:s:milliseconds  (hour,minutes,seconds,milliseconds)
print(t)
print(t.hour)
print(t.minute)
print(t.second)
print(datetime.time())#->00:00:00


#using date and time together
print()
dt=datetime.datetime(2019,1,5,4,20,45,110000)  #(year,month,day,hour,min,second,millisecond)
print(dt)
print(dt.date())
print(dt.time())
print(dt.year)
print(dt.month)
tdelta=datetime.timedelta(days=7)
print(dt+tdelta)
tdelta=datetime.timedelta(hours=7)
print(dt+tdelta)






