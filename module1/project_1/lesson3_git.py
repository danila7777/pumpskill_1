import time
i = 0
k = 7
while i <= k:
    if i == 0 or i == 5:
        i = i + 1
        continue
    if i < 5:
        print('Часть 1:', i)
    if i > 5:
        time.sleep(0.5)
        if i != k:
            print('Часть 2:', i, end='\r')
        if i == k:
            print('Часть 2:', i)
    i = i+3
