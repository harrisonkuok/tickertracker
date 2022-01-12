<template>
  <div>
    <b-container>
      <b-row align-h="center">
        <b-col cols="12" md="6">
          <b-table :items="items" :fields="fields"></b-table>
        </b-col>
        <b-col cols="12" md="6">
          <h4>
            Receives report of the top meme stocks daily!
          </h4>
          <!-- <b-form @submit="onSubmit" @reset="onReset" v-if="show">
            <b-form-group
              id="input-group-1"
              label="Email address:"
              label-for="input-1"
              description="We'll never share your email with anyone else."
            >
              <b-form-input
                id="input-1"
                v-model="form.email"
                type="email"
                placeholder="Enter email"
                required
              ></b-form-input>
            </b-form-group>

            <b-button type="submit" variant="primary">Submit</b-button>
          </b-form> -->
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
  import { getAPI } from '../axios-api'

// @ is an alias to /src

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
