<template>
  <v-container fluid>
    <ToolBar />
    <router-view />
  </v-container>
</template>

<script>
import ToolBar from "../Complains_Shared/ToolBar.vue";
export default {
  components: {
    ToolBar,
  },
};
</script>
