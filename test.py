import random

def create_massives(n):
    # this massive will contain little massives
    main_mas=[]
    
    # generate lens of little massives  
    numbers = list(range(1, n+1))
    random.shuffle(numbers)

    # generate n little massives
    for i in range(n):
        m=[]
        # choose len of little massive
        little_mas_len=numbers[i]


        # fill little massive
        for j in range(1,little_mas_len+1):
            a=random.uniform(1,10)
            m.append(a)
        main_mas.append(m)
        
    return main_mas, numbers


print(create_massives(1))
            
