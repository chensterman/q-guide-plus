<template>
  <v-app>
    <v-app-bar
      app
      height="100%"
      clipped-left
      color="#f8e8ca"
    >

      <div class="appbar">
        <h1 class="appbar">QGuide+</h1>
      </div>

      <v-btn dark large right class="mx-10" to="/" :color="buttonColor('/')">
        About
      </v-btn>

      <v-btn dark large right to="/query" :color="buttonColor('/query')">
        Query
      </v-btn>
    </v-app-bar>
    
    <!-- Sizes your content based upon application components -->
    <v-main>

      <!-- Provides the application the proper gutter -->
      <v-container fluid>
        <!-- If using vue-router -->
        <router-view></router-view>
      </v-container>
    </v-main>
    <v-footer app>
      <!-- -->
    </v-footer>
  </v-app>
</template>

<script>
  export default {
    data: () => ({
      test: "red",
    }),
    methods: {
      buttonColor(route) {
        if (route === window.location.pathname) {
          return "red lighten-1"
        } else {
          return "red darken-4"
        }
      },
    },
  }
</script>

<style scoped>
div.appbar {
  width: 50%;
  justify-content: center;
  text-align: right;
}

h1.appbar {
  font-weight: bold;
  font-family:'Courier New', Courier, monospace;
  font-size: 48px;
  color: #B71C1C;
}
</style>

