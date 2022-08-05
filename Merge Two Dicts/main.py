#How to merge two dicts
X={"a":1,"b":2,"c":3}
y={"b":3,"c":4,"d":5}
z={**x,**y}
print(z)