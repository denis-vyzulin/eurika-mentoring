<template>
  <section class="intro">
    <div class="intro__inner intro-content _container">
      <div class="intro-content__description">
        <h1 class="intro-content__heading">
          «Эврика — наставничество»
        </h1>
        <p class="intro-content__subtitle">
          Удобный помощник в&nbsp;поиске интересных проектов для&nbsp;учеников, опубликованных преподавателями Нижегородских школ и&nbsp;вузов
        </p>
        <a href="" class="intro-content__btn _btn _btn--primary">
          Узнать больше
        </a>
      </div>
      <img src="@/assets/img/introduction.png" alt="" class="intro-content__image">
    </div>
  </section>
  <!-- / end of introduction block -->

  <section class="advantages">
    <div class="advantages__inner advantages-list _container">
      <div class="advantages-list__item">
        <h2 class="advantages-list__heading">
          134 секции
        </h2>
        <p class="advantages-list__text">
          Различных направлений действует на базах вузов
        </p>
      </div>
      <div class="advantages-list__item">
        <h2 class="advantages-list__heading">
          53 раза
        </h2>
        <p class="advantages-list__text">
          Проводились ежегодные конференции НОУ
        </p>
      </div>
      <div class="advantages-list__item">
        <h2 class="advantages-list__heading">
          9 вузов
        </h2>
        <p class="advantages-list__text">
          Нижнего Новгорода сотрудничают с нами
        </p>
      </div>
    </div>
  </section>
  <!-- / end of advantages of evrika -->

  <section class="join">
    <div class="join__inner join-content _container">
      <div class="join-content__description">
        <h3 class="join-content__heading">
          Станьте частью Научного общества учащихся «Эврика»
        </h3>
        <router-link class="join-content__btn _btn _btn--primary" to="/account/sign-in">
          Присоединиться
        </router-link>
      </div>
      <img src="@/assets/img/join-us.png" alt="" class="join-content__image">
    </div>
  </section>
  <!-- / end of join us -->
</template>

<style scoped lang="scss">
@import '@/assets/scss/core/_mixins.scss';

.intro-content {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  width: 100%;
  padding-top: 32px;
  padding-bottom: 32px;

  &__description {
    max-width: 540px;
  }

  &__heading {
    margin-top: 10%;
    @include adaptive_font_size(36, 24);
  }

  &__subtitle {
    @include adaptive_font_size(18, 16);
  }

  &__image {
    max-height: 420px;
  }

  &__btn {
    margin-top: 16px;
  }
}

.advantages {
  margin-top: 32px;
}

.advantages-list {
  display: flex;
  align-items: center;
  justify-content: space-between;

  &__item {
    flex: 0 0 32%;
    padding: 24px;
    background-color: var(--background-area);
    border-radius: 32px;
  }

  &__heading {
    text-align: center;
  }

  &__text {
    max-width: 200px;
    margin: 0 auto;
    text-align: center;
    text-transform: lowercase;
  }
}

.join {
  margin-top: 48px;

  &__inner {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 16px 108px;
    background-color: var(--background-area);
    border-radius: 48px;
  }
}

.join-content {
  &__heading {
    max-width: 480px;
    line-height: 1.375;
    @include adaptive_font_size(32, 20);
  }
  &__btn {
    margin-top: 16px;
  }
}
</style>

<script>
export default {
  name: 'IntroView'
}
</script>
