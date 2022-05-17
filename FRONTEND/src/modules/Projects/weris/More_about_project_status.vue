<template>
  <v-app id="inspire">
    <LandingPageToolBar />
    <v-container fluid class="my-5">
      <v-card class="pa-3">
        <v-layout row wrap>
          <v-data-table
            fluid
            :headers="headers"
            :items="desserts"
            :items-per-page="5"
            class="elevation-1"
          ></v-data-table>
        </v-layout>
      </v-card>
    </v-container>
  </v-app>
</template>

<script>
// import LandingPageToolBar from './LandingPageToolBar.vue'
import LandingPageToolBar from "../weris_projects/LandingPageToolBar.vue";

export default {
  components: {
    LandingPageToolBar,
  },
  data() {
    return {
      headers: [
        {
          text: "Appointment Title",
          align: "start",
          sortable: false,
          value: "name",
        },
        { text: "Status", value: "calories" },
        { text: " ", value: "fat" },
        { text: "", value: "carbs" },
        { text: "", value: "protein" },
        { text: "Completion Status(%)", value: "iron" },
      ],
      desserts: [
        {
          name: "FYP",
          calories: 159,
          fat: 6.0,
          carbs: 24,
          protein: 4.0,
          iron: "1%",
        },
        {
          name: "Supervisor",
          calories: 237,
          fat: 9.0,
          carbs: 37,
          protein: 4.3,
          iron: "1%",
        },
        {
          name: "Bursar",
          calories: 262,
          fat: 16.0,
          carbs: 23,
          protein: 6.0,
          iron: "7%",
        },
        {
          name: "Personal Issues with hod",
          calories: 305,
          fat: 3.7,
          carbs: 67,
          protein: 4.3,
          iron: "8%",
        },
        {
          name: "Academic",
          calories: 356,
          fat: 16.0,
          carbs: 49,
          protein: 3.9,
          iron: "16%",
        },
        {
          name: "vpn",
          calories: 375,
          fat: 0.0,
          carbs: 94,
          protein: 0.0,
          iron: "0%",
        },
        {
          name: "latra",
          calories: 392,
          fat: 0.2,
          carbs: 98,
          protein: 0,
          iron: "2%",
        },
        {
          name: "USACF",
          calories: 408,
          fat: 3.2,
          carbs: 87,
          protein: 6.5,
          iron: "45%",
        },
        {
          name: "",
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

<style>
.card-container {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  margin-top: 16px;
}

.card {
  all: unset;
  border-radius: 20px;
  border: 1px solid #eee;
  background-color: #fafafa;
  height: 40px;
  width: 200px;
  margin: 0 8px 16px;
  padding: 16px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  transition: all 0.2s ease-in-out;
  line-height: 24px;
}

.card-container .card:not(:last-child) {
  margin-right: 0;
}

.card.card-small {
  height: 16px;
  width: 168px;
}

.card-container .card:not(.highlight-card) {
  cursor: pointer;
}

.card-container .card:not(.highlight-card):hover {
  transform: translateY(-3px);
  box-shadow: 0 4px 17px rgba(0, 0, 0, 0.35);
}

.card-container .card:not(.highlight-card):hover .material-icons path {
  fill: rgb(105, 103, 103);
}

.card.highlight-card {
  background-color: #1976d2;
  color: white;
  font-weight: 600;
  border: none;
  width: auto;
  min-width: 30%;
  position: relative;
}

.card.card.highlight-card span {
  margin-left: 60px;
}
</style>
