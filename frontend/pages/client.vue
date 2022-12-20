<template>
    <v-card>
      <v-card-title>
        Client List <v-btn icon @click="dialog = true"><v-icon>mdi-plus</v-icon></v-btn></v-card-title
      >
      <v-data-table :headers="headers" :items="clients">
        <template v-slot:item.active="{ item }">
          <v-btn icon @click="deleteClient(item.id)"><v-icon>mdi-delete</v-icon></v-btn>
        </template>
      </v-data-table>
      <v-dialog v-model="dialog">
        <client-form
          @save="
            dialog = false
            getClient()
          "
        />
      </v-dialog>
    </v-card>
  </template>
  
  <script>
  import ClientForm from '../components/ClientForm.vue'
  export default {
    components: { ClientForm },
    created() {
      this.getClient()
    },
  
    data() {
      return {
        dialog: false,
        clients: [],
        headers: [
          { text: 'Name', value: 'name' },
          { text: 'Email', value: 'email' },
          { text: 'Company', value: 'company' },
          { text: 'Address', value: 'address' },
          { text: 'Delete', value: 'active' },
        ],
      }
    },
  
    methods: {
      async getClient() {
        this.clients = await this.$axios.$get('/client/clients')
      },
      async deleteClient(id) {
        await this.$axios.$delete('/client/client', { params: { id } })
        this.getClient()
      },
    },
  }
  </script>
  
  <style></style>
  