<template>
  <div class="elements__container elist">
    <h1 class="elist__title">List of elements</h1>
    <ul class="elist__item elist-item">
      <li v-for="el in elements" :key="el.id" class="elist-item__info">
        <p>Name: {{ el.name }}</p>
        <p>Surname: {{ el.surname }}</p>
        <p>Age: {{ el.age }}</p>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  data () {
    return {
      elements: ['']
    }
  },
  methods: {
    async getData () {
      try {
        const response = await this.$http.get('http://127.0.0.1:8000/api/')
        this.elements = response.data
      } catch (error) {
        console.log(error)
      }
    }
  },
  created () {
    this.getData()
  }
}
</script>
