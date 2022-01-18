<template>
    <b-table :items="items" :fields="fields"></b-table>
</template>

<script>
  import { getAPI } from '../axios-api'


  export default {
    data() {
      return {
        show: true,
        items: [],
        fields: ['ticker', 'name', 'mention']
      }
    },
    mounted() {
      getAPI
        .get('api/stocks/top',)
        .then(response => {
          this.items = response.data
        })
        .catch(err => {
          console.log(err)
        })
    }
  }
</script>