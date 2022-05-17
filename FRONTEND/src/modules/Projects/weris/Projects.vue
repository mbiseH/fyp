<template>
  <div class="dashboard">
    <v-container fluid>
      <v-row>
        <v-flex xs12 md6>
          <div>
            <!-- <h1 class="subheading grey--text">Dashboard</h1> -->
          </div>
        </v-flex>
        <v-spacer></v-spacer>
        <v-tooltip top>
          <template v-slot:activator="{ on, attrs }">
            <CreateNewProjects v-bind="attrs" v-on="on"> </CreateNewProjects>
          </template>
          <span>Create New Project</span>
        </v-tooltip>
      </v-row>
      <br />
      <v-card outline class="pa-3">
        <v-layout row class="mb-5">
          <v-tooltip top color="primary">
            <template v-slot:activator="{ on, attrs }">
              <v-btn
                small
                flat
                @click="sortBy('title')"
                v-bind="attrs"
                v-on="on"
              >
                <v-icon fab left small>mdi-folder</v-icon>
                <span class="caption text-lowercase">By project name</span>
              </v-btn>
            </template>
            <span>Sort projects by project names</span>
          </v-tooltip>
          <v-tooltip top color="primary">
            <template v-slot:activator="{ on, attrs }">
              <v-btn
                small
                flat
                @click="sortBy('person')"
                v-bind="attrs"
                v-on="on"
              >
                <v-icon left small>mdi-account</v-icon>
                <span class="caption text-lowercase">Assigned to</span>
              </v-btn>
            </template>
            <span>Sort projects by people</span>
          </v-tooltip>
        </v-layout>
        <v-card
          flat
          class="pa-3"
          v-for="project in projects"
          :key="project.title"
        >
          <v-layout row wrap :class="`pa-3 project ${project.status}`">
            <v-flex xs6 sm4 md6>
              <div class="caption grey--text">Project Title</div>
              <div>
                <v-chip filter pill outlined link to="/more_about_project">
                  {{ project.title }}</v-chip
                >
              </div>
            </v-flex>
            <v-flex xs6 sm4 md2>
              <div class="caption grey--text">Reported By</div>
              <div>{{ project.person }}</div>
            </v-flex>
            <v-flex xs6 sm4 md2>
              <div class="caption grey--text">Due by</div>
              <div>{{ project.due }}</div>
            </v-flex>
            <v-flex xs2 sm4 md2>
              <div class="caption grey--text">Actions</div>
              <div>
                <v-menu
                  dense
                  flat
                  offset-x
                  v-model="menu"
                  :close-on-content-click="false"
                >
                  <template v-slot:activator="{ on, attrs }">
                    <v-btn
                      color="primary"
                      icon
                      v-bind="attrs"
                      v-on="on"
                      right
                      :nudge-width="200"
                    >
                      <v-icon>mdi-dots-vertical</v-icon>
                    </v-btn>
                  </template>

                  <v-list dense>
                    <v-list-item
                      v-for="(item, i) in items"
                      :key="i"
                      router
                      :to="item.route"
                      link
                    >
                      <v-list-item-icon>
                        <v-icon color="" left>{{ item.icon }} </v-icon>
                      </v-list-item-icon>
                      <v-list-item-title>{{ item.title }}</v-list-item-title>
                    </v-list-item>
                  </v-list>
                </v-menu>
              </div>
            </v-flex>
            <v-flex xs2 sm4 md2>
              <div class="caption grey--text">Status</div>
              <div>
                <v-chip
                  id="chip"
                  small
                  :class="`${project.status} white--text caption my-2`"
                  >{{ project.status }}</v-chip
                >
              </div>
            </v-flex>
          </v-layout>
          <v-divider></v-divider>
        </v-card>
      </v-card>
    </v-container>
  </div>
</template>

<script>
import CreateNewProjects from "../../Projects/weris_projects/CreateNewProject.vue";

export default {
  data() {
    return {
      projects: [
        {
          title: "e-mrejesho",
          person: "Edwin Pantaleo",
          due: "1st Jan 2019",
          status: "ongoing",
          Actions: "eee",
        },
        {
          title: "e-mikutano",
          person: "Yona Godwin",
          due: "1st Jan 2019",
          status: "complete",
        },
        {
          title: "a-project",
          person: "Ethan Kitila",
          due: "1st Jan 2019",
          status: "overdue",
        },
        {
          title: "e-mrejesho",
          person: "Edwin Pantaleo",
          due: "1st Jan 2019",
          status: "ongoing",
        },
        {
          title: "e-mikutano",
          person: "Yona Godwin",
          due: "1st Jan 2019",
          status: "complete",
        },
        {
          title: "a-project",
          person: "Ethan Kitila",
          due: "1st Jan 2019",
          status: "overdue",
        },
        {
          title: "e-mikutano",
          person: "Yona Godwin",
          due: "1st Jan 2019",
          status: "complete",
        },
        {
          title: "a-project",
          person: "Ethan Kitila",
          due: "1st Jan 2019",
          status: "overdue",
        },
      ],
      items: [
        {
          icon: "mdi-arrow-u-right-top-bold",
          title: "Reporting",
          route: "/reporting_page",
        },
        { icon: "mdi-eye", title: "View Details", route: "/more_about_status" },
      ],
    };
  },
  methods: {
    sortBy(prop) {
      this.projects.sort((a, b) => (a[prop] < b[prop] ? -1 : 1));
    },
  },
  components: { CreateNewProjects },
};
</script>

<style>
.project.complete {
  border-left: 4px solid #3cd1c2;
}
.project.ongoing {
  border-left: 4px solid orange;
}
.project.overdue {
  border-left: 4px solid tomato;
}
#chip.v-chip.complete {
  background: #3cd1c2;
}
#chip.v-chip.ongoing {
  background: #ffaa2c;
}
#chip.v-chip.overdue {
  background: #f83e70;
}
</style>
