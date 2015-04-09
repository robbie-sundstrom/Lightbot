class Bot(object):
	def __init__(self, row, column, game_board, commands):
		self.row = row
		self.column = column
		self.game_board = game_board
		self.commands = commands
		self.alive = True

	def check_move(self, direction):

		#check if direction is legit
		if direction not in 'wasd': return False

		#check if bot will hit a wall or a non-legit space
		elif direction == 'w':
			if self.row == 0 or if game_board[self.row-1][self.column] == '_': return False
		elif direction == 's':
			if self.row == len(self.game_board)-1 or if game_board[self.row+1][self.column] == '_': return False
		elif direction == 'a':
			if self.column == 0 or if game_board[self.row][self.column-1] == '_': return False
		elif direction == 'd':
			if self.column == len(self.row)-1 or if game_board[self.row][self.column+1] == '_': return False

		else:
			return True

	def move_bot(self, direction):
		direction = direction.lower()
		if self.check_move(direction):
			#then move the bot to the next location according to direction
			if direction == 'w':
				self.row -= 1
			elif direction == 's':
				self.row += 1
			elif direction == 'a':
				self.column -= 1
			elif direction == 'd':
				self.column += 1
		#if move is not legit
		else:
			self.alive = False

		if self.alive: return (self.row, self.column)










