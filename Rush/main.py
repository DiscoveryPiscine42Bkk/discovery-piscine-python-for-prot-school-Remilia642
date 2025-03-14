def print_chessboard_with_pieces():
    size = 8  # Define the size of the chessboard (8x8)
    king_position = (0, 0)  # Position of the King
    king_position2 = (1, 0)
    rook_position = (0, 1)  # Position of the Rook
    pawn_position = (1, 2)  # Position of the Pawn
    bishop_position = (2, 2)  # Position of the Bishop
    queen_position = (1, 1)  # Position of the Queen
    
    # Store the positions of each piece in a dictionary
    pieces = {
        "P": pawn_position,
        "B": bishop_position,
        "R": rook_position,
        "Q": queen_position
    }

    # Function to calculate the attackable position of each piece
    def get_attack_positions(piece, position):
        attacks = set()
        row, col = position
        if piece == "P":  # Attack pattern of Pawn
            if row + 1 < size:
                if col - 1 >= 0:
                    attacks.add((row + 1, col - 1))  # Attacks diagonally to the left
                if col + 1 < size:
                    attacks.add((row + 1, col + 1))  # Attacks diagonally to the right
        elif piece == "B":  # Attack pattern of Bishop
            directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]  # Direction of Bishop
            idx = 0
            while idx < len(directions):
                direction = directions[idx]
                r, c = row, col
                while 0 <= r < size and 0 <= c < size:
                    r, c = r + direction[0], c + direction[1]
                    if 0 <= r < size and 0 <= c < size:
                        attacks.add((r, c))
                idx += 1
        elif piece == "R":  # Attack pattern of Rook
            i = 0
            while i < size:
                attacks.add((row, i))  # Horizontal
                attacks.add((i, col))  # Vertical
                i += 1
        elif piece == "Q":  # Attack pattern of Queen ( Rook + Bishop)
            i = 0
            while i < size:
                attacks.add((row, i))  # Horizontal
                attacks.add((i, col))  # Vertical
                i += 1
            directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]  # Diagonal
            idx = 0
            while idx < len(directions):
                direction = directions[idx]
                r, c = row, col
                while 0 <= r < size and 0 <= c < size:
                    r, c = r + direction[0], c + direction[1]
                    if 0 <= r < size and 0 <= c < size:
                        attacks.add((r, c))
                idx += 1
        return attacks
    
    attack_positions = set()  # Save the attack location
    pieces_iter = iter(pieces.items())
    piece, pos = next(pieces_iter, (None, None))
    while piece is not None:
        attack_positions.update(get_attack_positions(piece, pos))
        piece, pos = next(pieces_iter, (None, None))
    
    is_in_check = king_position in attack_positions  # Check to see if the King has been attacked or not
    
    # Draw a chessboard with pieces and attack positions
    row = 0
    while row < size:
        col = 0
        while col < size:
            if (row, col) == rook_position:
                print("R", end="  ")  # print Rook
            elif (row, col) == pawn_position:
                print("P", end="  ")  # print Pawn
            elif (row, col) == bishop_position:
                print("B", end="  ")  # print Bishop
            elif (row, col) == queen_position:
                print("Q", end="  ")  # print Queen
            elif (row, col) == king_position:
                print("K", end="  ")  # print King
            elif (row, col) in attack_positions:
                print("x", end="  ")  # Attack location
            else:
                print(".", end="  ")  # vacant position
            col += 1
        print()
        row += 1
    
    print("Success" if is_in_check else "Fail")  # Displays whether the King has been attacked or not

# Use the function
print_chessboard_with_pieces()

if __name__ == "__main__":
    print_chessboard_with_pieces()
    def print_chessboard_with_pieces():
        size = 8
    king_position = (0, 0)  # position of King
    king_position2 = (1, 0)
    rook_position = (0, 1)  # position of Rook
    pawn_position = (1, 2)  # position of Pawn
    bishop_position = (2, 2)  # position of Bishop
    queen_position = (1, 1)  # position of Queen
    
    # Store the position of each piece in the Dictionary
    pieces = {
        "P": pawn_position,
        "B": bishop_position,
        "R": rook_position,
        "Q": queen_position,
    }
    
    # The movement pattern of each piece on the board
    movement_patterns = {
        "P": [  # Attack pattern of Pawn
            ". . . . . . . .",
            ". . . . . . . .",
            ". . X . X . . .",
            ". . . P . . . .",
            ". . . . . . . .",
            ". . . . . . . .",
            ". . . . . . . ."
        ],
        "B": [  # Attack pattern of Bishop
            "X . . . . . X .",
            ". X . . . X . .",
            ". . X . X . . .",
            ". . . B . . . .",
            ". . X . X . . .",
            ". X . . . X . .",
            "X . . . . . X ."
        ],
        "R": [  # Attack pattern of Rook
            ". . . X . . . .",
            ". . . X . . . .",
            ". . . X . . . .",
            "X X X R X X X X",
            ". . . X . . . .",
            ". . . X . . . .",
            ". . . X . . . ."
        ],
        "Q": [  # Attack pattern of Queen
            "X . . X . . X .",
            ". X . X . X . .",
            ". . X X X . . .",
            "X X X Q X X X X",
            ". . X X X . . .",
            ". X . X . X . .",
            "X . . X . . X ."
        ]
    }

    # Shows the movement pattern of each piece
    print("\nMovement Patterns:")
    for piece, pattern in movement_patterns.items():
        print(f"Movement Pattern for {piece}:")
        idx = 0
        while idx < len(pattern):
            print(pattern[idx])
            idx += 1
        print()
