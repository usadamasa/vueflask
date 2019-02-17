<template>
  <div>
    <p>Home page</p>
    <p>Random number from backend: {{ randomNumber }}</p>
    <button @click="getRandom">New random number</button>
    <p>object from backend: {{ lastModified }}</p>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data () {
    return {
      randomNumber: 0,
      lastModified: ""
    }
  },
  methods: {
    getRandom () {
      this.randomNumber = this.getRandomFromBackend()
    },
    getRandomFromBackend () {
      const path = `http://localhost:5000/api/random`
      axios.get(path)
        .then(response => {
          this.randomNumber = response.data.randomNumber
        })
        .catch(error => {
          console.log(error)
        })
    },
    getS3Object () {
      this.lastModified = this.getS3ObjectFromBackend()
    },
    getS3ObjectFromBackend () {
      const path = `http://localhost:5000/api/list`
      axios.get(path)
        .then(response => {
          this.lastModified = response.data.lastModified
        })
        .catch(error => {
          console.log(error)
        })
    }
  },
  created () {
    this.getRandom()
    this.getS3Object()
  }
}
</script>
