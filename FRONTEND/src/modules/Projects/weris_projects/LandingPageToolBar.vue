<template>
  <v-container fluid>
    <div class="text-center d-flex align-center justify-space-around">
      <v-toolbar dense>
        <v-btn icon color="primary" v-bind="attrs" v-on="on">
          <v-icon>mdi-projector</v-icon>
        </v-btn>
        <v-toolbar-title>Appointment</v-toolbar-title>

        <v-spacer></v-spacer>
        <v-tooltip bottom color="primary">
          <template v-slot:activator="{ on, attrs }">
            <v-btn icon color="primary" v-bind="attrs" v-on="on" link to="/">
              <v-icon>mdi-home</v-icon>
            </v-btn>
          </template>
          <span>go to Home </span>
        </v-tooltip>
      </v-toolbar>
    </div>
  </v-container>
</template>
