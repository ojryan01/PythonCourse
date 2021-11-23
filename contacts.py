contacts = {
    'Number' : 4,
    'Students':
    [
        {"Name" : "Olivia Ryan", "email" : "ojryan01@gmail.com"} , 
        {"Name" : "Pete Rosene", "email" : "pjrosene@gmail.com"}
    ]
}

for student in contacts["Students"]:    
    print(student["email"])