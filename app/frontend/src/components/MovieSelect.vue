<template>
  <v-autocomplete
    v-model="movie"
    clearable
    item-text="title"
    :items="movies"
    label="Search a movie"
    :loading="loading"
    return-object
    :search-input.sync="searchInput"
  ></v-autocomplete>
</template>

<script>
import { mapGetters } from 'vuex';
import { debounce } from 'lodash';

export default {
  name: 'MovieSelect',
  data: () => ({
    movies: [],
    searchInput: '',
    loading: false,
  }),
  computed: {
    ...mapGetters([
      'api',
    ]),
    movie: {
      get() {
        return this.value;
      },
      set(value) {
        this.$emit('input', value);
      },
    },
  },
  watch: {
    searchInput(value) {
      if (value && value.length >= 3) {
        return this.debouncedSearchMovies(value);
      }
      return null;
    },
  },
  methods: {
    searchMovies(searchInput) {
      this.loading = true;
      this.api(`/movies/list?title=${searchInput}`)
        .then((response) => {
          this.movies = response.data;
        })
        .catch((error) => console.log(error))
        .finally(() => {
          this.loading = false;
        });
      this.movies = [
        {
          id: 1,
          title: 'The Matrix',
          year: '1995',
        },
        {
          id: 12,
          title: 'Toy Story',
          year: '9458',
        },
      ];
    },
  },
  created() {
    this.debouncedSearchMovies = debounce(this.searchMovies, 600);
  },
};
</script>
