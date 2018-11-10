#   GameTable
# Key - команда
# 0 - Игр
# 1 - Побед
# 2 - Ничьих
# 3 - Поражений
GameTable = {}

for _ in range(int(input())):
	team1, goal1, team2, goal2 = input().split(';')
	GameTable[team1] = GameTable.get(team1,[0,0,0,0])
	GameTable[team2] = GameTable.get(team2,[0,0,0,0])
	# Увеличим количестов игр
	GameTable[team1][0] += 1
	GameTable[team2][0] += 1
	# Победы - ничьи - поряжения
	if int(goal1) > int(goal2):
		GameTable[team1][1] += 1
		GameTable[team2][3] += 1
	elif int(goal1) < int(goal2):
		GameTable[team1][3] += 1
		GameTable[team2][1] += 1
	else:
		GameTable[team1][2] += 1
		GameTable[team2][2] += 1

[print(k+':', *v, v[1]*3+v[2]) for k,v in GameTable.items()]
	

