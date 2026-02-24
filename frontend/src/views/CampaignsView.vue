<template>
  <div class="campaigns">
    <h1>Campaigns</h1>
    <p v-if="loading">Loading…</p>
    <p v-else-if="error" class="error">{{ error }}</p>
    <ul v-else class="list">
      <li v-for="c in campaigns" :key="c.id" class="card">
        <router-link :to="`/campaigns/${c.id}`" class="title">{{ c.name }}</router-link>
        <span class="slug">{{ c.slug }}</span>
        <p v-if="c.description" class="desc">{{ c.description }}</p>
        <span :class="['badge', c.is_active ? 'active' : 'inactive']">
          {{ c.is_active ? 'Active' : 'Inactive' }}
        </span>
      </li>
    </ul>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import api from '../api'

const campaigns = ref([])
const loading = ref(true)
const error = ref('')

onMounted(async () => {
  try {
    const { data } = await api.get('/api/campaigns/')
    campaigns.value = data.results ?? data
  } catch (e) {
    error.value = e.response?.data?.detail || e.message || 'Failed to load campaigns'
  } finally {
    loading.value = false
  }
})
</script>

<style scoped>
.campaigns h1 { margin: 0 0 1rem; }
.list { list-style: none; padding: 0; margin: 0; display: flex; flex-direction: column; gap: 0.75rem; }
.card {
  background: var(--surface); border: 1px solid var(--border); border-radius: var(--radius);
  padding: 1rem;
}
.title { font-weight: 600; color: var(--accent); text-decoration: none; }
.slug { color: var(--muted); font-size: 0.85rem; margin-left: 0.5rem; }
.desc { margin: 0.5rem 0 0; color: var(--muted); font-size: 0.9rem; }
.badge { font-size: 0.75rem; padding: 0.2rem 0.5rem; border-radius: 4px; margin-top: 0.5rem; display: inline-block; }
.badge.active { background: #238636; color: #fff; }
.badge.inactive { background: var(--border); color: var(--muted); }
.error { color: var(--danger); }
</style>
