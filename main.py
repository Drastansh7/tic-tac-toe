
def sum(a,b,c):
    return a + b + c
def print_board(x_state, o_state):

    zero = "X" if x_state[0] else ("0" if o_state[0] else "0")
    one = "X" if x_state[1] else ("0" if o_state[1] else "1")
    two = "X" if x_state[2] else ("0" if o_state[2] else "2")
    three = "X" if x_state[3] else ("0" if o_state[3] else "3")
    four = "X" if x_state[4] else ("0" if o_state[4] else "4")
    five = "X" if x_state[5] else ("0" if o_state[5] else "5")
    six = "X" if x_state[6] else ("0" if o_state[6] else "6")
    seven = "X" if x_state[7] else ("0" if o_state[7] else "7")
    eight = "X" if x_state[8] else ("0" if o_state[8] else "8")

    print(f" {zero} | {one} | {two}")
    print(f"---|---|---")
    print(f" {three} | {four} | {five} ")
    print(f"---|---|---")
    print(f" {six} | {seven} | {eight} ")

def check_winner(x_state, o_state):
    wins = [[0, 1, 2], [3, 4, 5,], [6, 7, 8,], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

    for win in wins:
        if sum(x_state[win[0]], x_state[win[1]], x_state[win[2]]) == 3:
            print("X won the match")
            return 1

        if sum(o_state[win[0]], o_state[win[1]], o_state[win[2]]) == 3:
            print("0 won the match")
            return 0

    return -1


if __name__ == '__main__':
    x_state = [0,0,0,0,0,0,0,0,0]
    o_state = [0,0,0,0,0,0,0,0,0]
    turn = 1 # 1 for X and 0 for 0
    print('Welcome ot tic tac toe')
    while True:
        print_board(x_state, o_state)
        if turn == 1:
            print("X's Chance")
            x_val = int(input("Enter a value: "))
            x_state[x_val] = 1
            turn = 0
        else:
            print("0's chance")
            o_val = int(input("Enter a value "))
            o_state[o_val] = 1
            turn = 1

        cwin = check_winner(x_state, o_state)
        if cwin != -1:
            print("match over")
            break






