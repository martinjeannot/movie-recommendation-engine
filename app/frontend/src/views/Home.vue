<template>
  <v-row>
    <v-col cols="6">
      <v-card>
        <v-card-title>
          Your movie preferences
        </v-card-title>
        <v-card-text>
          <div class="mb-4">
            Please rate some of the movies you have seen :
          </div>
          <movie-select
            v-model="selectedMovie"
          ></movie-select>
          <movie-list></movie-list>
        </v-card-text>
      </v-card>
    </v-col>
    <v-col cols="6">
      <movie-recommendation-card></movie-recommendation-card>
    </v-col>
  </v-row>
</template>

<script>
import { mapActions } from 'vuex';
import MovieSelect from '@/components/MovieSelect';
import MovieList from '@/components/MovieList';
import MovieRecommendationCard from '@/components/MovieRecommendationCard';

export default {
  name: 'Home',
  components: {
    MovieList,
    MovieSelect,
    MovieRecommendationCard,
  },
  data: () => ({
    selectedMovie: null,
  }),
  watch: {
    selectedMovie(movie) {
      if (movie) {
        this.addMovie(movie);
      } else {
        this.selectedMovie = null;
      }
    },
  },
  methods: {
    ...mapActions([
      'addMovie',
    ]),
  },
};
</script>
