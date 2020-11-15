<template>
  <v-row>
    <v-col cols="6" offset="1">
      <v-card>
        <v-card-title>About the project</v-card-title>
        <v-card-text>
          <p>
            I've recently been exposed to Gaussian Mixture models (GMM) as well as the Expectation
            Maximization algorithm in the context of GMM. I looked into simple applications of these
            and movie recommendations came up a lot, hence this project.
          </p>
          <p>
            The dataset used is the
            <a href="https://grouplens.org/datasets/movielens/" target="_blank"><i>small</i> MovieLens dataset</a>
            , it contains 100 000 ratings applied to 9 000 movies by 600 users.
          </p>
          <p>
            The model used in the demo has been trained with K=20 (number of gaussian components)
            and ultimately achieved a log-likelihood of about -122802.15.
          </p>
          <p>
            All of the code can be found on this
            <a href="https://github.com/martinjeannot/movie-recommendation-engine" target="_blank">github repository</a>.
          </p>
        </v-card-text>
      </v-card>
    </v-col>
    <v-col cols="4">
      <v-card>
        <v-card-title>About me</v-card-title>
        <v-card-text>
          Software engineer by training, after 9 years of full-stack development I decided to
          transition to data science and machine learning. You can contact me on
          <a href="https://www.linkedin.com/in/martinjeannot" target="_blank">LinkedIn</a>.
        </v-card-text>
      </v-card>
    </v-col>
  </v-row>
</template>

<script>
export default {
  name: 'About',
  data: () => ({}),
};
</script>
