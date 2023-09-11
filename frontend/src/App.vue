<template>
  <TheHeader />

  <router-view />

  <TheFooter />
</template>

<style lang="scss">
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700&family=Ubuntu:wght@500;700&display=swap');
@import '@/styles/general.scss';
</style>

<script>
import TheHeader from '@/components/TheHeader.vue'
import TheFooter from '@/components/TheFooter.vue'

export default {
  name: 'App',
  components: {
    TheHeader,
    TheFooter
  }
}
</script>
