<template>
  <header>
    <!-- Fixed navbar -->
    <nav class="navbar navbar-expand-md navbar-dark fixed-top bg-dark">
      <img alt="logo" class="logo" src="@/assets/logo.svg" height="50" />
      <a class="navbar-brand" href="#">Eleven GPT</a>
      <button
        class="navbar-toggler"
        type="button"
        data-toggle="collapse"
        data-target="#navbarCollapse"
        aria-controls="navbarCollapse"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarCollapse">
        <ul class="navbar-nav mr-auto">
          <li class="nav-item active">
            <RouterLink class="nav-link" to="/">Questions</RouterLink>
          </li>
        </ul>
      </div>
    </nav>
  </header>

  <!-- Begin page content -->
  <main role="main" class="container" style="margin-top: 60px">
    <slot />
  </main>

  <footer class="footer">
    <div class="container">
      <span class="text-muted">(c) 2023 - St. Jude Bio Hackathon Team 11</span>
    </div>
  </footer>
</template>

<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
</script>
