import heapq
n, D = map(int, raw_input().split())
R = map(int, raw_input().split())
C = map(int, raw_input().split())


RI = [(R[i],i) for i in range(len(R))]
print RI

RI = sorted(RI,key=lambda x:x[0])

print RI

j=len(RI)

for i in range(len(RI)):

    while j>=0:
         
        
