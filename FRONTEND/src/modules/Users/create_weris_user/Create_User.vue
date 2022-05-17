<template>
  <v-app>
    <div class="Create_User">
      <v-card class="my-5">
        <v-container fluid class="my-5">
          <v-card class="pa-13" outline>
            <v-layout wrap>
              <v-row>
                <v-dialog v-model="dialog1" persistent max-width="700px">
                  <template v-slot:activator="{ on, attrs }">
                    <v-btn
                      class="ma-2"
                      color="indigo"
                      outlined
                      v-bind="attrs"
                      v-on="on"
                    >
                      <v-icon small color="primary">
                        mdi-plus-circle-multiple
                      </v-icon>
                      <span style="text-color: primary">
                        <small class="TextColor">add user</small></span
                      >
                    </v-btn>
                  </template>
                  <v-card>
                    <v-card-title>
                      <span class="text-h5">User Information</span>
                    </v-card-title>
                    <v-card-text>
                      <v-container>
                        <v-row>
                          <v-col cols="12" sm="6" md="4">
                            <v-text-field
                              label="First Name"
                              outlined
                              dense
                              required
                            ></v-text-field>
                          </v-col>
                          <v-col cols="12" sm="6" md="4">
                            <v-text-field
                              label="Second Name"
                              outlined
                              dense
                              required
                            ></v-text-field>
                          </v-col>
                          <v-col cols="12" sm="6" md="4">
                            <v-text-field
                              label="Last Name"
                              outlined
                              dense
                              required
                            ></v-text-field>
                          </v-col>
                          <v-col cols="12">
                            <v-text-field
                              label="Email"
                              outlined
                              dense
                              required
                            ></v-text-field>
                          </v-col>
                          <v-col cols="12">
                            <v-text-field
                              label="Password"
                              outlined
                              dense
                              required
                              type="password"
                            ></v-text-field>
                          </v-col>
                          <v-col cols="12">
                            <v-text-field
                              label="Confirm Your Password"
                              outlined
                              dense
                              required
                              type="password"
                            ></v-text-field>
                          </v-col>
                          <v-col cols="12" sm="6"> </v-col>
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
                                  label="Date of Birth"
                                  prepend-icon="mdi-calendar-clock"
                                  readonly
                                  v-bind="attrs"
                                  v-on="on"
                                >
                                </v-text-field>
                              </template>
                              <v-date-picker
                                dense
                                v-model="date"
                                @input="menu2 = false"
                              ></v-date-picker>
                            </v-menu>
                          </v-col>
                        </v-row>
                      </v-container>
                      <small>*indicates required field</small>
                    </v-card-text>
                    <v-card-actions>
                      <v-spacer></v-spacer>
                      <v-btn
                        class="ma-2"
                        color="primary"
                        raised
                        text
                        @click="dialog1 = false"
                      >
                        <v-icon color="red"> mdi-close-circle 0 </v-icon>
                        Close
                      </v-btn>
                      <v-btn
                        class="ma-2"
                        color="indigo"
                        outlined
                        @click="dialog1 = false"
                      >
                        <v-icon color="primary"> mdi-send-check </v-icon>
                        Save
                      </v-btn>
                    </v-card-actions>
                  </v-card>
                </v-dialog>

                <v-btn class="ma-2" outlined color="indigo">
                  <v-icon small color="primary">
                    mdi-plus-circle-multiple
                  </v-icon>
                  <span><small>Add dummy user</small></span>
                </v-btn>

                <v-file-input small-chips truncate-length="15">
                  <span><small>Import(CSV)</small></span>
                </v-file-input>

                <v-btn class="ma-2" outlined color="indigo">
                  <v-icon small color="primary">
                    mdi-swap-vertical-circle
                  </v-icon>
                  <span><small>Import(JSON)</small></span>
                </v-btn>

                <v-btn class="ma-2" outlined color="indigo">
                  <v-icon small color="primary">
                    mdi-watch-export-variant
                  </v-icon>
                  <span><small>Export</small></span>
                </v-btn>
                <v-spacer></v-spacer>
                <v-btn class="ma-2" outlined color="indigo" link to="/home">
                  <v-icon color="primary"> mdi-backburger </v-icon>
                  <span>
                    <small>Go back To Home PAge</small>
                  </span>
                </v-btn>
              </v-row>
            </v-layout>
          </v-card>
          <v-divider></v-divider>
          <v-card class="my-5">
            <v-data-table
              :headers="headers"
              :items="desserts"
              sort-by="calories"
              class="elevation-1"
            >
              <template v-slot:top>
                <v-toolbar flat>
                  <v-toolbar-title></v-toolbar-title>
                  <v-divider class="mx-4" inset vertical></v-divider>
                  <v-spacer></v-spacer>
                  <v-dialog v-model="dialog" max-width="500px">
                    <template v-slot:activator="{}"> </template>
                    <v-card>
                      <v-card-title>
                        <span class="text-h5">{{ formTitle }}</span>
                      </v-card-title>

                      <v-card-text>
                        <v-container>
                          <v-row>
                            <v-col cols="12" sm="6" md="4">
                              <v-text-field
                                v-model="editedItem.name"
                                label="Dessert name"
                              ></v-text-field>
                            </v-col>
                            <v-col cols="12" sm="6" md="4">
                              <v-text-field
                                v-model="editedItem.calories"
                                label="Calories"
                              ></v-text-field>
                            </v-col>
                            <v-col cols="12" sm="6" md="4">
                              <v-text-field
                                v-model="editedItem.fat"
                                label="Fat (g)"
                              ></v-text-field>
                            </v-col>
                            <v-col cols="12" sm="6" md="4">
                              <v-text-field
                                v-model="editedItem.carbs"
                                label="Carbs (g)"
                              ></v-text-field>
                            </v-col>
                            <v-col cols="12" sm="6" md="4">
                              <v-text-field
                                v-model="editedItem.protein"
                                label="Protein (g)"
                              ></v-text-field>
                            </v-col>
                          </v-row>
                        </v-container>
                      </v-card-text>

                      <v-card-actions>
                        <v-spacer></v-spacer>
                        <v-btn color="blue darken-1" text @click="close">
                          Cancel
                        </v-btn>
                        <v-btn color="blue darken-1" text @click="save">
                          Save
                        </v-btn>
                      </v-card-actions>
                    </v-card>
                  </v-dialog>
                  <v-dialog v-model="dialogDelete" max-width="500px">
                    <v-card>
                      <v-card-title class="text-h5"
                        >Are you sure you want to delete this
                        item?</v-card-title
                      >
                      <v-card-actions>
                        <v-spacer></v-spacer>
                        <v-btn color="blue darken-1" text @click="closeDelete"
                          >Cancel</v-btn
                        >
                        <v-btn
                          color="blue darken-1"
                          text
                          @click="deleteItemConfirm"
                          >OK</v-btn
                        >
                        <v-spacer></v-spacer>
                      </v-card-actions>
                    </v-card>
                  </v-dialog>
                </v-toolbar>
              </template>
              <template v-slot:item.actions="{ item }">
                <v-icon small class="mr-2" @click="editItem(item)">
                  mdi-pencil
                </v-icon>
                <v-icon
                  small
                  color="#5d9ad0"
                  class="mr-3"
                  @click="editItem(item)"
                >
                  mdi-update
                </v-icon>
                <v-icon small color="red" @click="deleteItem(item)">
                  mdi-delete
                </v-icon>
              </template>
              <template v-slot:no-data>
                <v-btn color="primary" @click="initialize"> Reset </v-btn>
              </template>
            </v-data-table>
          </v-card>
        </v-container>
      </v-card>
    </div>
  </v-app>
</template>

<script>
export default {
  data: () => ({
    search: "",
    date: new Date(Date.now() - new Date().getTimezoneOffset() * 60000)
      .toISOString()
      .substr(0, 10),
    dialog1: false,
    dialog: false,
    dialogDelete: false,
    headers: [
      {
        text: "Dessert (100g serving)",
        align: "start",
        sortable: false,
        value: "name",
      },
      { text: "Calories", value: "calories" },
      { text: "Fat (g)", value: "fat" },
      { text: "Carbs (g)", value: "carbs" },
      { text: "Protein (g)", value: "protein" },
      { text: "Actions", value: "actions", sortable: false },
    ],
    desserts: [],
    editedIndex: -1,
    editedItem: {
      name: "",
      calories: 0,
      fat: 0,
      carbs: 0,
      protein: 0,
    },
    defaultItem: {
      name: "",
      calories: 0,
      fat: 0,
      carbs: 0,
      protein: 0,
    },
  }),

  computed: {
    formTitle() {
      return this.editedIndex === -1 ? "New Item" : "Edit Item";
    },
  },

  watch: {
    dialog(val) {
      val || this.close();
    },
    dialogDelete(val) {
      val || this.closeDelete();
    },
  },

  created() {
    this.initialize();
  },

  methods: {
    initialize() {
      this.desserts = [
        {
          name: "Frozen Yogurt",
          calories: 159,
          fat: 6.0,
          carbs: 24,
          protein: 4.0,
        },
        {
          name: "Ice cream sandwich",
          calories: 237,
          fat: 9.0,
          carbs: 37,
          protein: 4.3,
        },
        {
          name: "Eclair",
          calories: 262,
          fat: 16.0,
          carbs: 23,
          protein: 6.0,
        },
        {
          name: "Cupcake",
          calories: 305,
          fat: 3.7,
          carbs: 67,
          protein: 4.3,
        },
        {
          name: "Gingerbread",
          calories: 356,
          fat: 16.0,
          carbs: 49,
          protein: 3.9,
        },
        {
          name: "Jelly bean",
          calories: 375,
          fat: 0.0,
          carbs: 94,
          protein: 0.0,
        },
        {
          name: "Lollipop",
          calories: 392,
          fat: 0.2,
          carbs: 98,
          protein: 0,
        },
        {
          name: "Honeycomb",
          calories: 408,
          fat: 3.2,
          carbs: 87,
          protein: 6.5,
        },
        {
          name: "Donut",
          calories: 452,
          fat: 25.0,
          carbs: 51,
          protein: 4.9,
        },
        {
          name: "KitKat",
          calories: 518,
          fat: 26.0,
          carbs: 65,
          protein: 7,
        },
      ];
    },

    editItem(item) {
      this.editedIndex = this.desserts.indexOf(item);
      this.editedItem = Object.assign({}, item);
      this.dialog = true;
    },

    deleteItem(item) {
      this.editedIndex = this.desserts.indexOf(item);
      this.editedItem = Object.assign({}, item);
      this.dialogDelete = true;
    },

    deleteItemConfirm() {
      this.desserts.splice(this.editedIndex, 1);
      this.closeDelete();
    },

    close() {
      this.dialog = false;
      this.$nextTick(() => {
        this.editedItem = Object.assign({}, this.defaultItem);
        this.editedIndex = -1;
      });
    },

    closeDelete() {
      this.dialogDelete = false;
      this.$nextTick(() => {
        this.editedItem = Object.assign({}, this.defaultItem);
        this.editedIndex = -1;
      });
    },

    save() {
      if (this.editedIndex > -1) {
        Object.assign(this.desserts[this.editedIndex], this.editedItem);
      } else {
        this.desserts.push(this.editedItem);
      }
      this.close();
    },
  },
};
</script>

<style>
.TextColor {
  text-decoration-color: white;
  text-transform: small-fill;
}
</style>
