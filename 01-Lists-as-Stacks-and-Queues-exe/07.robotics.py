from datetime import datetime, timedelta
from collections import deque

robots_status = {x.split('-')[0]: [int(x.split('-')[1]), 0] for x in input().split(";")}
# dictionary with key as robot name and list [time for one task, time for current task]
starting_time = datetime.strptime(input(), '%H:%M:%S')
products = deque()
product = input()
while product != 'End': # collecting the products to process
    products.append(product)

    product = input()

while products:
    starting_time += timedelta(0, 1) # tact time - 1s
    product = products.popleft() # preparing product to process
    for robot, value in robots_status.items(): # find free robot and him a product to process
        if robots_status[robot][1] == 0:
            robots_status[robot][1] = robots_status[robot][0]
            print(f'{robot} - {product} [{starting_time.strftime("%H:%M:%S")}]')
            break
    else:
        products.append(product) # sending product back to queue if not free robot

    for robot, value in robots_status.items(): # reduce robots working time with tact time
        if robots_status[robot][1] != 0:
            robots_status[robot][1] -= 1

