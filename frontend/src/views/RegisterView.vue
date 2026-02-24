<template>
  <div class="auth-page">
    <div class="card">
      <h1>Register</h1>
      <form @submit.prevent="submit">
        <div class="field">
          <label>Username</label>
          <input v-model="form.username" type="text" required autocomplete="username" />
        </div>
        <div class="field">
          <label>Email</label>
          <input v-model="form.email" type="email" required autocomplete="email" />
        </div>
        <div class="field">
          <label>Password</label>
          <input v-model="form.password" type="password" required autocomplete="new-password" />
        </div>
        <div class="field">
          <label>Confirm password</label>
          <input v-model="form.password_confirm" type="password" required autocomplete="new-password" />
        </div>
        <p v-if="error" class="error">{{ error }}</p>
        <button type="submit" class="btn" :disabled="loading">Register</button>
      </form>
      <p class="foot">Already have an account? <router-link to="/login">Log in</router-link></p>
    </div>
  </div>
</template>

<script setup>
import { ref, reactive } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '../stores/auth'

const router = useRouter()
const authStore = useAuthStore()
const form = reactive({
  username: '',
  email: '',
  password: '',
  password_confirm: '',
})
const error = ref('')
const loading = ref(false)

async function submit() {
  if (form.password !== form.password_confirm) {
    error.value = 'Passwords do not match'
    return
  }
  error.value = ''
  loading.value = true
  try {
    await authStore.register(form)
    router.push('/')
  } catch (e) {
    const d = e.response?.data
    error.value = d?.password?.[0] || d?.email?.[0] || d?.username?.[0] || e.message || 'Registration failed'
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
