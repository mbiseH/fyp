<template>
  <v-app id="inspire">
    <v-content>
      <v-container class="fill-height" fluid>
        <v-row align="center" justify="center">
          <v-col cols="12" sm="8" md="8">
            <v-card class="elevation-12">
              <v-window v-model="step">
                <v-window-item :value="1">
                  <v-row>
                    <v-col cols="12" md="8">
                      <v-card-text class="mt-12">
                        <h1 class="text-center display-2 primary--text">
                          Sign in
                        </h1>
                        <h4 class="text-center mt-4">
                          Ensure input username and password is correct
                        </h4>
                        <v-form ref="form" v-model="valid" lazy-validation>
                          <v-text-field
                            v-model="email"
                            :rules="usernameRules"
                            label="Username"
                            prepend-icon="mdi-account"
                            color="primary--text"
                            required
                          />

                          <v-text-field
                            v-model="password"
                            :rules="passwordRules"
                            label="Password"
                            type="password"
                            prepend-icon="mdi-lock"
                            color="primary--text"
                            required
                          />
                          <div class="text-center mt-3">
                            <v-btn
                              rounded
                              color="primary accent-3"
                              dark
                              @click="handleLogin"
                              class="no-uppercase"
                              ><span>login</span></v-btn
                            >
                          </div>
                        </v-form>
                      </v-card-text>
                      <div class="text-center mt-3">
                        <h4 class="text-center mt-4">
                          <a @click="step++" style="text-decoration: none"
                            >Forgot your password ?</a
                          >
                        </h4>
                      </div>
                    </v-col>
                    <v-col cols="12" md="4" class="primary">
                      <v-card-text class="white--text mt-12">
                        <h1 class="text-center display-1">Hello, Friend!</h1>
                        <h5 class="text-center">Recover your password here</h5>
                      </v-card-text>
                      <div class="text-center">
                        <v-btn
                          rounded
                          outlined
                          dark
                          @click="step++"
                          class="no-uppercase"
                          >Recover</v-btn
                        >
                      </div>
                    </v-col>
                  </v-row>
                </v-window-item>
                <v-window-item :value="2">
                  <v-row class="fill-height">
                    <v-col cols="12" md="4" class="primary">
                      <v-card-text class="white--text mt-12">
                        <h1 class="text-center display-1">Welcome Back!</h1>
                        <h5 class="text-center">
                          To Keep connected with us please login with your
                          personnel info
                        </h5>
                      </v-card-text>
                      <div class="text-center">
                        <v-btn
                          class="no-uppercase"
                          rounded
                          outlined
                          dark
                          @click="step--"
                          >Sign in</v-btn
                        >
                      </div>
                    </v-col>

                    <v-col cols="12" md="8">
                      <v-card-text class="mt-12">
                        <h1
                          class="text-center display-2 primary--text text--accent-3"
                        >
                          Recover Your Password
                        </h1>
                        <h4 class="text-center mt-4">
                          Ensure your email for Recover
                        </h4>

                        <v-form>
                          <v-text-field
                            v-model="text"
                            label="Email"
                            prepend-icon="mdi-lock"
                            color="primary--text"
                            :rules="['Required']"
                          />
                        </v-form>

                        <br /><br />
                        <div class="text-center mt-n5">
                          <v-btn
                            class="no-uppercase"
                            rounded
                            color="primary accent-3"
                            dark
                            @click="handleSubmitEmail"
                            >Submit</v-btn
                          >
                        </div>
                      </v-card-text>
                    </v-col>
                  </v-row>
                </v-window-item>
              </v-window>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
export default {
  data: () => ({
    step: 1,
    valid: false,
    username: "",
    usernameRules: [
      (v) => !!v || "User name is required",
      (v) => (v && v.length <= 10) || "Name must be less than 10 characters",
    ],
    password: "",
    passwordRules: [
      (v) => !!v || "Password is required",
      (v) =>
        /(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{6,}/.test(v) ||
        "Password must contain at least lowercase letter, one number, a special character and one uppercase letter",
    ],
    email: "",
    emailRules: [
      (v) => !!v || "E-mail is required",
      (v) => /.+@.+\..+/.test(v) || "E-mail must be valid",
    ],
  }),

  props: {
    source: String,
  },
  methods: {
    handleLogin(e) {
      e.preventDefault(e);
      let data = {
        email: this.email,
        password: this.password,
      };
      // console.log(data);
      this.$emit("login-handler", data);
    },
    handleSubmitEmail(e) {
      e.preventDefault();
      this.$refs.form.validate();
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
        title: "credential didn't match!",
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
