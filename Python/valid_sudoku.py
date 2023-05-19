import random

def create_sudoku(n):
    # create empty n x n Sudoku grid
    sudoku = [[0 for i in range(n)] for j in range(n)]
    
    # populate rows randomly with values 1 to n
    for i in range(n):
        row = random.sample(range(1, n+1), n)
        for j in range(n):
            sudoku[i][j] = row[j]
    
    return sudoku


def is_valid_sudoku(arr):
    n = len(arr)
    target_sum = sum(range(1,n+1))
    
    # Check rows
    for row in arr:
        if sum(row)!= target_sum or len(set(row)) != n:
            return False
    

    # Check columns
    for col in range(n):
        if sum([arr[row][col] for row in range(n)]) != target_sum or len(set([arr[row][col] for row in range(n)])) != n:
            return False
        
    # Check sub grids
    block_size = int(n ** 0.5)
    for block_row in range(0,n,block_size):
        for block_col in range(0,n,block_size):
            block = [arr[row][col]   
                    for row in range(block_row,block_row+block_size)
                    for col in range(block_col,block_col+block_size)
                    ]

            if sum(block)!= target_sum or len(set(block))!= n:
                return False
    
    return True

if __name__ == "__main__":

    arr = create_sudoku(random.randint(3,5))
    print("Sudoku Length is:",len(arr))
    if is_valid_sudoku(arr):
        print("Sudoku is valid")
        print(arr)
    else:
        print("Sudoku is Invalid")
        print(arr)