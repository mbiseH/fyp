import Vue from "vue";
import VueRouter from "vue-router";
import Projects from "../modules/Projects/weris/Projects.vue";
import DashBoard from "../modules/Projects/weris/DashBoard.vue";
import Teams from "../modules/Projects/weris/Teams.vue";
import Home from "../modules/Projects/weris_projects/Home.vue";
import Create_User from "../modules/Users/create_weris_user/Create_User.vue";
import MainProject from "../modules/Projects/weris/MainProject.vue";
import Login_Page from "../modules/Authentication/Login.vue";
import ReportingPage from "../modules/Reporting/Report_Main/Report_Main.vue";
import My_Action from "../modules/Reporting/Report_Main/My_Action.vue";
import More_Status from "../modules/Projects/weris/More_about_project_status.vue";
import More_Project from "../modules/Projects/weris/More_About_Project.vue";
// import Reporting_Page from "../modules/Reporting/Report_Main/Reporting_Page.vue";
import Admin_Page from "../modules/Users/Main_Users.vue";
import New_Appointment from "../modules/Projects/weris/NewAppointment.vue";
import Previous_Appointment from "../modules/Projects/weris/Previous_Appointment.vue";
import Capture_fingerprint from "../modules/Users/Capture_fingerprint";
import Make_Appointment from "../modules/Projects/weris/MakeAppointment.vue";
import Complains from "../modules/Complains/Complains_Main/Complains_Main";
import Complains_Complains from "../modules/Students/Student_Main/Student_Other/Students_Complains/Complains_complains.vue";
import Complains_Dashboard from "../modules/Complains/Complains_Main/other_complains/Complains_Dashboard.vue";
import Reporting_Dashboard from "../modules/Reporting/Report_Main/Other_Report/Report_Dashboard.vue";
import Student from "../modules/Students/Student_Main/Student_Other/Students_Main.vue";
import Request_Appointment from "../modules/Students/Student_Main/Student_Other/Request_Appointment.vue";
import Landing from "../modules/Landing/Landing_Main/Landing_Main.vue";
import Track_Complains from "../modules/Students/Student_Main/Student_Other/Track_Complains/Track_Complains.vue";
// import Forgot_Password from "../modules/Authentication/Forgot_password.vue"
Vue.use(VueRouter);

const routes = [
  // route for redirect landing page
  {
    path: "/",
    name: "Landing",
    component: Landing,
  },
  // route for landing page
  {
    path: "/landing",
    name: "Landing",
    component: Landing,
  },
  // route for forgot password
  // {
  //   path: "/forgot_password",
  //   name: "Forgot_Password",
  //   component: Forgot_Password,
  // },
  // route for staff
  {
    path: "/projecti",
    name: "MainProject",
    component: MainProject,
    children: [
      {
        path: "projects",
        name: "Projects",
        component: Projects,
      },
      {
        path: "dashboard",
        name: "Dashboard",
        component: DashBoard,
      },
      {
        path: "new_appointment",
        name: "New_Appointment",
        component: New_Appointment,
      },
      {
        path: "teams",
        name: "Teams",
        component: Teams,
      },
      {
        path: "previous_appointment",
        name: "Previous_Appointment",
        component: Previous_Appointment,
      },
      {
        path: "make_appointment",
        name: "Make_Appointment",
        component: Make_Appointment,
      },
    ],
  },

  // route for admin
  {
    path: "/admin_page",
    name: "Admin_Page",
    component: Admin_Page,
    children: [
      {
        path: "create_users",
        name: "Create_User",
        component: Create_User,
      },
      {
        path: "capture_fingerprint",
        name: "Capture_fingerprint",
        component: Capture_fingerprint,
      },
    ],
  },

  {
    path: "/home",
    name: "Home",
    component: Home,
  },
  // route for complains
  {
    path: "/complains",
    name: "Complains",
    component: Complains,
    children: [
      {
        path: "complains_complains",
        name: "complains_Complains",
        component: Complains_Complains,
      },
      {
        path: "complains_dashboard",
        name: "complains_dashboard",
        component: Complains_Dashboard,
      },
    ],
  },
  // route for login page
  {
    path: "/login",
    name: "Login_Page",
    component: Login_Page,
  },
  // route for reporting
  {
    path: "/reporting",
    name: "ReportingPage",
    component: ReportingPage,
    children: [
      {
        path: "reporting_dashboard",
        name: "Reporting_Dashboard",
        component: Reporting_Dashboard,
      },
    ],
  },
  // route for students
  {
    path: "/students",
    name: "Student",
    component: Student,
    children: [
      {
        path: "request_appointment",
        name: "Request_Appointment",
        component: Request_Appointment,
      },
      {
        path: "complains_complains",
        name: "complains_Complains",
        component: Complains_Complains,
      },
      {
        path: "track_complains",
        name: "Track_Complains",
        component: Track_Complains,
      },
    ],
  },
  //  route for my action
  {
    path: "/my_action",
    name: "My_Action",
    component: My_Action,
  },
  //  route for more about about project status
  {
    path: "/more_about_status",
    name: "More_Status",
    component: More_Status,
  },
  //  more about project implementation
  {
    path: "/more_about_project",
    name: "More_Project",
    component: More_Project,
  },

  //  more about project implementation
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
