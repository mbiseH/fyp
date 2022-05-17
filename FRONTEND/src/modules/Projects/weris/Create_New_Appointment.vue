<template>
  <v-app>
    <v-container fluid>
      <v-card>
        <v-layout row wrap>
          <v-flex xs12 sm6 md3 lg3>
            <v-hover v-slot="{ hover }" open-delay="200">
              <v-card
                class="text-xs-center ma-3"
                max-width="344"
                :elevation="hover ? 16 : 2"
                :class="{ 'on-hover': hover }"
                link
                to="/more_about_status"
              >
                <v-card-title> Completed Appointment</v-card-title>
                <v-card-text
                  ><span>
                    <center><v-chip color="#3cd1c2">12</v-chip></center></span
                  ></v-card-text
                >
                <v-icon small color="#3cd1c2">mdi-comment-check</v-icon>
              </v-card>
            </v-hover>
          </v-flex>
          <v-flex xs12 sm6 md3 lg3>
            <v-hover v-slot="{ hover }" open-delay="200">
              <v-card
                raised
                class="text-xs-center ma-3"
                max-width="344"
                :elevation="hover ? 16 : 2"
                :class="{ 'on-hover': hover }"
                link
                to="/more_about_status"
              >
                <v-card-title> Appointment Delayed</v-card-title>
                <v-card-text
                  ><span>
                    <center><v-chip color="#f83e70">12</v-chip></center></span
                  ></v-card-text
                >
                <v-icon small color="#f83e70">mdi-cached</v-icon>
              </v-card>
            </v-hover>
          </v-flex>
          <v-flex xs12 sm6 md3 lg3>
            <v-hover v-slot="{ hover }" open-delay="200">
              <v-card
                class="text-xs-center ma-3"
                max-width="344"
                :elevation="hover ? 16 : 2"
                :class="{ 'on-hover': hover }"
                link
                to="/more_about_status"
              >
                <v-card-title>Appointment on progress</v-card-title>
                <v-card-text
                  ><span>
                    <center><v-chip color="#ffaa2c">12</v-chip></center></span
                  ></v-card-text
                >
                <v-icon small color="#ffaa2c">mdi-comment-processing</v-icon>
              </v-card>
            </v-hover>
          </v-flex>
          <v-flex xs12 sm6 md3 lg3>
            <v-hover v-slot="{ hover }" open-delay="200">
              <v-card
                class="text-xs-center ma-3"
                max-width="344"
                :elevation="hover ? 16 : 2"
                :class="{ 'on-hover': hover }"
                link
                to="/more_about_status"
              >
                <v-card-title>Appointment on Hold</v-card-title>
                <v-card-text
                  ><span>
                    <center><v-chip color="#ffaa2c">12</v-chip></center></span
                  ></v-card-text
                >
                <v-icon small color="primary">mdi-comment-flash</v-icon>
              </v-card>
            </v-hover>
          </v-flex>
        </v-layout>
        <br /><br />
        <v-divider> </v-divider>
        <br />
        <v-layout row wrap>
          <v-flex xs12 md6>
            <div>
              <v-card class="text-xs-center ma-3" max-width="500">
                <apexcharts
                  width="500"
                  height="350"
                  type="bar"
                  :options="chartOptions"
                  :series="series"
                ></apexcharts>
              </v-card>
            </div>
          </v-flex>
          <v-flex xs12 md6>
            <div>
              <v-card class="text-xs-center ma-3" max-width="500">
                <apexcharts
                  type="polarArea"
                  :options="chartOptions1"
                  :series="series1"
                ></apexcharts>
              </v-card>
            </div>
          </v-flex>
        </v-layout>
      </v-card>
    </v-container>
  </v-app>
</template>
