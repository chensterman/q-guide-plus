<template>
    <div class="d-flex flex-row">
        <v-checkbox 
            v-model="used"
            @change="emitToggle"
            color="red darken-4"
            class="my-auto"
        ></v-checkbox>
        <v-text-field
            v-model="value"
            @change="emitQuery"
            :label="label"
            :hint="hint"
            outlined
            dense
            background-color="white"
            :disabled="!used"
        ></v-text-field>
    </div>
</template>

<script>
export default {
    name: 'TextField',
    model: {
        prop: 'queries',
        event: 'emitQuery',
    },
    props: {
        param: {
            type: String,
            required: true,
        },
        label: String,
        queries: Array,
        hint: String,
    },
    data: function() {
        return {
            used: false,
            value: "",
            query: "",
        };
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
            this.query = "&" + this.param + "=" + this.value;
        },
    },
}
</script>