import Vue from 'vue'
import Router from 'vue-router'
import Portfolio from '@/components/Portfolio'
import HomePage from '@/components/HomePage'
import Betas from '@/components/Betas'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/Portfolio',
      name: 'Portfolio',
      component: Portfolio
    },
    {
      path: '/',
      name: 'HomePage',
      component: HomePage
    },
    {
      path: '/Betas',
      name: 'Betas',
      component: Betas
    }

  ]
})
