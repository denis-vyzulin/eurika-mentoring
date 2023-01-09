<template>
  <header class="header">
    <div class="header__inner _container">
      <!-- <img src="" alt="" class="header__logo"> -->
      <nav class="header__navigation menu">
        <router-link class="menu__item" to="/project">
          Проекты
        </router-link>
        <router-link class="menu__item" to="/news">
          Новости
        </router-link>
        <router-link class="menu__item" to="/documents">
          Документы
        </router-link>
        <router-link class="menu__item" to="/contacts">
          Контакты
        </router-link>
      </nav>
      <div class="header__auth-btn auth-btn">
        <router-link class="auth-btn__item" to="/contacts">
          Регистрация
        </router-link>
        <router-link class="auth-btn__item auth-btn-item" to="/contacts">
          <svg class="auth-btn-item__svg-icon" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path
              d="M15 3H19C19.5304 3 20.0391 3.21071 20.4142 3.58579C20.7893 3.96086 21 4.46957 21 5V19C21 19.5304 20.7893 20.0391 20.4142 20.4142C20.0391 20.7893 19.5304 21 19 21H15"
              stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />
            <path d="M10 17L15 12L10 7" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />
            <path d="M15 12H3" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />
          </svg>
          Вход
        </router-link>
      </div>
    </div>
  </header>

  <router-view />
</template>

<style lang="scss">
@import url('https://fonts.googleapis.com/css2?family=Fira+Sans:wght@300;400;500;600;700&display=swap');

// Colour Palette
$background-base: #EFEFF3;
$primary-base: #5048E5;
$plain-text: #6B6A85;
$headings: #1D1C39;

// Basic styles
body {
  margin: 0;
  padding: 0;
  color: $plain-text;
  line-height: 1.5;
  font-family: 'Fira Sans', sans-serif;
  background-color: $background-base;
}

._container {
  display: block;

  max-width: 1240px;
  margin: 0 auto;
  padding-left: 15px;
  padding-right: 15px;
}

// Header
.header {
  padding-top: 16px;
  padding-bottom: 16px;
  background-color: white;

  &__inner {
    display: flex;
    align-items: center;
    justify-content: space-between;
  }
}

.menu {
  &__item {
    padding: 8px;
    color: $plain-text;
    transition: color .3s;
    text-decoration: none;

    &:hover {
      color: $primary-base;
    }

    &:not(:last-child) {
      margin-right: 32px;
    }
  }
}

.auth-btn {
  display: flex;
  align-items: center;
  justify-content: center;

  &__item {
    display: inline-block;
    color: $plain-text;
    text-decoration: none;

    &:first-child {
      margin-right: 24px;
    }

    &:last-child {
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 8px 24px 8px 20px;
      color: white;
      font-weight: 500;
      border-radius: 12px;
      background-color: $primary-base;
    }
  }
}

.auth-btn-item {
  &__svg-icon {
    width: 20px;
    margin-right: 8px;

    path {
      stroke: white;
    }
  }
}
</style>
