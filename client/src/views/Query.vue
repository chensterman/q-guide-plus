<template>
  <div class="query">
    <v-app-bar 
      height=1000
      :collapse="!drawer"
      absolute
    >
      <v-checkbox
        v-model="drawer"
        color="white"
        hide-details
      ></v-checkbox>
    </v-app-bar>
    <!-- <v-card class="overflow-hidden">
      <v-app-bar
        :collapse="!collapseOnScroll"
        :collapse-on-scroll="collapseOnScroll"
        absolute
        color="deep-purple accent-4"
        dark
        scroll-target="#scrolling-techniques-6"
      >
        <v-app-bar-nav-icon></v-app-bar-nav-icon>

        <v-toolbar-title>Collapsing Bar</v-toolbar-title>

        <v-spacer></v-spacer>

        <v-checkbox
          v-model="collapseOnScroll"
          color="white"
          hide-details
        ></v-checkbox>
      </v-app-bar>
      <v-sheet
        id="scrolling-techniques-6"
        class="overflow-y-auto"
        max-height="600"
      >
        <v-container style="height: 1000px;"></v-container>
      </v-sheet>
    </v-card> -->
  </div>
  <!-- <v-navigation-drawer app>
    <v-list-item>
      <v-list-item-content>
        <v-list-item-title>
          QGuidePlus
        </v-list-item-title>
        <v-list-item-subtitle>
          Harvard QGuide but better.
        </v-list-item-subtitle>
      </v-list-item-content>
    </v-list-item>
    <v-divider></v-divider>
  </v-navigation-drawer> -->
</template>

<script>
  export default {
    name: 'Home',
    data: () => ({ drawer: true }),
  }
</script>
