def isParent(A, B):
	global Parents

	if B not in Parents.keys():
		return False
	if A == B:
		return True
	if not Parents[B]:
		return False
	if A in Parents[B]:
		return True
	
	res = False
	for p in Parents[B]:
		res = isParent(A, p)
		if res:
			break

	return res

Parents = {}

# read classes
for _ in range(int(input())):
	line = input().split()
	Parents[line[0]] = [] if len(line) == 1 else line[2:]

print(Parents)
# lets answer
for _ in range(int(input())):
	A, B = input().split()
	print('Yes' if isParent(A, B) else 'No')

