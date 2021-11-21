<template>
    <v-row>
        <v-checkbox 
            v-model="used"
        ></v-checkbox>
        <v-text-field
            :label="label"
            :hint="hint"
            :disabled="!used"
        ></v-text-field>
    </v-row>
</template>

<script>
    export default {
        name: 'TextField',
        props: {
            label: String,
            hint: String,
        },
        data: () => ({
            used: false,
        }),
    }
</script>