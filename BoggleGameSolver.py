

'''BoggleGameSolver finds all existing words (you have to input those yourself) on a board for filworld game'''

class prefTree:
    'класс специально для вложеных словарей'
    def __init__(self):
        self.kid = {}


    def put(self, word):
        point = self.kid
        for letter in word:
            if letter not in point:
                point[letter] = {}
            point = point[letter]
        point[word] = ''


    def first_is(self, prefix):
        point = self.child
        for letter in prefix:
            if letter not in point:
                return False
            point = point[letter]
        return True


    def search(self, word):
        point = self.child
        for letter in word:
            if letter not in point:
                return False
            point = point[letter]
        return True


def find_words_in_philword(board: list, existing_words: list) -> list: #Cамо задание
    all_words = set()
    selfPutDict = prefTree()
    for i in existing_words:
        selfPutDict.put(i)
    for yCoordinate in range(len(board)):
        for xCoordinate in range(len(board[yCoordinate])):
            generate_words_with_certain_coordinate(board, (yCoordinate, xCoordinate), set(), selfPutDict, all_words, '')
    return all_words


def all_neighbours(board, start): #находит на поле соседние вершины
    Y = start[0]
    X = start[1]
    neighbours = set()
    if(X + 1 < len(board[0])):
        neighbours.add((Y, X + 1))
    if(X - 1 >= 0):
        neighbours.add((Y, X - 1))
    if(Y + 1 < len(board)):
        neighbours.add((Y + 1, X))
    if(Y - 1 >= 0):
        neighbours.add((Y - 1, X))
    return neighbours


def generate_words_with_certain_coordinate(board, coordinates, visited, prefTree, all_words, currentWord): #"идет" по филворду
    Y = coordinates[0]
    X = coordinates[1]
    current_word = currentWord + str(board[Y][X])
    print(currentWord)
    if coordinates not in visited or not prefTree.first_is(currentWord):
        return all_words
    visited.add(coordinates)
    if prefTree.search(currentWord):
        all_words.add(currentWord)
    for neighbour in all_neighbours(coordinates, board):
        generate_words_with_certain_coordinate(board, neighbour, visited, prefTree, all_words, current_word) #рекурсия здесь
    visited.remove(coordinates)
    return all_words

