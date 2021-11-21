<template>
    <div class="d-flex flex-row">
        <v-checkbox 
            v-model="used"
            class="my-auto"
        ></v-checkbox>
        <v-select
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
        props: {
            label: String,
            items: Array,
        },
        data: () => ({
            used: false,
        }),
    }
</script>