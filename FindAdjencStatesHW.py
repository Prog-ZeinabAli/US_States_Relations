from logpy import fact,Relation,run,var,conde
adjence=Relation()
castal=Relation()
adjence1=file="adjacent_states.txt"
castal1=file="coastal_states.txt"
with open(adjence1,'r') as f:
    data=f.read()
    words=[line.strip().split(',')for line in f if line and line[0].isalpha()]
for state in words:
    fact(castal,state)

for L in words:
    head=L[0]
    tail=L[1:7]
    for state in tail:
       fact(adjence,head,state)
x=var()
z=run(0,x,(adjence('Montana',x),adjence('Nivada',x)))
print z
print('Yes' if len(z) else 'No')

