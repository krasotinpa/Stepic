def decompress(str):
    s, l = '', []
    count = -1
    for c in str:
        if c.isalpha():
            count += 1
            l.append([c, ''])
        if c.isdigit():
            l[count][1] += c
    for i in l:
        s += i[0] * int(i[1])
    return s
# 
with open('input.txt') as inf:
    for line in inf:
	    print(decompress(line.strip()))

