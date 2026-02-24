<template>
  <div class="dashboard">
    <h1>Dashboard</h1>
    <p class="muted">Welcome, {{ authStore.user?.email || authStore.user?.username }}.</p>
    <section class="tile">
      <h2>Quick links</h2>
      <router-link to="/campaigns" class="link">View campaigns</router-link>
    </section>
  </div>
</template>

<script setup>
import { useAuthStore } from '../stores/auth'
const authStore = useAuthStore()
</script>

<style scoped>
.dashboard h1 { margin: 0 0 0.25rem; }
.muted { color: var(--muted); margin-bottom: 1.5rem; }
.tile {
  background: var(--surface); border: 1px solid var(--border); border-radius: var(--radius);
  padding: 1rem;
}
.tile h2 { margin: 0 0 0.5rem; font-size: 1rem; }
.link { color: var(--accent); }
</style>
