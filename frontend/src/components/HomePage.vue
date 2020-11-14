<template>
  <div>
  <div class="jumbotron" :style="{'background-image':'url(https://images.unsplash.com/photo-1535320903710-d993d3d77d29?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2700&q=80)'}">
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
      Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Gravida arcu ac tortor dignissim convallis. Sed viverra ipsum nunc aliquet bibendum enim facilisis gravida. Bibendum ut tristique et egestas quis ipsum suspendisse.
        Sed turpis tincidunt id aliquet risus feugiat in ante.
    </b-card-text>
    <div class="mt-3">
      <b-button variant="primary" :to="'IndexSummary'">Index Summary</b-button>
    </div>
  </b-card>

        <b-card
    title="Create your portfolio"
    tag="article"
    style="max-width: 20rem;"
    class="mb-2"
  >
    <b-card-text>
      Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Gravida arcu ac tortor dignissim convallis. Sed viverra ipsum nunc aliquet bibendum enim facilisis gravida. Bibendum ut tristique et egestas quis ipsum suspendisse.
        Sed turpis tincidunt id aliquet risus feugiat in ante.
    </b-card-text>
    <div class="mt-3">
      <b-button variant="primary" :to="'Portfolio'">Portfolio</b-button>
    </div>
  </b-card>

        <b-card
    title="Portfolio Summaries"
    tag="article"
    style="max-width: 20rem;"
    class="mb-2"
  >
    <b-card-text>
      Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Gravida arcu ac tortor dignissim convallis. Sed viverra ipsum nunc aliquet bibendum enim facilisis gravida. Bibendum ut tristique et egestas quis ipsum suspendisse.
        Sed turpis tincidunt id aliquet risus feugiat in ante.
    </b-card-text>
    <div class="mt-3">
      <b-button variant="primary" :to="'PortfolioTime'">Portfolio Summary</b-button>
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

</style>
