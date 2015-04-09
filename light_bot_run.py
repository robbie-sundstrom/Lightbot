#from move.py import *

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



check_run(False, 4, 6)