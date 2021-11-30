<template>
  <div class="d-flex flex-row">
    <v-navigation-drawer
      v-model="drawer"
      app
      clipped
      align="center"
      width="25%"
    >
      <v-card rounded="0" color="red darken-4" height="10%" class="mb-5">
        <v-card-title class="justify-center">
          <p style="color: white">Search Filters</p>
        </v-card-title>
      </v-card>

      <v-expansion-panels multiple class="px-5 pb-5">
        <v-expansion-panel> 
          <v-expansion-panel-header color="#f8e8ca">
            Course Info
          </v-expansion-panel-header>
          <v-expansion-panel-content color="#f8e8ca">
            <TextField v-model="queries" param="courseSummary.catalog" label="Catalog (contains)" hint="e.g. COMPSCI 50"/>
            <TextField v-model="queries" param="courseSummary.title" label="Title (contains)" hint="e.g. Machine Learning"/>
            <TextField v-model="queries" param="courseSummary.instructor" label="Instructor (contains)" hint="e.g. Malan"/>
            <v-divider class="mt-3 mb-6" />
            <Dropdown v-model="queries" param="courseSummary.department" label="Department" :items="departments" />
            <Dropdown v-model="queries" param="courseSummary.term" label="Term" :items="terms" />
            <RatingSlider v-model="queries" param="courseStat.enrollment" label="Enrollment" :max=800 :step=1 />
            <RatingSlider v-model="queries" param="courseStat.responses" label="Responses" :max=800 :step=1 />
          </v-expansion-panel-content>
        </v-expansion-panel>

        <v-expansion-panel>
          <v-expansion-panel-header color="#f8e8ca">
            Course Ratings
          </v-expansion-panel-header >
          <v-expansion-panel-content color="#f8e8ca">
            <RatingSlider v-model="queries" param="courseRating.overall" label="Overall" />
            <RatingSlider v-model="queries" param="courseRating.materials" label="Materials" />
            <RatingSlider v-model="queries" param="courseRating.assignments" label="Assignments" />
            <RatingSlider v-model="queries" param="courseRating.feedback" label="Feedback" />
            <RatingSlider v-model="queries" param="courseRating.section" label="Section" />
          </v-expansion-panel-content>
        </v-expansion-panel>

        <v-expansion-panel>
          <v-expansion-panel-header color="#f8e8ca">
            Instructor Ratings
          </v-expansion-panel-header>
          <v-expansion-panel-content color="#f8e8ca">
            <RatingSlider v-model="queries" param="instructorRating.overall" label="Overall" />
            <RatingSlider v-model="queries" param="instructorRating.lectures" label="Lectures" />
            <RatingSlider v-model="queries" param="instructorRating.accessibility" label="Accessibility" />
            <RatingSlider v-model="queries" param="instructorRating.enthusiasm" label="Enthusiasm" />
            <RatingSlider v-model="queries" param="instructorRating.encouragement" label="Encouragement" />
            <RatingSlider v-model="queries" param="instructorRating.feedback" label="Feedback" />
            <RatingSlider v-model="queries" param="instructorRating.returning" label="Timeliness" />
          </v-expansion-panel-content>
        </v-expansion-panel>

        <v-expansion-panel>
          <v-expansion-panel-header color="#f8e8ca">
            Evaluations
          </v-expansion-panel-header>
          <v-expansion-panel-content color="#f8e8ca">
            <RatingSlider v-model="queries" param="courseEval.workload" label="Workload" :max=30 :step=1 />
            <RatingSlider v-model="queries" param="courseEval.recommend" label="Recommendability" />
            <RatingSlider v-model="queries" param="courseEval.sentiment" label="Comment Sentiment" :min=-1 :max=1 />
          </v-expansion-panel-content>
        </v-expansion-panel>
      </v-expansion-panels>
      <v-btn
        @click="getQuery"
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

    <v-card class="ma-5 flex-grow-1" color="red darken-4">
      <v-card class="ma-10" height="80" color="#f8e8ca">
        <v-card-title class="justify-center">
          <h1 class="title">RESULTS</h1>
        </v-card-title>
      </v-card>
      <Course v-for="c in this.courses" v-bind:key="c" :course="c" />
    </v-card>
  </div>
</template>

<script>
  import RatingSlider from "../components/RatingSlider.vue"
  import Dropdown from "../components/Dropdown.vue"
  import TextField from "../components/TextField.vue"
  import Course from "../components/Course.vue"
  import API from "../controllers/api"
  export default {
    name: 'Query',
    components: {
      RatingSlider,
      Dropdown,
      TextField,
      Course,
    },
    data: () => ({
      departments: [
        'ARTS', 'African and African American Studies', 'American Studies', 'Anthropology', 'Applied Computation', 
        'Applied Mathematics', 'Applied Physics', 'Art, Film, and Visual Studies', 'Astronomy', 'Biological Sciences in Public Health', 
        'Biomedical Engineering', 'Biophysics', 'Biostatistics', 'Celtic Languages and Literatures', 'Chemical Biology', 
        'Chemical and Physical Biology', 'Chemistry and Chemical Biology', 'Classics, The', 'Comparative Literature', 'Computer Science', 
        'Earth and Planetary Sciences', 'East Asian Languages and Civilizations', 'Economics', 'Engineering Sciences', 'English', 
        'Environmental Science and Engineering', 'Environmental Science and Public Policy', 'Ethnicity, Migration, Rights', 
        'Expository Writing', 'Folklore and Mythology', 'Freshman Seminars', 'General Education', 'Germanic Languages and Literatures', 
        'Global Health and Health Policy', 'Government', 'Graduate School of Arts and Sciences', 'Health Policy', 'History', 
        'History and Literature', 'History of Art and Architecture', 'History of Science', 'Human Evolutionary Biology', 'Humanities', 
        'Linguistics', 'Mathematics', 'Medical Sciences', 'Medieval Studies', 'Mind, Brain, and Behavior', 'Molecular and Cellular Biology', 
        'Music', 'Near Eastern Languages and Civilizations', 'Neuroscience', 'No Department', 'Organismic and Evolutionary Biology', 
        'Philosophy', 'Physics', 'Population Health Sciences', 'Psychology', 'Public Policy', 'Regional Studies - East Asia', 
        'Religion, The Study of', 'Romance Languages and Literatures', 'Russia, Eastern Europe, and Central Asia', 
        'Slavic Languages and Literatures', 'Social Studies', 'Sociology', 'South Asian Studies', 'Statistics', 
        'Stem Cell and Regenerative Biology', 'Systems Biology', 'Theater, Dance, and Media', 'Women, Gender, and Sexuality, Studies of'],
      terms: ['2021 Spring', '2020 Fall', '2019 Fall'],
      drawer: true,
      queries: [],
      courses: [],
    }),
    methods: {
      buttonSymbol() {
        return this.drawer ? "<" : ">";
      },
      async getQuery() {
        var finalq = this.queries.join("");
        finalq = finalq.slice(1);
        finalq = "?" + finalq;
        console.log(finalq);
        this.courses = await API.query(finalq);
      },
    },
  }
</script>

<style scoped>
h1.title {
  font-weight: 900;
  font-size: 108px;
  color: black;
}
</style>
