<template>
    <main role="main" class="container">
      <div class="starter-template">
          <Menu></Menu>
          <Home></Home>
      </div>
    </main>
</template>

<script>
    import Home from './Home.vue'
    import Menu from './Menu.vue'
    export default {
        name: "Layout",
        mounted() {},
        data() { return {} },
        methods: {},
        components:{
            Menu,
            Home
        }
    }
</script>

<style scoped>

</style>