<template>
  <div id="app">
    <Elements />
  </div>
</template>

<script>
import Elements from './components/elements.vue'
export default {
  name: 'App',
  components: {
    Elements
  }
}
</script>

<style>
  #app {
    font-family: 'Avenir', 'Helvetica', 'Arial', sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    margin-top: 60px;
  }
</style>
