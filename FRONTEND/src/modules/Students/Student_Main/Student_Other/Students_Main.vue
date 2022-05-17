<template>
  <v-container fluid>
    <ToolBar />
    <router-view />
  </v-container>
</template>

<script>
import ToolBar from "../../../Students/Students_Shared/Student_Navigation/ToolBar.vue";
export default {
  components: {
    ToolBar,
  },
};
</script>
