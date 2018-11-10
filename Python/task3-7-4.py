d = {'север':[0,1], 'запад':[-1,0], 'юг':[0,-1], 'восток':[1,0]}
coord = [0,0]

for _ in range(int(input())):
	direction, offset = input().split()
	coord[0] += int(offset) * d[direction][0]
	coord[1] += int(offset) * d[direction][1]

print(*coord)