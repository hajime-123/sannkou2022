# %%
import datetime
import time

todaydetail = datetime.datetime.today()#210921
#dt = datetime.datetime(2018, 2, 1, 12, 5, 30, 2000)
t2=todaydetail.strftime("%M%S.%f")
#t2=dt.strftime("%M%S.%f")
trig05=t2[5]
trig10_now=t2[3]
trig10_pas=t2[3]
trig600_now=t2[1]
trig600_pas=t2[1]
while True:
    todaydetail = datetime.datetime.today()#210921
    t2=todaydetail.strftime("%M%S.%f")
    trig05=t2[5]
    trig10_now=t2[3]
    trig600_now=t2[1]
    #print(trig10_now)
    
    if trig600_now!=trig600_pas:
        print('60.0秒',t2)
    elif trig10_now!=trig10_pas:
        print('1.0秒',t2)
    elif trig05=='5':
        print('0.5秒',t2)
    todaydetail = datetime.datetime.today()#210921
    t2=todaydetail.strftime("%M%S.%f")
    trig10_pas=t2[3]
    trig600_pas=t2[1]
    #print(trig10_pas)
    time.sleep(0.1)


# %%
t2

# %%
dt

# %%
t2[5]

# %%



