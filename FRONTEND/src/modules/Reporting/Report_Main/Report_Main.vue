<template>
  <v-container fluid>
    <ToolBar />
    <router-view />
  </v-container>
</template>

<script>
import ToolBar from "../Shared_Report/Navigation/ToolBar.vue";
export default {
  components: {
    ToolBar,
  },
};
</script>

<style></style>
