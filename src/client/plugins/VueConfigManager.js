"use strict";

// This is your plugin object. It can be exported to be used anywhere.
const VueConfigManager = {
    // The install method is all that needs to exist on the plugin object.
    // It takes the global Vue object as well as user-defined options.
    install(Vue, options) {
        Vue.prototype.$config = options.config;

        Vue.prototype.$localeRoute = function(uri) {
            return options.config.locale.base_uri + uri;
        }

        // We call Vue.mixin() here to inject functionality into all components.
        Vue.mixin({
            // Anything added to a mixin will be injected into all components.
            // In this case, the mounted() method runs when the component is added to the DOM.
            mounted() {
                //console.log('CDNManager Mounted!');
            }
        });
    }
};

export default VueConfigManager;

// Automatic installation if Vue has been added to the global scope.
if (typeof window !== 'undefined' && window.Vue) {
    window.Vue.use(VueConfigManager)
}