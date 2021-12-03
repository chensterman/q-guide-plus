<template>
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
                        <div :style="colorMap(value, 2, 5)">{{ value }}</div>
                        <div class="key">{{ key.charAt(0).toUpperCase() + key.slice(1) }}</div>
                    </div>
                </div>
                <v-divider class="ma-2"/>
                <div class="cardtitle">Instructor Ratings</div>
                <div class="d-flex flex-row justify-space-around">
                    <div class="center" v-for="(value, key) in this.course['instructorRating']" v-bind:key="(value, key)">
                        <div :style="colorMap(value, 2, 5)">{{ value }}</div>
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
                    <div class="center">
                        <div>{{ this.course['courseEval']['workload'] }}</div>
                        <div class="key">Workload</div>
                    </div>
                    <div class="center">
                        <div :style="colorMap(this.course['courseEval']['recommend'], 2, 5)">{{ this.course['courseEval']['recommend'] }}</div>
                        <div class="key">Recommendability</div>
                    </div>
                    <div class="center">
                        <div>{{ Math.round(this.course['courseEval']['sentiment'] * 100) / 100 }}</div>
                        <div class="key">Sentiment</div>
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
    methods: {
        colorMap(value, min, max) {
            if (!value) {
                return "";
            }

            var textShadow = " text-shadow: 0px 0px 2px #000000;";
            if (value < min) {
                return "color:rgb(255, 0, 0);" + textShadow;
            }
            
            var mid = (min + max) / 2;
            var mdiff = (max - min) / 2;
            var vdiff = value - min;
            if (value < mid) {
                var color = Math.round(255 * (vdiff / mdiff));
                return "color:rgb(255, " + String(color) + ", 0);" + textShadow;
            } else {
                var color = Math.round(255 * (1 - (vdiff - mdiff) / mdiff));
                return "color:rgb(" + String(color) + ", 255, 0);" + textShadow;
            }
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