import time, os

def remove_blank(str):
    if str == "":
        return False
    return True

all_programs = os.popen("wmic process get description, processid").read()

all_programs_arr = list(filter(remove_blank, all_programs.split("\n")))

required_program = None
for program in all_programs_arr:
    if "Spotify.exe" in program:
        required_program = program
        break

if required_program != None:
    try:
        required_pid = int(list(filter(remove_blank, required_program.split(" ")))[1])
        end_time = int(input('Enter time in minutes: '))*60
        for a in range(end_time):
            time.sleep(1)
            print(end_time-a)
        os.kill(required_pid, 9)
    except:
        print("Something went wrong!")
        time.sleep(3)
else:
    print("Spotify not running!")
    time.sleep(3)
