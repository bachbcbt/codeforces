n=int(input())
sum=0
for i in range(0,n):
    s=input()
    if s=='Tetrahedron':
        sum=sum+4
    if s=='Cube':
        sum=sum+6
    if s=='Octahedron':
        sum=sum+8
    if s=='Dodecahedron':
        sum=sum+12
    if s=='Icosahedron':
        sum=sum+20
print(sum)