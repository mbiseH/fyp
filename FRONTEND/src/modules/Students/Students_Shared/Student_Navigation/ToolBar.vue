<template>
  <v-container>
    <v-app-bar dense app color="#5d9ad0" dark>
      <div class="d-flex align-center">
        <v-app-bar-nav-icon @click="mini = !mini"></v-app-bar-nav-icon>
      </div>
      <v-spacer></v-spacer>
      <v-tooltip bottom color="primary">
        <template v-slot:activator="{ on, attrs }">
          <v-btn icon color="white" v-bind="attrs" v-on="on" link to="/home">
            <v-icon>mdi-step-backward</v-icon>
          </v-btn>
        </template>
        <span>go Back</span>
      </v-tooltip>
      <v-menu dense flat offset-y>
        <template v-slot:activator="{ on, attrs }">
          <v-btn plain color="white" dark v-bind="attrs" v-on="on">
            <span color="white"> Student</span>
            <v-icon right color="grey"> mdi-menu-down </v-icon>
          </v-btn>
        </template>
        <v-list dense>
          <v-list-item
            v-for="(item, index) in items"
            :key="index"
            router
            :to="item.route"
            link
          >
            <v-list-item-icon>
              <v-icon left>{{ item.icon }}</v-icon>
            </v-list-item-icon>

            <v-list-item-title>{{ item.title }}</v-list-item-title>
          </v-list-item>
        </v-list>
      </v-menu>
    </v-app-bar>
    <SideBar :mini="mini" />
  </v-container>
</template>

<script>
import SideBar from "../../../Students/Students_Shared/Student_Navigation/SideBar.vue";

export default {
  components: { SideBar },
  data() {
    return {
      mini: true,
      fav: true,
      menu: false,
      message: false,
      hints: true,
      items: [
        { icon: "mdi-help-circle", title: "Help", route: "" },
        { icon: "mdi-help-circle", title: "Help", route: "" },
        { icon: "mdi-power", title: "Logout", route: "/login" },
      ],
    };
  },
};
</script>
<style>
v-btn:hover:before {
  background-color: transparent;
}
.no-uppercase {
  text-transform: unset !important;
}
</style>
