class Board():
	"""
	The board
	"""
	def __init__(self, size, path):
		self.size = size #tuple of x and y
		self.matrix = [["_ " for i in xrange(size[0])] for j in xrange(size[1])]
		self.loc = (0,0)
		# for i in range(len(self.matrix)):
		# 	for j in range(len(self.matrix[i])):
		# 		if (i,j) in path:
		# 			self.matrix[i][j] = "X "
		for (i,j) in path:
			self.matrix[i][j] = "X "
		self.matrix[self.loc[0]][self.loc[1]] = "B "

	def __str__(self):
		array = []
		for i in range(len(self.matrix)):
			for j in range(len(self.matrix[i])):
				array.append(self.matrix[i][j])
			array.append('\n')
		return ''.join(array)

	def update(self, loc):
		self.matrix[self.loc[0]][self.loc[1]] = "_ "
		self.matrix[loc[0]][loc[1]] = "B "
		self.loc = loc


board = Board([7,7], [(0,1), (1,1)])
board.update((0,3))
print(board)
