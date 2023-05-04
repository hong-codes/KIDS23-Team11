<template>
  <header>
    <!-- Fixed navbar -->
    <nav class="navbar navbar-expand-md navbar-dark fixed-top bg-dark">
      <a class="navbar-brand" href="#">
        <img alt="logo" class="logo px-4" src="@/assets/logo-child.svg" height="50" />
        👋 Hey JudeGPT
      </a>
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
          <li class="nav-item active">
            <RouterLink class="nav-link" to="/ranking">Ranking</RouterLink>
          </li>
          <li class="nav-item active">
            <RouterLink class="nav-link" to="/about">About</RouterLink>
          </li>
        </ul>
      </div>
    </nav>
  </header>

  <!-- Begin page content -->
  <main role="main" class="container-xxl" style="margin-top: 80px">
    <slot />
  </main>

  <footer class="footer">
    <div class="container">
      <span class="text-muted">(c) 2023 - St. Jude Bio Hackathon Team 11</span>
    </div>
  </footer>
</template>

<script setup lang="ts">
import { RouterLink } from 'vue-router'
</script>
