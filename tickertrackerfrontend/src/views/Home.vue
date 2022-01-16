<template>
  <div>
    <b-container>
      <b-row align-h="center">
        <b-col cols="12" md="6">
          <ranking />
        </b-col>
        <b-col cols="12" md="6">
          <login />
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
  import Ranking from "@/components/ranking"
  import Login from "@/components/login"
  export default {
    components: {
      Ranking,
      Login
    }
  }
</script>
