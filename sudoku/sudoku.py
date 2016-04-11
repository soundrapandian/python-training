class Cell:
    def __init__(self, position):
        self.possibilities = [1,2,3,4,5,6,7,8,9]
        self.position = position
        
    @property
    def value(self):
        if len(self.possibilities) == 1:
            return self.possibilities[0]
        else:
            return 0
        
    @value.setter
    def value(self, val):
        self.possibilities = [val]
        
    def eliminate(self, number):
        try:
            self.possibilities.remove(number)
        except ValueError:
            pass
        if len(self.possibilities) == 1:
            self.value = self.possibilities[0]
            
    def block(self):
        row, col = self.position
        return (row // 3) * 3 + (col // 3)
    
    def is_same_row(self, another_cell):
        return self.position[0] == another_cell.position[0]
        
    def is_same_col(self, another_cell):
        return self.position[1] == another_cell.position[1]
        
    def is_same_block(self, another_cell):
        return self.block() == another_cell.block()
    
    def is_solved(self):
        return len(self.possibilities) == 1
        
    def __str__(self):
        return str(self.value)
        
class Board:
    def __init__(self):
        self.board = {(row, col): Cell((row, col)) for row in range(9) for col in range(9)}
        
    def __getitem__(self, position):
        return self.board[position]
        
    def __setitem__(self, position, value):
        cell = self[position]
        cell.value = value
        for related_position in self.related_cells(cell):
            cell = self[related_position]
            if not cell.is_solved():
                cell.eliminate(value)
                if cell.is_solved():
                    self[related_position].value = cell.value

    def is_complete(self):
        for cell in self.board.values():
            if not cell.is_solved():
                return False
        return True
        
    def load(self, solved_puzzle):
        #for i in range(0, 81):
        for i, v in enumerate(solved_puzzle):
            row = i // 9;
            col = i % 9;
            #self.board[(row, col)].value = int(solved_puzzle[i])
            if v == '.':
                v = 0
            self.board[(row, col)].value = int(v)
    
    def cells(self):
        return [self.board[(row, col)] for row in range(9) for col in range(9)]
        
    def related_cells(self, given_cell):
        return [cell.position for cell in self.cells() 
            if cell != given_cell and (cell.is_same_block(given_cell) or
                cell.is_same_col(given_cell) or
                cell.is_same_row(given_cell))]
    
    def print_board(self):
        for row, col in [(row, col) for row in range(9) for col in range(9)]:
            if col == 8:
                print(self.board[(row,col)].possibilities)
            else:
                print(self.board[(row,col)].possibilities, end=" ")