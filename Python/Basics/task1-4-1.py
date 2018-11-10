def add(name, var):
	global NameSpace
	NameSpace[name]['vars'].add(var)
	
def create(name, parent):
	global NameSpace
	NameSpace[name] = {'parent': parent, 'vars': set()}

def get(name, var):
	global NameSpace
	# print('=>'+name)
	if var in NameSpace[name]['vars']:
		print(name)
		return
	if name == 'global':
		print('None')
		return
	# print('==>'+NameSpace[name]['parent'])
	get(NameSpace[name]['parent'], var)

NameSpace = {'global': {
	'parent': 'None',
	'vars': set()}}

Request = {
	'add': add,
	'create': create,
	'get': get
}

for _ in range(int(input())):
	line = input().split()
	Request[line[0]](*line[1:])

print(NameSpace)