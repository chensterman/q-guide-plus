<template>
    <!-- <v-card class="pa-5 ma-10" color="#f8e8ca">
        <div class="d-flex flex-row justify-space-between">
            <div>
                <v-btn :href="this.course['courseSummary']['url']" target="_blank">
                    <v-card-title class="catalog">{{ this.course["courseSummary"]["catalog"] }}</v-card-title>
                    <v-icon color="red darken-4">mdi-open-in-new</v-icon> 
                </v-btn>
                <v-card-subtitle>
                    <div>{{ this.course["courseSummary"]["title"] }}</div>
                    <div>{{ this.course["courseSummary"]["instructor"] }}</div>
                </v-card-subtitle>
                <v-card-text>
                    <div>{{ this.course["courseSummary"]["department"] }}</div>
                    <div>{{ this.course["courseSummary"]["term"] }}</div>
                </v-card-text>
            </div>
            <div>
                <v-card-title class="pt-0">Course Ratings</v-card-title>
                <v-card-text>
                    <div>Overall - {{ this.course["courseSummary"]["test"] }}</div>
                    <div>Materials - </div>
                    <div>Assignments - </div>
                    <div>Feedback - </div>
                    <div>Section - </div>
                </v-card-text>
            </div>
            <div>
                <v-card-title class="pt-0">Instructor Ratings</v-card-title>
                <v-card-text>
                    <div>Overall - </div>
                    <div>Lectures - </div>
                    <div>Accessibility - </div>
                    <div>Enthusiasm - </div>
                    <div>Encouragement - </div>
                    <div>Feedback - </div>
                    <div>Timeliness - </div>
                </v-card-text>
            </div>
            <div>
                <v-card-title class="pt-0">Evaluations</v-card-title>
                <v-card-text>
                    <div>Workload - {{ this.course["courseEval"]["workload"] }}</div>
                    <div>Recommendability - </div>
                    <div>Comment Sentiment - </div>
                </v-card-text>
            </div>
        </div>  
    </v-card> -->

    <v-card class="pa-5 ma-10" color="#f8e8ca">
        <v-row>
            <v-col cols=4>
                <v-btn class="mb-2" :href="this.course['courseSummary']['url']" target="_blank">
                    <div class="catalog">{{ this.course["courseSummary"]["catalog"] }}</div>
                    <v-icon color="#B71C1C">mdi-open-in-new</v-icon> 
                </v-btn>
                <div class="title">{{ this.course["courseSummary"]["title"] }}</div>
                <v-divider class="ma-2"/>
                <div>Instructor - {{ this.course["courseSummary"]["instructor"] }}</div>
                <v-divider class="ma-2"/>
                <div>Department - {{ this.course["courseSummary"]["department"] }}</div>
                <v-divider class="ma-2"/>
                <div>Term - {{ this.course["courseSummary"]["term"] }}</div>
            </v-col>

            <v-col>
                <div class="cardtitle">Course Ratings</div>
                <div class="d-flex flex-row justify-space-around">
                    <div class="center" v-for="(value, key) in this.course['courseRating']" v-bind:key="(value, key)">
                        <div>{{ value }}</div>
                        <div class="key">{{ key.charAt(0).toUpperCase() + key.slice(1) }}</div>
                    </div>
                </div>
                <v-divider class="ma-2"/>
                <div class="cardtitle">Instructor Ratings</div>
                <div class="d-flex flex-row justify-space-around">
                    <div class="center" v-for="(value, key) in this.course['instructorRating']" v-bind:key="(value, key)">
                        <div>{{ value }}</div>
                        <div class="key">{{ key.charAt(0).toUpperCase() + key.slice(1) }}</div>
                    </div>
                </div>
                <v-divider class="ma-2"/>
                <div class="cardtitle">Evaluations</div>
                <div class="d-flex flex-row justify-space-around">
                    <div class="center">
                        <div>{{ this.course['courseStat']['enrollment'] }}</div>
                        <div class="key">Enrollment</div>
                    </div>
                    <div class="center">
                        <div>{{ this.course['courseStat']['responses'] }}</div>
                        <div class="key">Responses</div>
                    </div>
                    <div class="center" v-for="(value, key) in this.course['courseEval']" v-bind:key="(value, key)">
                        <div>{{ Math.round(value * 100) / 100 }}</div>
                        <div class="key">{{ key.charAt(0).toUpperCase() + key.slice(1) }}</div>
                    </div>
                </div>
            </v-col>
        </v-row>
    </v-card>
</template>

<script>
  export default {
    name: 'Course',
    props: {
        course: {
            type: Object,
            required: true,
        },
    },
  }
</script>

<style scoped>
div.catalog {
    text-align: center;
    font-size: 1.5vw;
    color: #B71C1C;
}

div.title {
    font-size: 1vw;
}

div.cardtitle {
    text-align: center;
    font-size: 1vw;
    margin-bottom: 5px;
}

div.center {
    text-align: center;
}

div.key {
    text-align: center;
    font-size: 0.8vw;
}
</style>