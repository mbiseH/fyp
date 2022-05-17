<template>
  <v-app>
    <!-- <LandingPageToolBar/> -->
    <v-app-bar app>
      <span style="color: #00baff; font-size: 20px; font-weight: bold"
        >Reporting Pages</span
      >
    </v-app-bar>
    <v-main>
      <form>
        <v-card fluid>
          <v-row>
            <v-col cols="12" sm="6" small outline center>
              <Workdone_Input @message="addTodo" />
              <v-list class="todo_list">
                <Workdone_Todo
                  v-for="(todo, index) in list"
                  @delete="deleteTodo"
                  @done="doneTodo"
                  :title="todo.message"
                  :id="todo.id"
                  :done="todo.done"
                  :key="index"
                ></Workdone_Todo>
              </v-list>
            </v-col>

            <v-col cols="12" sm="6">
              <Current_Activity_Input @message="addTodo_one" />
              <v-list class="todo_list">
                <Current_Activity_Todo
                  v-for="(todo1, index) in list1"
                  @delete="deleteTodo_one"
                  @done="doneTodo_one"
                  :title="todo1.message1"
                  :id="todo1.id"
                  :done="todo1.done"
                  :key="index"
                ></Current_Activity_Todo>
              </v-list>
            </v-col>

            <v-col cols="12" sm="6" icon>
              <Blocking_Issues_Input @message="addTodo_two" />
              <v-list class="todo_list">
                <Blocking_Issues_Todo
                  v-for="(todo, index) in list"
                  @delete="deleteTodo_two"
                  @done="doneTodo_two"
                  :title="todo2.message"
                  :id="todo2.id"
                  :done="todo2.done"
                  :key="index"
                ></Blocking_Issues_Todo>
              </v-list>
            </v-col>
            <v-col cols="12" sm="6" icon>
              <Way_Forward_Input @sendMessagemessage="addTodo" />
              <v-list class="todo_list">
                <Way_Forward_Todo
                  v-for="(todo, index) in list"
                  @delete="deleteTodo"
                  @done="doneTodo"
                  :title="todo.message"
                  :id="todo.id"
                  :done="todo.done"
                  :key="index"
                ></Way_Forward_Todo>
              </v-list>
            </v-col>
            <br />
            <v-col cols="12" sm="6" icon>
              <v-combobox
                small
                v-model="status"
                :items="items1"
                chips
                clearable
                label="Project Status"
                multiple
                prepend-icon="mdi-star-crescent"
                solo
              >
                <template v-slot:selection="{ attrs, item, select, selected }">
                  <v-chip
                    v-bind="attrs"
                    :input-value="selected"
                    close
                    @click="select"
                    @click:close="remove1(item)"
                  >
                    <strong>{{ item }}</strong
                    >&nbsp;
                  </v-chip>
                </template>
              </v-combobox>
            </v-col>
            <v-col cols="11" sm="6" icon>
              <center>
                <br />
                <v-btn
                  color="#00BAFF"
                  link
                  to="/projecti/projects"
                  class="no-uppercase"
                >
                  <span style="color: white">submit</span>
                </v-btn>
              </center>
            </v-col>
          </v-row>
        </v-card>
      </form>
    </v-main>
  </v-app>
</template>

<script>
// import LandingPageToolBar from '../../../modules/Reporting/Shared_Report/Navigation/ToolBar.vue'
import Workdone_Todo from "../Report_Main/Workdone_Activity/Workdone_Todo.vue";
import Workdone_Input from "../Report_Main/Workdone_Activity/Workdone_Input.vue";
import Current_Activity_Input from "../Report_Main/Current_Activity/Current_Activity_Input.vue";
import Current_Activity_Todo from "../Report_Main/Current_Activity/Current_Activity_Todo.vue";
import Blocking_Issues_Input from "../Report_Main/Blocking_Issues/Blocking_Issues_Input.vue";
import Blocking_Issues_Todo from "../Report_Main/Blocking_Issues/Blocking_Issues_Todo.vue";
import Way_Forward_Todo from "../Report_Main/Way_Forward/Way_Forward_Todo.vue";
import Way_Forward_Input from "../Report_Main/Way_Forward/Way_Forward_Input.vue";
export default {
  components: {
    //  LandingPageToolBar,
    Workdone_Input,
    Workdone_Todo,
    Current_Activity_Input,
    Current_Activity_Todo,
    Blocking_Issues_Input,
    Blocking_Issues_Todo,
    Way_Forward_Todo,
    Way_Forward_Input,
  },
  data: () => ({
    items1: ["Ongoing", "Completed", "On production"],
    list: [],
    list1: [],
    list2: [],
  }),
  mounted() {
    const list = JSON.parse(localStorage.getItem("list"));

    this.list = list || [];
  },
  methods: {
    addTodo(message) {
      const todoObj = {
        id: Math.random(),
        message,
        done: false,
      };
      this.list.push(todoObj);
    },
    addTodo_one(message1) {
      const todoObj_one = {
        id: Math.random(),
        message1,
        done: false,
      };
      this.list1.push(todoObj_one);
    },
    addTodo_two(message2) {
      const todoObj_two = {
        id: Math.random(),
        message2,
        done: false,
      };
      this.list2.push(todoObj_two);
    },
    doneTodo(id) {
      const todoIndex = this.list.findIndex((todo) => todo.id === id);
      const doneProp = this.list[todoIndex].done;
      this.$set(this.list[todoIndex], "done", !doneProp);
    },
    doneTodo_one(id) {
      const todoIndex1 = this.list1.findIndex((todo1) => todo1.id === id);
      const doneProp1 = this.list1[todoIndex1].done;
      this.$set(this.list1[todoIndex1], "done", !doneProp1);
    },
    doneTodo_two(id) {
      const todoIndex2 = this.list2.findIndex((todo2) => todo2.id === id);
      const doneProp2 = this.list2[todoIndex2].done;
      this.$set(this.list2[todoIndex2], "done", !doneProp2);
    },
    deleteTodo_one(id) {
      const todoIndex1 = this.list1.findIndex((todo1) => todo1.id === id);
      this.list1.splice(todoIndex1, 1);
      this.setLs();
    },
    deleteTodo_two(id) {
      const todoIndex2 = this.list2.findIndex((todo2) => todo2.id === id);
      this.list2.splice(todoIndex2, 1);
      this.setLs();
    },
    deleteTodo(id) {
      const todoIndex = this.list.findIndex((todo) => todo.id === id);
      this.list.splice(todoIndex, 1);
      this.setLs();
    },
    setLs() {
      const jsonList = JSON.stringify(this.list);
      localStorage.setItem("list", jsonList);
    },
  },
};
</script>

<style>
.no-uppercase {
  text-transform: unset !important;
}
</style>
