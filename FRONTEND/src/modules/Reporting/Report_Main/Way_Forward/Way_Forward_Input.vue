<template>
  <v-text-field
    class="input"
    placeholder="Way Forward"
    outline
    solo
    append-icon="mdi-plus-circle-outline"
    multiple
    prepend-icon="mdi-forwardburger"
    @keydown.enter="sendMessage"
    @click:append="sendMessage"
    v-model="message"
    small
    required
  >
  </v-text-field>
</template>

<script>
export default {
  name: "Input",
  data: () => ({
    message: "",
  }),
  methods: {
    sendMessage() {
      if (this.message === "") this.message = "Todo item ";
      this.$emit("message", this.message);
      console.log(this.message);
      this.message = "";
    },
  },
};
</script>

<style>
.input {
  width: 100%;
}
</style>
