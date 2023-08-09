import time, os

pid = int(input('Enter PID: '))
end_time = int(input('Enter time in minutes: '))*60

for a in range(end_time):
    time.sleep(1)
    print(end_time-a)

os.kill(pid, 9)