<template>
  <transition name="fade" mode="out-in" :duration="400" :css="false">
    <div class="popup" v-if="show">
      <div class="popup__backdrop" @click="closePopup()"/>
        <div class="popup__content popup-content">
          <button type="button" class="popup-content__close-btn" @click="closePopup()">
            &times;
          </button>
          <slot name="popup_content"></slot>
        </div>
        <!-- / end of popup content -->
    </div>
  </transition>
</template>

<script>
export default {
  name: 'PopupWindow',
  data () {
    return {
      show: false
    }
  },
  methods: {
    closePopup () {
      this.show = false
      document.querySelector('body').classList.remove('_noscroll')
    },
    openPopup () {
      this.show = true
      document.querySelector('body').classList.add('_noscroll')
    }
  }
}
</script>

<style scoped lang="scss">
</style>
