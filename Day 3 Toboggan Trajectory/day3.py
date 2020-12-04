def process_file(m_list):
    m = open('input.txt', 'r', encoding='utf-8')
    for line in m:
        m_list.append(line)
    m.close()
    
    
    
def specific_traj(x_skip, y_skip):
    m_list = []
    trees_hit = 0
    x = 0
    
    process_file(m_list)
    for y in m_list[::y_skip]:
        if x > 30:
            x -= 31
        if y[x] == '#':
            trees_hit += 1
        x += x_skip
            
    return trees_hit



def mult_of_traj():
    options = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    mult_of_traj = 1
    for opt in options:
        mult_of_traj *= specific_traj(opt[0], opt[1])
        
    return mult_of_traj