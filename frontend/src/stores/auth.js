import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import api from '../api'

const ACCESS_KEY = 'volleyball_access'
const REFRESH_KEY = 'volleyball_refresh'

export const useAuthStore = defineStore('auth', () => {
  const accessToken = ref(localStorage.getItem(ACCESS_KEY))
  const refreshToken = ref(localStorage.getItem(REFRESH_KEY))
  const user = ref(null)

  const isAuthenticated = computed(() => !!accessToken.value)

  function setTokens(access, refresh) {
    accessToken.value = access
    refreshToken.value = refresh
    if (access) localStorage.setItem(ACCESS_KEY, access)
    else localStorage.removeItem(ACCESS_KEY)
    if (refresh) localStorage.setItem(REFRESH_KEY, refresh)
    else localStorage.removeItem(REFRESH_KEY)
  }

  function setUser(u) {
    user.value = u
  }

  async function restoreSession() {
    if (!accessToken.value || user.value) return
    try {
      const { data } = await api.get('/api/auth/me/')
      user.value = data
    } catch {
      await tryRefresh()
    }
  }

  async function tryRefresh() {
    if (!refreshToken.value) return logout()
    try {
      const { data } = await api.post('/api/auth/refresh/', { refresh: refreshToken.value })
      setTokens(data.access, data.refresh || refreshToken.value)
      const me = await api.get('/api/auth/me/')
      user.value = me.data
    } catch {
      logout()
    }
  }

  async function login(username, password) {
    const { data } = await api.post('/api/auth/login/', { username, password })
    setTokens(data.access, data.refresh)
    user.value = data.user
  }

  async function register(payload) {
    const { data } = await api.post('/api/auth/register/', payload)
    user.value = data.user
    if (data.access) setTokens(data.access, data.refresh)
  }

  function logout() {
    setTokens(null, null)
    user.value = null
  }

  return {
    user,
    isAuthenticated,
    login,
    register,
    logout,
    restoreSession,
    tryRefresh,
    getAccessToken: () => accessToken.value,
  }
})
