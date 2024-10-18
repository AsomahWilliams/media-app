#class Travel:
   #def __init__(self,country,month,type):
    #  self.country = country
     # self.month = int(month)
      #self.type = type
      #self.price = 0 



    #def trip_info(self):
    #    if self.month >= 10 and self.month <= 3:
    #        print(f"You are going to {self.country} in the Winter! This is a {self.type} trip!")
     #   elif self.month >3 and self.month < 10:
     #       print(f"You are going to {self.country} in the Summer! This is a {self.type} trip!")
     #   else:
     #       print("Invalid Input")    
                




   #def calc_cost(self, cost):
      #costs = []
      #while cost != 0:
        # self.price += cost
         #costs.append(cost) 
         #cost = int(input("Enter another cost: ")) 




      #advice = self.advice(self.price)
      #inspect = self.list_inspect(costs)
      #return advice, inspect  




   #def advice(self, num):
        #if num < 500:
        # print("low budget!")
        #elif num >= 500 and num < 1500:
        # print("Take a flight to anywhere.....")
        #else:
        #  print("Luxury Trip") 



   #def list_inspect(self, costs):
        #less_than_ten = 0
        #for i in costs: 
         #if i >= 10:          
         #  less_than_ten += 1 

       # if less_than_ten <= 10:
        # self.price += 100
        #print(f"Updated price: {self.price}")



#location = input("Enter a country: ").capitalize()
#trip_type = input("Leisure or Business: ").capitalize()
#month = input("Enter a month: ") 


#test = Travel(location, month, trip_type)
#test.trip_info()


#flight_cost = int (input("Enter flight cost: "))
#test.calc_cost(flight_cost) 
                
           
         

        
      
   

class Guest:
   def __init__(self,first, last,rank, age):
      self.first_name = first
      self.last_name = last 
      self.rank = int(rank)
      self.age = int(age)  



   def guest_info(self,all_guests):
      for guest in all_guests:
         print(guest.first_name, guest.last_name, "Age:",guest.age)


   def loyalty_program(self, all_guests):
      gold_members = [guest.last_name for guest in all_guests if guest.rank >= 10]
      if gold_members:
         print("Gold members:")
         for member in gold_members:
            print("\tGuest:", member) 




   def guest_avg(self, all_guests):
      total_age = 0 
      for guest in all_guests:
          total_age += guest.age
      avg_age = total_age / len(all_guests)
      print("average customer age:",avg_age)



all_guests = list()
num_guests = int(input("Enter a member of guests: "))
for i in range(num_guests):
   data = input("First Name/Last Name/Rank/Age: ").split("/")

   guest = Guest(data[0],data[1],int(data[2]), int(data[3])) 
   all_guests.append(guest)



guest = all_guests[0]
guest.loyalty_program(all_guests)
guest.guest_info(all_guests)
guest.guest_avg(all_guests)
            
             
              
           



    #



class OnlineCourse:
        def __init__(self, course, instructor): 
           self.course = course
           self.instructor = instructor
           self.students = []



        def enroll_students(self, student):
            self.students.append(student)
            print(f"{student.name} has been enrolled in the {self.course} course.")



        def course_details(self):
           print(f"Course: {self.course}")
           print(f"Instructor Name: {self.instructor}")
           print(f"Erolled Students:")
           for student in self.students:
               print(student.name)
                       



        def completed_course(self, name):
            for student in self.students:
                if student.name in name:
                    self.students.remove(student)
                    print(f"{name} has completed the course!")               
            print(f"{name} is not enrolled in this course")



        def  avg_grade(self, grades):  
            total = sum(student.grades)
            average = total / len(student.grades)
            print(f"The average grade is: {round(average,1)}") 
            

class Student:
        def __init__(self, name, grades):
            self.name = name
            self.grades = grades
        

#
course_input = input("Enter a course: ").lower()
name = input("Enter a Instructor: ").lower() 
course = OnlineCourse(course_input, name)
#



num_students = int(input("Enter number of student: "))

for _ in range(num_students):
    student_name = input("Enter a student name: ").lower()
    grades = []
    for _ in range(3):
        grade = int(input("Enter a grade: "))
        grades.append(grade)
    student = Student(student_name, grades)
    course.enroll_students(student)
    course.avg_grade(student)
course.course_details()        



        




 


