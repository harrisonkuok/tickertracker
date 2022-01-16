<template>
    <div>
        <h4>
            Receives report of the top meme stocks daily!
        </h4>
        <p>
            Sign up and log in to opt in.
        </p>
        <b-alert v-if="incorrectAuth" show variant="danger">Incorrect username or password entered.</b-alert>
        <b-form @submit.prevent="login" class="text-left">
            <b-form-group
                id="input-group-1"
                label="Email address:"
                label-for="input-1"
                description="We'll never share your email with anyone else."
            >
                <b-form-input
                    id="input-1"
                    v-model="email"
                    type="email"
                    placeholder="Enter email"
                    required
                ></b-form-input>
            </b-form-group>

            <b-form-group id="input-group-2" label="Password:" label-for="input-2">
                <b-form-input
                    id="input-2"
                    v-model="password"
                    type="password"
                    placeholder="Enter password"
                    required
                ></b-form-input>
            </b-form-group>
            
            <b-button type="submit" variant="primary">Login</b-button>
        </b-form>
    </div>
</template>

<script>
    export default {
        data() {
            return {
                email: '',
                password: '',
                incorrectAuth: false
        }
        },
        methods: {
            login () { 
                this.$store.dispatch('userLogin', {
                    email: this.email,
                    password: this.password
                })
                .then(() => {
                    // this.$router.push({ name: 'settings' })
                })
                .catch(err => {
                    console.log(err)
                    this.incorrectAuth = true
                })
            }
        }
    }
</script>
