<template>
  <v-app id="inspire">
    <v-content>
      <LandingPageToolBar />
      <v-container class="fill-height">
        <v-row align="center" justify="center">
          <!-- <v-card class="pa-5"> -->
          <v-layout row wrap justify-space-around>
            <v-flex xs12 md4>
              <v-hover v-slot="{ hover }" open-delay="200">
                <v-card
                  raised
                  class="text-xs-center ma-3"
                  max-width="344"
                  height="150"
                  :elevation="hover ? 16 : 2"
                  :class="{ 'on-hover': hover }"
                  link
                  to="/"
                >
                  <v-card max-width="344" max-height="20" color="primary">
                  </v-card>
                  <v-card-text>
                    <center>
                      <v-icon color="primary" size="80">
                        mdi-calendar-clock-outline
                      </v-icon>
                      <h2>Appointment</h2>
                    </center>
                  </v-card-text>
                </v-card>
              </v-hover>
            </v-flex>
            <v-flex xs12 md4>
              <v-hover v-slot="{ hover }" open-delay="200">
                <v-card
                  class="text-xs-center ma-3"
                  max-width="344"
                  height="150"
                  :elevation="hover ? 16 : 2"
                  :class="{ 'on-hover': hover }"
                  link
                  to="/"
                >
                  <v-card-text>
                    <center>
                      <v-icon color="primary" size="80"> mdi-bell-ring </v-icon>
                      <h2>Notification Message</h2>
                    </center>
                  </v-card-text>
                </v-card>
              </v-hover>
            </v-flex>
            <v-flex xs12 md4>
              <v-hover v-slot="{ hover }" open-delay="400">
                <v-card
                  class="text-xs-center ma-3"
                  max-width="344"
                  height="150"
                  :elevation="hover ? 16 : 2"
                  :class="{ 'on-hover': hover }"
                  link
                  to="/"
                >
                  <v-card-text>
                    <center>
                      <v-icon color="primary" size="80">
                        mdi-fingerprint
                      </v-icon>
                      <h2>Biometric Confirmation</h2>
                    </center>
                  </v-card-text>
                </v-card>
              </v-hover>
            </v-flex>
          </v-layout>
          <!-- </v-card> -->
        </v-row>
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
import LandingPageToolBar from "../../Landing/Landing_Shared/LandingPageToolBar.vue";

export default {
  components: {
    LandingPageToolBar,
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
