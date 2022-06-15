<template>
  <v-card class="pa-1 ma-10" color="red darken-4">

      <v-card class="pa-5 ma-10" color="#f8e8ca">
          <div class="heading">
            UPDATED EVALUATIONS: 2021 FALL
          </div>
      </v-card>

      <v-card class="pa-5 ma-10" color="#f8e8ca">
          <div class="heading">
            The Q Guide Plus is designed by Harvard students, for Harvard students.
          </div>

          <div class="heading">
            Blake Young, Benny Chang, Leon Chen
          </div>

          <div class="body">
            We stand for convenience and utility during course registration periods,
            as we know this is the struggle of many in search of those precious gems.
          </div>
          <div class="body">
            Thus, we provide a tool that allows students to query the entirety of 
            the content of Harvard's newest course evaluations site based on select
            parameters for your convenience. Our query results are (hopefully) updated
            each semester as new course evaluations are made available.
          </div>
          <div class="body">
            To support the cause and help pay for our Jefe's, please consider a
            donation of any amount to the following Venmo account. We will gladly take in 
            suggestions through there and do our best to implement them in a timely manner.
          </div>
          <div class="heading">
            @Leon-Chen-24
          </div>
      </v-card>

      <v-card class="pb-5 ma-10" color="#f8e8ca">
          <div class="heading">
            Course and Instructor Ratings
          </div>

          <div class="body">
            Scores for each course are the mean of all responses, and based on the scale below.
          </div>
          <div class="body">
            <p style="color:green">5 - Excellent</p>
          </div>
          <div class="body">
            <p style="color:#5DBB63">4 - Very Good</p>
          </div>
          <div class="body">
            <p style="color:#FFD200">3 - Good</p>
          </div>
          <div class="body">
            <p style="color:orange">2 - Fair</p>
          </div>
          <div class="body">
            <p style="color:red">1 - Unsatisfactory</p>
          </div>
      </v-card>

      <v-card class="pb-5 ma-10" color="#f8e8ca">
          <div class="heading">
            Recommendability
          </div>

          <div class="body">
            Scores for each course are the mean of all responses, and based on the scale below.
          </div>
          <div class="body">
            <p style="color:green">5 - Recommend with Enthusiasm</p>
          </div>
          <div class="body">
            <p style="color:#5DBB63">4 - Likely to Recommend</p>
          </div>
          <div class="body">
            <p style="color:#FFD200">3 - Recommend with Reservations</p>
          </div>
          <div class="body">
            <p style="color:orange">2 - Unlikely to Recommend</p>
          </div>
          <div class="body">
            <p style="color:red">1 - Definitely not Recommend</p>
          </div>
      </v-card>

      <v-card class="pb-5 ma-10" color="#f8e8ca">
          <div class="heading">
            Workload
          </div>

          <div class="body">
            The workload for each course is given in terms of hours spent on
            coursework outside of class per week, and is the mean of all responses.
          </div>
      </v-card>

      <v-card class="pb-5 ma-10" color="#f8e8ca">
          <div class="heading">
            Comment Sentiment (BETA)
          </div>

          <div class="body">
            We are currently beta testing the comment sentiment feature which
            provides an estimated sentiment score for each course based on comments.
            This is achieved by running each comment through a NLP model, which scores
            it 1 for positive, 0 for neutral, and -1 for negative. The overall sentiment
            score for the course is simply the average over all of its comments.
          </div>
          <div class="body">
            You could generally assume that any course under a score of 0.0 has pretty
            bad sentiment, any score between 0.0-0.5 has "ok" sentiment, and anything
            above 0.5 as pretty solid sentiment. Accuracy may vary.
          </div>
      </v-card>
    </v-card>
</template>

<script>
  export default {
    name: 'Home',
  }
</script>

<style scoped>
div.heading {
  padding: 20px 10px 20px 10px;
  text-align: center;
  font-weight: 900;
  font-size: 2.0vw;
  color: #B71C1C;
}

div.body {
  padding: 10px 20px 10px 20px;
  text-align: center;
  font-weight: 900;
  font-size: 1.5vw;
  color: black;
}

p{
   margin:0;
   padding:0;
}
</style>