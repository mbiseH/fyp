# mutation{
#   register(
#     email:"gado98@gmail.com"
#     password1:"malgado45"
#     password2:"malgado45"
#     username:"6"
#   )

# {success
# errors
# token
# refreshToken
# }
# }
# mutation{
# 	createStudent(studentDegreeProgram:"TE"
#   studentRegNumber:"6"
#   studentGender:"F"
#   studentFirstName:"Alisia"
#   studentFingerprintId:"wiccllxxa888 stay here"
#   studentSurname:"Saidi"
#     studentMiddleName: "Kapenje"
#   )
#   {
#     student{
#       studentFirstName
      
#     }
#   }
# }
# mutation{
# createStaff(staffFirstName:"Geogina", 
# 	staffRole:"Dean"
#   staffGender:"F"
#   staffId:"6"
#   staffMiddleName:"TUMAINI"
#   staffOffice:"H_AB 024"
#   staffSurname
#   :"MWAISA"
  
# )
#   {
#     staff{
#       staffFirstName
      
#     }
#   }
#   # createStaff
# }

# {
#   allStaffs
#   {
#    staffId
#     staffOffice
#     staffRole
    
#   }
# }


# mutation mbise
# {
#   createAppointment(
    
   
#   appointmentTime:"20-11-2022"
#     appointmentType:"Indiv"
#     appointmentDescription:"njoo chapu kuna kesi ya maumbile"
  
#   appointmentCategory:"priv"
#     appointmentStatus:"missed"
#     staffId:"4"
#     studentRegNumber: "6"
   
#     staffPhoneNumber: 692067745
# 		studentPhoneNumber: 746778585
#   )
#   {
#     appointment
#     {
#       appointmentDescription
#     }
#   }
# }


# {
#   allAppointments(staffId:"9")
#   { 
#   appointmentStatus
#   }
# }


# {
#   allTasks{
#     taskId
#     taskDescription
#   }
# }

# mutation gadotz{
#   createTask
#   (
#   appointmentId:"3"
#     taskDescription:"Muzurure Tu mTakomaaaaa"
#     taskFeedbackFile:"kazi.pdf"
#     taskType:"coursewrok"
#     staffId:"1"
#     taskIssueDate:"16/10/2022"
#   )
  
# {
#   task{
#   taskId  
#   }
# }
# }

# mutation gadoboy
# {
# updateTask(appointmentId:"4"
# taskId:8
# taskDescription:"waosha karoti nyie kuweni wa poleeee") 
#   {
#     task{
#       appointmentId{
#         staffId{staffFirstName}
#         studentRegNumber{studentFirstName}
#       }
#       taskId
#     }
#   }
# }

# {
#     task(taskId:"2") {
#     taskType
#     taskDescription
#     taskIssueDate
#     taskFeedbackFile
#       appointmentId{
#         staffId{staffFirstName}
#         studentRegNumber{studentFirstName}
#       }
#       taskId
#     }
#   }
 # pull data from Various tables
# {
#   appointment(appointmentId:"10")
# {
#  appointmentDescription
#   appointmentCategory
#   appointmentTime
#   staffPhoneNumber
#   staffPhoneNumber
#   studentRegNumber{
#     studentRegNumber
#     studentFirstName
#     studentDegreeProgram
#     studentFingerprintId
#   }
#   staffId{
#     staffOffice
#     staffGender
#     staffFirstName
#     staffMiddleName
#     taskSet{
#       taskType
#       taskDescription
#     }
#   }
# }
# }

#Student View His/her Apppointments
# {
#   studentAppointment(studentRegNumber:"5"){
#     appointmentStatus
#     appointmentTime
#     appointmentDescription
    
#     staffId{
#       staffOffice
#       staffFirstName
#       staffSurname
#     }
#     studentRegNumber
#     {
#       studentFirstName
#       studentRegNumber
#       studentDegreeProgram
#     }
#   }
# }


# Staff View His/her Apppointments
# {
#   staffAppointment(staffId:"1"){
#     appointmentStatus
#     appointmentTime
#     appointmentDescription
#     # appointmentCategory
#     staffId{
#       staffOffice
#       staffFirstName
#       staffSurname
#     }
#     studentRegNumber
#     {
#       studentFirstName
#       studentRegNumber
#       studentDegreeProgram
#     }
#   }
# }










