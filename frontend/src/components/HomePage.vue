<template>
  <div>
  <div class="jumbotron">
  <b-jumbotron class="jumbotron"
               header="FSD Consulting" lead=
    "Welcome to FSD Consulting's interactive dashboard featuring visual and static representation of key risk statistics.">
    <br>
  </b-jumbotron>
  </div>

    <b-row align-h="center">
      <b-card-group deck>
  <b-card
    title="Index Summaries"
    tag="article"
    style="max-width: 20rem;"
    class="mb-2"
  >
    <b-card-text>
      Choose a specific index to use as benchmark when comparing stock performance. You can search for any stock and
      retrieve information on that stock, such as its Beta, Unique Risk, Total Risk and its constituent weight in a particular index.
      You can also have access to downloadable covariance matrices to view the co-movements between all the indices.
    </b-card-text>
    <div class ="row justify-content-center">
      <b-button pill variant="primary" :to="'IndexSummary'">Index Summary</b-button>
    </div>
  </b-card>

        <b-card
    title="Create your portfolio"
    tag="article"
    style="max-width: 20rem;"
    class="mb-2"
  >
    <b-card-text>
      Create a portfolio based on weights and stocks of your choice. You can then track
      the performance of the beta, Systematic risk, the specific variance and total risk of your portfolio over time.
    </b-card-text>
    <div class ="row justify-content-center">
      <b-button pill variant="primary" :to="'Portfolio'">Create your Portfolio</b-button>
    </div>
  </b-card>

        <b-card
    title="Portfolio Summaries"
    tag="article"
    style="max-width: 20rem;"
    class="mb-2"
  >
    <b-card-text>
     The portfolio summary allows you to track the performance of the portfolio of your chosen index over time. You can then track
      the performance of the beta, Systematic risk, the specific variance and total risk.
    </b-card-text>
    <div class ="row justify-content-center">
      <b-button pill variant="primary" :to="'PortfolioTime'">Portfolio Summary</b-button>
    </div>
  </b-card>

</b-card-group>
    </b-row>
  </div>

</template>

<script>
export default {
  name: 'HomePage'
}
</script>

<style scoped>
  .jumbotron {
    text-align: center;
  }
</style>
