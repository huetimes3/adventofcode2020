def process_file(num_list):
    expenses = open('input.txt', 'r', encoding='utf-8')
    for line in expenses:
        num_list.append(int(line))
    expenses.close()



def get_mult_of_two():
    
    num_list = []
    process_file(num_list)
    
    for entry in num_list:
        if 2020-entry in num_list:
            return entry * (2020-entry)
  
  
  
def get_mult_of_three():
    num_list = []
    process_file(num_list)
    
    for entry in num_list:
        diff_sum = 2020 - entry
        for entry2 in num_list:
            if diff_sum-entry2 in num_list:
                return entry * entry2 * (diff_sum - entry2)