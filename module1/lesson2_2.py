# Ctrl + K+С  закомментить выделенные строки

# i = 0

# while i < 10:
#     if i == 3:
#         i = i + 1
#         continue

#     print(i)
#     if i == 5:
#         break

#     i += 1


i = 0
while i < 10:
    if i == 0 or i == 5:
        i = i + 1
        continue
    if i < 5:
        print('Часть 1:', i)
    if i > 5:
        print('Часть 2:', i)
    
    i = i+1
