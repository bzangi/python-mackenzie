from test.test_tools.test_unparse import elif1
x=2
y=4
z=9
k=3
resultado=0
if x<y+k and k*2>4 and z+k<12:
    resultado=1
elif y+10<z or z>12:
    resultado=2
elif x+2>=y-4:
    resultado=4
print(resultado)