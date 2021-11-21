<template>
  <v-row>
    <v-column>
      <v-navigation-drawer
        app
        clipped
        width="30%"
        align="center"
        color="red lighten-2"
      >
        <v-card rounded="false" color="red darken-4" height="10%" class="mb-5">
          <v-card-title primary-title class="justify-center">
            <p style="color: white">Search Filters</p>
          </v-card-title>
        </v-card>

        <v-expansion-panels multiple class="px-5 pb-5">
          <v-expansion-panel> 
            <v-expansion-panel-header>
              Course Info
            </v-expansion-panel-header>
            <v-expansion-panel-content>
              <TextField label="Catalog (contains)" hint="e.g. COMPSCI 50"/>
              <TextField label="Title (contains)" hint="e.g. Machine Learning"/>
              <TextField label="Instructor (contains)" hint="e.g. Malan"/>
              <v-divider class="mt-5 mb-10" />
              <Dropdown label="Department" :items="departments" />
              <Dropdown label="Term" :items="terms" />
            </v-expansion-panel-content>
          </v-expansion-panel>

          <v-expansion-panel>
            <v-expansion-panel-header>
              Course Ratings
            </v-expansion-panel-header>
            <v-expansion-panel-content>
              <RatingSlider label="Overall" />
              <RatingSlider label="Materials" />
              <RatingSlider label="Assignments" />
              <RatingSlider label="Feedback" />
              <RatingSlider label="Section" />
            </v-expansion-panel-content>
          </v-expansion-panel>

          <v-expansion-panel>
            <v-expansion-panel-header>
              Instructor Ratings
            </v-expansion-panel-header>
            <v-expansion-panel-content>
              <RatingSlider label="Overall" />
              <RatingSlider label="Lectures" />
              <RatingSlider label="Accessibility" />
              <RatingSlider label="Enthusiasm" />
              <RatingSlider label="Encouragement" />
              <RatingSlider label="Feedback" />
              <RatingSlider label="Timeliness" />
            </v-expansion-panel-content>
          </v-expansion-panel>

          <v-expansion-panel>
            <v-expansion-panel-header>
              Evaluations
            </v-expansion-panel-header>
            <v-expansion-panel-content>
              <RatingSlider label="Workload" />
              <RatingSlider label="Recommendability" />
              <RatingSlider label="Comment Sentiment" />
            </v-expansion-panel-content>
          </v-expansion-panel>
        </v-expansion-panels>
        <v-btn
          x-large
          rounded
          width="50%"
          color="red darken-4"
          dark
          class="mx-5 mb-5"
        >
          Search
        </v-btn>
      </v-navigation-drawer>
    </v-column>
    <v-column>
      <h1>This is the home page</h1>
    </v-column>
  </v-row>
  
</template>

<script>
  import RatingSlider from "../components/RatingSlider.vue"
  import Dropdown from "../components/Dropdown.vue"
  import TextField from "../components/TextField.vue"
  export default {
    name: 'Query',
    components: {
      RatingSlider,
      Dropdown,
      TextField,
    },
    data: () => ({
      departments: ['Foo', 'Bar', 'Fizz', 'Buzz'],
      terms: ['2021 Spring', '2020 Fall', '2019 Fall']
    }),
  }
</script>
