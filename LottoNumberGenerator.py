import random as r

def get_powerball():
    list_pb = []
    for i in range(1,10):
        pw_rand = r.randint(1, 26)
        list_pb.append(pw_rand)
    avg = (sum(list_pb) / len(list_pb))
    return avg


def get_main_numbers():
    win_nums = []
    for num in range(1, 20):
        ran_num = r.randint(1, 69)
        if ran_num in win_nums:
            continue
        else:
            win_nums.append(ran_num)
        if len(win_nums) == 5:
            break
    win_nums.sort()
    return win_nums


if __name__ == '__main__':
    numbers = get_main_numbers()
    print(f'Winning numbers: {numbers} "PB": {round(get_powerball())}')