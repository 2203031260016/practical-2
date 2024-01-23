l=int(input("enter length : "))
w=int(input("enter width : "))
fh=open("output2.txt",'w')
area=l*w
perimeter=2*(l+w)
fh.write("area of rectangle is: "+str(area))
fh.write ("perimeter of rectangle is:"+str(perimeter))
