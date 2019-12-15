<template>
  <v-form ref="form" @submit.prevent="add">
    <v-alert type="success" dismissible="true" v-if="notif">
      {{ notif }}
    </v-alert>
    <v-text-field
      v-model="form.berat"
      label="Berat"
      required
      type="number"
    ></v-text-field>

    <v-text-field
      v-model="form.tambahan"
      label="Tambahan"
      required
      type="number"
    ></v-text-field>
    <v-text-field
      v-model="form.harga"
      label="Harga"
      required
      type="number"
    ></v-text-field>
    <!-- <v-text-field
      v-model="form.pelanggan"
      label="pelanggan"
      required
      type = 'number'
    ></v-text-field> -->
    <v-select
      v-model="form.pelanggan"
      :items="datas"
      item-text="nama"
      item-value="id"
      :rules="[v => !!v || 'Item is required']"
      label="PELANGGAN"
      required
    ></v-select>
    <v-card-actions>
      <v-btn color="success" class="mr-4" type="submit">
        submit
      </v-btn>

      <v-btn color="error" class="mr-4" @click="reset">
        Reset Form
      </v-btn>
    </v-card-actions>
  </v-form>
</template>
<script>
import axios from "axios";
import Vue from "vue";
import CxltToastr from "cxlt-vue2-toastr";
import "cxlt-vue2-toastr/dist/css/cxlt-vue2-toastr.css";

var toastrConfigs = {
  position: "top full width",
  showDuration: 1000,
  hideDuration: 6000,
  timeout: 2000,
  showMethod: "bounceInRight",
  hideMethod: "bounceOutLeft"
};
Vue.use(CxltToastr, toastrConfigs);
const url = "http://127.0.0.1:8000/pelanggan/";
const orderurl = "http://127.0.0.1:8000/orders/";
export default {
  data() {
    return {
      form: {
        id: "",
        berat: "",
        tambahan: "",
        harga: "",
        pelanggan: ""
      },
      datas: [],
      pelanggan: null,
      notif: null
    };
  },
  mounted() {
    this.load();
  },
  methods: {
    load() {
      axios.get(url).then(res => {
        this.datas = res.data;
      });
    },
    validate() {
      if (this.$refs.form.validate()) {
        this.snackbar = true;
      }
    },
    reset() {
      this.$refs.form.reset();
    },
    add() {
      axios
        .post(orderurl, {
          pelanggan: this.form.pelanggan,
          tambahan: this.form.tambahan,
          berat: this.form.berat,
          harga: this.form.harga
        })
        .then(res => {
          this.load();
          this.datas = res.data;
          this.form.pelanggan = "";
          this.form.tambahan = "";
          this.form.berat = "";
          this.form.harga = "";
          this.$toast.success({
            title: "Success",
            message: "Order di tambahkan"
          });
        });
    }
  }
};
</script>

<style lang="scss" scoped></style>
