<template>
  <div id='app'>
    <p>Home page</p>
    <div>
      <form@submit.prevent="getS3ObjectList">
          <p>s3PathPrefix:<input v-model="newEvent.prefix"
           type="text" placeholder="prefix" value=''/></p>
          <button type="submit">search</button>
      </form>
      <ul>
        <li v-for="item in files">
          {{ item }}
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data () {
    return {
      newEvent: {
        prefix: ''
      },
      files: []
    }
  },
  methods: {
    getS3ObjectList: function (e) {
      this.files = this.getS3ObjectListFromBackend(this.newEvent.prefix)
    },
    getS3ObjectListFromBackend (prefix) {
      const requestUrl = `http://localhost:5000/api/list?prefix=` + prefix
      axios.get(requestUrl)
        .then(response => {
          var files = response.data.files
          this.files = files
        })
        .catch(error => {
          console.log(error)
        })
    }
  },
  created () {
    this.getS3ObjectList('')
  }
}
</script>
