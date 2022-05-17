<template>
  <v-dialog v-model="dialog" ersistent max-width="700px">
    <template v-slot:activator="{ on, attrs }">
      <v-btn
        small
        left
        class="mx-2"
        fab
        color="primary"
        dark
        v-bind="attrs"
        v-on="on"
        dense
      >
        <v-icon small> mdi-plus</v-icon>
      </v-btn>
    </template>
    <v-card>
      <v-card-title>
        <span class="grey--text">Add Project</span>
      </v-card-title>
      <v-card-text>
        <v-form class="px-5">
          <v-container>
            <v-row>
              <v-col cols="12">
                <v-text-field
                  label="Project Title*"
                  v-model="projectTitle"
                  dense
                  required
                  prepend-icon="mdi-folder-multiple"
                ></v-text-field>
              </v-col>
              <v-col cols="12">
                <v-text-field
                  small
                  label="Project Description*"
                  v-model="projectDescription"
                  required
                  prepend-icon="mdi-pan"
                ></v-text-field>
              </v-col>
              <v-col cols="12">
                <v-text-field
                  small
                  label="Project Leader*"
                  v-model="projectLeader"
                  required
                  prepend-icon="mdi-account-tie"
                ></v-text-field>
              </v-col>

              <v-col cols="12">
                <v-combobox
                  small
                  v-model="chips"
                  :items="items"
                  chips
                  clearable
                  label="Project Team"
                  multiple
                  prepend-icon="mdi-filter-variant"
                  solo
                >
                  <template
                    v-slot:selection="{ attrs, item, select, selected }"
                  >
                    <v-chip
                      v-bind="attrs"
                      :input-value="selected"
                      close
                      @click="select"
                      @click:close="remove(item)"
                    >
                      <strong>{{ item }}</strong
                      >&nbsp;
                    </v-chip>
                  </template>
                </v-combobox>
              </v-col>
              <v-col cols="12">
                <v-combobox
                  small
                  v-model="status"
                  :items="items1"
                  chips
                  clearable
                  label="Project Status"
                  multiple
                  prepend-icon="mdi-star-crescent"
                  solo
                >
                  <template
                    v-slot:selection="{ attrs, item, select, selected }"
                  >
                    <v-chip
                      v-bind="attrs"
                      :input-value="selected"
                      close
                      @click="select"
                      @click:close="remove1(item)"
                    >
                      <strong>{{ item }}</strong
                      >&nbsp;
                    </v-chip>
                  </template>
                </v-combobox>
              </v-col>
              <v-col cols="12" sm="6">
                <v-menu
                  v-model="menu2"
                  :close-on-content-click="false"
                  :nudge-right="40"
                  transition="scale-transition"
                  offset-y
                  min-width="auto"
                >
                  <template v-slot:activator="{ on, attrs }">
                    <v-text-field
                      v-model="date"
                      label="Start Date"
                      prepend-icon="mdi-calendar-clock"
                      readonly
                      v-bind="attrs"
                      v-on="on"
                    >
                    </v-text-field>
                  </template>
                  <v-date-picker
                    v-model="date"
                    @input="menu2 = false"
                  ></v-date-picker>
                </v-menu>
              </v-col>
              <v-col cols="12" sm="6">
                <v-menu
                  v-model="menu1"
                  :close-on-content-click="false"
                  :nudge-right="40"
                  transition="scale-transition"
                  offset-y
                  min-width="auto"
                >
                  <template v-slot:activator="{ on, attrs }">
                    <v-text-field
                      v-model="date1"
                      label="Completion Date"
                      prepend-icon="mdi-calendar-end"
                      readonly
                      v-bind="attrs"
                      v-on="on"
                    ></v-text-field>
                  </template>
                  <v-date-picker
                    v-model="date1"
                    @input="menu1 = false"
                  ></v-date-picker>
                </v-menu>
              </v-col>
            </v-row>
          </v-container>
        </v-form>
      </v-card-text>

      <v-card-actions>
        <v-spacer></v-spacer>
        <v-tooltip bottom color="error">
          <template v-slot:activator="{ on, attrs }">
            <v-btn
              small
              fab
              color="#f83e70"
              dark
              @click="dialog = false"
              v-bind="attrs"
              v-on="on"
            >
              <v-icon small>mdi-close-octagon</v-icon>
            </v-btn>
          </template>
          <span>Cancel</span>
        </v-tooltip>
        <v-tooltip bottom color="success">
          <template v-slot:activator="{ on, attrs }">
            <v-btn
              small
              fab
              color="primary"
              dark
              @click="dialog = false"
              v-bind="attrs"
              v-on="on"
            >
              <v-icon small>mdi-send</v-icon>
            </v-btn>
          </template>
          <span>Submit you data !</span>
        </v-tooltip>
      </v-card-actions>
    </v-card>
  </v-dialog>
  <!-- </v-row> -->
</template>
<script>
export default {
  data: () => ({
    dialog: false,
    projectTitle: "",
    projectDescription: "",
    chips: "",
    status: "",
    items: ["Edwin", "Beatus", "Pantaleo"],
    items1: ["Ongoing", "Completed", "On production"],
    date: new Date(Date.now() - new Date().getTimezoneOffset() * 60000)
      .toISOString()
      .substr(0, 10),
    date1: new Date(Date.now() - new Date().getTimezoneOffset() * 60000)
      .toISOString()
      .substr(0, 10),
    menu: false,
    modal: false,
    menu1: false,
    menu2: false,
  }),
  methods: {
    remove(item) {
      this.chips.splice(this.chips.indexOf(item), 1);
      this.chips = [...this.chips];
    },
    remove1(item) {
      this.status.splice(this.status.indexOf(item), 1);
      this.status = [...this.status];
    },
  },
};
</script>
