<template>
  <Layout>
    <RouterView />
  </Layout>
</template>

<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
import Layout from './components/Layout.vue'
import HelloWorld from './components/HelloWorld.vue'
</script>
