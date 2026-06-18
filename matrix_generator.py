number_to_letters = {1:"A", 2:"B", 3:"C", 4:"D", 5:"E", 6:"F", 7:"G",8:"H", 9:"I",
                10:"J", 11:"K", 12:"L", 13:"M", 14:"N", 15:"O", 16:"P",17:"Q",
                18:"R", 19:"S", 20:"T", 21:"U", 22:"V", 23: "W", 24: "X", 25: "Y", 26: "Z"}

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
def fill_all_layers( matrix: list, layers: int, letters: dict):
    for i in range(0, layers-1):
        # Fill one square layer at a time from outside to inside.
        fill(matrix, i, 2*layers - 1 - i, letters[layers-i] )



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
        fill_all_layers( matrix, layers, number_to_letters )

    print_matrix( matrix )


create_and_print()