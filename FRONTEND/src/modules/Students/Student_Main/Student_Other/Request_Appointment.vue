<template>
  <RequestAppointmentContent @submit-appointment="requestAppoint" />
</template>

<script>
import RequestAppointmentContent from "./RequestAppointmentContent.vue";
import gql from "graphql-tag";

const REQUEST_APPOINTMENT = gql`
  mutation (
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
  }
`;
export default {
  name: "Request_Appointment",
  components: {
    RequestAppointmentContent,
  },
  methods: {
    requestAppoint(data) {
      this.$apollo.mutate({
        mutations: REQUEST_APPOINTMENT,
        variables: data,
        update(cache, data) {
          console.log(data);
          if (data.isEmpty()) {
            console.log("its empty");
          }
        },
      });
    },
  },
};
</script>

<style></style>
