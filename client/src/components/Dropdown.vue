<template>
    <div class="d-flex flex-row">
        <v-checkbox 
            v-model="used"
            @change="emitToggle"
            class="my-auto"
        ></v-checkbox>
        <v-select
            v-model="value"
            @change="emitQuery"
            :items="items"
            :label="label"
            dense
            outlined
            :disabled="!used"
        ></v-select>
    </div>
</template>

<script>
export default {
    name: 'Dropdown',
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
        items: Array,
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