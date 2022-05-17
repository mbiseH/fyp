<template>
  <v-container fluid>
    <ToolBar />
    <router-view />
  </v-container>
</template>

<script>
import ToolBar from "../weris_shared/navigations/ToolBar.vue";

export default {
  components: {
    ToolBar,
  },
};
</script>
