<template>
    <v-card>
      <v-card-title> Add Client </v-card-title>
      <v-card-text>
        <v-text-field v-model="client.name" label="Name" />
        <v-text-field v-model="client.email" label="Email" />
        <v-text-field v-model="client.company" label="Company" />
        <v-text-field v-model="client.address" label="Address" />
      </v-card-text>
      <v-card-actions>
        <v-btn :disabled="lock" @click="addClient()" color="primary">Save</v-btn>
      </v-card-actions>
    </v-card>
  </template>
  
  <script>
  export default {
    props: ['client_id'],
    data() {
      return {
        client: {},
        lock: false,
      }
    },
    methods: {
      async addClient() {
        this.lock = true
        await this.$axios.$post('/client/client', this.client)
        this.lock = false
        this.client = {}
        this.$emit('save')
      },
    },
  }
  </script>
  
  <style></style>
  