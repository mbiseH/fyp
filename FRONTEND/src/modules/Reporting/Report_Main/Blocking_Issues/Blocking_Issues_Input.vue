<template>
  <v-text-field
    class="input"
    placeholder="Blocking Issues"
    outline
    solo
    append-icon="mdi-plus-circle-outline"
    multiple
    prepend-icon="mdi-link-lock"
    @keydown.enter="sendMessage2"
    @click:append="sendMessage2"
    v-model="message2"
  >
  </v-text-field>
</template>

<script>
export default {
  name: "Input",
  data: () => ({
    message2: "",
  }),
  methods: {
    sendMessage2() {
      if (this.message2 === "") this.message2 = "Blocking Issues";
      this.$emit("message", this.message);
      console.log(this.message2);
      this.message2 = "";
    },
  },
};
</script>

<style>
.input {
  width: 100%;
}
</style>
