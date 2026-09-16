# -*- coding: utf-8 -*-
"""Parser BIFF12 (.xlsb) minimalista: valores, formulas e nomes definidos."""
import struct, zipfile, io, re

FTAB = {0:'COUNT',1:'IF',2:'ISNA',3:'ISERROR',4:'SUM',5:'AVERAGE',6:'MIN',7:'MAX',8:'ROW',9:'COLUMN',
10:'NA',11:'NPV',12:'STDEV',13:'DOLLAR',14:'FIXED',15:'SIN',16:'COS',17:'TAN',18:'ATAN',19:'PI',
20:'SQRT',21:'EXP',22:'LN',23:'LOG10',24:'ABS',25:'INT',26:'SIGN',27:'ROUND',28:'LOOKUP',29:'INDEX',
30:'REPT',31:'MID',32:'LEN',33:'VALUE',34:'TRUE',35:'FALSE',36:'AND',37:'OR',38:'NOT',39:'MOD',
40:'DCOUNT',41:'DSUM',42:'DAVERAGE',43:'DMIN',44:'DMAX',45:'DSTDEV',46:'VAR',47:'DVAR',48:'TEXT',
49:'LINEST',50:'TREND',51:'LOGEST',52:'GROWTH',53:'GOTO',54:'HALT',55:'RETURN',56:'PV',57:'FV',
58:'NPER',59:'PMT',60:'RATE',61:'MIRR',62:'IRR',63:'RAND',64:'MATCH',65:'DATE',66:'TIME',67:'DAY',
68:'MONTH',69:'YEAR',70:'WEEKDAY',71:'HOUR',72:'MINUTE',73:'SECOND',74:'NOW',75:'AREAS',76:'ROWS',
77:'COLUMNS',78:'OFFSET',79:'ABSREF',80:'RELREF',81:'ARGUMENT',82:'SEARCH',83:'TRANSPOSE',84:'ERROR',
85:'STEP',86:'TYPE',87:'ECHO',88:'SET.NAME',89:'CALLER',90:'DEREF',91:'WINDOWS',92:'SERIES',
93:'DOCUMENTS',94:'ACTIVE.CELL',95:'SELECTION',96:'RESULT',97:'ATAN2',98:'ASIN',99:'ACOS',100:'CHOOSE',
101:'HLOOKUP',102:'VLOOKUP',103:'LINKS',104:'INPUT',105:'ISREF',106:'GET.FORMULA',107:'GET.NAME',
108:'SET.VALUE',109:'LOG',110:'EXEC',111:'CHAR',112:'LOWER',113:'UPPER',114:'PROPER',115:'LEFT',
116:'RIGHT',117:'EXACT',118:'TRIM',119:'REPLACE',120:'SUBSTITUTE',121:'CODE',122:'NAMES',
123:'DIRECTORY',124:'FIND',125:'CELL',126:'ISERR',127:'ISTEXT',128:'ISNUMBER',129:'ISBLANK',130:'T',
131:'N',132:'FOPEN',133:'FCLOSE',134:'FSIZE',135:'FREADLN',136:'FREAD',137:'FWRITELN',138:'FWRITE',
139:'FPOS',140:'DATEVALUE',141:'TIMEVALUE',142:'SLN',143:'SYD',144:'DDB',145:'GET.DEF',146:'REFTEXT',
147:'TEXTREF',148:'INDIRECT',149:'REGISTER',150:'CALL',151:'ADD.BAR',152:'ADD.MENU',153:'ADD.COMMAND',
154:'ENABLE.COMMAND',155:'CHECK.COMMAND',156:'RENAME.COMMAND',157:'SHOW.BAR',158:'DELETE.MENU',
159:'DELETE.COMMAND',160:'GET.CHART.ITEM',161:'DIALOG.BOX',162:'CLEAN',163:'MDETERM',164:'MINVERSE',
165:'MMULT',166:'FILES',167:'IPMT',168:'PPMT',169:'COUNTA',170:'CANCEL.KEY',171:'FOR',172:'WHILE',
173:'BREAK',174:'NEXT',175:'INITIATE',176:'REQUEST',177:'POKE',178:'EXECUTE',179:'TERMINATE',
180:'RESTART',181:'HELP',182:'GET.BAR',183:'PRODUCT',184:'FACT',185:'GET.CELL',186:'GET.WORKSPACE',
187:'GET.WINDOW',188:'GET.DOCUMENT',189:'DPRODUCT',190:'ISNONTEXT',191:'GET.NOTE',192:'NOTE',
193:'STDEVP',194:'VARP',195:'DSTDEVP',196:'DVARP',197:'TRUNC',198:'ISLOGICAL',199:'DCOUNTA',
200:'DELETE.BAR',201:'UNREGISTER',204:'USDOLLAR',205:'FINDB',206:'SEARCHB',207:'REPLACEB',208:'LEFTB',
209:'RIGHTB',210:'MIDB',211:'LENB',212:'ROUNDUP',213:'ROUNDDOWN',214:'ASC',215:'DBCS',216:'RANK',
219:'ADDRESS',220:'DAYS360',221:'TODAY',222:'VDB',223:'ELSE',224:'ELSE.IF',225:'END.IF',226:'FOR.CELL',
227:'MEDIAN',228:'SUMPRODUCT',229:'SINH',230:'COSH',231:'TANH',232:'ASINH',233:'ACOSH',234:'ATANH',
235:'DGET',236:'CREATE.OBJECT',237:'VOLATILE',238:'LAST.ERROR',239:'CUSTOM.UNDO',240:'CUSTOM.REPEAT',
241:'FORMULA.CONVERT',242:'GET.LINK.INFO',243:'TEXT.BOX',244:'INFO',245:'GROUP',246:'GET.OBJECT',
247:'DB',248:'PAUSE',251:'RESUME',252:'FREQUENCY',253:'ADD.TOOLBAR',254:'DELETE.TOOLBAR',255:'_UDF_',
256:'RESET.TOOLBAR',257:'EVALUATE',258:'GET.TOOLBAR',259:'GET.TOOL',260:'SPELLING.CHECK',
261:'ERROR.TYPE',262:'APP.TITLE',263:'WINDOW.TITLE',264:'SAVE.TOOLBAR',265:'ENABLE.TOOL',
266:'PRESS.TOOL',267:'REGISTER.ID',268:'GET.WORKBOOK',269:'AVEDEV',270:'BETADIST',271:'GAMMALN',
272:'BETAINV',273:'BINOMDIST',274:'CHIDIST',275:'CHIINV',276:'COMBIN',277:'CONFIDENCE',278:'CRITBINOM',
279:'EVEN',280:'EXPONDIST',281:'FDIST',282:'FINV',283:'FISHER',284:'FISHERINV',285:'FLOOR',
286:'GAMMADIST',287:'GAMMAINV',288:'CEILING',289:'HYPGEOMDIST',290:'LOGNORMDIST',291:'LOGINV',
292:'NEGBINOMDIST',293:'NORMDIST',294:'NORMSDIST',295:'NORMINV',296:'NORMSINV',297:'STANDARDIZE',
298:'ODD',299:'PERMUT',300:'POISSON',301:'TDIST',302:'WEIBULL',303:'SUMXMY2',304:'SUMX2MY2',
305:'SUMX2PY2',306:'CHITEST',307:'CORREL',308:'COVAR',309:'FORECAST',310:'FTEST',311:'INTERCEPT',
312:'PEARSON',313:'RSQ',314:'STEYX',315:'SLOPE',316:'TTEST',317:'PROB',318:'DEVSQ',319:'GEOMEAN',
320:'HARMEAN',321:'SUMSQ',322:'KURT',323:'SKEW',324:'ZTEST',325:'LARGE',326:'SMALL',327:'QUARTILE',
328:'PERCENTILE',329:'PERCENTRANK',330:'MODE',331:'TRIMMEAN',332:'TINV',334:'MOVIE.COMMAND',
335:'GET.MOVIE',336:'CONCATENATE',337:'POWER',338:'PIVOT.ADD.DATA',339:'GET.PIVOT.TABLE',
340:'GET.PIVOT.FIELD',341:'GET.PIVOT.ITEM',342:'RADIANS',343:'DEGREES',344:'SUBTOTAL',345:'SUMIF',
346:'COUNTIF',347:'COUNTBLANK',348:'SCENARIO.GET',349:'OPTIONS.LISTS.GET',350:'ISPMT',351:'DATEDIF',
352:'DATESTRING',353:'NUMBERSTRING',354:'ROMAN',355:'OPEN.DIALOG',356:'SAVE.DIALOG',357:'VIEW.GET',
358:'GETPIVOTDATA',359:'HYPERLINK',360:'PHONETIC',361:'AVERAGEA',362:'MAXA',363:'MINA',364:'STDEVPA',
365:'VARPA',366:'STDEVA',367:'VARA',368:'BAHTTEXT',369:'THAIDAYOFWEEK',370:'THAIDIGIT',
371:'THAIMONTHOFYEAR',372:'THAINUMSOUND',373:'THAINUMSTRING',374:'THAISTRINGLENGTH',
375:'ISTHAIDIGIT',376:'ROUNDBAHTDOWN',377:'ROUNDBAHTUP',378:'THAIYEAR',379:'RTD',380:'CUBEVALUE',
381:'CUBEMEMBER',382:'CUBEMEMBERPROPERTY',383:'CUBERANKEDMEMBER',384:'HEX2BIN',385:'HEX2DEC',
386:'HEX2OCT',387:'DEC2BIN',388:'DEC2HEX',389:'DEC2OCT',390:'OCT2BIN',391:'OCT2HEX',392:'OCT2DEC',
393:'BIN2DEC',394:'BIN2OCT',395:'BIN2HEX',396:'IMSUB',397:'IMDIV',398:'IMPOWER',399:'IMABS',
400:'IMSQRT',401:'IMLN',402:'IMLOG2',403:'IMLOG10',404:'IMSIN',405:'IMCOS',406:'IMEXP',
407:'IMARGUMENT',408:'IMCONJUGATE',409:'IMAGINARY',410:'IMREAL',411:'COMPLEX',412:'IMSUM',
413:'IMPRODUCT',414:'SERIESSUM',415:'FACTDOUBLE',416:'SQRTPI',417:'QUOTIENT',418:'DELTA',
419:'GESTEP',420:'ISEVEN',421:'ISODD',422:'MROUND',423:'ERF',424:'ERFC',425:'BESSELJ',426:'BESSELK',
427:'BESSELY',428:'BESSELI',429:'XIRR',430:'XNPV',431:'PRICEMAT',432:'YIELDMAT',433:'INTRATE',
434:'RECEIVED',435:'DISC',436:'PRICEDISC',437:'YIELDDISC',438:'TBILLEQ',439:'TBILLPRICE',
440:'TBILLYIELD',441:'PRICE',442:'YIELD',443:'DOLLARDE',444:'DOLLARFR',445:'NOMINAL',446:'EFFECT',
447:'CUMPRINC',448:'CUMIPMT',449:'EDATE',450:'EOMONTH',451:'YEARFRAC',452:'COUPDAYBS',453:'COUPDAYS',
454:'COUPDAYSNC',455:'COUPNCD',456:'COUPNUM',457:'COUPPCD',458:'DURATION',459:'MDURATION',
460:'ODDLPRICE',461:'ODDLYIELD',462:'ODDFPRICE',463:'ODDFYIELD',464:'RANDBETWEEN',465:'WEEKNUM',
466:'AMORDEGRC',467:'AMORLINC',468:'CONVERT',724:'SHEETJS',469:'ACCRINT',470:'ACCRINTM',
471:'WORKDAY',472:'NETWORKDAYS',473:'GCD',474:'MULTINOMIAL',475:'LCM',476:'FVSCHEDULE',
477:'CUBEKPIMEMBER',478:'CUBESET',479:'CUBESETCOUNT',480:'IFERROR',481:'COUNTIFS',482:'SUMIFS',
483:'AVERAGEIF',484:'AVERAGEIFS'}

ERRS={0x00:'#NULL!',0x07:'#DIV/0!',0x0F:'#VALUE!',0x17:'#REF!',0x1D:'#NAME?',0x24:'#NUM!',0x2A:'#N/A',0x2B:'#GETTING_DATA'}

def colname(c):
    s=''
    c+=1
    while c: c,r=divmod(c-1,26); s=chr(65+r)+s
    return s

def a1(r,c): return '%s%d'%(colname(c),r+1)

class Rec:
    __slots__=('id','data')
    def __init__(self,i,d): self.id=i; self.data=d

def records(buf):
    i=0; n=len(buf)
    while i<n:
        b=buf[i]; i+=1
        if b&0x80:
            b2=buf[i]; i+=1; rid=(b&0x7F)|(b2<<7)
        else: rid=b
        ln=0
        for k in range(4):
            bb=buf[i]; i+=1
            ln |= (bb&0x7F)<<(7*k)
            if not (bb&0x80): break
        yield Rec(rid, buf[i:i+ln]); i+=ln

def rd_wstr(b,o):
    n=struct.unpack_from('<I',b,o)[0]; o+=4
    if n==0xFFFFFFFF: return None,o
    s=b[o:o+2*n].decode('utf-16-le','replace'); return s,o+2*n

def rk(v):
    fx100=v&1; fint=v&2
    if fint: num=float(v>>2 if (v>>2)<0x20000000 else (v>>2)-0x40000000)
    else: num=struct.unpack('<d',struct.pack('<q',(v&0xFFFFFFFC)<<32))[0]
    return num/100.0 if fx100 else num

# ---------------- formula (rgce) ----------------
def _ref(rw,colpkg,rel_base=None,abs_only=False):
    col=colpkg&0x3FFF; fcol=bool(colpkg&0x4000); frow=bool(colpkg&0x8000)
    if rel_base is None:
        return ('' if fcol else '$')+colname(col)+('' if frow else '$')+str(rw+1)
    br,bc=rel_base
    c = bc+col if fcol else col
    r = br+rw if frow else rw
    if c<0: c+=16384
    if c>=16384: c-=16384
    if r<0: r+=1048576
    if r>=1048576: r-=1048576
    return ('' if fcol else '$')+colname(c)+('' if frow else '$')+str(r+1)

class FormulaParser:
    def __init__(self, names=None, xti=None, sheetnames=None):
        self.names=names or []; self.xti=xti or []; self.sheetnames=sheetnames or []
    def sheetref(self,ixti):
        try:
            sup,t1,t2=self.xti[ixti]
        except Exception:
            return "[?%d]"%ixti
        def nm(i):
            if 0<=i<len(self.sheetnames): return self.sheetnames[i]
            return '#REF'
        s = nm(t1) if t1==t2 else nm(t1)+':'+nm(t2)
        if re.search(r"[^A-Za-z0-9_.À-ɏ]",s) or s=='': s="'"+s.replace("'","''")+"'"
        return s
    def nameat(self,i):
        i-=1
        if 0<=i<len(self.names): return self.names[i][0]
        return 'NOME_%d'%(i+1)
    def parse(self, rgce, rgcb=b'', base=None):
        st=[]; o=0; n=len(rgce); cbo=0
        def pop(k):
            nonlocal st
            if k<=0: return []
            if len(st)<k:
                a=['?']*(k-len(st))+st[:]; st=[]; return a
            a=st[-k:]; del st[-k:]; return a
        BIN={0x03:'+',0x04:'-',0x05:'*',0x06:'/',0x07:'^',0x08:'&',0x09:'<',0x0A:'<=',0x0B:'=',
             0x0C:'>=',0x0D:'>',0x0E:'<>',0x0F:' ',0x10:',',0x11:':'}
        while o<n:
            p=rgce[o]; o+=1
            b=p; 
            if p>=0x60: b=p-0x40
            elif p>=0x40: b=p-0x20
            if p in BIN:
                a,bb=pop(2); st.append('%s%s%s'%(a,BIN[p],bb))
            elif p==0x12: a,=pop(1); st.append('+'+a)
            elif p==0x13: a,=pop(1); st.append('-'+a)
            elif p==0x14: a,=pop(1); st.append(a+'%')
            elif p==0x15: a,=pop(1); st.append('('+a+')')
            elif p==0x16: st.append('')
            elif p==0x17:
                cch=struct.unpack_from('<H',rgce,o)[0]; o+=2
                s=rgce[o:o+2*cch].decode('utf-16-le','replace'); o+=2*cch
                st.append('"'+s.replace('"','""')+'"')
            elif p==0x18:  # extended ptg: eptg 0x19 = PtgList (referencia estruturada de tabela)
                eptg=rgce[o]; o+=1
                if eptg==0x19:
                    ixti,flags,lidx,c1,c2=struct.unpack_from('<HHIHH',rgce,o); o+=12
                    st.append('TABELA#%d'%lidx)
                else:
                    o+=12; st.append('#EXT%02X#'%eptg)
            elif p==0x19:
                g=rgce[o]; o+=1
                if g&0x04:
                    cof=struct.unpack_from('<H',rgce,o)[0]; o+=2+ (cof+1)*2
                else:
                    o+=2
                    if g&0x10:
                        a,=pop(1); st.append('SUM(%s)'%a)
            elif p==0x1C:
                e=rgce[o]; o+=1; st.append(ERRS.get(e,'#ERR!'))
            elif p==0x1D:
                v=rgce[o]; o+=1; st.append('TRUE' if v else 'FALSE')
            elif p==0x1E:
                v=struct.unpack_from('<H',rgce,o)[0]; o+=2; st.append(str(v))
            elif p==0x1F:
                v=struct.unpack_from('<d',rgce,o)[0]; o+=8
                st.append(('%r'%v).rstrip('0').rstrip('.') if v!=int(v) else str(int(v)))
            elif b==0x20:  # PtgArray
                o+=14
                arr,cbo=self._array(rgcb,cbo); st.append(arr)
            elif b==0x21:
                ix=struct.unpack_from('<H',rgce,o)[0]; o+=2
                f=FTAB.get(ix&0x7FFF,'FUNC%d'%(ix&0x7FFF))
                arity=_ARITY.get(f,1)
                args=pop(arity); st.append('%s(%s)'%(f,','.join(args)))
            elif b==0x22:
                cp=rgce[o]; ix=struct.unpack_from('<H',rgce,o+1)[0]; o+=3
                cp&=0x7F; ix&=0x7FFF
                args=pop(cp)
                if ix==255:
                    fn=args[0] if args else '?'; args=args[1:]
                    fn=fn.replace('_xlfn.','').replace('_xlws.','')
                    st.append('%s(%s)'%(fn,','.join(args)))
                else:
                    st.append('%s(%s)'%(FTAB.get(ix,'FUNC%d'%ix),','.join(args)))
            elif b==0x23:
                i=struct.unpack_from('<I',rgce,o)[0]; o+=4; st.append(self.nameat(i))
            elif b==0x24:
                rw,cp=struct.unpack_from('<IH',rgce,o); o+=6; st.append(_ref(rw,cp,None))
            elif b==0x25:
                r1,r2,c1,c2=struct.unpack_from('<IIHH',rgce,o); o+=12
                st.append(_ref(r1,c1,None)+':'+_ref(r2,c2,None))
            elif b==0x26 or b==0x27 or b==0x28:
                o+=6
            elif b==0x29:
                o+=2
            elif b==0x2A:
                o+=6; st.append('#REF!')
            elif b==0x2B:
                o+=12; st.append('#REF!')
            elif b==0x2C:
                rw,cp=struct.unpack_from('<IH',rgce,o); o+=6; st.append(_ref(rw,cp,base))
            elif b==0x2D:
                r1,r2,c1,c2=struct.unpack_from('<IIHH',rgce,o); o+=12
                st.append(_ref(r1,c1,base)+':'+_ref(r2,c2,base))
            elif b==0x2E:
                o+=6
            elif b==0x2F:
                o+=6
            elif b==0x39:
                ixti,i=struct.unpack_from('<HI',rgce,o); o+=6
                st.append(self.nameat(i))
            elif b==0x3A:
                ixti,rw,cp=struct.unpack_from('<HIH',rgce,o); o+=8
                st.append(self.sheetref(ixti)+'!'+_ref(rw,cp,None))
            elif b==0x3B:
                ixti,r1,r2,c1,c2=struct.unpack_from('<HIIHH',rgce,o); o+=14
                sr=self.sheetref(ixti)
                st.append(sr+'!'+_ref(r1,c1,None)+':'+_ref(r2,c2,None))
            elif b==0x3C:
                o+=8; st.append('#REF!')
            elif b==0x3D:
                o+=14; st.append('#REF!')
            elif p==0x01:
                rwm=struct.unpack_from('<I',rgce,o)[0]; o+=4
                st.append('@SHARED@%d'%rwm); break
            elif p==0x02:
                o+=4
                st.append('@TABLE@'); break
            else:
                st.append('?PTG%02X'%p); break
        return st[-1] if st else ''
    def _array(self,rgcb,cbo):
        try:
            cols=struct.unpack_from('<I',rgcb,cbo)[0]; rows=struct.unpack_from('<I',rgcb,cbo+4)[0]
            cbo+=8; out=[]
            for i in range(rows*cols):
                t=rgcb[cbo]; cbo+=1
                if t==0: out.append(''); 
                elif t==1: out.append(str(struct.unpack_from('<d',rgcb,cbo)[0])); cbo+=8
                elif t==2:
                    s,cbo=rd_wstr(rgcb,cbo); out.append('"%s"'%s)
                elif t==4: out.append('TRUE' if rgcb[cbo] else 'FALSE'); cbo+=1
                elif t==16: out.append(ERRS.get(rgcb[cbo],'#ERR')); cbo+=1
                else: out.append('?')
            return '{'+';'.join(out)+'}',cbo
        except Exception:
            return '{...}',len(rgcb)

_ARITY={'IFERROR':2,'ABS':1,'INT':1,'LEN':1,'SIGN':1,'SQRT':1,'EXP':1,'LN':1,'LOG10':1,'SIN':1,'COS':1,'TAN':1,
'ATAN':1,'ASIN':1,'ACOS':1,'NOT':1,'ISNA':1,'ISERROR':1,'ISERR':1,'ISTEXT':1,'ISNUMBER':1,'ISBLANK':1,
'ISREF':1,'ISLOGICAL':1,'ISNONTEXT':1,'T':1,'N':1,'TYPE':1,'ROW':1,'COLUMN':1,'ROWS':1,'COLUMNS':1,
'AREAS':1,'TRANSPOSE':1,'PROPER':1,'LOWER':1,'UPPER':1,'TRIM':1,'CLEAN':1,'CHAR':1,'CODE':1,'VALUE':1,
'DAY':1,'MONTH':1,'YEAR':1,'HOUR':1,'MINUTE':1,'SECOND':1,'DATEVALUE':1,'TIMEVALUE':1,'PI':0,'NA':0,
'TRUE':0,'FALSE':0,'RAND':0,'NOW':0,'TODAY':0,'MOD':2,'ROUND':2,'ROUNDUP':2,'ROUNDDOWN':2,'POWER':2,
'ATAN2':2,'MDETERM':1,'MINVERSE':1,'MMULT':2,'DATE':3,'TIME':3,'MID':3,'REPLACE':4,'SUBSTITUTE':3,
'EXACT':2,'FIXED':2,'TEXT':2,'DOLLAR':2,'REPT':2,'SLN':3,'SYD':4,'DDB':4,'RATE':3,'TRUNC':1,
'FACT':1,'DEGREES':1,'RADIANS':1,'ERROR.TYPE':1,'PHONETIC':1,'HYPERLINK':2,'SUMPRODUCT':2,
'SUMXMY2':2,'SUMX2MY2':2,'SUMX2PY2':2,'CEILING':2,'FLOOR':2,'COMBIN':2,'DCOUNT':3,'DSUM':3,
'DAVERAGE':3,'DMIN':3,'DMAX':3,'DGET':3,'DCOUNTA':3,'DPRODUCT':3,'DSTDEV':3,'DVAR':3,
'ISPMT':4,'SUMIF':2,'COUNTIF':2,'COUNTBLANK':1,'GETPIVOTDATA':2,'AVEDEV':1,'DEVSQ':1,'GEOMEAN':1,
'HARMEAN':1,'KURT':1,'SKEW':1,'MEDIAN':1,'MODE':1,'PRODUCT':1,'SUMSQ':1,'CONCATENATE':2,'MMULT':2}

# ---------------- workbook ----------------
class Book:
    def __init__(self, path):
        self.z=zipfile.ZipFile(path)
        self.sst=[]; self.sheets=[]; self.names=[]; self.xti=[]
        self._load_sst(); self._load_wb()
    def _load_sst(self):
        try: buf=self.z.read('xl/sharedStrings.bin')
        except KeyError: return
        for r in records(buf):
            if r.id==19:
                b=r.data; o=1
                s,o=rd_wstr(b,o); self.sst.append(s or '')
    def _load_wb(self):
        buf=self.z.read('xl/workbook.bin')
        rels={}
        import xml.etree.ElementTree as ET
        rx=ET.fromstring(self.z.read('xl/_rels/workbook.bin.rels'))
        for e in rx:
            rels[e.get('Id')]=e.get('Target')
        raw_names=[]
        for r in records(buf):
            if r.id==156:
                b=r.data; o=8
                rid,o=rd_wstr(b,o); nm,o=rd_wstr(b,o)
                tgt=rels.get(rid,'')
                if tgt and not tgt.startswith('/'): tgt='xl/'+tgt.lstrip('./')
                self.sheets.append((nm,tgt))
            elif r.id==39:
                b=r.data
                flags=struct.unpack_from('<I',b,0)[0]
                itab=struct.unpack_from('<I',b,5)[0]
                nm,o=rd_wstr(b,9)
                cce=struct.unpack_from('<I',b,o)[0]; o+=4
                rgce=b[o:o+cce]; o+=cce
                cb=struct.unpack_from('<I',b,o)[0]; o+=4
                rgcb=b[o:o+cb]
                raw_names.append((nm,itab,rgce,rgcb,flags))
            elif r.id==362:
                b=r.data; c=struct.unpack_from('<I',b,0)[0]; o=4
                for i in range(c):
                    sup,t1,t2=struct.unpack_from('<Iii',b,o); o+=12
                    self.xti.append((sup,t1,t2))
        self.names=[(n[0],n[1],None) for n in raw_names]
        fp=FormulaParser(self.names,self.xti,[s[0] for s in self.sheets])
        self.names=[(n[0],n[1],fp.parse(n[2],n[3]),n[4]) for n in raw_names]
        self.fp=FormulaParser(self.names,self.xti,[s[0] for s in self.sheets])
    def sheet(self, name):
        tgt=dict(self.sheets)[name]
        return parse_sheet(self.z.read(tgt), self.sst, self.fp)

def parse_sheet(buf, sst, fp):
    cells={}; row=0; shared={}
    dims=None
    merges=[]
    dv=[]
    for r in records(buf):
        b=r.data
        if r.id==0:
            row=struct.unpack_from('<I',b,0)[0]
        elif r.id in (1,2,3,4,5,6,7,8,9,10,11):
            col=struct.unpack_from('<I',b,0)[0]; o=8
            v=None; f=None
            if r.id==1: v=None
            elif r.id==2: v=rk(struct.unpack_from('<I',b,o)[0]); o+=4
            elif r.id==3: v=ERRS.get(b[o],'#ERR'); o+=1
            elif r.id==4: v=bool(b[o]); o+=1
            elif r.id==5: v=struct.unpack_from('<d',b,o)[0]; o+=8
            elif r.id==6:
                v,o=rd_wstr(b,o)
            elif r.id==7:
                i=struct.unpack_from('<I',b,o)[0]; o+=4
                v=sst[i] if i<len(sst) else ''
            elif r.id==8:
                v,o=rd_wstr(b,o); o+=2
            elif r.id==9:
                v=struct.unpack_from('<d',b,o)[0]; o+=10
            elif r.id==10:
                v=bool(b[o]); o+=3
            elif r.id==11:
                v=ERRS.get(b[o],'#ERR'); o+=3
            if r.id in (8,9,10,11):
                cce=struct.unpack_from('<I',b,o)[0]; o+=4
                rgce=b[o:o+cce]; o+=cce
                cb=struct.unpack_from('<I',b,o)[0]; o+=4
                rgcb=b[o:o+cb]
                f=fp.parse(rgce,rgcb,(row,col))
            cells[(row,col)]=(v,f)
        elif r.id==426:
            r1,r2,c1,c2=struct.unpack_from('<IIII',b,0)
            cce=struct.unpack_from('<I',b,17)[0]
            rgce=b[21:21+cce]; o2=21+cce
            cb=struct.unpack_from('<I',b,o2)[0]
            shared[(r1,r2,c1,c2)]=(rgce,b[o2+4:o2+4+cb])
        elif r.id==427:
            r1,r2,c1,c2=struct.unpack_from('<IIII',b,0)
            cce=struct.unpack_from('<I',b,16)[0]
            rgce=b[20:20+cce]; o2=20+cce
            cb=struct.unpack_from('<I',b,o2)[0]
            shared[(r1,r2,c1,c2)]=(rgce,b[o2+4:o2+4+cb])
        elif r.id==176:
            r1,r2,c1,c2=struct.unpack_from('<IIHH',b,0) if len(b)>=12 else (0,0,0,0)
            try:
                r1,r2,c1,c2=struct.unpack_from('<IIII',b,0)
            except Exception: pass
            merges.append((r1,r2,c1,c2))
    for (rr,cc),(v,f) in list(cells.items()):
        if f and f.startswith('@SHARED@'):
            for (r1,r2,c1,c2),(rgce,rgcb) in shared.items():
                if r1<=rr<=r2 and c1<=cc<=c2:
                    cells[(rr,cc)]=(v, fp.parse(rgce,rgcb,(rr,cc))); break
    return cells, merges

def shared_resolve(cells, fp):
    """Resolve @SHARED@ placeholders re-parsing from master cell."""
    return cells
