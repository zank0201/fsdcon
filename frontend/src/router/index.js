import Vue from 'vue'
import Router from 'vue-router'
import IndexSummary from '@/components/IndexSummary'
import HomePage from '@/components/HomePage'
import Portfolio from '@/components/Portfolio'
import PortfolioTime from '@/components/PortfolioTime'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/IndexSummary',
      name: 'IndexSummary',
      component: IndexSummary
    },
    {
      path: '/',
      name: 'HomePage',
      component: HomePage
    },
    {
      path: '/Portfolio',
      name: 'Portfolio',
      component: Portfolio
    },
    {
      path: '/PortfolioTime',
      name: 'PortfolioTime',
      component: PortfolioTime
    }

  ]
})
