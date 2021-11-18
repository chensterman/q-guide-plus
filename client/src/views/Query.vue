<template>
  <v-row>
    <v-column>
    <v-navigation-drawer
      app
      clipped
      width=360
    >
      <v-container>
        <v-expansion-panels multiple>
          <v-expansion-panel>
            <v-expansion-panel-header>
              Course Info
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
              color="red darken-4"
              dark
            >
          Search
        </v-btn>
      </v-container>
    </v-navigation-drawer>
    </v-column>
    <v-column>
      <h1>This is the home page</h1>
    </v-column>
  </v-row>
  
</template>

<script>
  import RatingSlider from "../components/RatingSlider.vue"
  export default {
    name: 'Query',
    components: {
      RatingSlider,
    }
  }
</script>
