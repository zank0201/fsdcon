<template>
  <div id="app">
    <nav class="navbar navbar-expand-lg navbar-dark bg-primary">
  <a class="navbar-brand" href="#">FSDCON</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarColor01" aria-controls="navbarColor01" aria-expanded="false" aria-label="Toggle navigation" wfd-id="657">
    <span class="navbar-toggler-icon" wfd-id="472"></span>
  </button>

  <div class="collapse navbar-collapse" id="navbarColor01" wfd-id="462">
    <ul class="navbar-nav mr-auto" wfd-id="464">
      <li class="nav-item" wfd-id="470">
         <router-link class="nav-link" to="/">Home</router-link>
      </li>
      <li class="nav-item" wfd-id="468">
        <router-link class="nav-link" to="/IndexSummary">Index Summary</router-link>
      </li>
      <li class="nav-item" wfd-id="468">
        <router-link class="nav-link" to="/Portfolio">Portfolio</router-link>
      </li>

            <li class="nav-item" wfd-id="468">
        <router-link class="nav-link" to="/PortfolioTime">Portfolio Time</router-link>
      </li>

      <li class="nav-item" wfd-id="467">
        <a class="nav-link" href="http://fsd-documentation.s3-website.af-south-1.amazonaws.com/docs/build/html/index.html">About</a>
      </li>

    </ul>

  </div>
</nav>

    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style >

</style>
