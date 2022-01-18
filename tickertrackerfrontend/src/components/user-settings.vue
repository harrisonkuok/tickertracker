<template>
    <div>
        <h4>
            Welcome {{ this.email }}!
        </h4>
        <p>
            Change your account settings here.
        </p>
        <b-form @submit.prevent="submit" class="text-left">

            <b-form-group id="input-group-1" label="Do you want to receive a daily report of the top stocks on r/wallstreetbets?">
                <b-form-checkbox v-model="opt_in" >Check the box to receive.</b-form-checkbox>
            </b-form-group>

            <b-button type="submit" variant="primary">Submit Change</b-button>
            
        </b-form>
    </div>
</template>

<script>
    import { getAPI } from '../axios-api'
    import { mapState } from 'vuex'

    export default {
        data() {
            return {
                email: '',
                opt_in: false,
            }
        },
        computed: mapState(['APIData']),
        mounted () {
            getAPI.get('api/auth/settings/', {
                headers: {
                    "Authorization": "JWT " + this.$store.state.accessToken,}
            })
            .then(response => {
                this.email = response.data.email,
                this.opt_in = response.data.opt_in
            })
            .catch(() => {
                this.$router.push({ name: 'Home' })
            })
        }
    }

</script>