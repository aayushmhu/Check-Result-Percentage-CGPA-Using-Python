# check Student Percentage Division 
sub = input("Enter How many Subject you have? : ")
sub = int(sub)

if sub != 0:
    total = 0
    for i in range(1,sub+1):
        sub1 = input(f"Enter marks of Subject {i} : ")
        if int(sub1) > 100:
            break
        else:
            total = total + int(sub1)
            i += 1
else:
    print("Please Enter Vaild Subject")
    
if int(sub1) < 100:
    if sub != 0:
        per = total/sub
        print(f"Total Marks is : {total}")
        print(f"Percentage is : {float(per)}%")
        cgpa = per / 9.5
        print(f"CGPA is : {round(cgpa, 2)}")
        if 100 >= per >=80:
            print("Congratulations!!! Your Division is First!!!")
        elif 80 >= per >=60:
            print("Hurray!!!! Your Division is Second!!")
        elif 60 >= per >=40:
            print("Your Division is Third!!")
        else:
            print("Sorry!!! You are Fail")
    else:
        pass
else:
    print("Please Enter Right Values")


    
    

