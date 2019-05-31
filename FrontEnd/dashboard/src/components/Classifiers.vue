<template>
    <div class="">
        <div class="row ">
            <div class="col-sm-6">
                <div class="md-form input-group mb-3">
              <input v-model="article.url" v-on:keyup.enter="logName('test')" type="text" class="form-control" placeholder="Link to Online Article" aria-label="Recipient's username"
                aria-describedby="MaterialButton-addon2">
              <div class="input-group-append">
                <button v-on:click.prevent="post" class="btn btn-md btn-secondary m-0 px-3" type="button" id="MaterialButton-addon2">Button</button>
              </div>
            </div>
            </div>
        </div>
        <div class="row">
            <div class="col-sm-12">
                 <textarea rows="7" cols="80" v-model="article.content"></textarea>
            </div>
        </div>
        <div class="">
            <li v-for="article in articles" v-bind:key="article" v-bind:target="_blank"><a v-bind:href="article.SOURCE">{{article.TITLE}}</a></li>
        </div>
    </div>
</template>

<script>
/* eslint-disable */
// https://www.youtube.com/watch?v=inJDWcHmsss&list=PLoYCgNOIyGADZuvKJweutZDOO9VI9YiJ9&index=5
export default {
    data () {
        return {
            articles:["Article1","Article2"],
            article: {
                url: '',
                title: '',
                content: '',
                categories: [],
                author: ''
            },
            // authors: ['The Net Ninja', 'The Angular Avenger', 'The Vue Vindicator'],
            submitted: false
        }
    },
    mounted()
    {
       fetch("http://gbcsystem-ice-wolf.c9users.io:8082/article").then(response => response.json())
       .then((data) => {
           this.articles = data.objects;
       })
    },
    methods: {
       logName: function(frominput){
            console.log(this.article.url);
            console.log(frominput);
        },
        post: function(){
            this.$http.post('http://gbcsystem-ice-wolf.c9users.io:8082/articledata', {
                url:this.article.url
                // email:'yesnext',
                // name:'david2'
                // dataType: "json",
                // headers: {
                //     accepts: 'application/vnd.api+json'
                // },
                // ContentType: "application/json"
                // title: this.article.url,
                // body: this.article.content,
                // userId: 1
            }).then(function(data){
                if(data.body.message)
                    console.log(data.body.message);
                else
                    console.log(data);
                this.submitted = true;
                this.article.url = "";
                this.article.content = data.body.CONTENT;
            });
        }
    }
}
</script>
<style type="text/css" scoped>
    textarea {
 resize: both;
 overflow: auto;
}
</style>
