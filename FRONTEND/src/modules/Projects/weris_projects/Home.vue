<template>
  <v-app id="inspire">
    <v-content>
      <LandingPageToolBar />
      <v-container class="fill-height" fluid>
        <v-row align="center" justify="center">
          <!-- <v-col cols="12" sm="8" md="8"> -->
          <v-card class="pa-10">
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
                    to="/projecti"
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
                    to="/complains"
                  >
                    <v-card-text>
                      <center>
                        <v-icon color="primary" size="80">
                          mdi-account-question-outline
                        </v-icon>
                        <h2>Complains</h2>
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
                    to="/reporting"
                  >
                    <v-card-text>
                      <center>
                        <v-icon color="primary" size="80">
                          mdi-file-edit-outline
                        </v-icon>
                        <h2>Report</h2>
                      </center>
                    </v-card-text>
                  </v-card>
                </v-hover>
              </v-flex>
              <v-flex xs12 md4>
                <v-hover v-slot="{ hover }" open-delay="200">
                  <v-card
                    class="text-xs-center ma-3"
                    max-width="350"
                    height="150"
                    :elevation="hover ? 16 : 2"
                    :class="{ 'on-hover': hover }"
                    link
                    to="/create_users"
                  >
                    <v-card-text>
                      <center>
                        <v-icon size="80" color="primary">
                          mdi-account-multiple-plus
                        </v-icon>
                        <h2>Students</h2>
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
                  >
                    <v-card-text>
                      <center>
                        <v-icon color="primary" size="80">
                          mdi-creation
                        </v-icon>
                        <h2>Self Services</h2>
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
                    to=""
                  >
                    <v-card-text>
                      <center>
                        <v-icon size="80" color="primary"> mdi-cog </v-icon>
                        <h2>Settings</h2>
                      </center>
                    </v-card-text>
                  </v-card>
                </v-hover>
              </v-flex>
            </v-layout>
          </v-card>
          <!-- </v-col> -->
        </v-row>
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
import LandingPageToolBar from "./LandingPageToolBar.vue";

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
