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
            <h3 color="indigo">Make Appointment</h3>
          </center>
          <v-card class="my-5">
            <v-container fluid class="my-5">
              <v-card class="pa-13" outline>
                <form>
                  <v-layout row wrap>
                    <v-row>
                      <v-col cols="12" sm="6" class="d-flex">
                        <v-autocomplete
                          v-model="values"
                          :items="items"
                          dense
                          chips
                          small-chips
                          label="Type Of Appointment"
                          outlined
                          small
                        ></v-autocomplete>
                      </v-col>
                      <v-col class="d-flex" cols="12" sm="6">
                        <v-autocomplete
                          v-model="values"
                          :items="items"
                          dense
                          chips
                          small-chips
                          label="Category"
                          outlined
                          small
                        ></v-autocomplete>
                      </v-col>
                    </v-row>
                  </v-layout>
                  <v-layout row wrap>
                    <v-row>
                      <v-col cols="12" sm="6" class="d-flex">
                        <v-autocomplete
                          v-model="values"
                          :items="items"
                          dense
                          chips
                          small-chips
                          label="With"
                          outlined
                          small
                        ></v-autocomplete>
                      </v-col>
                      <v-col cols="12" sm="6" class="d-flex">
                        <v-textarea
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
                    <v-row>
                      <v-col cols="12" sm="6">
                        <v-dialog
                          ref="dialog"
                          v-model="modal2"
                          :return-value.sync="time"
                          persistent
                          width="290px"
                        >
                          <template v-slot:activator="{ on, attrs }">
                            <v-text-field
                              v-model="time"
                              label="Favoride Time"
                              prepend-icon="mdi-clock-time-four-outline"
                              readonly
                              v-bind="attrs"
                              v-on="on"
                            ></v-text-field>
                          </template>
                          <v-time-picker
                            v-if="modal2"
                            v-model="time"
                            full-width
                          >
                            <v-spacer></v-spacer>
                            <v-btn text color="primary" @click="modal2 = false">
                              Cancel
                            </v-btn>
                            <v-btn
                              text
                              color="primary"
                              @click="$refs.dialog.save(time)"
                            >
                              OK
                            </v-btn>
                          </v-time-picker>
                        </v-dialog>
                      </v-col>
                      <v-col class="d-flex" cols="12" sm="6">
                        <vue-tel-input-vuetify
                          outlined
                          x-large
                          v-model="phone"
                        ></vue-tel-input-vuetify>
                      </v-col>
                    </v-row>
                  </v-layout>
                  <v-layout row wrap>
                    <v-col cols="12" sm="6" class="d-flex"> </v-col>
                    <v-col cols="12" sm="6" class="d-flex">
                      <v-btn color="primary" class="hange"> Submit</v-btn>
                    </v-col>
                  </v-layout>
                </form>
              </v-card>
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
    phone: null,
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
