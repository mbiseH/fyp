<template>
  <v-container fluid>
    <ToolBar />
    <router-view />
  </v-container>
</template>

<script>
import ToolBar from "./Shared_Users/Navigation/ToolBar.vue";
export default {
  components: {
    ToolBar,
  },
};
</script>
