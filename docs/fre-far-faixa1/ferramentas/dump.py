import sys,os,json; sys.path.insert(0,'lib')
from xlsb import Book, a1, colname
b=Book('FRE.xlsb')
os.makedirs('out',exist_ok=True)
summary=[]
allcells={}
for nm,tgt in b.sheets:
    cells,merges=b.sheet(nm)
    allcells[nm]=cells
    nf=sum(1 for v,f in cells.values() if f)
    sh=sum(1 for v,f in cells.values() if f and '@SHARED@' in f)
    summary.append((nm,len(cells),nf,sh))
    safe=nm.replace('/','_').replace(' ','_')
    with open('out/%s.txt'%safe,'w') as fh:
        rows=sorted(set(r for r,c in cells))
        for r in rows:
            cs=sorted(c for rr,c in cells if rr==r)
            line=[]
            for c in cs:
                v,f=cells[(r,c)]
                if v is None and not f: continue
                t=a1(r,c)+': '
                if f: t+='='+f
                if v is not None:
                    t+=('  {'+repr(v)+'}' if f else repr(v))
                line.append(t)
            if line: fh.write(' | '.join(line)+'\n')
print('%-38s %8s %8s %8s'%('sheet','cells','formulas','shared'))
for s in summary: print('%-38s %8d %8d %8d'%s)
json.dump({'names':[[n[0],n[1],n[2]] for n in b.names]},open('out/_names.json','w'),ensure_ascii=False,indent=0)
