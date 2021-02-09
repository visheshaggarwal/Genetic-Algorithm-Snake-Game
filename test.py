import numpy as np
def load():
    f = open("basicBarrier/uniformCrossover/gen_"+str(11), 'r')
    c = f.read()
    load_pop = np.zeros((75, 42))
    i = 0

    k = 0
    while i < 75:
        j = 0
        while j < 42:
            while k < len(c) and c[k]!='-' and (c[k]<'0' or c[k]>'9'):
                k+=1
            
            if k>= len(c):
                j += 1
                i += 1
                break

            neg = False
            if c[k]=='-':
                neg = True
                k += 1
            
            l = k
            while l<len(c) and (c[l]!=' ' and c[l]!='\n' and c[l]!=']'):
                l+= 1
        
            num = float(c[k:l])
        
            if neg:
                num *= -1
            
            load_pop[i][j] = num
            k = l
            j += 1
            
        i+=1
    return load_pop