def process_file(pas_list):
    pas = open('input.txt', 'r', encoding='utf-8')
    for line in pas:
        line = line.replace('-', ' ')
        line = line.replace(':', ' ')
        line_split = line.split()
        pas_list.append(line_split)
    pas.close()



def get_valid_pass_1():
    num = 0
    pas_list = []
    process_file(pas_list)
    
    for line in pas_list:
        if int(line[0]) <= line[3].count(line[2]) <= int(line[1]):
            num += 1
    
    return num



def get_valid_pass_2():
    num = 0
    pas_list = []
    process_file(pas_list)
    
    for line in pas_list:
        if (line[3][int(line[0])-1] == line[2]) != (line[3][int(line[1])-1] == line[2]):
            num += 1
    
    return num