class multiplefunction():
    def Subfields():
        fields = ["Machine Learning","Neural Networks","Vision","Robotics","Speech Processing","Natural Language Processing"]
        print("Sub-fields in AI are: ")
        for SubfieldsInAI in fields:
            print(SubfieldsInAI)
            message = SubfieldsInAI
        return Subfields
    def oddeven():
        num = int(input("Enter a number: "))
        if ((num % 2 == 0)):
            print(num," is Even number ")
            message = num," is Even number "
        else:
            print(num," is Odd number ")
            message = num," is Odd number "
        return message
    def marriage():
        gender=input("Enter Your Gender: ")
        age =int(input(" Your Age: "))
        if((age>21) and (gender =="male")):
            print("ELIGIBLE")
            mrg="ELIGIBLE"
        elif((age>18) and (gender=="female")):
            print("ELIGIBLE")
            mrg="ELIGIBLE"
        else:
            print("NOT ELIGIBLE") 
            mrg="NOT ELIGIBLE"
        return mrg
    def percentage():
        subject1= float(input("Subject1= ")),
        subject2= float(input("Subject2= ")) ,           
        subject3= float(input("Subject3= ")),
        subject4= float(input("Subject4= ")),
        subject5= float(input("Subject5= ")),
        total = sum(subject1+subject2+subject3+subject4+subject5)
        percentage= float(total / 5)
        print("Total = ", total)
        print("Percentage : ",percentage)
        return percentage
    def triangle():
        height=float(input("Height: "))
        breadth=float(input("Breadth: "))
        area= float((height*breadth)/2)
        print("Area of Triangle:  ", area)
        height1=float(input("Height 1: ")),
        height2=float(input("Height 2: ")),
        breadth1=float(input("Breadth 1: ")),
        perimeter = sum(height1+height2+breadth1) 
        print("Perimeter formula: Height1+Height2+Breadth1")
        print("Perimeter of Triangle:  ",perimeter)
        print("Area of Triangle:  ", area)
        return triangle