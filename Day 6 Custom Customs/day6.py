def process_file(c_list):
    c = open('input.txt', 'r', encoding='utf-8')
    temp = []
    for line in c:
        if len(line) == 1:
            c_list.append(temp)
            temp = []
            continue
        temp.append(line[:-1])
    c.close()
    
    
    
def sum_count():
    c_list = []
    process_file(c_list)
    count = 0
    
    for q in c_list:
        count += len(set(q))
    return count

    


def every_one():
    c_list = []
    process_file(c_list)
    count = 0
    
    for q in c_list: # I'm so sorry if you're reading this
        for char in q[0]:
            in_all = True
            
            for q2 in q[1:]:
                if q2.count(char) == 1:
                    continue
                else:
                    in_all = False
                    break
                
            if in_all:
                count+=1
    return count