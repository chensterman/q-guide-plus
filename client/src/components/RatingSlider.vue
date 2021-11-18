<template>
    <div style="margin:0px">
        <v-subheader>{{ label }}</v-subheader>
        <v-slider
            thumb-color="red"
            track-color="red"
            color="grey"
            value=2.5
            step=0.1
            max=5
            thumb-label="always"
            thumb-size=24
        >
            <template v-slot:prepend>
                <v-simple-checkbox/>
            </template>
        </v-slider>
    </div>
</template>

<script>
  export default {
    name: 'RatingSlider',
    props: {
        label: String,
    }
  }
</script>