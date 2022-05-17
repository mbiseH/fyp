<template>
  <v-app>
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
        <v-layout row wrap>
          <v-flex xs12>
            <v-data-table
              loading
              :headers="headers"
              :items="desserts"
              :items-per-page="5"
              class="elevation-1"
              loading-text="Loading... Previous Appointment wait"
            ></v-data-table>
          </v-flex>
        </v-layout>
      </v-card>
    </v-container>
  </v-app>
</template>
<script>
export default {
  data() {
    return {
      headers: [
        {
          text: "Appointment Name",
          align: "start",
          sortable: true,
          value: "name",
        },
        { text: "Appointment Id", value: "calories" },
        { text: "Appointment Catgory", value: "fat" },
        { text: "Staff Phone Number", value: "carbs" },
        { text: "Student Phone Number", value: "protein" },
        { text: "Student Regestration Number", value: "iron" },
      ],
      desserts: [
        {
          name: "FYP",
          calories: 159,
          fat: 6.0,
          carbs: 24,
          protein:5,
          iron: "T/UDOM/2018.03592",
        },
        {
          name: "Academic Supersivison",
          calories: 237,
          fat: 9.0,
          carbs: 37,
          protein: 4.3,
          iron: "T/UDOM/2018.03592",
        },
        {
          name: "HOD",
          calories: 262,
          fat: 16.0,
          carbs: 23,
          protein: 6.0,
          iron: "T/UDOM/2018.03592",
        },
        {
          name: "Bursor",
          calories: 305,
          fat: 3.7,
          carbs: 67,
          protein: 4.3,
          iron: "T/UDOM/2018.03592",
        },
        {
          name: "Gingerbread",
          calories: 356,
          fat: 16.0,
          carbs: 49,
          protein: 3.9,
          iron: "T/UDOM/2018.03592",
        },
        {
          name: "Jelly bean",
          calories: 375,
          fat: 0.0,
          carbs: 94,
          protein: 0.0,
          iron: "0%",
        },
        {
          name: "Lollipop",
          calories: 392,
          fat: 0.2,
          carbs: 98,
          protein: 0,
          iron: "2%",
        },
        {
          name: "Honeycomb",
          calories: 408,
          fat: 3.2,
          carbs: 87,
          protein: 6.5,
          iron: "45%",
        },
        {
          name: "Donut",
          calories: 452,
          fat: 25.0,
          carbs: 51,
          protein: 4.9,
          iron: "22%",
        },
        {
          name: "KitKat",
          calories: 518,
          fat: 26.0,
          carbs: 65,
          protein: 7,
          iron: "6%",
        },
      ],
    };
  },
};
</script>

<style scoped>
.weka {
  justify-content: center;
  align-items: center;
}
</style>
