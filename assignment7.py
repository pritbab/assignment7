#Question 1: Create user defined dictionary and print keys and value
dict=eval(input("Enter the keys with corresponding values: "))
for key in dict:
    print("{}:{}".format(key,dict[key]))



#Question 2: nested dictionary
records={'Jill':{'Maths':100,'Physical':95,'English':95},'Jack':\
         {'Maths':96,'Physical':95,'English':98},'Nick':\
         {'Maths':92,'Physical':90,'English':94}}
name=input("Enter the name: ")
for key in records:
    if name==key:
        print(key,records[key])
