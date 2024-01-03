#log of names, durations
jedi_log = {}
#lists of keys & values
keys = []
values = []
#prompt user for session count
sessions = int(input("Amount of sessions: "))
#goes through each session, logs name and duration
for i in range(0, sessions):
    names = input("Jedi name: ")
    duration = int(input("Session duration(in minutes) : "))
    #hours
    if duration % 60 == 0:
        hours = duration // 60
        print("hours: "+ str(hours))
    #hours & minutes
    elif duration >= 60:
        hours = duration // 60
        minutes = duration % 60
        print("hours: "+ str(hours))
        print("minutes: "+ str(minutes))
    #minutes
    else:
        minutes = duration
        print("minutes: "+ str(minutes))
    jedi_log[names] = duration

for key, value in jedi_log.items():
    keys.append(key)
    values.append(value)

total_time = sum(values)

if total_time % 60 == 0:
    time = total_time // 60
elif total_time >= 60:
    time = 
    total_time = 

print(total_time)
print(jedi_log)