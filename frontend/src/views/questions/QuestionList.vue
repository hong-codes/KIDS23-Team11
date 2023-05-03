<template>
  <div
    class="d-flex flex-column align-items-stretch flex-shrink-0 bg-body-tertiary"
    style="width: 380px"
  >
    <a
      href="/"
      class="d-flex align-items-center flex-shrink-0 p-3 link-body-emphasis text-decoration-none border-bottom"
    >
      <svg class="bi pe-none me-2" width="30" height="24"><use xlink:href="#bootstrap" /></svg>
      <span class="fs-5 fw-semibold">Questions</span>
    </a>
    <div
      class="list-group list-group-flush border-bottom scrollarea"
      v-for="(question, index) in props.questions"
      :key="index"
    >
      <a
        href="#"
        class="list-group-item list-group-item-action active py-3 lh-sm"
        aria-current="true"
      >
        <div class="d-flex w-100 align-items-center justify-content-between">
          <strong class="mb-1">{{ question.text }} </strong>
          <small>Wed</small>
        </div>
        <div class="col-10 mb-1 small">something something</div>
      </a>
    </div>
  </div>
</template>

<script setup lang="ts">
const props = defineProps(['questions'])
</script>
