import sys,struct,zipfile,re; sys.path.insert(0,'lib')
import xml.etree.ElementTree as ET
from xlsb import records, rd_wstr, Book, a1
b=Book('FRE.xlsb'); z=b.z
out=open('out/_comentarios.txt','w')
for nm,tgt in b.sheets:
    rp='xl/worksheets/_rels/'+tgt.split('/')[-1]+'.rels'
    try: x=ET.fromstring(z.read(rp))
    except KeyError: continue
    for e in x:
        t=e.get('Target')
        if 'comments' not in t: continue
        path='xl/'+t.replace('../','')
        cur=None
        out.write('\n########## %s (%s)\n'%(nm,path))
        for r in records(z.read(path)):
            if r.id==635:
                r1,r2,c1,c2=struct.unpack_from('<IIII',r.data,4); cur=a1(r1,c1)
            elif r.id==637:
                o=1; n=struct.unpack_from('<I',r.data,o)[0]; o+=4
                s=r.data[o:o+2*n].decode('utf-16-le','replace')
                out.write('%s: %s\n'%(cur, s.replace('\n',' \\n ')))
out.close()
print(open('out/_comentarios.txt').read()[:200])
