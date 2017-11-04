
class Vector:
	def __init__(this, x, y):
		this.x = x
		this.y = y
	def __str__(this):
		return '({}, {})'.format(this.x, this.y)

class Game:
	def __init__(this, x, y, limit):
		this.limit = limit
		this.board = [['' for i in range(0, x)] for j in range(0, y)]

	def has_winner(this):
		for y in range(0, len(this.board)):
			for x in range(0, len(this.board[y])):
				if this._consecutive_matches(Vector(x, y), None) == this.limit - 1:
					return this.board[y][x]
		return 'no winner found';

	def _consecutive_matches(this, location, direction):
		if location.x == len(this.board[0]) or location.y == len(this.board):
			return 0
		elif direction is None:
			highest = 0
			for direction in [Vector(-1,1),Vector(0,1),Vector(1,1),Vector(1,0)]:
				if this._is_match(location, direction):
					result = this._consecutive_matches(Vector(location.x + direction.x, location.y + direction.y), direction) + 1
					if result > highest:
						highest = result
			return highest
		elif this._is_match(location, direction):
			return this._consecutive_matches(Vector(location.x + direction.x, location.y + direction.y), direction) + 1
		return 0

	def _is_match(this, location, direction):
		return (location.x + direction.x < len(this.board[0]) and
				location.y + direction.y < len(this.board) and
				this.board[location.y][location.x] == this.board[location.y + direction.y][location.x + direction.x])

game = Game(5,4,4)
game.board = [['o','x','o','x','o'],
			  ['x','x','x','o','o'],
			  ['x','x','o','x','x'],
			  ['o','o','o','x','o']]
print(game.has_winner())