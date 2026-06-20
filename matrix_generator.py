import string

    # Fills the border of a square area in the matrix
    # with the given letter.
def fill( matrix: list, start: int, end: int, letter: str ):
    for i in range(start, end):
        for j in range(start, end):
            if i == start or i == end - 1:
                matrix[i][j] = letter
            elif j == start or j == end - 1:
                matrix[i][j] = letter

            
    # Builds the letter square layer by layer,
    # starting from the outermost layer.
def fill_all_layers( matrix: list, layers ):
    for i in range(0, layers):
        # Fill one square layer at a time from outside to inside.
        fill(matrix, i, 2*layers - 1 - i, string.ascii_uppercase[layers - 1 - i] )



    # Creates an empty square matrix filled with 'A'.
    # Matrix size is (2 * layers - 1).
def create_matrix(layers: int)->list:  
    return [["A" for _ in range(2*layers - 1)] for _ in range(2*layers-1)]
    
        

def print_matrix(matrix: list):
    for row in matrix:
        for char in row:
            print(char, end="")
        print()

def create_and_print():
    layers = int(input("enter number of layers:"))
    matrix = create_matrix( layers )

    if layers != 1:
        fill_all_layers( matrix, layers )

    print_matrix( matrix )


create_and_print()
