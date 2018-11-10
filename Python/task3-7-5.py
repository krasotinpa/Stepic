C = dict(zip([i for i in range(1,12)], [[0,0] for _ in range(11)]))

with open('input.txt') as inf:
	for line in inf:
		cls, name, h = line.strip().split('\t')
		C[int(cls)][0] += 1
		C[int(cls)][1] += int(h)


for i in range(1,12):
	print(i, end=' ')
	if C[i][0] == 0:
		print('-')
	else:
		print(C[i][1]/C[i][0])
