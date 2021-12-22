<template>
  <v-app>
    <v-app-bar
      app
      height=100
      clipped-left
      color="#f8e8ca"
    >
      <div class="appbar">
        <h1 class="appbar">QGuide+</h1>
      </div>

      <v-btn dark large right class="mx-5" to="/" color="red darken-4">
        About
      </v-btn>

      <v-btn dark large right class="mx-5" to="/query" color="red darken-4">
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
      about: false,
    }),
    methods: {
    
    },
  }
</script>

<style scoped>
div.appbar {
  position: absolute;
  left: 50%;
  transform: translateX(-50%);
  justify-content: center;
  text-align: center;
}

h1.appbar {
  font-weight: bold;
  font-family:'Courier New', Courier, monospace;
  font-size: 48px;
  color: #B71C1C;
}
</style>

