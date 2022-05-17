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
            <h3 color="indigo">Track Appointment</h3>
          </center>
          <v-card class="my-5">
            <v-container fluid class="my-5">
              <v-card class="pa-13" outline> </v-card>
            </v-container>
          </v-card>
        </v-card>
      </v-container>
    </v-form>
  </v-app>
</template>
<script>
export default {
  data: () => ({
    items: ["Academic Supervisor", "FYP", "Bursar Issues", "HOd office"],
    items1: ["Supervisor", "Bursar", "Administrator", "HOd"],
    time: null,
    menu2: false,
    modal2: false,
  }),
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
