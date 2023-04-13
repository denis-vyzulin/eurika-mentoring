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
        <router-link class="authbtn__item" to="/account/sign-up">
          Регистрация
        </router-link>
        <router-link class="authbtn__item authbtn__item--outlined" to="/account/sign-in">
          <svg viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path
              d="M12.5 2.5H15.8333C16.2754 2.5 16.6993 2.67559 17.0118 2.98816C17.3244 3.30072 17.5 3.72464 17.5 4.16667V15.8333C17.5 16.2754 17.3244 16.6993 17.0118 17.0118C16.6993 17.3244 16.2754 17.5 15.8333 17.5H12.5"
              stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />
            <path d="M8.33325 14.1667L12.4999 10L8.33325 5.83333" stroke-width="2" stroke-linecap="round"
              stroke-linejoin="round" />
            <path d="M12.5 10H2.5" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />
          </svg>
          Вход
        </router-link>
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

</template>

<style lang="scss">
// Import FiraSans-font from GoogleFonts
@import url('https://fonts.googleapis.com/css2?family=Fira+Sans:wght@300;400;500;600;700&display=swap');

// Import base styles
@import '@/assets/scss/styles.scss';
</style>

<script>
document.title = 'Эврика – наставничество | Веб-сервис для поиска проектов'
</script>
