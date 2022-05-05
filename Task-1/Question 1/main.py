
with open('onelinefile.txt','r') as f:      #Context manager Will automatically gets closed
    data = f.readline()
    print(data)
    sD = data.split()
    print(sD)




#f = open('onelinefile.txt','r')
#print(f.name)
#print(f.mode)

