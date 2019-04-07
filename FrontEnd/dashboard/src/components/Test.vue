<template>
  <section id="tables">
    <h1>apples</h1>
     <mdb-btn color="primary">Primary</mdb-btn>
      <form class="md-form">
             <input type="file">
        </form>
  </section>
</template>

<script>
import { mdbBtn, mdbRow, mdbCol, mdbCard, mdbView, mdbCardBody, mdbTbl } from 'mdbvue'

export default {
  name: 'Tables',
  components: {
    mdbBtn,
    mdbRow,
    mdbCol,
    mdbCard,
    mdbView,
    mdbCardBody,
    mdbTbl
  },
  data () {
    return {}
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.card.card-cascade .view.gradient-card-header {
  padding: 1rem 1rem;
  text-align: center;
}
.card.card-cascade h3,
.card.card-cascade h4 {
  margin-bottom: 0;
}
</style>
