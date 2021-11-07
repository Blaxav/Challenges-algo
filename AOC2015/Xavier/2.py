import sys

total = 0
ribbon = 0
current_size = 0
input_file = open(sys.argv[1], 'r')
for line in input_file:
    l, h, w = line[0:-1].split("x")
    l = int(l)
    h = int(h)
    w = int(w)
    ribbon += l*w*h
    ribbon += 2*(sum([i for i in sorted([h, w, l])[0:2]]))
    total += 2*(l*h + l*w + h*w) + min([l*h, l*w, h*w])
print("Total  : ", total)
print("Ribbon : ", ribbon)
