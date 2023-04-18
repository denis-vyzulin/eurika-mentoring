import { createRouter, createWebHashHistory } from 'vue-router'
// import SignInView from '@/views/account/SignInView.vue'

const routes = [
  {
    path: '/',
    name: 'intro',
    component: () => import('@/views/IntroView.vue')
  },
  {
    path: '/about',
    name: 'about',
    component: () => import('@/views/AboutView.vue')
  },
  {
    path: '/brand',
    name: 'brand',
    component: () => import('@/views/BrandView.vue')
  },
  {
    path: '/account',
    name: 'account',
    children: [
      {
        path: 'sign-up',
        name: 'sign-up',
        component: () => import('@/views/account/SignUpView.vue')
      }
    ]
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
