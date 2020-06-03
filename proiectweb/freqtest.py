import time

t1 = time.time()


filename = "input_1.txt"
data  = open(filename).read()

words = data.split()
mylist = list(set(words))

for j in range(0,len(mylist)):
    id = [i for i, x in enumerate(words) if x == mylist[j]]
    print(mylist[j] + ": " + "*"*len(id))


    t2 = time.time()
    print (t2-t1)