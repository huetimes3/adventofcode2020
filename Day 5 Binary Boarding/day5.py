def process_file(b_list):
    b = open('input.txt', 'r', encoding='utf-8')
       
    for line in b:
        line = line.replace('F', '0')
        line = line.replace('B', '1')
        line = line.replace('L', '0')
        line = line.replace('R', '1')
        line_l = []
        
        line_l.append(line[:7])
        line_l.append(line[7:-1])
        b_list.append(line_l)
    b.close()
    
def get_id(b):
    row = int(b[0],2)
    col = int(b[1],2)
    return row * 8 + col
    
def highest_id():
    b_list = []
    process_file(b_list)
    highest_id = 0
    for b in b_list:
        s_id = get_id(b)
        if s_id > highest_id:
            highest_id = s_id
    return highest_id



def get_seat():
    b_list = []
    process_file(b_list)
    b_id = []
    for b in b_list:
        s_id = get_id(b)
        b_id.append(s_id)
    b_id.sort()
    for i, b in enumerate(b_id):
        if i == 0:
            continue
        if b - 1 != b_id[i-1] or b + 1 != b_id[i+1]:
            return b+1

        