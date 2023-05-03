<template>
  <div
    class="d-flex flex-column align-items-stretch flex-shrink-0 bg-body-tertiary"
    style="width: 380px"
  >
    <pre> {{ props.question }} </pre>
  </div>
</template>

<script setup lang="ts">
const props = defineProps(['question'])
</script>
