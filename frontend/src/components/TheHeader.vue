<template>
  <header class="header">
    <div class="header__inner _container">
      <nav class="menu header__menu">
        <router-link to="/" class="menu__item">
          Главная
        </router-link>
        <router-link to="/" class="menu__item">
          Проекты
        </router-link>
        <router-link to="/" class="menu__item">
          Контакты
        </router-link>
      </nav>
      <!-- / end of navigation -->

      <div class="btns header__btns">
        <router-link to="/" class="btns__item">
          Регистрация
        </router-link>
        <router-link to="/" class="btns__item btns__item--icon">
          <svg class="btns__icon" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M12.5 2.5H15.8333C16.2754 2.5 16.6993 2.67559 17.0118 2.98816C17.3244 3.30072 17.5 3.72464 17.5 4.16667V15.8333C17.5 16.2754 17.3244 16.6993 17.0118 17.0118C16.6993 17.3244 16.2754 17.5 15.8333 17.5H12.5" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
            <path d="M8.33325 14.1667L12.4999 10L8.33325 5.83334" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
            <path d="M12.5 10H2.5" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>
          Вход
        </router-link>
      </div>
      <!-- / end of buttons -->
    </div>
  </header>
</template>

<style lang="scss" scoped>
@import '@/styles/components/header';
</style>
