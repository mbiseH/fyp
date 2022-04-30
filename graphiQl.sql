mutation registerUser{
  register(
    email:"gado98@gmail.com"
    password1:"malgado45"
    password2:"malgado45"
    username:"6"
  )
{
  success
errors
token
refreshToken
}
}
mutation createStudent{
	createStudent(studentDegreeProgram:"TE"
  studentRegNumber:"2"
  studentGender:"F"
  studentFirstName:"ALISIA"
  studentFingerprintId:"wiccllxxa888 stay here"
  studentSurname:"JUMA"
    studentMiddleName: "JUMBE"
  )
  {
    student{
      studentFirstName
      
    }
  }
}
mutation CreateStaff{
createStaff(staffFirstName:"Leila", 
	staffRole:"Coordinator"
  staffGender:"F"
  staffId:"2"
  staffMiddleName:"Madam"
  staffOffice:"H_AB 024"
  staffSurname
  :"MRS"
  
)
  {
    staff{
      staffFirstName
      
    }
  }
  # createStaff
}

query ViewAllStaff{
  allStaffs
  {
   staffId
    staffOffice
    staffRole
    
  }
}


mutation createAppointment
{
  createAppointment(
  	appointmentTime:"20:20:20"
    appointmentDate:"2022-11-20"
    appointmentType:"Indiv"
    appointmentDescription:"Maadam , tunakuja kufanya clearance ofini, please"
    appointmentCategory:"priv"
    appointmentStatus:"missed"
    staffId:"2"
    studentRegNumber: "1"
    staffPhoneNumber: 68920677
		studentPhoneNumber: 994677857
  )
  {
    appointment
    {
      appointmentDescription
    }
  }
}


query allAppointments{
  allAppointments
  { 
  appointmentStatus
  }
}


 # pull data from Various tables
query ViewAppointmentID{
  appointment(appointmentId:"1")
{
 appointmentDescription
  appointmentCategory
  appointmentTime
  staffPhoneNumber
  staffPhoneNumber
  studentRegNumber{
    studentRegNumber
    studentFirstName
    studentDegreeProgram
    studentFingerprintId
  }
  staffId{
    staffOffice
    staffGender
    staffFirstName
    staffMiddleName
    taskSet{
      taskType
      taskDescription
    }
  }
}
}

# #Student View His/her Apppointments
query ViewStudentIDAppointment{
  studentAppointment(studentRegNumber:"2"){
    appointmentStatus
    appointmentTime
    appointmentDescription
    
    staffId{
      staffOffice
      staffFirstName
      staffSurname
    }
    studentRegNumber
    {
      studentFirstName
      studentRegNumber
      studentDegreeProgram
    }
  }
}


# Staff View His/her Apppointments
query ViewStaffIDAppointment{
  staffAppointment(staffId:"1"){
    appointmentStatus
    appointmentTime
    appointmentDescription
    appointmentCategory
    staffId{
      staffOffice
      staffFirstName
      staffSurname
    }
    studentRegNumber
    {
      studentFirstName
      studentRegNumber
      studentDegreeProgram
    }
  }
}


query allTasks{
  allTasks{
    taskId
    taskDescription
  }
}

mutation createTask{
  createTask
  (
  appointmentId:"2"
    taskDescription:"Muzurure Tu mTakomaaaaa"
    taskFeedbackFile:"kazi.pdf"
    taskType:"deployment"
    taskDeadlineDate:"2022-02-22"
    staffId:"2"
    taskIssueDate:"2022-02-26"
  )
{
  task{
  taskId  
  }
}
}

mutation updateTask
{
updateTask(appointmentId:"4"
taskId:8
taskDescription:"waosha karoti nyie kuweni wa poleeee") 
  {
    task{
      appointmentId{
        staffId{staffFirstName}
        studentRegNumber{studentFirstName}
      }
      taskId
    }
  }
}

query ViewTaskD{
    task(taskId:"2") {
    taskType
    taskDescription
    taskIssueDate
    taskFeedbackFile
      appointmentId{
        staffId{staffFirstName}
        studentRegNumber{studentFirstName}
      }
      taskId
    }
  }