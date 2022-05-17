<template>
  <v-app>
    <div class="Create_User">
      <v-card class="my-5">
        <v-container fluid class="my-5">
          <v-card class="pa-13" outline>
            <v-layout row wrap>
              <v-flex xs12 sm6>
                <span>Add FingerPrint</span>
                <br />
                <v-btn rounded raised small>
                  Search
                  <v-icon dark small> mdi-magnify-expand </v-icon>
                </v-btn>
              </v-flex>
              <v-flex xs12 sm6>
                <span>Capture</span>
                <br />
                <v-btn rounded raised small>
                  <v-icon dark> mdi-fingerprint </v-icon>
                </v-btn>
              </v-flex>
            </v-layout>
          </v-card>
        </v-container>
      </v-card>
    </div>
  </v-app>
</template>

<script>
export default {};
</script>

<style>
.border_radius {
  border-radius: 20px;
  text-transform: unset !important;
}
</style>
