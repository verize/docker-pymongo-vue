"use strict";

import config from './config';
import Vue from 'vue';
import router from "./router.js";
import VueResource from "vue-resource";
import VueConfigManager from "./plugins/VueConfigManager";

Vue.use(VueResource);
Vue.use(VueConfigManager, {
    config: config
});

new Vue({
    router: router,
    render: h => h("router-view")
}).$mount('#app');


$(window).on("load", function() {
    console.log("Running App in mode: " + config.environment);
    console.log("Copyright (c) 2017-2018 Verize.com - All rights reserved.");
});



