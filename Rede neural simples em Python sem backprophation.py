import math
print("digite os inputs dos neurônios:")
n=float(input())
y=float (input ())#camada de entrada

p1=2
p2=3 #camadas oculta
S=n*p1+n*p2+y*p1+y*p2
n1=1/(1+math.exp (-S))#saida
print(n1)
  

  
  
  
  
