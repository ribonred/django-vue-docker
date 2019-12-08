import Vue from "vue";
import App from "./App.vue";
import vuetify from "./plugins/vuetify";
import VueRouter from "vue-router";
import Pelanggan from "./components/pelanggan.vue";
import order from "./components/order.vue";
import table from "./components/datauser.vue";

Vue.use(VueRouter);

Vue.config.productionTip = false;
const routes = [
  { path: "/" },
  { path: "/pelanggan", component: Pelanggan },
  { path: "/order", component: order },
  { path: "/table", component: table }
];
const router = new VueRouter({ routes });
new Vue({
  router,
  vuetify,
  render: h => h(App)
}).$mount("#app");
