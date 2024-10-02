mtocm={}
cmtom={}

try:
    n=int(input("Enter number of conversion : "))
    for i in range(n):
        vm=float(input("Enter measurement in meter : "))
        vcm=vm*100
        mtocm[vm]=vcm
        cmtom[vcm]=vm
    
    print("Meters to Centimeters Dictionary:",mtocm)
    print("\nCentimeters to Meters Dictionary:",cmtom)
except:
    print("Some error occured")