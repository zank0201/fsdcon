
<template>
<!--    input date-->
  <div class = 'charts'>
  <form @submit.prevent="GetIcs">
    <div class="form-control">
      <label for="user-date">Pick A date</label>
      <input id="user-date" name="rdate" type="text" placeholder="yyyy-mm" v-model="rdate"/>
    </div>
    <!--      Input index Code-->
<div class="form-control">
      <label for="indexcode">Please select an index code</label>
      <select id="indexcode" name="indexcode" v-model="indexCode">
        <option value="ALSI">ALSI</option>
        <option value="FLED">FLED</option>
        <option value="TOPI">TOPI</option>
        <option value="LRGC">LRGC</option>
        <option value="MIDC">MIDC</option>
        <option value="SMLC">SMLC</option>
        <option value="RESI">RESI</option>
        <option value="FINI">FINI</option>
        <option value="INDI">INDI</option>
        <option value="PCAP">PCAP</option>
        <option value="SAPY">SAPY</option>
        <option value="ALTI">ALTI</option>
      </select>

    </div>

    <!--    mktindex input-->
    <div class="form-control">
      <label for="mktindex">Please select the market index code </label>
      <select id="mktindex" name="mktindex" v-model="mktIndex">
        <option value="J200">J200</option>
        <option value="J203">J203</option>
        <option value="J250">J250</option>
        <option value="J257">J257</option>
        <option value="J258">J258</option>
      </select>
    </div>

    <div>
      <button>Submit</button>
     </div>
  </form>
    <div>
      <zing-grid
    ref="myGrid"
    caption="Portfolio Summary"
    layout="row"
    viewport-stop
    :data.prop="allweights"
    filter sort pager
  >
    <zg-colgroup>
      <zg-column index="instrument" header="Share"></zg-column>
      <zg-column index="beta" header="Beta"></zg-column>
      <zg-column index="unique_risk" header="Unique Risk"></zg-column>
      <zg-column index = 'total_risk' header="Total Risk"></zg-column>

    </zg-colgroup>
  </zing-grid>
    </div>
    <div>

    </div>
  <div>

<!--      function 3-->
    <div>

    <zing-grid
    ref="newGrid"
    caption="Portfolio stats"
    layout="row"
    viewport-stop
    :data.prop="statsvals"
    filter sort pager
      >
<!--        table starts-->

        <zg-column index='pfBetas' header="Portfolio betas"></zg-column>
        <zg-column index='pfSysVol' header="Portfolio Systematic Variance"></zg-column>
        <zg-column index="pfSpecVol" header="Portfolio Specific Variance"></zg-column>
        <zg-column index="pfVol" header="Portfolio Variance"></zg-column>
    </zing-grid>
    </div>
  </div>

  </div>
</template>

<script>
// eslint-disable-next-line no-unused-vars
import Zingrid from 'zinggrid'
import axios from 'axios'

export default {

  data () {
    return {
      rdate: '',
      indexCode: 'ALSI',
      mktIndex: 'J200',
      allweights: [],
      statsvals: []

    }
  },
  mounted () {
    // this.$refs.myGrid.setData(this.allweights)
    // this.$refs.newGrids.setData(this.statsvals)
  },
  methods: {
    getstats () {
      axios.get('http://localhost:5000/getweights/stats')
        .then((response) => {
          console.log(response)
          this.statsvals = response.data
          return this.statsvals
        })
    },

    GetIcs () {
      const formdata = {
        rdate: this.rdate,
        indexCode: this.indexCode,
        mktIndex: this.mktIndex

      }
      console.log(formdata)
      axios.post('http://localhost:5000/getweights', formdata, {crossdomain: true})
        // eslint-disable-next-line no-unused-vars
        .then(response => {
          this.allweights = response.data
          this.getstats()
          console.log(response)
          // return this.allweights
        })
        .catch(error => console.log(error))
    }
  }

}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
form {
  margin: 2rem auto;
  max-width: 40rem;
  border-radius: 12px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.26);
  padding: 2rem;
  background-color: #ffffff;
}

.form-control {
  margin: 0.5rem 0;
}

label {
  font-weight: bold;
}

h2 {
  font-size: 1rem;
  margin: 0.5rem 0;
}

input,
select {
  display: block;
  width: 100%;
  font: inherit;
  margin-top: 0.5rem;
}

select {
  width: auto;
}

  button {
  font: inherit;
  border: 1px solid #0076bb;
  background-color: #0076bb;
  color: white;
  cursor: pointer;
  padding: 0.75rem 2rem;
  border-radius: 30px;
}

button:hover,
button:active {
  border-color: #002350;
  background-color: #002350;
}

</style>
