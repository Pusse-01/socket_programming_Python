import time
import random
import pandas as pd

   
# making data frame 
data = pd.read_csv("TestData.csv") 
    
# Send this many items per second
sends_per_second = 50    

# Simulate send time by introducing a random delay of at most this many seconds
max_item_delay_seconds = .000000000000000

# How many items to send
item_count = 50

def do_one_item(i):
    # time.sleep(random.random() * max_item_delay_seconds)
    print("Sent item {} {} {} {} {} {} {}".format(data.iloc[i, 0], data.iloc[i, 1], data.iloc[i, 2], data.iloc[i, 3],data.iloc[i, 4],data.iloc[i, 5],data.iloc[i, 6]))


# Record the starting time
start_time = time.time()
print(start_time)
# For each item to send...

for i in range(item_count):      
    # Send the item
    do_one_item(i)

    # Compute how much time we've spent so far
    time_spent = time.time() - start_time

    # Compute how much time we want to have spent so far based on the desired send rate
    should_time = (i + 1) / sends_per_second

    # If we're going too fast, wait just long enough to get us back on track
    if should_time > time_spent:
        print("Delaying {} seconds".format(should_time - time_spent))
        time.sleep(should_time - time_spent)

time_spent = time.time() - start_time
print("Sent {} items in {} seconds ({} items per second)".format(item_count, time_spent, item_count / time_spent))