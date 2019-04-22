<template>
  <!--https://github.com/vuejs/vetur/issues/261-->
  <div class="container">
    <div class="row">
      <div class="col-sm-2 mb-1" v-for="ninja in ninjas" v-on:click="ninja.show = !ninja.show" :key="ninja.id">
        <div class="card">
          <div class="card-body">
            <h4 class="card-title"><a>{{ ninja.name }}</a></h4>
            <!--<p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>-->
            <!--<a href="#" class="btn btn-primary">Button</a>-->
            <!--<h2>{{ ninja.name }}</h2>-->
            <p v-show="ninja.show">{{ ninja.speciality }}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
/* eslint-disable */
  export default {
      data(){
          return{
              ninjas: [
                  {name: 'Ryu', speciality: 'Vue Components', show: false},
                  {name: 'Crystal', speciality: 'HTML Wizardry', show: false},
                  {name: 'Hitoshi', speciality: 'Click Events', show: false},
                  {name: 'Tango', speciality: 'Conditionals', show: false},
                  {name: 'Kami', speciality: 'Webpack', show: false},
                  {name: 'Yoshi', speciality: 'Data Diggin', show: false},
                  {name: 'Test1', speciality: '1', show: false},
                  {name: 'Test2', speciality: '2', show: false},
                  {name: 'Test3', speciality: '3', show: false}
              ]
          }
      }
  }
</script>
<style scoped>

/*#ninjas{*/
/*    width: 100%;*/
/*    max-width: 1200px;*/
/*    margin: 40px auto;*/
/*    padding: 0 20px;*/
/*    box-sizing: border-box;*/
/*}*/
/*ul{*/
/*    display: flex;*/
/*    flex-wrap: wrap;*/
/*    list-style-type: none;*/
/*    padding: 0;*/
/*}*/
/*li{*/
/*    flex-grow: 1;*/
/*    flex-basis: 300px;*/
/*    text-align: center;*/
/*    padding: 30px;*/
/*    border: 1px solid #222;*/
/*    margin: 10px;*/
/*}*/
</style>
