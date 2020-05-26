ctime = int(input("Whats the time now?"))
alarm = int(input("How many hours should I wait?"))
atime = (((alarm%24)+ctime)%24)
print("Alarm will go off at: ", atime)
