<template>
  <div class="auth-page">
    <div class="card">
      <h1>Log in</h1>
      <form @submit.prevent="submit">
        <div class="field">
          <label>Username</label>
          <input v-model="username" type="text" required autocomplete="username" />
        </div>
        <div class="field">
          <label>Password</label>
          <input v-model="password" type="password" required autocomplete="current-password" />
        </div>
        <p v-if="error" class="error">{{ error }}</p>
        <button type="submit" class="btn" :disabled="loading">Log in</button>
      </form>
      <p class="foot">No account? <router-link to="/register">Register</router-link></p>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '../stores/auth'

const router = useRouter()
const authStore = useAuthStore()
const username = ref('')
const password = ref('')
const error = ref('')
const loading = ref(false)

async function submit() {
  error.value = ''
  loading.value = true
  try {
    await authStore.login(username.value, password.value)
    router.push('/')
  } catch (e) {
    error.value = e.response?.data?.detail || e.response?.data?.username?.[0] || e.message || 'Login failed'
  } finally {
    loading.value = false
  }
}
</script>

<style scoped>
.auth-page { display: flex; justify-content: center; align-items: center; min-height: 60vh; }
.card {
  width: 100%; max-width: 360px; padding: 1.5rem; background: var(--surface);
  border: 1px solid var(--border); border-radius: var(--radius);
}
.card h1 { margin: 0 0 1rem; font-size: 1.25rem; }
.field { margin-bottom: 1rem; }
.field label { display: block; margin-bottom: 0.25rem; color: var(--muted); font-size: 0.9rem; }
.field input {
  width: 100%; padding: 0.5rem 0.75rem; background: var(--bg); border: 1px solid var(--border);
  border-radius: var(--radius); color: var(--text);
}
.error { color: var(--danger); font-size: 0.9rem; margin-bottom: 0.5rem; }
.btn {
  width: 100%; padding: 0.6rem; background: var(--accent); color: #fff; border: none;
  border-radius: var(--radius); font-weight: 600; cursor: pointer;
}
.btn:hover:not(:disabled) { background: var(--accent-hover); }
.btn:disabled { opacity: 0.6; cursor: not-allowed; }
.foot { margin-top: 1rem; color: var(--muted); font-size: 0.9rem; }
.foot a { color: var(--accent); }
</style>
