import Vue from 'vue'
import Vuex from 'vuex'
import { getAPI } from './axios-api'

Vue.use(Vuex)
export default new Vuex.Store({
    state: {
        accessToken: null,
        refreshToken: null,
        APIData: '',
    },
    mutations: {
        updateStorage (state, { access, refresh }) {
            state.accessToken = access
            state.refreshToken = refresh
        },
    },
    actions: {
        userLogin (context, usercredentials) {
            return new Promise((resolve, reject) => {
                getAPI.post('/api/token/', {
                    email: usercredentials.email,
                    password: usercredentials.password
                })
                .then(res => {
                    context.commit('updateStorage', { access: res.data.access, refresh: res.data.refresh })
                    console.log(this.state.accessToken)
                    resolve()
                })
                .catch(err => {
                    reject(err)
                })
            })
        }
    }
})