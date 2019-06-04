<template>
  <section id="articles">
    <mdb-row>
      <mdb-col md="12">
        <mdb-card cascade narrow class="mt-5">
          <mdb-view class="gradient-card-header blue darken-2">
            <h4 class="h4-responsive text-white">Articles</h4>
          </mdb-view>
          <mdb-card-body>
            <div class="input-group md-form form-sm form-2 pl-0">
              <input class="form-control my-0 py-1 lime-border" v-model="searchQuery" v-on:keyup.enter="classify" type="text" placeholder="Search" aria-label="Search">
              <div class="input-group-append">
                <!--<span v-on:click.prevent="classify" class="input-group-text lime lighten-2" id="basic-text1"><i class="fas fa-dot-circle text-grey"-->
                <!--    aria-hidden="true"></i>-->
                <!--</span>-->
              </div>
            </div>
        <!--  </mdb-card-body>-->
        <!--</mdb-card>-->
        <!--<mdb-card cascade narrow class="mt-5">-->
        <!--    <mdb-card-body>-->
              <div class="input-group md-form form-sm form-2 pl-0">
               <!--<div class="panel-body" style="max-height: 400px;overflow-y: scroll;">-->
                    <table v-if="resources.length" class="table">
                        <thead>
                            <tr>
                                <th>Articles</th>
                                <!--<th>Source</th>-->
                            </tr>
                        </thead>
                        <tbody>
                            <tr v-for="item in filteredResources"  v-bind:key="item.title">
                                <td>
                                    <a href="item.uri" target="_blank">{{item.title}}</a>
                                    <!--{{item.title}}-->
                                </td>
                            </tr>
                        </tbody>
                    </table>
                <!--</div>-->
              </div>
            </mdb-card-body>
        </mdb-card>
      </mdb-col>
    </mdb-row>
      <!--<mdb-container>-->
        <!--<mdb-card class="mb-4">-->
        <!--  <mdb-card-body>-->
                      <!--<mdb-card-text>Article Source</mdb-card-text>-->
        <!--      <div style="display: block">-->
        <!--        <mdb-pie-chart :data="pieChartData" :height="200" :width="200"/>-->
        <!--      </div>-->
        <!--  </mdb-card-body>-->
        <!--</mdb-card>-->
        <!--<mdb-row>-->
        <!--  <mdb-col col="sm">One of three columns</mdb-col>-->
        <!--  <mdb-col col="sm">-->
        <!--   <mdb-card class="mb-4">-->
        <!--          <mdb-card-header class="text-center">Article Title</mdb-card-header>-->
                  <!--<mdb-card-body>-->
                      <!--<mdb-card-text>Article Source</mdb-card-text>-->
                      <!--<div style="display: block">-->
        <!--                <mdb-pie-chart :data="pieChartData" :height="200" :width="200"/>-->
                      <!--</div>-->
                  <!--</mdb-card-body>-->
        <!--    </mdb-card>-->
        <!--  </mdb-col>-->
        <!--  <mdb-col col="sm">One of three columns</mdb-col>-->
        <!--  <mdb-col col="sm">One of three columns</mdb-col>-->
        <!--  <mdb-col col="sm">One of three columns</mdb-col>-->
        <!--  <mdb-col col="sm">One of three columns</mdb-col>-->
        <!--</mdb-row>-->
      <!--</mdb-container>-->
  </section>
</template>

<script>
// https://stackoverflow.com/questions/52558770/vuejs-search-filter
import { mdbCardHeader, mdbPieChart, mdbContainer, mdbRow, mdbCol, mdbCard, mdbCardBody, mdbView, mdbMask, mdbCardTitle, mdbCardText, mdbCardFooter, mdbIcon, mdbBtn, mdbPagination, mdbPageNav, mdbPageItem } from 'mdbvue'

export default {
  name: 'Articles',
  components: {
    mdbCardHeader,
    mdbPieChart,
    mdbContainer,
    mdbRow,
    mdbCol,
    mdbCard,
    mdbCardBody,
    mdbView,
    mdbMask,
    mdbCardTitle,
    mdbCardText,
    mdbCardFooter,
    mdbIcon,
    mdbBtn,
    mdbPagination,
    mdbPageNav,
    mdbPageItem
  },
  data () {
    return {
      submitted: false,
      showFrameModalTop: false,
      showFrameModalBottom: false,
      showSideModalTopRight: false,
      showSideModalTopLeft: false,
      showSideModalBottomRight: false,
      showSideModalBottomLeft: false,
      showCentralModalSmall: false,
      showCentralModalMedium: false,
      showCentralModalLarge: false,
      showCentralModalFluid: false,
      showFluidModalRight: false,
      showFluidModalLeft: false,
      showFluidModalTop: false,
      showFluidModalBottom: false,
      pieChartData: {
        labels: ['aaaaaaaaaaaaaaaaaaaaa', 'bbbbbbbbbbbbbbbbbb', 'cccccccccccccccccccccc'],
        datasets: [
          {
            data: [12, 44, 20],
            backgroundColor: ['#F7464A', '#46BFBD', '#FDB45C'],
            hoverBackgroundColor: ['#FF5A5E', '#5AD3D1', '#FFC870']
          }
        ]
      },
      pieChartOptions: {
        responsive: true,
        maintainAspectRatio: false
      },
      /* eslint-disable */
      searchQuery:'',
      resources:[
        {title:"aaa", uri:"aaaa.com", category:"a", icon:null},
        {title:"add", uri:"aaaa.com", category:"a", icon:null},
        {title:"aff", uri:"aaaa.com", category:"a", icon:null},
        {title:"bbb", uri:"bbbb.com", category:"b", icon:null},
        {title:"bdd", uri:"bbbb.com", category:"b", icon:null},
        {title:"bsb", uri:"bbbb.com", category:"b", icon:null},
        {title:"ccc", uri:"cccc.com", category:"c", icon:null},
        {title:"ddd", uri:"dddd.com", category:"d", icon:null}
      ]
    }
  },
  /* eslint-disable */
  computed: {
    filteredResources (){
      if(this.searchQuery){
      return this.resources.filter((item)=>{
        return item.title.startsWith(this.searchQuery);
      })
      }else{
        return this.resources;
      }
    }
   }
}
</script>

<style scoped>
.profile-card-footer {
  background-color: #F7F7F7 !important;
  padding: 1.25rem;
}
.card.card-cascade .view {
  box-shadow: 0 3px 10px 0 rgba(0, 0, 0, 0.15), 0 3px 12px 0 rgba(0, 0, 0, 0.15);
}
.gradient-card-header {
  padding: 1rem 1rem;
  text-align: center;
}
</style>
