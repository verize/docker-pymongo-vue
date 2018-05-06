"use strict";

import Vue from 'vue'
import VueRouter from 'vue-router'
import VueResource from 'vue-resource'
import VueConfigManager from "./plugins/VueConfigManager";
import config from './config';

import Layout from './components/Layout.vue'

Vue.use(VueRouter);
Vue.use(VueResource);
Vue.use(VueConfigManager, {
    config: config
});

const router = new VueRouter({
    mode: 'history',
    saveScrollPosition: false,
    routes: [
        { name: 'homepage', path: '/', component: Layout },
    ]
});

// GLobal AFTER hooks:
router.afterEach((to, from) => {
    // This fires after each route is entered.
    console.log(`Just moved from '${from.path}' to '${to.path}'`)
});

export default router;