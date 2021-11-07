import datetime
import sys

'''
########################################################################################
Part 1
########################################################################################
'''

floor = 0
n_repeat = 1000

timer = datetime.datetime.now()
for k in range(n_repeat):
    input_file = open(sys.argv[1], 'r')
    for line in input_file:
        for element in line:
            if element == '(':
                floor += 1
            elif element == ')':
                floor -= 1
            else:
                print("Last element found : ", element)
                break

    #print("Final floor : ", floor)
    input_file.close()
print("With for loop : ", datetime.datetime.now() - timer)


timer = datetime.datetime.now()
for k in range(n_repeat):
    input_file = open(sys.argv[1], 'r')
    data = input_file.readline()
    floor = data.count('(') - data.count(')')
    #print("Final floor : ", floor)
    input_file.close()
print("With count    : ", datetime.datetime.now() - timer)
print("Final floor : ", floor)

'''
########################################################################################
Part 2
########################################################################################
'''
floor = 0
n_repeat = 100
index = 1
timer = datetime.datetime.now()
for k in range(n_repeat):
    input_file = open(sys.argv[1], 'r')
    for line in input_file:
        for element in line:
            if element == '(':
                floor += 1
            elif element == ')':
                floor -= 1

            if floor == -1:
                #print("Basement index : ", index)
                break
            index += 1
    input_file.close()
print("With for loop : ", datetime.datetime.now() - timer)


timer = datetime.datetime.now()
count = 0
for k in range(n_repeat):
    input_file = open(sys.argv[1], 'r')
    for line in input_file:
        count = 0 if line[0] == '(' else 1  # initialization
        for k in range(1, len(line), 2):
            if count + line[k:k+2].count(')') >= (k+1) / 2:
                #print("index : ", k)
                break
            count += line[k:k+2].count(')')
    input_file.close()
print("With count    : ", datetime.datetime.now() - timer)
