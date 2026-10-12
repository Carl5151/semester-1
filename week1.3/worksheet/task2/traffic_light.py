"""
Portfolio Task - Week 1.3
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name:
"""
import time

states = { "red":4, "red_amber":3, "green":5, "amber":3 }

systime = 0
maxtime = int(input("Enter an integer number of steps: ")) # read an integer number of steps (>0)

state = "red"
state_index = 0
stop = False

# Simulate the traffic light system up to time=maxtime in 1-second steps
for step in range(maxtime):
    if not stop: # check if steps met
        for second in range(states[state]):
            time.sleep(1)
            print(f"Time {systime:03} State {state}")
            systime += 1
            if systime == maxtime + 1: # check if steps met
                stop = True
                break
        if state == 'amber':
            state_index = 0
            state = 'red'
        else:
            state_index += 1
            key = 0
            for s in states:
                if key == state_index:
                    state = s
                    break
                else:
                    key += 1
    else:
        # stops steps once maxtime met
        break
        

# At the end of each step you should output the time and state using the statement on line 14
