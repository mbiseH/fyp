<template>
  <div>
    <!-- <v-alert
      v-for="err of errors"
      :key="err.code"
      border="bottom"
      color="red"
      dismissible
      elevation="21"
      icon="mdi-alert-circle"
      type="error"
    >
      {{ err.message }}
    </v-alert> -->
    <Login_Page @login-handler="loginHandler" />
  </div>
</template>

<script>
import Login_Page from "./LoginContent.vue";

// creating mutation here
import gql from "graphql-tag";
import router from "../../router";

const LOGIN_QUERY = gql`
  mutation ($email: String!, $password: String!) {
    tokenAuth(email: $email, password: $password) {
      token
      success
      errors
    }
  }
`;

export default {
  name: "Login",
  components: {
    Login_Page,
  },
  data() {
    return {
      errors: [],
    };
  },
  methods: {
    loginHandler(data) {
      this.$apollo.mutate({
        mutation: LOGIN_QUERY,
        variables: data,
        update: (cache, { data }) => {
          console.log(data);
          if (!data.tokenAuth.errors) {
            localStorage.setItem("token", data.tokenAuth.token);
            const Toast = this.$swal.mixin({
              toast: true,
              position: "top-end",
              showConfirmButton: false,
              timer: 3000,
              timerProgressBar: true,
              didOpen: (toast) => {
                toast.addEventListener("mouseenter", this.$swal.stopTimer);
                toast.addEventListener("mouseleave", this.$swal.resumeTimer);
              },
            });

            Toast.fire({
              icon: "success",
              title: "Signed in successfully",
            });
            router.push("/home");
          } else {
            let errors = [];
            for (let e of data.tokenAuth.errors.nonFieldErrors) {
              errors.push(e);
            }
            this.errors = errors;
            const Toast = this.$swal.mixin({
              toast: true,
              position: "top-end",
              showConfirmButton: false,
              timer: 3000,
              timerProgressBar: true,
              didOpen: (toast) => {
                toast.addEventListener("mouseenter", this.$swal.stopTimer);
                toast.addEventListener("mouseleave", this.$swal.resumeTimer);
              },
            });

            Toast.fire({
              icon: "warning",
              title: "Credential didn't match!",
            });
          }
        },
      });
    },
  },
};
</script>
<style scoped>
.no-uppercase {
  text-transform: unset !important;
}
</style>
