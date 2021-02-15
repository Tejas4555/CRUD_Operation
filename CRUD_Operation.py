clist=[]
class course:
    def __init__(self,course_id,course_name,course_fees,course_duration):
        self.course_id=course_id
        self.course_name=course_name
        self.course_fees=course_fees
        self.course_duration=course_duration

    def __str__(self):  
        return f"course_id:{self.course_id},course_name:{self.course_name},course_fees:{self.course_fees},course_duration:{self.course_duration}"

blist=[]
class batch:
    def __init__(self,batch_id,batch_name,batch_time,course_id):
        self.batch_id=batch_id
        self.batch_name=batch_name
        self.batch_time=batch_time
        self.course_id=course_id
    def __str__(self):
        return f"batch_id:{self.batch_id},batch_name:{self.batch_name},batch_time:{self.batch_time},course_id:{self.course_id}"

slist=[] 
class student:
    def __init__(self,student_rollno,student_name,student_add,student_email,batch_id):
        self.student_rollno=student_rollno
        self.student_tuname=student_name
        self.student_add=student_add
        self.student_email=student_email
        self.batch_id=batch_id
    def __str__(self):
        return f"student_rollno:{self.student_rollno},student_name:{self.student_name},student_add:{self.student_add},student_email:{self.student_email},batch_id:{self.batch_id}"
        


while True:
    try:
        ch=int(input("-----*plz select your choice*-----\n"
              "1.Enter a cours information\n"
              "2.Enter a batch information\n"
              "3.Enter a student information\n"
              "4.Exit\n----------------------------------\nChoice="))
        if ch==1:
            print("\t*Enter a cours*\n----------------------------------")
            while True:
                    ch=int(input('1.Add course \n2.Update course\n3.Delet course\n4.Show course Details\n5.Back>\n----------------------------------\nChoice='))
                    if ch==1:
                        x=int(input("How many course added you\nChoice="))
                        
                        for i in range(x):
                                print('\t*Adding course*')
                                print("----------------------------------")
                                course_id=int(input("Cours ID:"))
                                course_name=input("Cours Name:")
                                course_fees=input("Cours Fees:")
                                course_duration=input("Cours Duration:")
                                c=course(course_id,course_name,course_fees,course_duration)
                                clist.append(c)
                                print("course added\n----------------------------------")
                    elif ch==2:
                            cs1=int(input("what you want to update\n1.update name\n2.update fees\n3.update duration"))
                            if cs1==1:
                                f=int(input("Enter course_id whitch want to name update"))
                                for i in clist:
                                    if f==i.course_id:
                                       s=input("Enter new name of course")
                                       i.course_name=s
                                        
                                    else:
                                       print("course_id invalid")
                                    for i in clist:
                                        print(i)
                            elif cs1==2:
                                f=int(input("Enter course_id whitch want to fees update"))
                                for i in clist:
                                    if f==i.course_id:
                                        y=int(input("Enter your fees"))
                                        i.course_fees=y
                                    else:
                                        print("course_id invalid")
                                    for i in clist:
                                        print(i)
                            elif cs1==3:
                                f=int(input("Enter course_id whitch want to Duration update"))
                                for i in clist:
                                    if f==i.course_id:
                                        z=int(input("Enter your fees"))
                                        i.course_duration=z
                                    else:
                                        print("course_duration invalid")
                                    for i in clist:
                                        print(i)
                            else:
                                print("plz Enter choice 1 to 3")
                            
                    elif ch==3:
                            d=int(input("Enter course_id you want to delet"))
                            for i in clist:
                                clist.remove(i)
                            if d==i.course_id:
                                print("course deleted succesfuly",d)
                            else:
                                print("invalide choice your")
                    elif ch==4:
                    #show
                        for i in clist:
                                print(i)
                    elif ch==5:
                        break
                    else:
                        print("Invalid choice,plz choose betn 1-5")

        elif ch==2:
            if len (clist)==0:
                print("No course added it")
                
            else:
                ch=int(input('\n1.Add Batch \n2.Update Batch\n3.Delet Batch\n4.Show Batch Details\n5.Exit\n\t'))
                if ch==1:
                            print('Adding Batch:')
                            batch_id=int(input("Batch ID:"))
                            batch_name=input("Batch Name:")
                            batch_time=input("Batch Time:")
                            course_id=int(input("Enter your course_id"))
                            for course in clist:
                                if course.course_id==course_id:
                                    b=batch(batch_id,batch_name,batch_time,course_id)
                                    blist.append(b)
                                    print("batch added")
                                else:
                                    print("invalide course id")
                elif ch==2:
                            cs1=int(input("what you want to update\n1.update batch_name\n2.update batch_time\n"))
                            if cs1==1:
                                f=int(input("Enter course_id whitch want to batch name update"))
                                for i in clist:
                                    if f==i.batch_id:
                                        s=input("Enter your batch_name")
                                        i.batch_name=s
                                    else:
                                        print("batch_id invalid")
                                    for i in clist:
                                        print(i)
                            elif cs1==2:
                                f=int(input("Enter batch_id whitch want to fees update"))
                                for i in clist:
                                    if f==i.course_id:
                                        y=int(input("Enter your fees"))
                                        i.course_fees=y
                                    else:
                                        print("course_id invalid")
                                    for i in clist:
                                        print(i)
                                else:
                                    print("plz Enter choice 1 to 3")

                elif ch==3:
                            d=int(input("Enter batch_id you want to delet"))
                            for i in blist:
                                blist.remove(i)
                            if d==i.batch_id:
                                print("course deleted succesfuly",d)
                            else:
                                print("invalide choice your")
                elif ch==4:
                            #show
                            for i in blist:
                                print(i)
                elif ch==5:
                            break
                else:
                            print("Invalid choice,plz choose betn 1-5")

        
        elif ch==3:
            print("3.Enter a student ")
            if len (blist)==0:
                print("No course added it")
            else:
                ch=int(input('\n1.Add Student\n2.Update Student\n3.Delet Student\n4.Show Student Details\n5.Exit\n\t'))
                if ch==1:
                            print('Adding Student:')
                            student_rollno=int(input("Roll Number:"))
                            student_name=input("Name:")
                            student_add=input("Addres:")
                            student_email=input("Email:")
                            batch_id=int(input("batch_id"))
                            for course in clist:
                                if student.student_rollno==student_rollno:
                                    s=student(student_rollno,student_name,student_add,student_email,batch_id)
                                    slist=append(batch_id)
                                    slist.append(s)
                                    print("Student added")
                                else:
                                    print("invalide course id")
                            
                elif ch==2:
                            cs1=int(input("what you want to update student\n1.update student_name\n2.update student_add\n3.student_email"))
                            if cs1==1:
                                f=int(input("Enter student_rollno whitch want to student name update"))
                                for i in clist:
                                    if f==i.student_rollno:
                                        s=input("Enter your student_name")
                                        i.student_name=s
                                    else:
                                        print("student_rollno invalid")
                                    for i in clist:
                                        print(i)
                            elif cs1==2:
                                f=int(input("Enter student_rollno whitch want to Addres update"))
                                for i in clist:
                                    if f==i.student_rollno:
                                        y=int(input("Enter your new Addres"))
                                        i.course_add=y
                                    else:
                                        print("student_rollno invalid")
                                    for i in clist:
                                        print(i)
                            elif cs1==3:
                                f=int(input("Enter student_rollno whitch want to Email update"))
                                for i in clist:
                                    if f==i.student_rollno:
                                        z=int(input("Enter your fees"))
                                        i.student_email=z
                                    else:
                                        print("student_email invalid")
                                    for i in clist:
                                        print(i)
                            else:
                                print("plz Enter choice 1 to 3")

                elif ch==3:
                    d=int(input("Enter student_rollno you want to delet"))
                    for i in clist:
                                slist.remove(i)
                    if d==i.student_rollno:
                                print("course deleted succesfuly",d)
                    else:
                                print("invalide choice your")
        elif ch==4:
                for i in slist:
                    print(i)
        elif ch==5:
                break
        else:
                print("Invalid choice,plz choose betn 1-5")

    except BaseException:
        print("\nValue Error......!\n\n")
        continue
        

