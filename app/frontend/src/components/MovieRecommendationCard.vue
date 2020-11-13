<template>
  <v-card>
    <v-card-title>Your movie recommendations</v-card-title>
    <v-card-text>
      <v-btn color="primary" @click="getRecommendations">get recommendations</v-btn>
    </v-card-text>
  </v-card>
</template>

<script>
import { mapGetters } from 'vuex';

export default {
  name: 'MovieRecommendationCard',
  data: () => ({}),
  computed: {
    ...mapGetters(
      [
        'movies',
      ],
    ),
  },
  methods: {
    getRecommendations() {
      console.log(this.movies);
    },
  },
};
</script>
