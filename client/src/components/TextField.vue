<template>
    <div class="d-flex flex-row">
        <v-checkbox 
            v-model="used"
        ></v-checkbox>
        <v-text-field
            :label="label"
            :hint="hint"
            :disabled="!used"
        ></v-text-field>
    </div>
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