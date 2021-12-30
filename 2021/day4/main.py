import numpy as np

with open('test.txt') as f:
    test = f.read().splitlines()

with open('input.txt') as f:
    input = f.read().splitlines()

SIZE = 5

def convert_list_string_to_int(x):
    return list(map(int,x))

def remove_empty_string_from_list(x):
    return [i for i in x if i]

def load_data(data):
    number_list = convert_list_string_to_int(data[0].split(','))
    board_list = []
    remaining_data = data[1:]
    for i in range(0,len(remaining_data),6):
        temp_board = remaining_data[i+1:i+6]
        value_board = np.zeros([SIZE,SIZE])
        for j in range(5):
            temp = temp_board[j].split(' ')
            temp_no_empty = [i for i in temp if i]
            temp_int = convert_list_string_to_int(temp_no_empty)
            value_board[j] = np.array(temp_int)
        board_list.append(value_board)
    board_list = np.array(board_list)
    return number_list,board_list

# check if the board wins
def check_board(bool_board):
    win = False
    check_columns = any(bool_board.sum(axis=0) == SIZE)
    check_rows= any(bool_board.sum(axis=1) == SIZE)
    if check_columns or check_rows:
        win = True
    return win

def mark_board(value_board,bool_board,number):
    bool_board[np.where(value_board==number)] = 1
    return bool_board

def sum_unmarked_numbers(value_board,bool_board):
    unmarked = np.where(bool_board==0)
    unmarked_values = value_board[unmarked]
    sum = unmarked_values.sum()
    return sum 

def play_bingo(data):
    number_list,value_board_list = load_data(data)
    bool_board_list = np.zeros(value_board_list.shape)
    win = False
    nb = 0
    while not win and nb < len(number_list):
        number_called = number_list[nb]
        for i in range(len(value_board_list)):
            value_board = value_board_list[i]
            bool_board = bool_board_list[i]
            bool_board = mark_board(value_board,bool_board,number_called)
            win = check_board(bool_board)
            
            value_board_list[i] = value_board
            bool_board_list[i] = bool_board
        print(number_called,bool_board_list)
        nb += 1

    sum = sum_unmarked_numbers(value_board,bool_board)
    print(number_called,sum)
    return number_called*sum

# print(play_bingo(test)) # 4512
print(play_bingo(input)) #54720