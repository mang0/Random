from turtle import*
def f(l,d):
 if d<2:
  fd(l);return
 for x in[60,240,60]:
  f(l/3,d-1);lt(x)
 f(l/3,d-1)
for i in"   ":
 f(100,3);lt(240)
input()