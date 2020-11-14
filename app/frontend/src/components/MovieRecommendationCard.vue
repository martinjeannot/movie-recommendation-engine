<template>
  <v-card>
    <v-card-title>Your movie recommendations</v-card-title>
    <v-card-text>
      <div class="text-center mb-5">
        <v-btn color="primary"
               :loading="loading"
               :disabled="movies.length < 5"
               @click="getRecommendations"
        >
          get recommendations
        </v-btn>
      </div>
      <div v-if="movies.length < 5" class="text-center mb-4 pt-2">
        <h2>Please rate at least 5 movies to get recommendations</h2>
      </div>
      <div v-if="loading" class="text-center pt-6">
        <v-progress-circular
          indeterminate
          :size="50"
          color="primary"
        ></v-progress-circular>
      </div>
      <v-simple-table v-else>
        <template v-slot:default>
          <thead>
          <tr>
            <th class="text-left">
              Title
            </th>
            <th class="text-left">
              Year
            </th>
            <th class="text-left">
              Predicted rating
            </th>
            <th class="text-left">
              IMDb
            </th>
          </tr>
          </thead>
          <tbody>
          <tr v-for="recommendation in recommendations" :key="recommendation.id">
            <td>{{ recommendation.title }}</td>
            <td>{{ recommendation.year }}</td>
            <td>{{ recommendation.predicted_rating.toFixed(5) }}</td>
            <td>
              <v-btn icon :href="getImdbLink(recommendation)"
                     color="primary" target="_blank" rel="noopener noreferrer"
              >
                <v-icon>mdi-open-in-new</v-icon>
              </v-btn>
            </td>
          </tr>
          </tbody>
        </template>
      </v-simple-table>
    </v-card-text>
  </v-card>
</template>

<script>
import { mapGetters } from 'vuex';

export default {
  name: 'MovieRecommendationCard',
  data: () => ({
    loading: false,
    recommendations: [],
  }),
  computed: {
    ...mapGetters(
      [
        'api',
        'movies',
      ],
    ),
  },
  methods: {
    getRecommendations() {
      this.loading = true;
      const path = '/movies/recommendations';
      let queryString = '';
      this.movies.forEach((movie) => {
        queryString += queryString ? '&' : '';
        queryString += `indices=${movie.index}&ratings=${movie.rating}`;
      });
      this.api(`${path}?${queryString}`)
        .then((response) => {
          this.recommendations = response.data;
        })
        // eslint-disable-next-line
        .catch((error) => console.log(error))
        .finally(() => {
          this.loading = false;
        });
    },
    getImdbLink(recommendation) {
      let link = 'https://www.imdb.com/find?q=';
      link += recommendation.title.split(' ')
        .join('+');
      return link;
    },
  },
};
</script>
