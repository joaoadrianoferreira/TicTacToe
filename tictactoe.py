import os 

# Global Variables 

moves = [' '] * 9 # Save the player moves 
coord = [x+y for x in '123' for y in 'ABC'] # Coordenate system 
wins = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]] # All win conditions 
p1 = ["Player_Name", "Player_Symbol"] # Player 1, name and symbol 
p2 = ["Player_Name", "Player_Symbol"] # Player 1, name and symbol 
player_time = 1; # Track who is playing 

# Functions 
def start_game():
	p1[0] = raw_input('Player 1 Name: ')
	p1[1] = raw_input('Choose x or o: ')
	p2[0] = raw_input('Player 2 Name: ')
	p2[1] = 'o' if p1[1] == 'x' else 'x'

def print_header():
	print "Player1 - Name: " + p1[0] + "\nSymbol: " + p1[1]
	print "Player2 - Name: " + p2[0] + "\nSymbol: " + p2[1]

def print_board():
	print "   A   B   C"
	print "1  %s | %s | %s " %(moves[0],moves[1],moves[2])
	print "  ---+---+---"
	print "2  %s | %s | %s " %(moves[3],moves[4],moves[5])
	print "  ---+---+---"
	print "3  %s | %s | %s " %(moves[6],moves[7],moves[8])

def play():
	global player_time
	move = raw_input('Player %s Choose: ' %player_time)
	x = 0
	while x < 9: 
		if move == coord[x] and moves[x] == " ":
			if player_time == 1:
				moves[x] = p1[1]
				player_time = 2
			else:
				moves[x] = p2[1]
				player_time = 1
			break
		x+= 1

def game_over():
	if " " in moves: return False 

def win_game():
	for win_cond in wins: 
		if moves[win_cond[0]] == moves[win_cond[1]] and moves[win_cond[1]] == moves[win_cond[2]] and moves[win_cond[2]] != " ":
			return True

def start_move():
	print_header()
	print_board()
	play()

# Start Game
os.system('clear') 
start_game()
os.system('clear') 
while True:
	os.system('clear') 	
	if win_game() != True:
		if game_over() == False: 
			start_move()
		else:
			print "Game Over"
			print_board()
			break
	else: 
		if player_time == 1:
			print "Player 2 Wins"
			print_board()
			break
		else: 
			print "Player 1 Wins"
			print_board()
			break