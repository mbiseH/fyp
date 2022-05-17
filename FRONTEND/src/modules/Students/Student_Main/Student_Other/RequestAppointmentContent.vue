<template>
  <v-app>
    <v-form v-model="valid">
      <v-container fluid>
        <v-card>
          <v-layout row wrap>
            <v-flex xs12 sm6 md3 lg3>
              <v-spacer></v-spacer>
            </v-flex>
          </v-layout>
          <br /><br />
          <v-divider> </v-divider>
          <br />
          <center>
            <h3 color="indigo">Request Appointment</h3>
          </center>
          <v-card class="my-5">
            <v-form ref="form" v-model="valid" lazy-validation>
              <v-container fluid class="my-5">
                <v-card class="pa-13" outline>
                  <v-layout row wrap>
                    <v-row>
                      <v-col cols="12" sm="6" class="d-flex">
                        <v-autocomplete
                          v-model="appointmentCriteria.type_of_appointment"
                          :items="items1"
                          dense
                          chips
                          small-chips
                          label="Type Of Appointment"
                          outlined
                          small
                          required
                        ></v-autocomplete>
                      </v-col>
                      <v-col class="d-flex" cols="12" sm="6">
                        <v-autocomplete
                          v-model="appointmentCriteria.category_of_appointment"
                          :items="items"
                          dense
                          chips
                          small-chips
                          label="Category"
                          outlined
                          small
                          required
                        ></v-autocomplete>
                      </v-col>
                    </v-row>
                  </v-layout>
                  <v-layout row wrap>
                    <v-row>
                      <v-col cols="12" sm="6" class="d-flex">
                        <v-autocomplete
                          v-model="appointmentCriteria.with_who_appointment"
                          :items="items"
                          dense
                          chips
                          small-chips
                          label="With"
                          outlined
                          small
                          :rules="[(v) => !!v || 'Item is required']"
                        ></v-autocomplete>
                      </v-col>
                      <v-col cols="12" sm="6" class="d-flex">
                        <v-textarea
                          v-model="appointmentCriteria.appointment_reason"
                          label="Reason"
                          auto-grow
                          outlined
                          rows="3"
                          row-height="25"
                          shaped
                          required
                        ></v-textarea>
                      </v-col>
                    </v-row>
                  </v-layout>
                  <br />
                  <br />
                  <v-layout row wrap>
                    <v-col class="d-flex" cols="12" sm="6">
                      <!-- <vue-tel-input-vuetify
                        outlined
                        x-large
                        v-model="appointmentCriteria.phone"
                      ></vue-tel-input-vuetify> -->
                    </v-col>
                    <v-col cols="12" sm="6" class="d-flex">
                      <div class="text-center">
                        <v-btn
                          class="ma-2 hange"
                          color="primary"
                          outlined
                          @click="SubmitAppointment"
                        >
                          Submit</v-btn
                        >
                        <v-btn
                          class="ma-2 hange"
                          color="success"
                          outlined
                          @click="RescheduleAppointment"
                        >
                          Reschedule
                        </v-btn>
                        <v-btn
                          class="ma-2 hange"
                          color="error"
                          outlined
                          disabled
                          @click="ComplainsAppointment"
                          >Complains</v-btn
                        >
                      </div>
                    </v-col>
                  </v-layout>
                </v-card>
              </v-container>
            </v-form>
          </v-card>
        </v-card>
      </v-container>
    </v-form>
  </v-app>
</template>
<script>
// import gql from "graphql-tag";

// const ALL_STAFF_QUERY = gql``;
export default {
  data: () => ({
    items1: ["Individual", "Group"],
    items: ["Supervisor", "Bursar", "Administrator", "HOd"],
    time: null,
    menu2: false,
    modal2: false,
    valid: false,
    appointmentCriteria: {
      with_who_appointment: "",
      appointment_reason: "",
      category_of_appointment: "",
      type_of_appointment: "",
      // phone: null,
    },
  }),
  methods: {
    SubmitAppointment() {
      this.$refs.form.validate();
      let data = {
        appointmentCriteria: this.appointmentCriteria,
      };
      console.log(data);
      this.$emit("submit-appointment", data);
    },
    RescheduleAppointment() {
      console.log("reschedule");
    },
    ComplainsAppointment() {
      console.log("complain");
    },
  },
};
</script>
<style scoped>
.weka {
  justify-content: center;
  align-items: center;
}
.hange {
  text-transform: unset !important;
}
</style>
