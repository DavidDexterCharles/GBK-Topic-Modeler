<template>
 <div class="card">
  <h3 class="card-header text-center font-weight-bold text-uppercase py-4">Editable table</h3>
  <div class="card-body">
    <div id="table" class="table-editable">
      <span class="table-add float-right mb-3 mr-2"><a href="#!" class="text-success"><i class="fas fa-plus fa-2x"
            aria-hidden="true"></i></a></span>
      <table class="table table-bordered  table-striped text-center">
        <tr>
          <th class="text-center">CATEGORIES</th>
          <th class="text-center">KEY WORDS</th>
          <th class="text-center">Sort</th>
          <th class="text-center">Remove</th>
        </tr>
        <tr>
          <td class="" contenteditable="true">Aurelia Vega</td>
          <td class="pt-3-half" contenteditable="true">30</td>
          <td class="pt-3-half">
            <span class="table-up"><a href="#!" class="indigo-text"><i class="fas fa-long-arrow-alt-up" aria-hidden="true"></i></a></span>
            <span class="table-down"><a href="#!" class="indigo-text"><i class="fas fa-long-arrow-alt-down"
                  aria-hidden="true"></i></a></span>
          </td>
          <td>
            <span class="table-remove"><button type="button" class="btn btn-danger btn-rounded btn-sm my-0">Remove</button></span>
          </td>
        </tr>
      </table>
    </div>
  </div>
</div>
</template>
<script>
/* eslint-disable */

// https://mdbootstrap.com/docs/jquery/tables/editable/
// https://mdbootstrap.com/docs/vue/tables/editable/
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
