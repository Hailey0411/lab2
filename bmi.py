def calculate_bmi(height,weight):
    print("Height="+str(height))
    print("Weight="+str(weight))

    bmi = (weight)/(height*height)
    print("The BMI value is: ",bmi)
    
    if bmi < 18.5:
        
        print("Under Weight")
        return -1
        
      

    elif bmi >=18.5 and bmi <=25.0:
        
        print("Normal Weight")
        return 0
        
    else:
        
        print("Over Weight")
        return 1
    

calculate_bmi(weight=87, height=1.73)