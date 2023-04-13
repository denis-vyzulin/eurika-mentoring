<template>

  <section class="colours _container">
    <h2 class="section__heading">Цветовая палитра</h2>
    <div class="colours__list colours-list">

      <div class="colours-list__item colours-item colours-item--primary">
        <p class="colours-item__subtitle">base</p>
        <p class="colours-item__title">primary</p>
        <p class="colours-item__hex">#5851E2</p>
      </div>
      <!-- / end of colour -->

      <div class="colours-list__item colours-item colours-item--secondary">
        <p class="colours-item__subtitle">base</p>
        <p class="colours-item__title">secondary</p>
        <p class="colours-item__hex">#8851E2</p>
      </div>
      <!-- / end of colour -->

      <div class="colours-list__item colours-item colours-item--tertiary">
        <p class="colours-item__subtitle">base</p>
        <p class="colours-item__title">tertiary</p>
        <p class="colours-item__hex">#8C86FF</p>
      </div>
      <!-- / end of colour -->

      <div class="colours-list__item colours-item colours-item--heading">
        <p class="colours-item__subtitle">typography</p>
        <p class="colours-item__title">heading</p>
        <p class="colours-item__hex">#1D1C39</p>
      </div>
      <!-- / end of colour -->

      <div class="colours-list__item colours-item colours-item--paragraph">
        <p class="colours-item__subtitle">typography</p>
        <p class="colours-item__title">plain text</p>
        <p class="colours-item__hex">#6B6A85</p>
      </div>
      <!-- / end of colour -->

      <div class="colours-list__item colours-item colours-item--lborder">
        <p class="colours-item__subtitle">border</p>
        <p class="colours-item__title">light</p>
        <p class="colours-item__hex">#EBEBF3</p>
      </div>
      <!-- / end of colour -->

      <div class="colours-list__item colours-item colours-item--dborder">
        <p class="colours-item__subtitle">border</p>
        <p class="colours-item__title">dark</p>
        <p class="colours-item__hex">#9997B5</p>
      </div>
      <!-- / end of colour -->

      <div class="colours-list__item colours-item colours-item--success">
        <p class="colours-item__subtitle">technical</p>
        <p class="colours-item__title">success</p>
        <p class="colours-item__hex">#51E271</p>
      </div>
      <!-- / end of colour -->

      <div class="colours-list__item colours-item colours-item--warning">
        <p class="colours-item__subtitle">technical</p>
        <p class="colours-item__title">warning</p>
        <p class="colours-item__hex">#E29751</p>
      </div>
      <!-- / end of colour -->

      <div class="colours-list__item colours-item colours-item--danger">
        <p class="colours-item__subtitle">technical</p>
        <p class="colours-item__title">danger</p>
        <p class="colours-item__hex">#E25151</p>
      </div>
      <!-- / end of colour -->

    </div>
  </section>

</template>

<style lang="scss">
.section__heading {
  margin-bottom: 16px;
  color: var(--heading);
  font-size: 28px;
}

// ==> Colours styles
.colours {
  margin-top: 36px;
  margin-bottom: 48px;

  &__list {
    display: flex;
    align-items: flex-start;
    justify-content: flex-start;
    flex-wrap: wrap;
  }
}

// ==> Style of colours list item
.colours-item {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  justify-content: flex-end;
  height: 140px;
  width: 140px;
  padding: 16px;

  &__subtitle {
    margin: 0;
    margin-bottom: 2px;
    line-height: 1;
    font-size: 11px;
    font-weight: 500;
  }

  &__title {
    margin: 0;
    line-height: 1;
    font-size: 15px;
    font-weight: 600;
    text-transform: capitalize;
  }

  &__hex {
    margin: 0;
    margin-top: 4px;
    font-size: 13px;
  }

  &__subtitle,
  &__title,
  &__hex {
    color: inherit;
  }

  &--primary {
    color: white;
    background-color: var(--primary);
  }

  &--secondary {
    color: white;
    background-color: var(--secondary);
  }

  &--tertiary {
    color: white;
    background-color: var(--tertiary);
  }

  &--heading {
    color: white;
    background-color: var(--heading);
  }

  &--paragraph {
    color: white;
    background-color: var(--paragraph);
  }

  &--success {
    color: white;
    background-color: var(--success);
  }

  &--warning {
    color: white;
    background-color: var(--warning);
  }

  &--danger {
    color: white;
    background-color: var(--danger);
  }

  &--lborder {
    color: var(--paragraph);
    background-color: var(--border-base);
  }

  &--dborder {
    color: white;
    background-color: var(--border-dark);
  }

}
</style>
