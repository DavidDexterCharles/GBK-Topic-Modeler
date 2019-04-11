<template>
    <div class="container">
        <div class="row ">
            <div class="col-sm-6">
                <div class="md-form input-group mb-3">
              <input v-model="article.url" v-on:keyup.enter="logName('test')" type="text" class="form-control" placeholder="Recipient's username" aria-label="Recipient's username"
                aria-describedby="MaterialButton-addon2">
              <div class="input-group-append">
                <button v-on:click.prevent="post" class="btn btn-md btn-secondary m-0 px-3" type="button" id="MaterialButton-addon2">Button</button>
              </div>
            </div>
            </div>
        </div>
        <div class="row">
            <div class="col-md-12">
                 <textarea v-model="article.url"></textarea>
            </div>
        </div>
    </div>
</template>

<script>
/* eslint-disable */
export default {
    data () {
        return {
            article: {
                url: '',
                title: '',
                content: 'TESt CONTENT',
                categories: [],
                author: ''
            },
            authors: ['The Net Ninja', 'The Angular Avenger', 'The Vue Vindicator'],
            submitted: false
        }
    },
    methods: {
       logName: function(frominput){
            console.log(this.article.url);
            console.log(frominput);
        },
        post: function(){
            this.$http.post('http://gbcsystem-ice-wolf.c9users.io:8082/domain', {
                domainname:this.article.url
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
                console.log(data);
                this.submitted = true;
                this.article.url = "";
            });
        }
    }
}
</script>