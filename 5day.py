import sys

all=[]
todo=[]
for line in sys.stdin:
    all.append(line.rstrip())
  
for cadena in all:
	min=0
	max=127
	min1=0
	max1=7
	for letra in cadena:
		if letra == "F" and i<8:
			max=min+int((max-min)/2)
			r=max
		elif i<8:
			min=min+int((max-min)/2)+1
			r=min
		elif i>7 and letra == "L":
			max1=min1+int((max1-min1)/2)
			c=max1
		else:
			min1=min1+int((max1-min1)/2)+1
			c=min1
			
	ok=r*8+c
	todo.append(int(ok))

todo.sort()
i=todo[0]
max=todo[len(todo)-1]

for asi in todo:
	if i != asi:
		break
	i=i+1
	
print (max)
print(i-1)
