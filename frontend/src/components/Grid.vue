<template>
  <zing-grid
    ref="myGrid"
    caption="Beta details"
    layout="row"
    viewport-stop

  >
    <zg-colgroup>
      <zg-column index="instrument" header="Instrument"></zg-column>
      <zg-column index="beta" header="Beta"></zg-column>
    </zg-colgroup>
  </zing-grid>
</template>

<script>
// eslint-disable-next-line no-unused-vars
import Zingrid from 'zinggrid'

export default {
  props: ['entries'],
  mounted () {
  }
}
</script>
<style>
zg-head-cell {
  background: white;
  color: #5d7d9a;
  font-size: 1rem;
}
zg-row:nth-child(odd) {
  background: rgb(250, 250, 250);
}
zg-control-bar {
  display: none;
}
zg-caption {
color: #5d7d9a;
font-family: "Avenir", Helvetica, Arial, sans-serif;
font-weight: bold;
background: white;
padding-left: 0;
font-size: 1.4rem;
height: 54px;
text-align: left;
}
zing-grid {
  border: 0px;
}
zing-grid input[type="text"], zing-grid input[type="number"]{
  border-radius: 5px;
}
</style>
