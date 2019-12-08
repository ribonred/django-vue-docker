<template>
<v-container>
  <v-row justify="center">
    <v-col cols="12" sm="10" md="8" lg="6">
      <v-card ref="form">
        <form @submit.prevent="add">  
        <v-card-text>
          <v-text-field
            v-model="form.nama"
            label="Nama"
            placeholder="input nama"
            required
          ></v-text-field>
          <v-text-field
            v-model="form.alamat"
            label="Alamat"
            placeholder="input alamat"
            counter="25"
            required
          ></v-text-field> 
        </v-card-text>
        
        <v-divider class="mt-12"></v-divider>
        <v-card-actions>
          <v-btn text>Cancel</v-btn>
          <v-spacer></v-spacer>
          <v-btn color="primary" text v-show="!updateSubmit" type="submit">Tambah</v-btn>
          <v-btn color="primary" text v-show="updateSubmit" type="button"  @click="update(form)">Update</v-btn>
        </v-card-actions>
        </form>
       <v-sheet class="text-center">PELANGGAN</v-sheet>
    <v-simple-table>
    <template v-slot:default>
      <thead>
        <tr>
          <th class="text-left">ID</th>
          <th class="text-left">Nama</th>
          <th class="text-left">Alamat</th>
          <th class="text-left">Edit</th>
          <th class="text-left">Delete</th>
        </tr>
      </thead>
      <tbody>
        
        <tr v-for="a in pelanggan" :key="a.id">
          <td>{{ a.id }}</td>
          <td>{{ a.nama }}</td>
          <td>{{ a.alamat }}</td>
          <td><v-btn color="primary" text @click="edit(a)">Edit</v-btn></td>
          <td><v-btn color="warning" text @click="del(a)">delete</v-btn></td>
        </tr>

      </tbody>
    </template>
  </v-simple-table>     
      </v-card>
    </v-col>
  </v-row>

</v-container>
</template>

<script>
import axios from "axios";
const url = "http://127.0.0.1:8000/pelanggan/";
export default {
  data() {
    return {
      form: {
        id: "",
        nama: "",
        alamat: ""
      },
      pelanggan: "",
      updateSubmit: false
    };
  },
  mounted() {
    this.load();
  },
  methods: {
    load() {
      axios.get(url).then(res => {
        this.pelanggan = res.data;
      });
    },
    add() {
      axios
        .post(url, {
          nama: this.form.nama,
          alamat: this.form.alamat
        })
        .then(res => {
          this.load();
          this.pelanggan = res.data;
          this.form.nama = "";
          this.form.alamat = "";
        });
    },
    del(a) {
      axios.delete(url + a.id).then(res => {
        this.load();
        let index = this.pelanggan.indexOf(this.form.nama);
        this.pelanggan.splice(index, 1);
        this.pelanggan = res.data;
      });
    },
    edit(a) {
      this.updateSubmit = true;
      this.form.id = a.id;
      this.form.nama = a.nama;
      this.form.alamat = a.alamat;
    },
    update(form) {
      return axios
        .put(url + form.id + "/", {
          nama: this.form.nama,
          alamat: this.form.alamat
        })
        .then(res => {
          this.load();
          this.pelanggan = res.data;
          this.form.id = "";
          this.form.nama = "";
          this.form.alamat = "";
          this.updateSubmit = false;
        });
    }
  }
};
</script>

<style>
</style>