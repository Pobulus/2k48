#!D:\Python36\python
#2K48 a terminal based 2048 game
#Made by Paweł Chmielewski 19-07-2019
#You may edit this program as you wish




#IMPORT
import random, os



#DEFAULT VALUES
rows = 4
cols = 4
base = 2
multiplier = 2
prob = 20
init = 2
highnum = base

debug = 0



#FUNCTIONS
def addNum(n):
	free = []
	for y in range(rows):
		for x in range(cols):
			crd = [x, y]
			if matrix[crd[1]][crd[0]] == 0:
					free.append(crd)
	if len(free) == 0:
		failure("moves")
	rndcrd = free[random.randint(0, len(free)-1)]
	matrix[rndcrd[1]][rndcrd[0]] = n


def createMx(x, y):	
	matrix = []
	for i in range(y):
		row = []
		for i in range(x):
			row.append(0)
		matrix.append(row)

	return matrix


def failure(x):
	if x == "key":
		print("You decided to quit")
	if x == "moves":
		print("No more moves")
	print("You scored: "+ score()+ "!")
	print("Good Job!")
	quit()


def handle(line):
	global highnum
	prevline = []
	for i in line:
		prevline.append(i)
		if i == 0:
				line.remove(i)
				line.append(0)

	for i in range(len(line)-1):
		if line[i] == line[i+1] and not line[i] == 0 and not line[i + 1] == 0:
			line[i] = line[i] * multiplier
			if line[i] > highnum:
				highnum = line[i]
			line.remove(line[i+1])
			line.append(0)
	return line


def move(dir):
	global matrix
	if dir == "up":
		for x in range(cols):
			line = []
			for y in range(rows):
				line.append(matrix[y][x])
			oline = handle(line)

			for i in range(rows):
				matrix[i][x] = oline[i]	
				
	elif dir == "down":
		for x in range(cols):
			line = []
			for y in range(rows):
				y = rows-1-y
				line.append(matrix[y][x])
			oline = handle(line)
			for i in range(rows):
				matrix[rows-1-i][x] = oline[i]	
				
	elif dir == "right":
		for y in range(rows):
			line = []
			for n in range(cols):
				n = cols-1-n
				line.append(matrix[y][n])
			oline = handle(line)
			for i in range(cols):	
				matrix[y][cols-1-i] = oline[i]
				
	elif dir == "left":
		for y in range(rows):
			line = matrix[y]
			oline = handle(line)

			for i in range(cols):
				matrix[y][i] = oline[i]
				
	else:
		print("Unknown dirrection: "+ dir)
		return


def readArguments():	
	global base
	global rows
	global cols
	global init
	global prob
	global multiplier
	global debug
	args = os.sys.argv
	if len(args) > 1:
		for i in range(len(args)-1):
			i += 1
			if args[i][0] == "-":
				if args[i][1] == "b":
					base = int(args[i+1])
					
				elif args[i][1] == "r":
					rows = int(args[i+1])
					
				elif args[i][1] == "m":
					multiplier = int(args[i+1])
					
				elif args[i][1] == "p":
					prob = int(args[i+1])
					
				elif args[i][1] == "i":
					init = int(args[i+1])
					
				elif args[i][1] == "c":
					cols = int(args[i+1])
					
				elif args[i][1] == "d":
					debug = 1
					
				elif args[i][1] == "h":
					showHelp("ext")
					
				else:
					showHelp("quick")
			
					
def readInput():
	inp = input(">")
	if inp == "w" or inp == "W":
		move("up")
		spawn()
		
	elif inp == "s" or inp == "S":
		move("down")
		spawn()
		
	elif inp == "a" or inp == "A":
		move("left")
		spawn()
		
	elif inp == "d" or inp == "D":
		move("right")
		spawn()
		
	elif inp == "q" or inp == "Q":
		failure("key")
		
	else:
		pass


def score():
	sc = 0
	for y in range(rows):
		for x in range(cols):
			crd = [x, y]
			sc += matrix[crd[1]][crd[0]]
	return str(sc)


def showHelp(x):
	if x == "quick":
		print("Welcome to 2k48,  a terminal based game of 2048!")
		print("Use WASD to control the direction of sliding tiles.")
		print("When two tiles with the same value touch, they merge and their values add up")
		print("Try to get 2048 as quickly as possilbe.")
		print("Use Q to quit.")
		print("Yes, you have to press enter after every keypress.")
		print("For extended help please run the program with the argument \"-h\".")
	
	elif x == "ext":
		print("This is the extended help.")
		print("")
		print("You can control certain aspects of the game by passing additional arguments while running the \'2k48.py\' command.")
		print("")
		print("-d		turns on the DEBUG mode, where the game field isn't cleared.")
		print("-h 		shows this message")
		print("")

		print("-c integer	changes the number of COLumnS in the gamefield, default is 4")
		print("-r integer	changes the number of ROWS in the gamefiels, default is 4")
		print("")
		print("-b integer	changes the BASE, the first number, default is 2")
		print("")
		print("-m integer	changes the value by which the tile is MULTIPLIED when two tiles merge, default is 2")
		print("")
		print("-p integer	changes the PROBABILITY of spawning a higher number. Represents 1/P. default is 20")
		print("")
		print("-i integer	changes how many tiles are filled when the game INITialises, default is 2")


		quit()


def showMx():
	if not debug:
		if os.name == "nt":
			os.system("cls")
			
		elif os.name == "posix":
			os.system("clear")
			
		else:
			pass
			
	cellsize = len(str(highnum))
	for i in matrix:
		print("—"*cols*(cellsize+1))
		line = "|"
		for l in range(len(i)):
			if i[l] == 0:
				cell = " "
				
			else:
				cell = str(i[l])
				
			while len(cell) < cellsize:
				cell += " "
			line += cell + "|"
		print(line)
	print("—"*cols*(cellsize+1))
	print(highnum)


def spawn():
	global highnum
	if random.randint(1, prob) == 1:
			addNum(base*multiplier)
			if highnum == base:
				highnum = base*multiplier
				
	else:
		addNum(base)	

		

#Here the actual program begins		



#SETUP
readArguments()
matrix = createMx(cols, rows)

for i in range(init):
	spawn()
	
showHelp("quick")
input()



#LOOP
while True:			
	showMx()
	readInput()
	
	

#This line is here because I wanted to get it to 300 lines
