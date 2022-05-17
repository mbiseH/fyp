<template>
  <v-app id="inspire">
    <LandingPageToolBar />
    <v-container fluid class="my-5">
      <v-card flat>
        <v-layout row wrap>
          <v-row justify="center">
            <v-expansion-panels>
              <v-expansion-panel>
                <v-expansion-panel-header>
                  <template v-slot:default="{ open }">
                    <v-row no-gutters>
                      <v-col cols="4"> Task </v-col>
                      <v-col cols="8" class="text--secondary">
                        <v-fade-transition leave-absolute>
                          <span v-if="open" key="0">
                            Enter a name for the task
                          </span>
                          <span v-else key="1">
                            {{ trip.name }}
                          </span>
                        </v-fade-transition>
                      </v-col>
                    </v-row>
                  </template>
                </v-expansion-panel-header>

                <v-expansion-panel-content>
                  <v-text-field
                    v-model="trip.name"
                    placeholder="Caribbean Cruise"
                  ></v-text-field>
                </v-expansion-panel-content>
              </v-expansion-panel>
              <v-expansion-panel>
                <v-expansion-panel-header>
                  <template v-slot:default="{ open }">
                    <v-row no-gutters>
                      <v-col cols="4"> Sub Task </v-col>
                      <v-col cols="8" class="text--secondary">
                        <v-fade-transition leave-absolute>
                          <span v-if="open" key="0">
                            Enter a name for the task
                          </span>
                          <span v-else key="1">
                            {{ trip.name }}
                          </span>
                        </v-fade-transition>
                      </v-col>
                    </v-row>
                  </template>
                </v-expansion-panel-header>

                <v-expansion-panel-content>
                  <v-text-field
                    v-model="trip.name"
                    placeholder="Caribbean Cruise"
                  ></v-text-field>
                </v-expansion-panel-content>
              </v-expansion-panel>

              <v-expansion-panel>
                <v-expansion-panel-header v-slot="{ open }">
                  <v-row no-gutters>
                    <v-col cols="4"> Teams </v-col>
                    <v-col cols="8" class="text--secondary">
                      <v-fade-transition leave-absolute>
                        <span v-if="open" key="0"> Select TEAMS </span>
                        <span v-else key="1">
                          {{ trip.location }}
                        </span>
                      </v-fade-transition>
                    </v-col>
                  </v-row>
                </v-expansion-panel-header>
                <v-expansion-panel-content>
                  <v-row no-gutters>
                    <v-spacer></v-spacer>
                    <v-col cols="5">
                      <v-select
                        v-model="trip.location"
                        :items="locations"
                        chips
                        flat
                        solo
                      ></v-select>
                    </v-col>
                  </v-row>
                </v-expansion-panel-content>
              </v-expansion-panel>

              <v-expansion-panel>
                <v-expansion-panel-header v-slot="{ open }">
                  <v-row no-gutters>
                    <v-col cols="4"> Start and end dates </v-col>
                    <v-col cols="8" class="text--secondary">
                      <v-fade-transition leave-absolute>
                        <span v-if="open">When do you want to START?</span>
                        <v-row v-else no-gutters style="width: 100%">
                          <v-col cols="4">
                            Start date: {{ trip.start || "Not set" }}
                          </v-col>
                          <v-col cols="4">
                            End date: {{ trip.end || "Not set" }}
                          </v-col>
                        </v-row>
                      </v-fade-transition>
                    </v-col>
                  </v-row>
                </v-expansion-panel-header>
                <v-expansion-panel-content>
                  <v-row justify="space-around" no-gutters>
                    <v-col cols="3">
                      <v-menu
                        ref="startMenu"
                        :close-on-content-click="false"
                        :return-value.sync="trip.start"
                        offset-y
                        min-width="290px"
                      >
                        <template v-slot:activator="{ on, attrs }">
                          <v-text-field
                            v-model="trip.start"
                            label="Start date"
                            prepend-icon="mdi-calendar"
                            readonly
                            v-bind="attrs"
                            v-on="on"
                          ></v-text-field>
                        </template>
                        <v-date-picker v-model="date" no-title scrollable>
                          <v-spacer></v-spacer>
                          <v-btn
                            text
                            color="primary"
                            @click="$refs.startMenu.isActive = false"
                          >
                            Cancel
                          </v-btn>
                          <v-btn
                            text
                            color="primary"
                            @click="$refs.startMenu.save(date)"
                          >
                            OK
                          </v-btn>
                        </v-date-picker>
                      </v-menu>
                    </v-col>

                    <v-col cols="3">
                      <v-menu
                        ref="endMenu"
                        :close-on-content-click="false"
                        :return-value.sync="trip.end"
                        offset-y
                        min-width="290px"
                      >
                        <template v-slot:activator="{ on, attrs }">
                          <v-text-field
                            v-model="trip.end"
                            label="End date"
                            prepend-icon="mdi-calendar"
                            readonly
                            v-bind="attrs"
                            v-on="on"
                          ></v-text-field>
                        </template>
                        <v-date-picker v-model="date" no-title scrollable>
                          <v-spacer></v-spacer>
                          <v-btn
                            text
                            color="primary"
                            @click="$refs.endMenu.isActive = false"
                          >
                            Cancel
                          </v-btn>
                          <v-btn
                            text
                            color="primary"
                            @click="$refs.endMenu.save(date)"
                          >
                            OK
                          </v-btn>
                        </v-date-picker>
                      </v-menu>
                    </v-col>
                  </v-row>
                </v-expansion-panel-content>
              </v-expansion-panel>
            </v-expansion-panels>
          </v-row>
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
  data: () => ({
    date: null,
    trip: {
      name: "",

      location: null,
      start: null,
      end: null,
    },
    locations: ["edwin", "yogona", "Cinama", "JAackson", "Mgosi", "Mussa"],
  }),
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
