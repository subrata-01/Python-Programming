import cmath
x=int(input("enter a real number : "))
y=int(input("enter a real number : "))
z=complex(x,y)
print("the complex number is : ",z)
if z.real>z.imag:
    print("real part is greater of this complx number ")
else:
    print("imaginary part is greater of this complex numebr ")
