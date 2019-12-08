<template>
  <v-table :data="users" class="tabs">
    <thead slot="head" id="ndas">
      <th id="ndas">Nama</th>
      <th id="ndas">Berat</th>
      <th id="ndas">Harga</th>
      <th id="ndas">tambahan</th>
      <th id="ndas">Total</th>
      <th id="ndas">Tanggal Order</th>
    </thead>
    <tbody slot="body" slot-scope="{ displayData }">
      <tr v-for="row in displayData" :key="row.id">
        <td id="ndas">{{ row.nama_pelanggan }}</td>
        <td id="ndas">{{ row.berat }}</td>
        <td id="ndas">{{ row.harga }}</td>
        <td id="ndas">{{ row.tambahan }}</td>
        <td id="ndas">{{ row.Total }}</td>
        <td id="ndas">{{ row.created }}</td>
      </tr>
    </tbody>
  </v-table>
</template>

<script>
import SmartTable from "vuejs-smart-table";
import Vue from "vue";
import axios from "axios";
Vue.use(SmartTable);
const url = "http://127.0.0.1:8000/orders/?format=json";
export default {
  data() {
    return {
      users: []
    };
  },
  mounted() {
    this.load();
  },
  methods: {
    load() {
      axios.get(url).then(res => {
        this.users = res.data;
      });
    }
  }
};
</script>

<style lang="scss" scoped>
.tabs {
  width: 100%;
}
#ndas {
  width: 150px;
  text-align: center;
}
</style>
