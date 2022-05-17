<template>
  <v-text-field
    class="input"
    placeholder=" Currently Activity"
    outline
    solo
    append-icon="mdi-plus-circle-outline"
    multiple
    prepend-icon="mdi-curling"
    @keydown.enter="sendMessage1"
    @click:append="sendMessage1"
    v-model="message1"
    required
  >
  </v-text-field>
</template>

<script>
export default {
  name: "Input",
  data: () => ({
    message1: "",
  }),
  methods: {
    sendMessage1() {
      if (this.message1 === "") this.message1 = "Currently Activity ";
      this.$emit("message", this.message1);
      console.log(this.message1);
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
