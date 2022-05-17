<template>
  <v-list-item class="todo">
    <!-- <v-checkbox @click="$emit('done',id)" v-model="doneData"></v-checkbox> -->
    <div :class="{ 'todo__title--done': doneData2 }" class="todo_title">
      {{ title }}
    </div>
    <v-spacer></v-spacer>
    <v-btn
      color="error"
      @click="$emit('delete', id)"
      class="todo_action"
      icon
      small
    >
      <v-icon small>mdi-trash-can</v-icon>
    </v-btn>
  </v-list-item>
</template>

<script>
export default {
  name: "Todo",
  props: {
    title: {
      type: String,
      required: true,
    },
    id: {
      type: Number,
      require: true,
    },
    done: {
      type: Boolean,
      default: false,
    },
    data: () => ({
      doneData2: false,
    }),
    mounted() {
      this.doneData2 = this.done;
    },
    computed: {
      controllDone: {
        get() {
          return this.doneData2;
        },
        set(value) {
          this.doneData2 = value;
        },
      },
    },
  },
};
</script>

<style lang="scss">
.todo {
  display: flex;
  justify-content: space-between;
  &__title--done {
    text-decoration: line-through;
  }
}
</style>
