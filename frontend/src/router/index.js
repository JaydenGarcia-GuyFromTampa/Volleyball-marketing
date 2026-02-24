import { createRouter, createWebHistory } from 'vue-router'
import { useAuthStore } from '../stores/auth'

const router = createRouter({
  history: createWebHistory('/'),
  routes: [
    { path: '/', name: 'Home', component: () => import('../views/DashboardView.vue'), meta: { requiresAuth: true } },
    { path: '/login', name: 'Login', component: () => import('../views/LoginView.vue'), meta: { guest: true } },
    { path: '/register', name: 'Register', component: () => import('../views/RegisterView.vue'), meta: { guest: true } },
    { path: '/campaigns', name: 'Campaigns', component: () => import('../views/CampaignsView.vue'), meta: { requiresAuth: true } },
  ],
})

router.beforeEach((to, _from, next) => {
  const auth = useAuthStore()
  auth.restoreSession()
  if (to.meta.requiresAuth && !auth.isAuthenticated) return next({ name: 'Login' })
  if (to.meta.guest && auth.isAuthenticated) return next({ name: 'Home' })
  next()
})

export default router
