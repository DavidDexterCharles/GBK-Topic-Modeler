import Vue from 'vue'
import Router from 'vue-router'
import Dashboard from '@/components/Dashboard'
import Profile from '@/components/Profile'
import Tables from '@/components/Tables'
import Maps from '@/components/Maps'
import BadGateway from '@/components/BadGateway'
import Test from '@/components/Test'
import Model from '@/components/Model'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/dashboard',
      name: 'Dashboard',
      component: Dashboard,
      props: { page: 1 },
      alias: '/'
    },
    {
      path: '/profile',
      name: 'Profile',
      props: { page: 2 },
      component: Profile
    },
    {
      path: '/tables',
      name: 'Tables',
      props: { page: 3 },
      component: Tables
    },
    {
      path: '/maps',
      name: 'Maps',
      props: { page: 4 },
      component: Maps
    },
    {
      path: '/404',
      name: 'BadGateway',
      props: { page: 5 },
      component: BadGateway
    },
    {
      path: '*',
      props: { page: 5 },
      redirect: '/404'
    },
    {
      path: '/test',
      name: 'Test',
      props: { page: 6 },
      component: Test
    },
    {
      path: '/models',
      name: 'Models',
      props: { page: 7 },
      component: Model
    }
  ]
})
