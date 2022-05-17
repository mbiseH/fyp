import gql from "graphql-tag";

export const CREATE_APPOINTMENT = gql`
  mutation createAppointment(
    $appointmentTime: String!
    $appointmentDate: String!
    $appointmentType: String!
    $appointmentDescription: String!
    $appointmentCategory: String!
    $appointmentStatus: String!
    $staffId: String!
    $studentRegNumber: String!
    $staffPhoneNumber: Int!
    $studentPhoneNumber: Int!
  ) {
    createAppointment(
      appointmentTime: $appointmentTime
      appointmentDate: $appointmentDate
      appointmentType: $appointmentType
      appointmentDescription: $appointmentDescription
      appointmentCategory: $appointmentCategory
      appointmentStatus: $appointmentStatus
      staffId: $staffId
      studentRegNumber: $studentRegNumber
      staffPhoneNumber: $staffPhoneNumber
      studentPhoneNumber: $studentPhoneNumber
    )
     appointment {
       
    }
  }
`;
