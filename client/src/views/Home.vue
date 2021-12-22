<template>
  <v-card class="pa-1 ma-10" color="red darken-4">
      <v-card class="pa-5 ma-10" color="#f8e8ca">
          <div class="heading">
            The Q Guide Plus is designed by Harvard students, for Harvard students.
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

          <div class="body">5 - Excellent</div>
          <div class="body">4 - Very Good</div>
          <div class="body">3 - Good</div>
          <div class="body">2 - Fair</div>
          <div class="body">1 - Unsatisfactory</div>
      </v-card>

      <v-card class="pb-5 ma-10" color="#f8e8ca">
          <div class="heading">
            Recommendability
          </div>

          <div class="body">5 - Recommend with Enthusiasm</div>
          <div class="body">4 - Likely to Recommend</div>
          <div class="body">3 - Recommend with Reservations</div>
          <div class="body">2 - Unlikely to Recommend</div>
          <div class="body">1 - Definitely not Recommend</div>
      </v-card>

      <v-card class="pb-5 ma-10" color="#f8e8ca">
          <div class="heading">
            Workload
          </div>

          <div class="body">5 - </div>
      </v-card>

      <v-card class="pb-5 ma-10" color="#f8e8ca">
          <div class="heading">
            Comment Sentiment (BETA)
          </div>

          <div class="body">5 - </div>
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
</style>