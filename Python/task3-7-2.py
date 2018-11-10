dict1, dict2 = input(), input()
Cypher = {}

for i in range(len(dict1)):
	Cypher[dict1[i]] = dict2[i]
DeCypher = dict(zip(Cypher.values(), Cypher.keys()))

print(Cypher)
print(DeCypher)

print(''.join([Cypher[c] for c in input()]))
