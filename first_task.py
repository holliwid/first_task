import string


def data_preparation(filepath):
    with open(filepath) as file:
        sorted_list = []
        lines = file.read()
        lines_list = lines.split(',')
        lines_list_without_quotes = [name[1:-1] for name in lines_list]
        sorted_list = sorted(lines_list_without_quotes)       
    return sorted_list

def calculating_an_alphabetical_sum(list_names):
    alphabetical_sum = []
    alphabet = list(string.ascii_uppercase)
    for name in list_names:
        alphabetical_sum_name = 0
        for char in name:
            alphabetical_sum_name += alphabet.index(char)+1
        alphabetical_sum.append(alphabetical_sum_name)
    return alphabetical_sum

def multiplication_alp_sum_by_index_of_word(list_names, alphabetical_sum):
    resulting_sum = 0
    for index in range(len(list_names)):
        resulting_sum += alphabetical_sum[index] * (index + 1)
    return resulting_sum     


if __name__ == "__main__":
    filepath = 'names.txt'

    list_names = data_preparation(filepath)
    alphabetical_sum = calculating_an_alphabetical_sum(list_names)
    resulting_sum = multiplication_alp_sum_by_index_of_word(list_names, alphabetical_sum)
    print(resulting_sum)