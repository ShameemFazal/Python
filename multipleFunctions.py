class multipleFunctions:
    def Subfields():
        lists = ["Machine Learning","Neural Networks","Vision","Robotics","Speech Processing","Natural Language Processing"]
        print("Sub-fields in AI sgsdfsdfsfd:")
        for temp in lists:
            print(temp)
    
    def OddEven():
        number = int(input("Enter a number:"))
       
        if(number%2 ==0):
            print(number," is Even number")
        else:
            print(number," is Odd number") 

    def Elegible():
        gender = input("Your Gender : ") 
        age = int(input("Your Age : "))
        
        if(gender =="Male" and age >= 21):
            print("ELIGIBLE")
        elif (gender =="Female" and age >= 18):
            print("ELIGIBLE")
        else:
            print("NOT ELIGIBLE")

    def percentage():
        subject1 = int(input("subject1 ="))
        subject2 = int(input("subject2 ="))
        subject3 = int(input("subject3 ="))
        subject4 = int(input("subject4 ="))
        subject5 = int(input("subject5 ="))

        total = subject1+subject2+subject3+subject4+subject5
        print("Total :",total)
        print("Percentage :",total/5)


    def triangle():
        Height = int(input("Height :"))
        Breadth = int(input("Breadth :"))
        print("Area formula : (Height*Breadth)/2")
        print("Area of Triangle:", (Height*Breadth)/2)
        Height1 = int(input("Height1 :"))
        Height2 = int(input("Height2 :"))
        Breadth1 = int(input("Breadth :"))
        print("Perimeter formula : Height1+Height2+Breadth")
        print("Perimater of Triangle:", Height1+Height2+Breadth1)
