import sys; sys.path.insert(0,'lib')
from xlsb import Book, a1, colname
b=Book('FRE.xlsb')
sheet=sys.argv[1]; cols=sys.argv[2].split(','); r1=int(sys.argv[3]); r2=int(sys.argv[4])
show=sys.argv[5] if len(sys.argv)>5 else 'v'
cells,_=b.sheet(sheet)
def ci(s):
    n=0
    for ch in s: n=n*26+ord(ch)-64
    return n-1
idx=[ci(c) for c in cols]
for r in range(r1-1,r2):
    row=[]
    for c in idx:
        v,f=cells.get((r,c),(None,None))
        t=''
        if show=='f' and f: t='='+f
        elif v is not None: t=str(v)
        row.append(t)
    if any(row): print(r+1,'|','|'.join(row))
