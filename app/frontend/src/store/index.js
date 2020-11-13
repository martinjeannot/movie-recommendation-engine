import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    api: axios.create({
      baseURL: 'http://localhost:5000/api',
    }),
  },
  mutations: {},
  actions: {},
  getters: {
    api(state) {
      return state.api;
    },
  },
  modules: {},
});
