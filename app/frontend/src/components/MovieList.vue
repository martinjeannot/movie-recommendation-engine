<template>
  <div>
    <v-row v-for="movie in movies" :key="movie.id">
      <v-col cols="5" class="mt-2">
        <h3>
          {{ movie.title }}
        </h3>
      </v-col>
      <v-col cols="5">
        <v-rating v-model="movie.rating"></v-rating>
      </v-col>
      <v-col cols="2">
        <v-btn icon color="error" @click="removeMovie(movie)">
          <v-icon>mdi-delete</v-icon>
        </v-btn>
      </v-col>
    </v-row>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex';

export default {
  name: 'MovieList',
  data: () => ({}),
  computed: {
    ...mapGetters([
      'movies',
    ]),
  },
  methods: {
    ...mapActions([
      'removeMovie',
    ]),
  },
};
</script>
