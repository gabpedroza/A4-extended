import numpy as np
multipliers = np.ones((5,3))
with open("code/myKaiser9Diary") as file:
    d = file.readlines()
    i = 0
    j = 0
    while i < len(d):
        if('_ch' in d[i] or 'x:' in d[i]): 
            if 'e' not in d[i+1]:
                d.insert(i+1, '\n')
                d.insert(i+1, "1.0e+00 *\n")
            multipliers[(j//3)][j%3] = float(d[i+1][:-3])
            j += 1
        
        i+=1   
    #print(d) 
    #print(multipliers)
    d = "".join(d)
    d = d.split("ch1:")

d = d[1:]
for i, s in enumerate(d):
    d[i] = s.split('--')
    d[i] = d[i][0]
    d[i] = d[i].split('\n\n')
    #print(d)
    d[i] = [k for k in d[i] if len(k) > 100]
    d[i] = [a.split('\n') for a in d[i]]
    d[i] = [[n.replace(' ', '').replace('i', 'j') for n in j if len(n.replace(' ', '')) > 0 and 'x' not in n and 'ch' not in n] for j in d[i]]
    #print(len(d[i][0]))
    d[i] = [multipliers[i][k]*np.array([complex(n) if k < 2 else float(n) for n in j])[:1000] for k, j in enumerate(d[i])]
    
print(d)