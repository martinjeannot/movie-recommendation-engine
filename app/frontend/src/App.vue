<template>
  <v-app>
    <v-app-bar app color="primary lighten-2">
      <v-toolbar-title>
        <v-icon large>mdi-movie-search</v-icon>
      </v-toolbar-title>

      <v-spacer></v-spacer>

      <v-toolbar-items class="hidden-xs-only">
        <v-btn text v-for="menuItem in menuItems"
               :key="menuItem.key" :to="menuItem.route" exact
        >
          {{ menuItem.title }}
        </v-btn>
      </v-toolbar-items>
    </v-app-bar>

    <v-main>
      <v-container fluid>
        <router-view></router-view>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
export default {
  name: 'App',
  data: () => ({
    menuItems: [
      {
        key: 'home',
        icon: 'exit_to_app',
        title: 'Movie recommender',
        route: { name: 'Home' },
      },
      {
        key: 'about',
        icon: 'exit_to_app',
        title: 'About',
        route: { name: 'About' },
      },
    ],
  }),
};
</script>
