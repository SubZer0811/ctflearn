N = 5
lawn = []

mowed_state = {
		'*':'/',
		'|':'-',
		'/':'\\',
		'-':'_',
		'\\':'.',
		'_':'.',
		'.':'.'
	}

growth_state = {
		'*':'*',
		'|':'*',
		'/':'|',
		'-':'/',
		'\\':'-',
		'_':'\\',
		'.':'.'
	}

def create_lawn():
	f = open("lawn.txt", "r")
	global lawn, N
	lawn = []
	N = 0
	row = f.readline()
	while row:
		N += 1
		row = row.rstrip('\n')
		row = [x for x in row]
		lawn.append(row)
		row = f.readline()

	show_lawn()

def mowed(state):
	return mowed_state[state]

def growth(state):
	return growth_state[state]

def show_lawn():
	for row in lawn:
		print(row)
	print()

def grow():
	for i in range(N):
		for j in range(N):
			# print(type(lawn[i][j]))
			if(type(lawn[i][j]) == tuple):
				# print("test")
				if(lawn[i][j][1] == N):
					lawn[i][j] = (growth(lawn[i][j][0]), 1)
				else:
					# print(lawn[i][j])
					lawn[i][j] = (lawn[i][j][0], lawn[i][j][1]+1)
					# print(lawn[i][j])

def count_flowers():
	count = 0
	for i in range(N):
		for j in range(N):
			if(lawn[i][j][0] == '*'):
				count += 1

	return count

create_lawn()

for j in range(N):
	if(j%2 == 0):
		for i in range(N):
			grow()
			lawn[i][j] = (mowed(lawn[i][j]), 1)
			# show_lawn()
	else:
		for i in range(N-1, -1, -1):
			grow()
			lawn[i][j] = (mowed(lawn[i][j]), 1)
			# show_lawn()

show_lawn()
print(count_flowers())