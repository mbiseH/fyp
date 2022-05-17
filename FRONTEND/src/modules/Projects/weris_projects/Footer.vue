<template>
  <div class="Footer">
    <v-footer padless background-color="primary">
      <v-col class="text-center primary dense" color="primary" cols="12">
        {{ new Date().getFullYear() }} — CIVE - All right reserved
      </v-col>
    </v-footer>
  </div>
</template>
<script>
export default {};
</script>

<style>
.Footer {
  text-align: center;
  text-emphasis-color: white;
}
</style>
