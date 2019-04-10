import Vue from 'vue'
import Router from 'vue-router'
import Dashboard from '@/components/Dashboard'
import Profile from '@/components/Profile'
import Tables from '@/components/Tables'
import Maps from '@/components/Maps'
import BadGateway from '@/components/BadGateway'
import Classifiers from '@/components/Classifiers'
import Models from '@/components/Models'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/models',
      name: 'Models',
      props: { page: 1 },
      component: Models,
      alias: '/'
    },
    {
      path: '/classifiers',
      name: 'Classifiers',
      props: { page: 2 },
      component: Classifiers
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
      path: '/profile',
      name: 'Profile',
      props: { page: 6 },
      component: Profile
    },
    {
      path: '/dashboard',
      name: 'Dashboard',
      props: { page: 7 },
      component: Dashboard
    }
  ]
})
