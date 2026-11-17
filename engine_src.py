import sys,random,json,os,urllib.request,urllib.error
V=[0,100,320,330,500,900,20000]
NS=(-33,-31,-18,-14,14,18,31,33)
KS=(-17,-16,-15,-1,1,15,16,17)
BS=(-17,-15,15,17)
RS=(-16,-1,1,16)
P='KKKKKKKKUUUUUUUUMMOQQOMMLLMPPMLLKKKOOKKKLJIKKIJLLMMGGMMLKKKKKKKKACEEEECACGKKKKGCEKMNNMKEELNOONLEEKNOONKEELMNNMLECGKLLKGCACEEEECAGIIIIIIGIKKKKKKIIKLMMLKIILLMMLLIIKMMMMKIIMMMMMMIILKKKKLIGIIIIIIGKKKKKKKKLMMMMMMLJKKKKKKJJKKKKKKJJKKKKKKJJKKKKKKJJKKKKKKJKKKLLKKKGIIJJIIGIKKKKKKIIKLLLLKIJKLLLLKJKKLLLLKJILLLLLKIIKLKKKKIGIIJJIIGECCAACCEECCAACCEECCAACCEECCAACCEGEECCEEGIGGGGGGIOOKKKKOOOQMKKMQO'
R=random.Random(0)
Z=[R.getrandbits(64) for _ in range(12*128+1+16+8)]
def zk(t,s,q): return Z[((t-1)+(0 if s>0 else 6))*128+q]
M=100000
class A(Exception): pass
class B:
 def __init__(s):
  s.b=[0]*128;s.d=1;s.c=0;s.e=-1;s.h=0;s.k={1:4,-1:116};s.n=[];s.z=0
 def f(s,F):
  p=F.split();s.b=[0]*128
  for r,w in enumerate(p[0].split('/')):
   k=7-r;f=0
   for c in w:
    if c.isdigit(): f+=int(c)
    else:
     t='pnbrqk'.index(c.lower())+1
     s.b[k*16+f]=t if c.isupper() else -t
     if t==6: s.k[1 if c.isupper() else -1]=k*16+f
     f+=1
  s.d=1 if p[1]=='w' else -1;s.c=0
  if len(p)>2:
   for c in p[2]:
    if c=='K': s.c|=1
    elif c=='Q': s.c|=2
    elif c=='k': s.c|=4
    elif c=='q': s.c|=8
  s.e=-1
  if len(p)>3 and p[3]!='-': s.e='abcdefgh'.index(p[3][0])+(int(p[3][1])-1)*16
  s.h=int(p[4]) if len(p)>4 else 0;s.n=[]
  h=0
  for q in range(128):
   if q&0x88: continue
   v=s.b[q]
   if v: h^=zk(abs(v),v,q)
  if s.d==-1: h^=Z[12*128]
  h^=Z[12*128+1+s.c]
  if s.e>=0: h^=Z[12*128+17+(s.e&7)]
  s.z=h
 def a(s,q,d):
  b=s.b
  if d==1:
   for o in (-15,-17):
    t=q+o
    if not(t&0x88) and b[t]==1: return 1
  else:
   for o in (15,17):
    t=q+o
    if not(t&0x88) and b[t]==-1: return 1
  for o in NS:
   t=q+o
   if not(t&0x88) and b[t]==2*d: return 1
  for o in KS:
   t=q+o
   if not(t&0x88) and b[t]==6*d: return 1
  for o in BS:
   t=q+o
   while not(t&0x88):
    v=b[t]
    if v:
     if v==3*d or v==5*d: return 1
     break
    t+=o
  for o in RS:
   t=q+o
   while not(t&0x88):
    v=b[t]
    if v:
     if v==4*d or v==5*d: return 1
     break
    t+=o
  return 0
 def g(s):
  b=s.b;d=s.d;m=[]
  for q in range(128):
   if q&0x88: continue
   v=b[q]
   if v==0 or (v>0)!=(d>0): continue
   t=abs(v)
   if t==1: s._p(q,d,m)
   elif t==2:
    for o in NS:
     x=q+o
     if x&0x88: continue
     w=b[x]
     if w==0: m.append(q|(x<<7))
     elif (w>0)!=(d>0): m.append(q|(x<<7)|(1<<17))
   elif t==6:
    for o in KS:
     x=q+o
     if x&0x88: continue
     w=b[x]
     if w==0: m.append(q|(x<<7))
     elif (w>0)!=(d>0): m.append(q|(x<<7)|(1<<17))
    if d==1 and q==4:
     if s.c&1 and b[5]==0 and b[6]==0 and b[7]==4 and not s.a(4,-1) and not s.a(5,-1) and not s.a(6,-1): m.append(4|(6<<7)|(8<<17))
     if s.c&2 and b[3]==0 and b[2]==0 and b[1]==0 and b[0]==4 and not s.a(4,-1) and not s.a(3,-1) and not s.a(2,-1): m.append(4|(2<<7)|(8<<17))
    elif d==-1 and q==116:
     if s.c&4 and b[117]==0 and b[118]==0 and b[119]==-4 and not s.a(116,1) and not s.a(117,1) and not s.a(118,1): m.append(116|(118<<7)|(8<<17))
     if s.c&8 and b[115]==0 and b[114]==0 and b[113]==0 and b[112]==-4 and not s.a(116,1) and not s.a(115,1) and not s.a(114,1): m.append(116|(114<<7)|(8<<17))
   else:
    S=BS if t==3 else RS if t==4 else BS+RS
    for o in S:
     x=q+o
     while not(x&0x88):
      w=b[x]
      if w==0: m.append(q|(x<<7))
      else:
       if (w>0)!=(d>0): m.append(q|(x<<7)|(1<<17))
       break
      x+=o
  return m
 def _p(s,q,d,m):
  b=s.b
  if d==1: f, st, pr, cd=(16,1,7,(15,17))
  else: f, st, pr, cd=(-16,6,0,(-15,-17))
  r=q>>4;t=q+f
  if not(t&0x88) and b[t]==0:
   if (t>>4)==pr:
    for v in (5,4,3,2): m.append(q|(t<<7)|(v<<14))
   else:
    m.append(q|(t<<7))
    if r==st:
     t2=q+2*f
     if b[t2]==0: m.append(q|(t2<<7)|(2<<17))
  for o in cd:
   t=q+o
   if t&0x88: continue
   w=b[t]
   if w!=0 and (w>0)!=(d>0):
    if (t>>4)==pr:
     for v in (5,4,3,2): m.append(q|(t<<7)|(v<<14)|(1<<17))
    else: m.append(q|(t<<7)|(1<<17))
   elif t==s.e: m.append(q|(t<<7)|(1<<17)|(4<<17))
 def mk(s,m):
  b=s.b;f=m&127;t=(m>>7)&127;v=(m>>14)&7;l=(m>>17)&15;d=s.d;p=b[f];c=0;w=t
  if l&4:
   w=t-16*d;c=b[w];b[w]=0
  else: c=b[t]
  s.n.append((m,c,w,s.c,s.e,s.h,s.z))
  h=s.z;h^=zk(abs(p),d,f)
  if c: h^=zk(abs(c),-d,w)
  h^=zk(v if v else abs(p),d,t)
  if l&8:
   if t==6: b[7]=0;b[5]=4;h^=zk(4,1,7)^zk(4,1,5)
   elif t==2: b[0]=0;b[3]=4;h^=zk(4,1,0)^zk(4,1,3)
   elif t==118: b[119]=0;b[117]=-4;h^=zk(4,-1,119)^zk(4,-1,117)
   elif t==114: b[112]=0;b[115]=-4;h^=zk(4,-1,112)^zk(4,-1,115)
  b[f]=0;b[t]=v*d if v else p
  if abs(p)==6: s.k[d]=t
  h^=Z[12*128+1+s.c]
  if s.e>=0: h^=Z[12*128+17+(s.e&7)]
  if f==4 or t==4: s.c&=~3
  if f==116 or t==116: s.c&=~12
  if f==0 or t==0: s.c&=~2
  if f==7 or t==7: s.c&=~1
  if f==112 or t==112: s.c&=~8
  if f==119 or t==119: s.c&=~4
  if l&2:
   e=-d;s.e=f+16*d if ((not((t-1)&0x88) and b[t-1]==e) or (not((t+1)&0x88) and b[t+1]==e)) else -1
  else: s.e=-1
  h^=Z[12*128+1+s.c]
  if s.e>=0: h^=Z[12*128+17+(s.e&7)]
  h^=Z[12*128];s.z=h
  s.h=0 if (abs(p)==1 or c) else s.h+1
  s.d=-d
 def un(s):
  m,c,w,ca,ep,ha,hh=s.n.pop()
  b=s.b;f=m&127;t=(m>>7)&127;v=(m>>14)&7;l=(m>>17)&15;d=-s.d;p=b[t]
  b[t]=0
  if l&4: b[w]=-d
  elif c: b[t]=c
  b[f]=d if v else p
  if l&8:
   if t==6: b[5]=0;b[7]=4
   elif t==2: b[3]=0;b[0]=4
   elif t==118: b[117]=0;b[119]=-4
   elif t==114: b[115]=0;b[112]=-4
  if abs(p)==6: s.k[d]=f
  s.c,s.e,s.h,s.z=ca,ep,ha,hh;s.d=d
 def lm(s):
  o=[]
  for m in s.g():
   s.mk(m)
   if not s.a(s.k[-s.d],s.d): o.append(m)
   s.un()
  return o
 def ck(s): return s.a(s.k[s.d],-s.d)
 def ev(s):
  b=s.b;r=0;n=0
  for q in range(128):
   if q&0x88: continue
   p=b[q]
   if p==0: continue
   t=abs(p);v=V[t];k,ff=q>>4,q&7
   if p>0:
    r+=v+(ord(P[(t-1)*64+(7-k)*8+ff])-75)*5
    if t==3: n+=1
   else:
    r-=v+(ord(P[(t-1)*64+k*8+ff])-75)*5
    if t==3: n-=1
  if n==2: r+=30
  elif n==-2: r-=30
  return r if s.d==1 else -r
class S:
 def __init__(s,bg=30000):
  s.bg=bg;s.nd=0;s.tt={};s.kl=[[0,0] for _ in range(128)];s.pa=[];s.hi=[0]*1536
 def os(s,b,m,tm):
  if m==tm: return 1000000
  t=(m>>7)&127;l=(m>>17)&15;f=m&127
  if l&1:
   v=b.b[t]
   if l&4: v=-b.d
   return 900000+10*V[abs(v)]-V[abs(b.b[f])]//16
  if m==s.kl[len(s.pa)][0] or m==s.kl[len(s.pa)][1]: return 800000
  p=b.b[f];return s.hi[(abs(p)-1+(0 if p>0 else 6))*128+t]
 def q(s,b,al,be,pl):
  s.nd+=1
  if s.nd>s.bg: raise A
  if b.h>=100: return 0
  st=b.ev()
  if st>=be: return be
  if st>al: al=st
  if b.ck(): mv=b.lm()
  else:
   mv=[]
   for m in b.g():
    if ((m>>17)&1) or ((m>>14)&7): mv.append(m)
  sc=[]
  for m in mv:
   t=(m>>7)&127;l=(m>>17)&15;f=m&127;v=b.b[t]
   if l&4: v=-b.d
   sc.append((-(10*V[abs(v)]-V[abs(b.b[f])]//16 if v else 0),m))
  sc.sort()
  for _,m in sc:
   b.mk(m)
   if b.a(b.k[-b.d],b.d): b.un();continue
   x=-s.q(b,-be,-al,pl+1);b.un()
   if x>=be: return be
   if x>al: al=x
  return al
 def sr(s,b,dp,al,be,pl):
  s.nd+=1
  if s.nd>s.bg: raise A
  if b.h>=100: return 0
  if b.z in s.pa: return 0
  if dp<=0: return s.q(b,al,be,pl)
  tm=0;e=s.tt.get(b.z)
  if e is not None:
   d2,s2,f2,m2=e
   if d2>=dp:
    if f2==0: return s2
    elif f2==1 and s2>=be: return s2
    elif f2==2 and s2<=al: return s2
   tm=m2
  s.pa.append(b.z)
  mv=b.g()
  sc=[]
  for m in mv: sc.append((-s.os(b,m,tm),m))
  sc.sort()
  be2=-M;bm=0;fl=2;lg=0;a=al
  for _,m in sc:
   b.mk(m)
   if b.a(b.k[-b.d],b.d): b.un();continue
   lg+=1
   x=-s.sr(b,dp-1,-be,-a,pl+1);b.un()
   if x>be2: be2=x;bm=m
   if x>a:
    a=x;fl=0
    if a>=be:
     fl=1;k=s.kl[pl]
     if m!=k[0]: k[1]=k[0];k[0]=m
     f=m&127;t=(m>>7)&127;p=b.b[f];s.hi[(abs(p)-1+(0 if p>0 else 6))*128+t]+=dp*dp
     break
  s.pa.pop()
  if lg==0: return -M+pl if b.ck() else 0
  if len(s.tt)<500000: s.tt[b.z]=(dp,be2,fl,bm)
  return be2
 def rt(s,b,md=64):
  lg=b.lm()
  if not lg: return None,(-M if b.ck() else 0)
  if len(lg)==1: return lg[0],0
  bs=lg[0];s.nd=0;s.tt={};s.kl=[[0,0] for _ in range(128)];s.pa=[]
  for dp in range(1,md+1):
   try:
    sc=[]
    for m in lg: sc.append((-s.os(b,m,0),m))
    sc.sort()
    a=-M;cb=bs
    for _,m in sc:
     b.mk(m);x=-s.sr(b,dp-1,-M,-a,1);b.un()
     if x>a: a=x;cb=m
    bs=cb
   except A:
    while b.n: b.un()
    break
  return bs,a
def _po(p,bo):
 q=urllib.request.Request(ENV_URL+p,data=json.dumps(bo).encode(),headers={"content-type":"application/json"})
 try:
  with urllib.request.urlopen(q) as r: return json.load(r)
 except urllib.error.HTTPError as e: sys.exit(f"{p}: HTTP {e.code} {e.read().decode(errors='replace')}")
def _uc(m):
 f=m&127;t=(m>>7)&127;v=(m>>14)&7
 w=lambda q:'abcdefgh'[q&7]+str((q>>4)+1)
 u=w(f)+w(t)
 if v: u+=['','','n','b','r','q'][v]
 return u
ENV_URL=os.environ.get("MAKEFUN_ENV_URL","")
BUDGET=int(os.environ.get("MAKEFUN_NODES","150000"))
def _run():
 if not ENV_URL: sys.exit("MAKEFUN_ENV_URL is not set")
 sr=S(BUDGET)
 while 1:
  g=_po("/game",{})
  if g["status"]=="done": break
  while g["status"]=="your_move":
   bd=B();bd.f(g["fen"]);m,_=sr.rt(bd)
   if m is None: break
   g=_po("/move",{"game":g["game"],"move":_uc(m)})
  print(f"game {g['game']}: {g['outcome']} by {g['reason']}",file=sys.stderr)
 print(f"done: {g.get('wins')} won, {g.get('draws')} drawn, {g.get('losses')} lost",file=sys.stderr)
if __name__=='__main__': _run()
