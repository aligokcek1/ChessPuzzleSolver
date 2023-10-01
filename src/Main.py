board_file = input()
opponent_file = input()
# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
board_fp = open(board_file, "r")
moves_file = open(opponent_file, "r")
board_string = board_fp.read()
my_color = board_string[:5]
opp_color = "black" if my_color == "white" else "white"
# creating opponent moves list:
opp_moves = moves_file.read()
opp_moves = opp_moves.split("\n")
opponent_moves = []
for i in opp_moves:
    if i.find(",") != -1:
        dumlist = i.split(",")
        opponent_moves.append(dumlist)
    else:
        dumlist = []
        dumlist.append(i)
        opponent_moves.append(dumlist)

# creating piece locations dictionary:
piece_list = board_string.split("\n")[1:-1]
piece_locations = dict()
for i in range(8, 0, -1):
    for j in ["a", "b", "c", "d", "e", "f", "g", "h"]:
        coordinate = f"{j}{i}"
        piece_locations[f"{coordinate}"] = "_"
for piece in piece_list:
    piece_name = piece[:2]
    piece_loc = piece[3:]
    piece_locations[f"{piece_loc}"] = f"{piece_name}"

# creating my pieces list and opponent's pieces list

my_pieces = []
opp_pieces = []
for piece in piece_list:
    if piece[0] == my_color[0].upper():
        my_pieces.append(piece)
    else:
        opp_pieces.append(piece)



def board_printer(piece_locations):
    for i in range(8, 0, -1):
        for j in ["a", "b", "c", "d", "e", "f", "g", "h"]:
            print(piece_locations[f"{j}{i}"], end=" ")
        print()

def pawn_move_list_creator(piece_locations, pawn_location, color, opp_or_me):
    word_list = ["a", "b", "c", "d", "e", "f", "g", "h"]
    if opp_or_me == "me":
        if color == "w":
            move_list = []
            word = pawn_location[0]
            num = int(pawn_location[1])
            if pawn_location[1] != "8":
                if piece_locations[f"{word}{num + 1}"] == "_":
                    move_list.append(f"{pawn_location} {word}{num + 1}")
                if pawn_location[0] != "a":
                    if (piece_locations[f"{word_list[word_list.index(word) - 1]}{num + 1}"] != "_") and (
                            piece_locations[f"{word_list[word_list.index(word) - 1]}{num + 1}"][0] != "W"):
                        move_list.append(f"{pawn_location} {word_list[word_list.index(word) - 1]}{num + 1}")
                if pawn_location[0] != "h":
                    if (piece_locations[f"{word_list[word_list.index(word) + 1]}{num + 1}"] != "_") and (
                            piece_locations[f"{word_list[word_list.index(word) + 1]}{num + 1}"][0] != "W"):
                        move_list.append(f"{pawn_location} {word_list[word_list.index(word) + 1]}{num + 1}")
        else:
            move_list = []
            word = pawn_location[0]
            num = int(pawn_location[1])
            if pawn_location[1] != "8":
                if piece_locations[f"{word}{num + 1}"] == "_":
                    move_list.append(f"{pawn_location} {word}{num + 1}")
                if pawn_location[0] != "a":
                    if (piece_locations[f"{word_list[word_list.index(word) - 1]}{num + 1}"] != "_") and (
                            piece_locations[f"{word_list[word_list.index(word) - 1]}{num + 1}"][0] != "B"):
                        move_list.append(f"{pawn_location} {word_list[word_list.index(word) - 1]}{num + 1}")
                if pawn_location[0] != "h":
                    if (piece_locations[f"{word_list[word_list.index(word) + 1]}{num + 1}"] != "_") and (
                            piece_locations[f"{word_list[word_list.index(word) + 1]}{num + 1}"][0] != "B"):
                        move_list.append(f"{pawn_location} {word_list[word_list.index(word) + 1]}{num + 1}")
    else:
        if color == "w":
            move_list = []
            word = pawn_location[0]
            num = int(pawn_location[1])
            if pawn_location[1] != "1":
                if piece_locations[f"{word}{num - 1}"] == "_":
                    move_list.append(f"{pawn_location} {word}{num - 1}")
                if pawn_location[0] != "a":
                    if (piece_locations[f"{word_list[word_list.index(word) - 1]}{num - 1}"] != "_") and (
                            piece_locations[f"{word_list[word_list.index(word) - 1]}{num - 1}"][0] != "W"):
                        move_list.append(f"{pawn_location} {word_list[word_list.index(word) - 1]}{num - 1}")
                if pawn_location[0] != "h":
                    if (piece_locations[f"{word_list[word_list.index(word) + 1]}{num - 1}"] != "_") and (
                            piece_locations[f"{word_list[word_list.index(word) + 1]}{num - 1}"][0] != "W"):
                        move_list.append(f"{pawn_location} {word_list[word_list.index(word) + 1]}{num - 1}")
        else:
            move_list = []
            word = pawn_location[0]
            num = int(pawn_location[1])
            if pawn_location[1] != "1":
                if piece_locations[f"{word}{num - 1}"] == "_":
                    move_list.append(f"{pawn_location} {word}{num - 1}")
                if pawn_location[0] != "a":
                    if (piece_locations[f"{word_list[word_list.index(word) - 1]}{num - 1}"] != "_") and (
                            piece_locations[f"{word_list[word_list.index(word) - 1]}{num - 1}"][0] != "B"):
                        move_list.append(f"{pawn_location} {word_list[word_list.index(word) - 1]}{num - 1}")
                if pawn_location[0] != "h":
                    if (piece_locations[f"{word_list[word_list.index(word) + 1]}{num - 1}"] != "_") and (
                            piece_locations[f"{word_list[word_list.index(word) + 1]}{num - 1}"][0] != "B"):
                        move_list.append(f"{pawn_location} {word_list[word_list.index(word) + 1]}{num - 1}")
    return move_list

def knight_move_list_creator(piece_locations, knight_location, color):
    w_list = ["0", "0", "0", "a", "b", "c", "d", "e", "f", "g", "h", "0", "0", "0"]
    move_list = []
    word = knight_location[0]
    num = int(knight_location[1])
    pos1 = w_list[w_list.index(word) - 1] + str(num + 2)
    pos2 = w_list[w_list.index(word) - 2] + str(num + 1)
    pos3 = w_list[w_list.index(word) - 2] + str(num - 1)
    pos4 = w_list[w_list.index(word) - 1] + str(num - 2)
    pos5 = w_list[w_list.index(word) + 1] + str(num - 2)
    pos6 = w_list[w_list.index(word) + 2] + str(num - 1)
    pos7 = w_list[w_list.index(word) + 2] + str(num + 1)
    pos8 = w_list[w_list.index(word) + 1] + str(num + 2)
    pos_list = []
    pos_list.append(pos1), pos_list.append(pos2), pos_list.append(pos3), pos_list.append(pos4), pos_list.append(pos5)
    pos_list.append(pos6), pos_list.append(pos7), pos_list.append(pos8)
    for pos in pos_list:
        if color == "w":
            if piece_locations.get(pos) is not None:
                if piece_locations[pos][0] != "W":
                    move_list.append(f"{knight_location} {pos}")
            else:
                continue
        else:
            if piece_locations.get(pos) is not None:
                if piece_locations[pos][0] != "B":
                    move_list.append(f"{knight_location} {pos}")
            else:
                continue
    return move_list

def rook_move_list_creator(piece_locations, rook_location, color):
    move_list = []
    word = rook_location[0]
    num = int(rook_location[1])
    word_list = ["a", "b", "c", "d", "e", "f", "g", "h"]
    index = word_list.index(word)
    if index != 0:
        while index > 0:
            if color == "w":
                if piece_locations[f"{word_list[index-1]}{num}"] == "_":
                    move_list.append(f"{rook_location} {word_list[index-1]}{num}")
                    index -= 1
                    continue
                elif piece_locations[f"{word_list[index-1]}{num}"][0] == "W":
                    break
                else:
                    move_list.append(f"{rook_location} {word_list[index - 1]}{num}")
                    break
            else:
                if piece_locations[f"{word_list[index-1]}{num}"] == "_":
                    move_list.append(f"{rook_location} {word_list[index-1]}{num}")
                    index -= 1
                    continue
                elif piece_locations[f"{word_list[index-1]}{num}"][0] == "B":
                    break
                else:
                    move_list.append(f"{rook_location} {word_list[index - 1]}{num}")
                    break
    index = word_list.index(word)
    if index != 7:
        while index < 7:
            if color == "w":
                if piece_locations[f"{word_list[index+1]}{num}"] == "_":
                    move_list.append(f"{rook_location} {word_list[index+1]}{num}")
                    index += 1
                    continue
                elif piece_locations[f"{word_list[index+1]}{num}"][0] == "W":
                    break
                else:
                    move_list.append(f"{rook_location} {word_list[index + 1]}{num}")
                    break
            else:
                if piece_locations[f"{word_list[index+1]}{num}"] == "_":
                    move_list.append(f"{rook_location} {word_list[index+1]}{num}")
                    index += 1
                    continue
                elif piece_locations[f"{word_list[index+1]}{num}"][0] == "B":
                    break
                else:
                    move_list.append(f"{rook_location} {word_list[index + 1]}{num}")
                    break
    if num != 1:
        while num > 1:
            if color == "w":
                if piece_locations[f"{word}{num - 1}"] == "_":
                    move_list.append(f"{rook_location} {word}{num - 1}")
                    num -= 1
                    continue
                elif piece_locations[f"{word}{num - 1}"][0] == "W":
                    break
                else:
                    move_list.append(f"{rook_location} {word}{num - 1}")
                    break
            else:
                if piece_locations[f"{word}{num - 1}"] == "_":
                    move_list.append(f"{rook_location} {word}{num - 1}")
                    num -= 1
                    continue
                elif piece_locations[f"{word}{num - 1}"][0] == "B":
                    break
                else:
                    move_list.append(f"{rook_location} {word}{num - 1}")
                    break
    num = int(rook_location[1])
    if num != 8:
        while num < 8:
            if color == "w":
                if piece_locations[f"{word}{num + 1}"] == "_":
                    move_list.append(f"{rook_location} {word}{num + 1}")
                    num += 1
                    continue
                elif piece_locations[f"{word}{num + 1}"][0] == "W":
                    break
                else:
                    move_list.append(f"{rook_location} {word}{num + 1}")
                    break
            else:
                if piece_locations[f"{word}{num + 1}"] == "_":
                    move_list.append(f"{rook_location} {word}{num + 1}")
                    num += 1
                    continue
                elif piece_locations[f"{word}{num + 1}"][0] == "B":
                    break
                else:
                    move_list.append(f"{rook_location} {word}{num + 1}")
                    break
    return move_list

def bishop_move_list_creator(piece_locations, bishop_location, color):
    move_list = []
    num = int(bishop_location[1])
    word = bishop_location[0]
    word_list = ["a", "b", "c", "d", "e", "f", "g", "h"]
    index = word_list.index(word)
    while (index - 1 >= 0) and (num - 1 >= 1):
        if color == "w":
            if piece_locations[f"{word_list[index-1]}{num-1}"] == "_":
                move_list.append(f"{bishop_location} {word_list[index-1]}{num-1}")
                index -= 1
                num -= 1
                continue
            elif piece_locations[f"{word_list[index-1]}{num-1}"][0] == "B":
                move_list.append(f"{bishop_location} {word_list[index - 1]}{num - 1}")
                break
            else: break
        else:
            if piece_locations[f"{word_list[index-1]}{num-1}"] == "_":
                move_list.append(f"{bishop_location} {word_list[index-1]}{num-1}")
                index -= 1
                num -= 1
                continue
            elif piece_locations[f"{word_list[index-1]}{num-1}"][0] == "W":
                move_list.append(f"{bishop_location} {word_list[index - 1]}{num - 1}")
                break
            else: break
    num = int(bishop_location[1])
    index = word_list.index(word)
    while (index + 1 <= 7) and (num + 1 <= 8):
        if color == "w":
            if piece_locations[f"{word_list[index+1]}{num+1}"] == "_":
                move_list.append(f"{bishop_location} {word_list[index+1]}{num+1}")
                index += 1
                num += 1
                continue
            elif piece_locations[f"{word_list[index+1]}{num+1}"][0] == "B":
                move_list.append(f"{bishop_location} {word_list[index + 1]}{num + 1}")
                break
            else: break
        else:
            if piece_locations[f"{word_list[index+1]}{num+1}"] == "_":
                move_list.append(f"{bishop_location} {word_list[index+1]}{num+1}")
                index += 1
                num += 1
                continue
            elif piece_locations[f"{word_list[index+1]}{num+1}"][0] == "W":
                move_list.append(f"{bishop_location} {word_list[index + 1]}{num + 1}")
                break
            else: break
    num = int(bishop_location[1])
    index = word_list.index(word)
    while (index - 1 >= 0) and (num + 1 <= 8):
        if color == "w":
            if piece_locations[f"{word_list[index - 1]}{num + 1}"] == "_":
                move_list.append(f"{bishop_location} {word_list[index - 1]}{num + 1}")
                index -= 1
                num += 1
                continue
            elif piece_locations[f"{word_list[index - 1]}{num + 1}"][0] == "B":
                move_list.append(f"{bishop_location} {word_list[index - 1]}{num + 1}")
                break
            else:
                break
        else:
            if piece_locations[f"{word_list[index - 1]}{num + 1}"] == "_":
                move_list.append(f"{bishop_location} {word_list[index - 1]}{num + 1}")
                index -= 1
                num += 1
                continue
            elif piece_locations[f"{word_list[index - 1]}{num + 1}"][0] == "W":
                move_list.append(f"{bishop_location} {word_list[index - 1]}{num + 1}")
                break
            else:
                break
    num = int(bishop_location[1])
    index = word_list.index(word)
    while (index + 1 <= 7) and (num - 1 >= 1):
        if color == "w":
            if piece_locations[f"{word_list[index + 1]}{num - 1}"] == "_":
                move_list.append(f"{bishop_location} {word_list[index + 1]}{num - 1}")
                index += 1
                num -= 1
                continue
            elif piece_locations[f"{word_list[index + 1]}{num - 1}"][0] == "B":
                move_list.append(f"{bishop_location} {word_list[index + 1]}{num - 1}")
                break
            else:
                break
        else:
            if piece_locations[f"{word_list[index + 1]}{num - 1}"] == "_":
                move_list.append(f"{bishop_location} {word_list[index + 1]}{num - 1}")
                index += 1
                num -= 1
                continue
            elif piece_locations[f"{word_list[index + 1]}{num - 1}"][0] == "W":
                move_list.append(f"{bishop_location} {word_list[index + 1]}{num - 1}")
                break
            else:
                break
    return move_list

def queen_move_list_creator(piece_locations, queen_location, color):
    return bishop_move_list_creator(piece_locations, queen_location, color) + rook_move_list_creator(piece_locations, queen_location, color)

def king_move_list_creator(piece_locations, king_location, color):
    word_list = ["0","a", "b", "c", "d", "e", "f", "g", "h","0"]
    word = king_location[0]
    word_index = word_list.index(word)
    num = int(king_location[1])
    pos_list = []
    move_list = []
    pos1 = word_list[word_index-1] + str(num)
    pos2 = word_list[word_index - 1] + str(num-1)
    pos3 = word_list[word_index] + str(num-1)
    pos4 = word_list[word_index + 1] + str(num-1)
    pos5 = word_list[word_index + 1] + str(num)
    pos6 = word_list[word_index + 1] + str(num+1)
    pos7 = word_list[word_index] + str(num+1)
    pos8 = word_list[word_index - 1] + str(num+1)
    pos_list.append(pos1), pos_list.append(pos2), pos_list.append(pos3), pos_list.append(pos4)
    pos_list.append(pos5), pos_list.append(pos6), pos_list.append(pos7), pos_list.append(pos8)
    for pos in pos_list:
        if color == "w":
            if piece_locations.get(pos) is not None:
                if piece_locations[f"{pos}"] == "_":
                    move_list.append(f"{king_location} {pos}")
                    continue
                elif piece_locations[f"{pos}"][0] == "B":
                    move_list.append(f"{king_location} {pos}")
                    continue
                else: continue
        else:
            if piece_locations.get(pos) is not None:
                if piece_locations[f"{pos}"] == "_":
                    move_list.append(f"{king_location} {pos}")
                    continue
                elif piece_locations[f"{pos}"][0] == "W":
                    move_list.append(f"{king_location} {pos}")
                    continue
                else: continue

    return move_list

def king_location_finder(piece_locations):
    for k, v in piece_locations.items():
        if v == "_":
            continue
        if v[1] == "K" and v[0] == opp_color.upper()[0]:
            king_location = k
    return king_location
def my_move_list(my_pieces, my_color, piece_locations):
    color = my_color[0]
    move_list = []
    for piece in my_pieces:
        piece_location = piece[3:]
        if piece[1] == "Q":
            move_list += queen_move_list_creator(piece_locations, piece_location, color)
        elif piece[1] == "B":
            move_list += bishop_move_list_creator(piece_locations,piece_location,color)
        elif piece[1] == "N":
            move_list += knight_move_list_creator(piece_locations,piece_location,color)
        elif piece[1] == "R":
            move_list += rook_move_list_creator(piece_locations,piece_location,color)
        elif piece[1] == "P":
            move_list += pawn_move_list_creator(piece_locations,piece_location, color, "me")
        elif piece[1] == "K":
            move_list += king_move_list_creator(piece_locations, piece_location, color)
    return move_list
def opp_move_list(opp_pieces, opp_color, piece_locations):
    color = opp_color[0]
    move_list = []
    new_move_list = []
    for piece in opp_pieces:
        piece_location = piece[3:]
        if piece[1] == "Q":
            move_list += queen_move_list_creator(piece_locations, piece_location, color)
        elif piece[1] == "B":
            move_list += bishop_move_list_creator(piece_locations,piece_location,color)
        elif piece[1] == "N":
            move_list += knight_move_list_creator(piece_locations,piece_location,color)
        elif piece[1] == "R":
            move_list += rook_move_list_creator(piece_locations,piece_location,color)
        elif piece[1] == "P":
            move_list += pawn_move_list_creator(piece_locations,piece_location, color, "opp")
        elif piece[1] == "K":
            move_list += king_move_list_creator(piece_locations, piece_location, color)
    for move in move_list:
        dum_board = piece_locations.copy()
        dum_board = piece_list_converter(dum_board, move)
        if check_controller(my_move_list(new_piece_lists("my", dum_board),my_color,dum_board),king_location_finder(dum_board)) != "check":
            new_move_list.append(move)
    return new_move_list
def check_controller(move_list, king_location):
    for i in move_list:
        attacking_square = i[3:]
        if attacking_square == king_location:
            return "check"
    return "no check"


def new_piece_lists(my_or_opp, board_locations):
    new_pieces = []
    if my_or_opp == "my":
        for k, v in board_locations.items():
            if v == "_":
                continue
            elif v[0] == my_color.upper()[0]:
                str = v + " " + k
                new_pieces.append(str)
            else:
                continue
    else:
        for k, v in board_locations.items():
            if v == "_":
                continue
            elif v[0] == opp_color.upper()[0]:
                str = v + " " + k
                new_pieces.append(str)
            else:
                continue
    return new_pieces
def piece_list_converter(location_list, move):
    initial_pos = move[:2]
    next_pos = move[3:]
    piece = location_list.get(initial_pos)
    location_list[next_pos] = piece
    location_list[initial_pos] = "_"
    return location_list
result = ""

index = 0
def chess_solver(board):

    global index, opponent_moves
    global result
    opp_king_location = king_location_finder(board)
    for move in my_move_list(new_piece_lists("my",board), my_color,board):

        dummy = board.copy()
        dum_board = piece_list_converter(dummy,move)
        opp_valid = opp_move_list(new_piece_lists("opp",dum_board),opp_color,dum_board)
        if opp_valid == [] and check_controller(
                my_move_list(new_piece_lists("my", dum_board), my_color, dum_board), opp_king_location) == "check":
            result += move + "\n"
            return print(result[:-1])
        if index > len(opponent_moves)-1:
            continue
        if opp_valid == opponent_moves[index]:
            result += move + "\n"
            dum_board = piece_list_converter(dum_board, opponent_moves[index][0])
            index += 1
            chess_solver(dum_board)
        else:
            continue


chess_solver(piece_locations)


moves_file.close()
board_fp.close()
# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
