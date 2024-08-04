from random import choice

def alpha_characters():
    lower_list = [chr(asc) for asc in range(ord('A'), ord('Z')+1)]
    upper_list = [chr(asc) for asc in range(ord('a'), ord('z')+1)]
    alpha_list = upper_list + lower_list
    return(alpha_list)

def num_characters():
    num_list = [str(num) for num in range(10)]
    return(num_list)

def special_characters():
    special_1 = [chr(asc) for asc in range(ord('!'), ord('/'))]
    special_2 = [chr(asc) for asc in range(ord(':'), ord('@'))]
    special_3 = [chr(asc) for asc in range(ord('['), ord('_'))]
    special_4 = [chr(asc) for asc in range(ord('{'), ord('~'))]
    special_list = special_1 + special_2 + special_3 + special_4
    return(special_list)

def include_numbers(password_list, num_characters):
    add_numbers = None
    while add_numbers != 'y' and add_numbers != 'n':
        add_numbers = input('would you like to include numbers for added security? [y/n]: ')
        if add_numbers == 'y':
            password_list += num_characters()
        elif add_numbers == 'n': break
    return(password_list)

def include_special(password_list, special_characters):
    add_special = None
    while add_special != 'y' and add_special != 'n':
        add_special = input('would you like to include special characters for added security? [y/n]: ')
        if add_special == 'y':
            password_list += special_characters()
        elif add_special == 'n': break
    return(password_list)

def password_length():
    while True:
        try:
            number = (int(input('How long would you like your password to be?: ')))
            if number > 0: break
            else: print('Invalid input try again!')
        except ValueError:
             print('Invalid input try again!')
    return number
            

def generate_password(password_list,length):
    generated_list = []
    for character in range(length):
        generated_list.append(choice(password_list))
    return generated_list

def main():
    password_list = alpha_characters()
    password_list = include_numbers(password_list, num_characters)
    password_list = include_special(password_list, special_characters)
    length = password_length()
    password = generate_password(password_list, length)
    print(''.join(password))


main()