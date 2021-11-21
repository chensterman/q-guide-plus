<template>
    <div class="d-flex flex-row">
        <v-checkbox 
            v-model="used"
        ></v-checkbox>
        <div class="flex-grow-1">
            <v-subheader>{{ label }}</v-subheader>
            <v-slider
                height=5
                thumb-color="red darken-4"
                track-color="red darken-4"
                color="grey"
                value=2.5
                step=0.1
                :min="min"
                :max="max"
                thumb-label="always"
                thumb-size=24
                :disabled="!used"
            ></v-slider>
        </div>
    </div>
</template>

<script>
  export default {
    name: 'RatingSlider',
    props: {
        label: String,
        min: {
            type: Number,
            default: 0,
        },
        max: {
            type: Number,
            default: 5,
        },
    },
    data: () => ({
      used: false,
    }),
  }
</script>