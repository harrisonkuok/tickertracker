<template>
  <b-container>
    <b-row align-h="center">
      <b-col cols="12" md="6">
        <b-table   :items="items"></b-table>
      </b-col>
      <b-col cols="12" md="6">
        <h4>
          Receives <a href="http://" target="_blank" rel="noopener noreferrer"></a> report of the top meme stocks daily!
        </h4>
        <b-form @submit="onSubmit" @reset="onReset" v-if="show">
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
        </b-form>
      </b-col>
    </b-row>
  </b-container>
</template>

<script>
// @ is an alias to /src

export default {
  name: 'Home',
  data() {
      return {
        form: {
          email: ''
        },
        show: true,
        items: [
          { age: 40, first_name: 'AAA' },
          { age: 21, first_name: 'Larsen', },
          { age: 89, first_name: 'Geneva' },
          { age: 38, first_name: 'Jami' },
          { age: 40, first_name: 'AAA' },
          { age: 21, first_name: 'Larsen', },
          { age: 89, first_name: 'Geneva' },
          { age: 38, first_name: 'Jami' }
        ]
      }
    }
}
</script>
