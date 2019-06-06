<template>
  <section id="articles">
    <mdb-row>
      <mdb-col md="12">
        <mdb-card cascade narrow class="mt-5">
          <mdb-view class="gradient-card-header blue darken-2">
            <h4 class="h4-responsive text-white">Articles</h4>
          </mdb-view>
          <mdb-card-body class="sticky-top" style="padding-top:29px;backgroundColor:white;">
            <div class="input-group md-form form-sm form-2 pl-0">
              <input class="form-control my-0 py-1 lime-border" v-model="searchQuery" v-on:keyup.enter="classify" type="text" placeholder="Search Document Content" aria-label="Search">
            </div>
            <div class="input-group-append">
                <button v-on:click.prevent="addPage" class="btn btn-md btn-secondary m-0 px-3 right" type="button" id="MaterialButton-addon2">Add Page</button>
              </div>
          </mdb-card-body>
        <!--</mdb-card>-->
        <!--<mdb-card cascade narrow class="mt-5">-->
            <mdb-card-body>
              <div class="input-group md-form form-sm form-2 pl-0">
               <!--<div class="panel-body" style="max-height: 400px;overflow-y: scroll;">-->
                    <table v-if="resources.length" class="table">
                        <thead>
                            <tr>
                                <th>Articles</th>
                                <th>Content</th>
                                <th>Categories</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr v-for="item in filteredResources"  v-bind:key="item.title">
                                <td>
                                    <a href="item.uri" target="_blank">{{item.title}}</a>
                                    <!--{{item.title}}-->
                                </td>
                                 <td>
                                    {{item.content}}
                                    <!--{{item.title}}-->
                                </td>
                                 <td>
                                   <div style="width:200px;">
                                      <mdb-pie-chart :data="item.pieChartData" :height="300" :width="300"/>
                                   </div>
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
import {_} from 'vue-underscore'
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
      articles: '',
      numpages: '',
      maxpages: '',
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
      searchQuery2:'',
      allCategories:[
        'Art and Culture',
        'Conflicts and War',
        'Crime',
        'Diaster and Accidents',
        'Economy',
        'Education',
        'Environment',
        'Health',
        'Human Interest',
        'Labor',
        'Lifestyle and Leisure',
        'Politics',
        'Religion and Belief',
        'Science and Technology',
        'Society',
        'Sport',
        'Weather'
      ],
      allBackgroundColor: [
        '#00FFFF',
        '#7FFFD4',
        '#000000',
        '#0000FF',
        '#FFFF00',
        '#A52A2A',
        '#DEB887',
        '#5F9EA0',
        '#7FFF00',
        '#D2691E',
        '#DC143C',
        '#FF8C00',
        '#9932CC',
        '#8FBC8F',
        '#FF1493',
        '#FF00FF',
        '#8A2BE2'
      ],
      resources:[
        // {
        //   title:"", 
        //   uri:"", 
        //   content:"",
        //   pieChartData: {
        //     labels:[],
        //     datasets: [
        //       {
        //         data: [],
        //         backgroundColor: [],
        //         hoverBackgroundColor: []
        //       }
        //     ]
        //   },
        //   pieChartOptions: {
        //     responsive: true,
        //     maintainAspectRatio: false
        //   }
        // }
      ]
    }
  },
  /* eslint-disable */
  computed: 
  {
    filteredResources ()
    {
          if(this.searchQuery){
             console.log("Test1")
          return this.resources.filter((item)=>{
            return item.content.toLowerCase().includes(this.searchQuery);
          })
          }
          else{
            return this.resources;
          }
        }
   },
   created (){
        // console.log("Test");
        this.getData(1);
       
          // this.getData(page);
    },
    methods:{
       getData: function(page){
            this.$http.get('http://gbcsystem-ice-wolf.c9users.io:8082/article?page='+page).then(
              function(data){
                // if(data.body.message)
                //     console.log(data.body.message);
                // else
                //     console.log("TEST DATA");
                // this.submitted = true;
                this.numpages = data.body.total_pages;
                this.articles =  data.body.data;
                this.maxpages = 1;
                var i,k,cdata,categorylabel;
                var title, uri,content, categorylabels,categoryvalues,categorycolors,catgorydata;
                 var tempresource;// = this.resources[0];
                this.resources=[];
                for(i=0;i<this.articles.length;i++){
                  categorylabel =[]
                  categoryvalues =[]
                  categorycolors = []
                  // tempresource = this.resources[0];
                  // if(this.articles[i].TITLEI='undefned')
                  //   title = this.articles[i].TITLE;
                  // else
                  //   title = '';
                  
                  cdata = _.values(this.articles[i].articlecategories)
                  categorylabel  .push(cdata[0][0])
                  categorylabel  .push(cdata[1][0])
                  categorylabel  .push(cdata[2][0])
                  categoryvalues .push(cdata[0][1])
                  categoryvalues .push(cdata[1][1])
                  categoryvalues .push(cdata[2][1])
                  // this.allCategories
                  for(k=0;k<categorylabel.length;k++)
                    categorycolors.push(this.allBackgroundColor[this.allCategories.indexOf(categorylabel[k])])
                  // console.log(categorylabel)
                  // console.log(categoryvalues)
                  // console.log(categorycolors)
                  // console.log(title)
                  tempresource={
                    title:this.articles[i].TITLE, 
                    uri:"", 
                    content:this.articles[i].CONTENT,
                    pieChartData: {
                      labels:categorylabel,
                      datasets: [
                        {
                          data: categoryvalues,
                          backgroundColor: categorycolors,
                          hoverBackgroundColor: []
                        }
                      ]
                    },
                    pieChartOptions: {
                      responsive: true,
                      maintainAspectRatio: false
                    }
                  };
                  
                  // tempresource.title = i;//this.articles[i].TITLE;
                  // console.log(tempresource.title);
                  console.log(tempresource)
                  // console.log(tempresource.title);
                  // tempresource[i].content = this.articles[i].CONTENT;
                  // tempresource.content = content;
                  // tempresource.pieChartData.labels = categorylabel;
                  // tempresource.pieChartData.datasets[0].data= categoryvalues;
                  // tempresource.pieChartData.datasets[0].backgroundColor=categorycolors;
                  this.resources.push(tempresource)
                  // console.log( tempresource)
                }
               
              
                var page;
                for(page=2;page<=this.numpages;page++)
                
                    console.log("Test")
                // this.article.content = data.body.CONTENT;
                console.log(this.numpages)
            });
        },
        addPage: function(){
          var page = this.maxpages+1
          if(this.maxpages<=this.numpages){
           this.$http.get('http://gbcsystem-ice-wolf.c9users.io:8082/article?page='+page.toString()).then(
              function(data){
                  this.maxpages++;
                  this.articles.push(...data.body.data);
                  // console.log(this.maxpages)
                  // console.log(data.body.data)
                  console.log(this.articles.length)
                  var i;
                  for(i=0;i<this.articles.length;i++)
                    console.log(this.articles[i].TITLE)
            });
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
