import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    api: axios.create({
      baseURL: 'https://my-movie-recommendation-engine.herokuapp.com/api',
    }),
    movies: [],
  },
  mutations: {
    addMovie(state, movie) {
      const found = state.movies.find((item) => item.id === movie.id);
      if (!found) {
        // eslint-disable-next-line no-param-reassign
        movie.rating = 1; // init movie rating
        state.movies.push(movie);
      }
    },
    removeMovie(state, movie) {
      const indexToRemove = state.movies.findIndex((item) => item.id === movie.id);
      state.movies.splice(indexToRemove, 1);
    },
  },
  actions: {
    addMovie({ commit }, movie) {
      commit('addMovie', movie);
    },
    removeMovie({ commit }, movie) {
      commit('removeMovie', movie);
    },
  },
  getters: {
    api(state) {
      return state.api;
    },
    movies(state) {
      return state.movies;
    },
  },
  modules: {},
});
