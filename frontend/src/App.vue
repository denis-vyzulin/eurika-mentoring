<template>

  <header class="header">
    <div class="header__inner _container">

      <div class="header__open-btn">
        <span></span>
        <span></span>
        <span></span>
      </div>

      <nav class="header__navigation menu">
        <router-link class="menu__item" to="/home">
          Главная
        </router-link>
        <router-link class="menu__item" to="/projects">
          Проекты
        </router-link>
        <router-link class="menu__item" to="/articles">
          Блог
        </router-link>
        <router-link class="menu__item" to="/announcements">
          Объявления
        </router-link>
        <router-link class="menu__item" to="/contacts">
          Контакты
        </router-link>
      </nav>
      <!-- / end of main navigation -->

      <div class="header__authbtn authbtn">
        <router-link class="authbtn__item" v-if="$route.name !== 'sign-up'" to="/account/sign-up">
          Регистрация
        </router-link>
        <button class="authbtn__item authbtn__item--outlined" @click="$refs.LoginPopup.openPopup()">
          <svg viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path
              d="M12.5 2.5H15.8333C16.2754 2.5 16.6993 2.67559 17.0118 2.98816C17.3244 3.30072 17.5 3.72464 17.5 4.16667V15.8333C17.5 16.2754 17.3244 16.6993 17.0118 17.0118C16.6993 17.3244 16.2754 17.5 15.8333 17.5H12.5"
              stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />
            <path d="M8.33325 14.1667L12.4999 10L8.33325 5.83333" stroke-width="2" stroke-linecap="round"
              stroke-linejoin="round" />
            <path d="M12.5 10H2.5" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />
          </svg>
          Вход
        </button>
      </div>
      <!-- / end of auth buttons -->

    </div>
  </header>
  <!-- / end of header -->

  <router-view />
  <!-- / end of main content side -->

  <footer class="footer">
    <div class="footer__inner _container">

      <div class="footer__navigation footer-tline">
        <p class="footer-tline__heading">
          НОУ «Эврика»
        </p>
        <div class="footer-tline__menu fmenu">
          <router-link class="fmenu__item" to="/home">
            Главная
          </router-link>
          <router-link class="fmenu__item" to="/projects">
            Проекты
          </router-link>
          <router-link class="fmenu__item" to="/articles">
            Блог
          </router-link>
          <router-link class="fmenu__item" to="/announcements">
            Объявления
          </router-link>
          <router-link class="fmenu__item" to="/contacts">
            Контакты
          </router-link>
        </div>
      </div>
      <!-- / end of topside -->

      <div class="footer__sepline"></div>
      <!-- / end of sepline -->

      <div class="footer__info footer-bline">
        <p class="footer-bline__copyright">
          ©2023, Научное общество учащихся «Эврика».
        </p>
        <div class="footer-bline__links flinks">
          <router-link class="flinks__item" to="/sitemap">
            Карта сайта
          </router-link>
          <router-link class="flinks__item" to="/terms-of-use">
            Условия использования
          </router-link>
          <router-link class="flinks__item" to="/privacy-policy">
            Политика конфиденциальности
          </router-link>
          <a href="https://vk.com/nn.evrica" target="_blank" class="flinks__social">
            <svg viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path
                d="M19.5466 4.82004C19.3216 5.52754 19.0183 6.14338 18.6383 6.70254L18.6541 6.67754C18.2808 7.29976 17.8349 8.01865 17.3166 8.83421C16.8722 9.4781 16.6369 9.81143 16.6108 9.83421C16.4958 9.97837 16.4158 10.155 16.3883 10.3492L16.3874 10.355C16.4099 10.5317 16.4916 10.6859 16.6108 10.8009L16.9441 11.1725C18.7274 13.0053 19.7305 14.2687 19.9533 14.9625C19.9824 15.0392 19.9991 15.1275 19.9991 15.22C19.9991 15.3817 19.9474 15.5309 19.8599 15.6534L19.8616 15.6509C19.7149 15.8017 19.5099 15.895 19.2833 15.895C19.2583 15.895 19.2324 15.8942 19.2083 15.8917H19.2116H17.0191C17.0183 15.8917 17.0166 15.8917 17.0149 15.8917C16.7341 15.8917 16.4758 15.7934 16.2733 15.63L16.2758 15.6317C15.9808 15.3892 15.7183 15.1267 15.4833 14.8417L15.4758 14.8317C15.0919 14.3978 14.7513 14.0325 14.4541 13.7359C13.4641 12.7948 12.7336 12.3242 12.2624 12.3242C12.2449 12.3225 12.2249 12.3217 12.2041 12.3217C12.0666 12.3217 11.9383 12.3642 11.8324 12.4367L11.8349 12.435C11.7483 12.5434 11.6958 12.6834 11.6958 12.8342C11.6958 12.8642 11.6974 12.8925 11.7016 12.9217V12.9184C11.6791 13.18 11.6658 13.4842 11.6658 13.7917C11.6658 13.8909 11.6674 13.9892 11.6699 14.0875V14.0734V15.0392C11.6783 15.0784 11.6833 15.1234 11.6833 15.1692C11.6833 15.3709 11.5916 15.5509 11.4483 15.67L11.4474 15.6709C11.1249 15.8184 10.7483 15.905 10.3508 15.905C10.2658 15.905 10.1824 15.9009 10.0999 15.8934L10.1108 15.8942C8.79911 15.8692 7.58244 15.485 6.54827 14.8375L6.57744 14.8542C5.31827 14.0892 4.27494 13.0934 3.47994 11.9167L3.45744 11.8817C2.70244 10.88 1.99827 9.74838 1.39827 8.55504L1.33994 8.42671C0.989108 7.75838 0.625775 6.93671 0.312441 6.09171L0.262441 5.93754C0.134941 5.55754 0.0424414 5.11588 0.00410807 4.65838L0.00244141 4.63754C0.00244141 4.21643 0.250219 4.00588 0.745775 4.00588H2.93744C2.95744 4.00421 2.98077 4.00338 3.00494 4.00338C3.21161 4.00338 3.40244 4.07421 3.55327 4.19338L3.55161 4.19171C3.71827 4.37421 3.84161 4.59838 3.90244 4.84838L3.90494 4.85838C4.30827 5.99754 4.73577 6.95421 5.22744 7.87088L5.17161 7.75671C5.57327 8.56504 6.01744 9.26088 6.52411 9.90338L6.50494 9.87754C6.94939 10.4231 7.29605 10.6959 7.54494 10.6959C7.55244 10.6967 7.56161 10.6967 7.57161 10.6967C7.69494 10.6967 7.80244 10.63 7.86077 10.53L7.86161 10.5284C7.92327 10.37 7.95911 10.1859 7.95911 9.99421C7.95911 9.95338 7.95744 9.91254 7.95411 9.87254V9.87754V6.64504C7.93661 6.26421 7.84327 5.90838 7.68744 5.58921L7.69411 5.60504C7.59077 5.38504 7.46661 5.19504 7.31911 5.02588L7.32161 5.02921C7.18494 4.89254 7.09161 4.71338 7.06244 4.51338L7.06161 4.50838C7.06161 4.36671 7.12661 4.23921 7.22827 4.15588L7.22911 4.15504C7.32994 4.06254 7.46494 4.00671 7.61244 4.00671H7.61911H11.0741C11.0924 4.00421 11.1133 4.00338 11.1349 4.00338C11.2974 4.00338 11.4433 4.07671 11.5399 4.19171L11.5408 4.19254C11.6266 4.34921 11.6774 4.53671 11.6774 4.73504C11.6774 4.76671 11.6758 4.79754 11.6733 4.82838V4.82421V9.13504C11.6716 9.15504 11.6708 9.17838 11.6708 9.20171C11.6708 9.35504 11.7133 9.49921 11.7866 9.62171L11.7849 9.61838C11.8458 9.70838 11.9474 9.76671 12.0624 9.76671H12.0633C12.2099 9.75671 12.3433 9.70837 12.4558 9.63171L12.4533 9.63338C12.6799 9.47754 12.8749 9.30004 13.0441 9.09921L13.0474 9.09504C13.5533 8.52338 14.0199 7.89171 14.4266 7.22004L14.4591 7.16171C14.7458 6.68671 15.0558 6.10171 15.3366 5.50088L15.3883 5.37838L15.7599 4.63504C15.8891 4.26338 16.2358 4.00171 16.6433 4.00171C16.6591 4.00171 16.6749 4.00171 16.6908 4.00254H16.6883H18.8808C19.473 4.00254 19.6952 4.27504 19.5474 4.82004H19.5466Z"
                fill="#5851E2" />
            </svg>
          </a>
          <a href="https://nou.ddt-chkalov.ru/" target="_blank" class="flinks__social">
            <svg viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path
                d="M10.0001 18.3333C14.6025 18.3333 18.3334 14.6023 18.3334 9.99996C18.3334 5.39759 14.6025 1.66663 10.0001 1.66663C5.39771 1.66663 1.66675 5.39759 1.66675 9.99996C1.66675 14.6023 5.39771 18.3333 10.0001 18.3333Z"
                stroke="#5851E2" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />
              <path d="M1.66675 10H18.3334" stroke="#5851E2" stroke-width="2" stroke-linecap="round"
                stroke-linejoin="round" />
              <path
                d="M10.0001 1.66663C12.0845 3.94859 13.269 6.90999 13.3334 9.99996C13.269 13.0899 12.0845 16.0513 10.0001 18.3333C7.91568 16.0513 6.73112 13.0899 6.66675 9.99996C6.73112 6.90999 7.91568 3.94859 10.0001 1.66663V1.66663Z"
                stroke="#5851E2" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />
            </svg>
          </a>
        </div>
      </div>
      <!-- / end of bottom side -->

    </div>
  </footer>
  <!-- / end of footer -->

  <PopupWindow ref="LoginPopup">
    <template v-slot:popup_content>
      <h3 class="login-content__heading">
        Авторизация на сайте
      </h3>
      <p class="login-content__subtitle">
        Еще нет аккаунта?
        <router-link to="/account/sign-up" @click="$refs.LoginPopup.closePopup()">
          Зарегистрироваться
        </router-link>
      </p>
      <form action="" class="login-content__form login-form">
        <p class="login-content__error _alert-box _hidden" id="login_error">
          Неверный логин или пароль!
        </p>
        <label for="auth_email" class="login-form__field _field">
          <p class="login-form__suptitle _field__title">
            Адрес почты
          </p>
          <input type="email" name="auth_email" ref="login_email" class="login-form__input _field__input" placeholder="ivanov-ivan@ivanovich.ru">
        </label>
        <label for="auth_pwd" class="login-form__field _field">
          <p class="login-form__suptitle _field__title">
            <span>Пароль</span>
            <router-link class="login-form__recovery" to="/account/recovery" @click="$refs.LoginPopup.closePopup()">
              Забыли пароль?
            </router-link>
          </p>
          <input type="password" name="auth_pwd" ref="login_pwd" class="login-form__input _field__input" placeholder="************">
        </label>
        <button class="login-form__btn _btn _btn--primary" type="button" @click="handleSubmit()">
          Войти
        </button>
      </form>
      <div class="login-content__sepline">
        <span>через соцсети</span>
      </div>
      <div class="login-content__socials-auth social-auth">
        <a href="#" class="social-auth__link social-auth__link--google">
          <svg class="social-auth__icon" viewBox="0 0 25 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M6.87601 10.068C6.66326 10.6899 6.55513 11.3427 6.55601 12C6.55601 12.734 6.68801 13.437 6.93201 14.086C7.23612 14.8972 7.71381 15.6321 8.33165 16.2393C8.94949 16.8466 9.69256 17.3115 10.5089 17.6015C11.3252 17.8916 12.195 17.9998 13.0575 17.9185C13.92 17.8372 14.7543 17.5684 15.502 17.131H15.503C16.6811 16.4404 17.5862 15.3661 18.067 14.088H12.72V10.132H22.325C22.5734 11.4405 22.5585 12.7854 22.281 14.088C21.8002 16.3399 20.5569 18.3568 18.761 19.798C16.9872 21.2264 14.7774 22.0035 12.5 22C10.783 22.001 9.09464 21.5597 7.59765 20.7187C6.10065 19.8778 4.84547 18.6655 3.95302 17.1986C3.06058 15.7317 2.56095 14.0597 2.50227 12.3437C2.44359 10.6276 2.82785 8.92542 3.61801 7.401C4.46098 5.77291 5.7354 4.40796 7.30189 3.4554C8.86838 2.50284 10.6666 1.99936 12.5 2C14.926 2 17.151 2.864 18.883 4.302L15.643 6.954C14.884 6.48164 14.0283 6.18643 13.1395 6.09034C12.2507 5.99424 11.3517 6.09972 10.5093 6.39894C9.66691 6.69816 8.90279 7.18342 8.27376 7.81864C7.64472 8.45386 7.16697 9.2227 6.87601 10.068Z"/>
          </svg>
          Google
        </a>
        <a href="#" class="social-auth__link social-auth__link--vk">
          <svg class="social-auth__icon" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M23.456 5.784C23.186 6.633 22.822 7.372 22.366 8.043L22.385 8.013C21.937 8.75967 21.402 9.62233 20.78 10.601C20.2467 11.3737 19.9643 11.7737 19.933 11.801C19.795 11.974 19.699 12.186 19.666 12.419L19.665 12.426C19.692 12.638 19.79 12.823 19.933 12.961L20.333 13.407C22.473 15.6063 23.6767 17.1223 23.944 17.955C23.979 18.047 23.999 18.153 23.999 18.264C23.999 18.458 23.937 18.637 23.832 18.784L23.834 18.781C23.658 18.962 23.412 19.074 23.14 19.074C23.11 19.074 23.079 19.073 23.05 19.07H23.054H20.423C20.422 19.07 20.42 19.07 20.418 19.07C20.081 19.07 19.771 18.952 19.528 18.756L19.531 18.758C19.177 18.467 18.862 18.152 18.58 17.81L18.571 17.798C18.1103 17.2773 17.7017 16.839 17.345 16.483C16.157 15.3537 15.2803 14.789 14.715 14.789C14.694 14.787 14.67 14.786 14.645 14.786C14.48 14.786 14.326 14.837 14.199 14.924L14.202 14.922C14.098 15.052 14.035 15.22 14.035 15.401C14.035 15.437 14.037 15.471 14.042 15.506V15.502C14.015 15.816 13.999 16.181 13.999 16.55C13.999 16.669 14.001 16.787 14.004 16.905V16.888V18.047C14.014 18.094 14.02 18.148 14.02 18.203C14.02 18.445 13.91 18.661 13.738 18.804L13.737 18.805C13.35 18.982 12.898 19.086 12.421 19.086C12.319 19.086 12.219 19.081 12.12 19.072L12.133 19.073C10.559 19.043 9.09899 18.582 7.85799 17.805L7.89299 17.825C6.38199 16.907 5.12999 15.712 4.17599 14.3L4.14899 14.258C3.24299 13.056 2.39799 11.698 1.67799 10.266L1.60799 10.112C1.18699 9.31 0.750991 8.324 0.374991 7.31L0.314991 7.125C0.161991 6.669 0.0509907 6.139 0.00499072 5.59L0.00299072 5.565C0.00299072 5.05967 0.300324 4.807 0.894991 4.807H3.52499C3.54899 4.805 3.57699 4.804 3.60599 4.804C3.85399 4.804 4.08299 4.889 4.26399 5.032L4.26199 5.03C4.46199 5.249 4.60999 5.518 4.68299 5.818L4.68599 5.83C5.16999 7.197 5.68299 8.345 6.27299 9.445L6.20599 9.308C6.68799 10.278 7.22099 11.113 7.82899 11.884L7.80599 11.853C8.33932 12.5077 8.75532 12.835 9.05399 12.835C9.06299 12.836 9.07399 12.836 9.08599 12.836C9.23399 12.836 9.36299 12.756 9.43299 12.636L9.43399 12.634C9.50799 12.444 9.55099 12.223 9.55099 11.993C9.55099 11.944 9.54899 11.895 9.54499 11.847V11.853V7.974C9.52399 7.517 9.41199 7.09 9.22499 6.707L9.23299 6.726C9.10899 6.462 8.95999 6.234 8.78299 6.031L8.78599 6.035C8.62199 5.871 8.50999 5.656 8.47499 5.416L8.47399 5.41C8.47399 5.24 8.55199 5.087 8.67399 4.987L8.67499 4.986C8.79599 4.875 8.95799 4.808 9.13499 4.808H9.14299H13.289C13.311 4.805 13.336 4.804 13.362 4.804C13.557 4.804 13.732 4.892 13.848 5.03L13.849 5.031C13.952 5.219 14.013 5.444 14.013 5.682C14.013 5.72 14.011 5.757 14.008 5.794V5.789V10.962C14.006 10.986 14.005 11.014 14.005 11.042C14.005 11.226 14.056 11.399 14.144 11.546L14.142 11.542C14.215 11.65 14.337 11.72 14.475 11.72H14.476C14.652 11.708 14.812 11.65 14.947 11.558L14.944 11.56C15.216 11.373 15.45 11.16 15.653 10.919L15.657 10.914C16.264 10.228 16.824 9.47 17.312 8.664L17.351 8.594C17.695 8.024 18.067 7.322 18.404 6.601L18.466 6.454L18.912 5.562C19.067 5.116 19.483 4.802 19.972 4.802C19.991 4.802 20.01 4.802 20.029 4.803H20.026H22.657C23.3677 4.803 23.6343 5.13 23.457 5.784H23.456Z"/>
          </svg>
          Вконтакте
        </a>
        <a href="#" class="social-auth__link social-auth__link--tg">
          <svg class="social-auth__icon" viewBox="0 0 25 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M22.9392 4.62225L19.7705 19.566C19.5312 20.6205 18.908 20.883 18.0222 20.3865L13.1937 16.8285L10.8642 19.0695C10.6062 19.3275 10.391 19.5428 9.89374 19.5428L10.241 14.6258L19.1892 6.54C19.5785 6.1935 19.1045 6.00075 18.5847 6.348L7.52224 13.314L2.75974 11.823C1.72399 11.4998 1.70524 10.7873 2.97574 10.29L21.6035 3.11325C22.466 2.79 23.2205 3.30525 22.9392 4.623V4.62225Z"/>
          </svg>
          Telegram
        </a>
      </div>
    </template>
  </PopupWindow>
  <!-- / end of login popup -->
</template>

<style lang="scss">
// Import FiraSans-font from GoogleFonts
@import url('https://fonts.googleapis.com/css2?family=Fira+Sans:wght@300;400;500;600;700&display=swap');

// Import base styles
@import '@/assets/scss/styles.scss';
</style>

<script>
// Connect all components
import PopupWindow from '@/components/PopupWindow.vue'
import { mapMutations } from 'vuex'
import axios from 'axios'

export default {
  name: 'App',
  components: {
    PopupWindow
  },
  data () {
    return {
      formValidate: {
        email: '',
        password: ''
      },
      token: ''
    }
  },
  methods: {
    ...mapMutations(['changeLogin']),
    handleSubmit () {
      this.formValidate.email = this.$refs.login_email.value
      this.formValidate.password = this.$refs.login_pwd.value
      if (
        this.formValidate.email === '' ||
        this.formValidate.password === ''
      ) {
        alert('Login failed!')
      } else {
        const headers = {
          'Content-type': 'application/json; charset=utf-8'
        }
        axios.post('http://127.0.0.1:8000/login/', this.formValidate, headers)
          .then((res) => {
            console.log(res.data)
            this.changeLogin({ token: res.data })
            this.token = res.data
            localStorage.setItem('token', this.token)
            axios.post('http://127.0.0.1:8000/api/v1/users/', this.formValidate, headers)
              .then((userInfo) => {
                console.log(userInfo.data)
              })
          })
      }
    }
  }
}

document.title = 'Эврика – наставничество | Веб-сервис для поиска проектов'
console.log()
</script>
