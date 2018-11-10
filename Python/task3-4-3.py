# 0 - Имя
# 1 - Математика
# 2 - Физика
# 3 - Русский

D = []
with open('input.txt', encoding='utf-8') as inf:
    for line in inf:
	    D.append(line.strip().split(';'))


[print(sum([int(i) for i in item[1:]])/3) for item in D]

print(
    sum([int(item[1]) for item in D])/len(D),
	sum([int(item[2]) for item in D])/len(D),
	sum([int(item[3]) for item in D])/len(D)
	)
