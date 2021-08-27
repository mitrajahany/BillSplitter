from random import choice


DICT_FRIENDS = {}


def input_of_friends():
    try:
        number_of_friends = int(input('Enter the number of friends joining (including you):\n'))
    except ValueError:
        return 'No one is joining for the party'
    else:
        if number_of_friends < 1:
            return 'No one is joining for the party'
        print('Enter the name of every friend (including you), each on a new line:\n')
        for _ in range(number_of_friends):
            name_of_friend = input()
            DICT_FRIENDS[name_of_friend] = 0
        total_bill_value = int(input('Enter the total bill value:\n'))
        split_the_total_bill_equally_and_update_values(number_of_friends, total_bill_value)
        print(choose_the_lucky_one(number_of_friends, total_bill_value))
        return DICT_FRIENDS


def split_the_total_bill_equally_and_update_values(number_of_friends, total_bill_value, lucky_name=None):
    split_values = round(total_bill_value / number_of_friends, 2)
    for name in DICT_FRIENDS:
        DICT_FRIENDS[name] = split_values
    if lucky_name:
        DICT_FRIENDS[lucky_name] = 0
    return split_values


def choose_the_lucky_one(number_of_friends, total_bill_value):
    """This function chooses a random name from the dictionary,

    this person's share will be paid for by others
    """
    use_choose_the_lucky_one = input('Do you want to use the "Who is lucky?" feature? Write Yes/No:\n').lower()
    if use_choose_the_lucky_one == 'no':
        return 'No one is going to be lucky'
    else:
        lucky_name = choice(list(DICT_FRIENDS.keys()))
        split_the_total_bill_equally_and_update_values(number_of_friends - 1, total_bill_value, lucky_name)
        return f'{lucky_name} is the lucky one!\n'


print(input_of_friends())
