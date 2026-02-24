<template>
  <div class="app">
    <header v-if="authStore.isAuthenticated" class="header">
      <router-link to="/" class="brand">Volleyball Marketing</router-link>
      <nav>
        <router-link to="/">Dashboard</router-link>
        <router-link to="/campaigns">Campaigns</router-link>
        <span class="user">{{ authStore.user?.email }}</span>
        <button type="button" class="btn-logout" @click="authStore.logout">Logout</button>
      </nav>
    </header>
    <main class="main">
      <router-view />
    </main>
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useAuthStore } from './stores/auth'

const authStore = useAuthStore()
onMounted(() => authStore.restoreSession())
</script>

<style>
:root {
  --bg: #0f1419;
  --surface: #1a2332;
  --border: #2d3a4f;
  --text: #e6edf3;
  --muted: #8b949e;
  --accent: #58a6ff;
  --accent-hover: #79b8ff;
  --danger: #f85149;
  --radius: 8px;
}
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Segoe UI', system-ui, sans-serif; background: var(--bg); color: var(--text); min-height: 100vh; }
.app { min-height: 100vh; display: flex; flex-direction: column; }
.header {
  display: flex; align-items: center; justify-content: space-between;
  padding: 0.75rem 1.5rem; background: var(--surface); border-bottom: 1px solid var(--border);
}
.brand { font-weight: 700; font-size: 1.1rem; color: var(--text); text-decoration: none; }
.header nav { display: flex; align-items: center; gap: 1rem; }
.header nav a { color: var(--muted); text-decoration: none; }
.header nav a.router-link-active { color: var(--accent); }
.user { color: var(--muted); font-size: 0.9rem; }
.btn-logout {
  background: transparent; color: var(--muted); border: 1px solid var(--border);
  padding: 0.35rem 0.75rem; border-radius: var(--radius); cursor: pointer;
}
.btn-logout:hover { color: var(--text); border-color: var(--muted); }
.main { flex: 1; padding: 1.5rem; max-width: 1200px; margin: 0 auto; width: 100%; }
</style>
