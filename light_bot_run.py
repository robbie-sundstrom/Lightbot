from move import *
from visual import *

def get_raw():
	user_moves = raw_input()
	move_list = []
	for letter in user_moves:
		move_list.append(letter)
	return move_list


class RunAttemptCheck(object):
	def __init__(self, error_status, row, column):
		self.error_status = error_status
		self.row = row
		self.column = column

	def display_error(self):
		print "Sorry, try again, you got stuck at row:", self.row, "and column:", self.column

	def yay(self):
		print "WOOHOO, You Win"


def check_run(error_status, row, column):
	run = RunAttemptCheck(error_status, row, column)
	if run.error_status == False:
		run.display_error()
	else:
		pass


if __name__ == '__main__':
	user_commands = get_raw()
	board = Board([7,7], [(0,1), (1,1)])
	light_bot = Bot(0, 0, board, user_commands)
	for letter in user_commands:
		if light_bot.alive == True:
			light_bot.game_board = board
			position = light_bot.move_bot(letter)
			if position:
				board = board.update(position)
				print(board)
			else:
				print('Error')
		else:
			break

	check_run(light_bot.alive, light_bot.row, light_bot.column)


