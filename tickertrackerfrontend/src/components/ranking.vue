<template>
    <b-table :items="items" :fields="fields"></b-table>
</template>

<script>
  import { getAPI } from '../axios-api'


  export default {
    name: 'Home',
    data() {
      return {
        form: {
          email: ''
        },
        show: true,
        items: [],
        fields: ['ticker', 'name', 'mention']
      }
    },
    mounted() {
      getAPI
        .get('api/stocks/top',)
        .then(response => {
          console.log('Received data')
          this.items = response.data
        })
        .catch(err => {
          console.log(err)
        })
    }
  }
</script>