// import Vue from 'vue'
import { createStore } from 'vuex'

export default createStore({
  state: {
    token: localStorage.getItem('token') ? localStorage.getItem('token') : ''
  },
  getters: {
  },
  mutations: {
    changeLogin (state, token) {
      state.token = token
      localStorage.setItem('token', token)
    }
  },
  actions: {
  },
  modules: {
  }
})
