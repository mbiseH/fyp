<template>
  <v-app>
    <v-main class="mx-4 mb-4">
      <router-view />
    </v-main>
  </v-app>
</template>

<script>
export default {
  components: {},
};
</script>
<style lang="css">
main {
  background-image: url("./assets/images/background.png");
  background-size: cover;
}
</style>
