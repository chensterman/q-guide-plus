<template>
    <v-row class="d-flex align-center">
         <v-checkbox 
            v-model="used"
        ></v-checkbox>
        <v-select
            :items="items"
            :label="label"
            dense
            outlined
            :disabled="!used"
        ></v-select>
    </v-row>
</template>

<script>
    export default {
        name: 'Dropdown',
        props: {
            label: String,
            items: Array,
        },
        data: () => ({
            used: false,
        }),
    }
</script>