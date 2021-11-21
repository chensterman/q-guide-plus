<template>
    <div class="d-flex flex-row">
        <v-checkbox 
            v-model="used"
            @change="emitToggle"
            color="red darken-4"
        ></v-checkbox>
        <div class="flex-grow-1">
            <v-subheader>{{ label }}</v-subheader>
            <v-range-slider
                v-model="values"
                @change="emitQuery"
                height=15
                thumb-color="red darken-4"
                track-color="grey"
                color="red darken-4"
                :step="step"
                :min="min"
                :max="max"
                thumb-label="always"
                thumb-size=24
                :disabled="!used"
            ></v-range-slider>
        </div>
    </div>
</template>

<script>
export default {
    name: 'RatingSlider',
    model: {
        prop: 'queries',
        event: 'emitQuery',
    },
    props: {
        label: String,
        queries: Array,
        param: {
            type: String,
            required: true,
        },
        step: {
            type: Number,
            default: 0.1,
        },
        min: {
            type: Number,
            default: 0,
        },
        max: {
            type: Number,
            default: 5,
        },
    },
    data: function() {
        return {
            used: false,
            values: [0, 0],
            query: "",
        };
    },
    created: function() {
        this.values = [this.min, this.max];
        this.genQuery();
    },
    methods: {
        emitToggle() {
            if (this.used) {
                this.queries.push(this.query);
            }
            else {
                const index = this.queries.indexOf(this.query);
                if (index > -1) {
                    this.queries.splice(index, 1);
                }
            }
            this.$emit("emitToggle", this.queries);
        },
        emitQuery() {
            const index = this.queries.indexOf(this.query);
            if (index > -1) {
                this.queries.splice(index, 1);
            }
            this.genQuery();
            this.queries.push(this.query);
            this.$emit("emitQuery", this.queries);
        },
        genQuery() {
            this.query = "&" + this.param + ".min=" + String(this.values[0]) + "&" + this.param + ".max=" + String(this.values[1]);
        },
    },
}
</script>