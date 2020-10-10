// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
import './../node_modules/bulma/css/bulma.css'
import Buefy from 'buefy'
import 'buefy/dist/buefy.css'

// eslint-disable-next-line no-unused-vars
import ZingGrid from 'zinggrid'
Vue.component('zinggrid')

// Import the ZingGrid library, By default, the ZingGrid library registers itself as a web component.

Vue.use(Buefy)
Vue.use(BootstrapVue)
// Optionally install the BootstrapVue icon components plugin
Vue.use(IconsPlugin)

// Import the ZingGrid library, By default, the ZingGrid library registers itself as a web component.

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
