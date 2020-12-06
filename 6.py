import sys

all=[]

for line in sys.stdin:
    all.append(line.rstrip())
    
i=0
p=0
j=0
conj=set()
all_yes=set()
todo=''
for person in all:
	
	if len(person.strip()) == 0:
		i=i+len(conj)
		for elem in conj:
			if todo.count(elem, 0, len(todo)) == p:
				all_yes.add(elem)
		
		j=j+len(all_yes)
		all_yes=set()
		conj=set()
		todo=''
		p=0
			
	else:
		todo=todo+person
		p=p+1
		
	for question in person:
		conj.add(question)
	
		
i=i+len(conj)
for elem in conj:
	if todo.count(elem, 0, len(todo)) == p:
		all_yes.add(elem)
		
j=j+len(all_yes)
print("final 1:",i)
print("final 2:",j)
