<template>
     <div>
      <b-form v-show="step===1">
 <b-form-group id="input-group-2"
  label="Please select an index code"
  label-for="indexcode">
    <b-form-select
      name="indexcode"
      id="indexcode"
      v-model="indexCode"
      :options="['ALSI', 'TOPI',
        'RESI', 'FINI', 'INDI']"
      required></b-form-select>

  </b-form-group>
        <div>

      <button @click.prevent="riskDates">Next</button>

     </div>
   </b-form>

<div class="row">
        <div class="col-md-6">
          <chart :options="chartOptionsLine"></chart>
        </div>

</div>
       <div class="row">
        <div class="col-md-6">
          <chart :options="chartRisks"></chart>
        </div>

       </div>
       <b-row align-h="center" v-show="showbutton">
          <div>
       <button  @click.prevent="reset">Clear</button>
         </div>
      </b-row>>
     </div>

</template>

<script>
import axios from 'axios'
export default {

  name: 'PortfolioTime',
  data () {
    return {
      step: 1,
      indexCode: 'ALSI',
      dates_list: [],
      betalist: [],
      chartOptionsLine: {},
      chartRisks: {},
      risk_sysvols: [],
      risk_pfvols: [],
      risk_pfspec: [],
      showbutton: true

    }
  },
  methods: {
    reset () {
      this.betalist = []
      this.dates_list = []
      this.step = 1
      this.chartOptionsLine = {}
      this.chartRisks = {}
      this.showbutton = true
      this.risk_sysvols = []
      this.risk_pfvols = []
      this.risk_pfspec = []
    },
    prev () {
      this.step--
    },
    // next page method
    next () {
      this.step++
    },
    riskDates () {
      this.step++
      const formdata = {
        indexCode: this.indexCode
      }
      axios.post('http://localhost:5000/getweights/portfolio', formdata, {crossdomain: true})
        .then(response => {
          this.betalist = response.data
          this.portfolioDates()
        })
    },
    riskSysVol () {
      axios.get('http://localhost:5000/getweights/ics/risk/sysvols')
        .then(response => {
          this.risk_sysvols = response.data
          this.riskPfVols()
          console.log(response.data)
        })
    },
    riskPfVols () {
      axios.get('http://localhost:5000/getweights/ics/risk/pfvols')
        .then(response => {
          this.risk_pfvols = response.data
          this.riskPfSpec()
        })
    },
    riskPfSpec () {
      axios.get('http://localhost:5000/getweights/ics/risk/pfspec')
        .then(response => {
          this.risk_pfspec = response.data
          this.plotRisks()
        })
    },

    portfolioDates () {
      axios.get('http://localhost:5000/getweights/ics/dates')
        .then(response => {
          this.dates_list = response.data
          this.riskSysVol()
          this.plotBeta()
        })
    },
    plotRisks () {
      this.chartRisks = {
        title: {
          text: 'Portfolio Risks',
          x: 'center',
          textStyle: {
            fontSize: 24
          }
        },
        tooltip: {
          trigger: 'axis'
        },
        grid: {
          left: '3%',
          right: '4%',
          bottom: '3%',
          containLabel: true
        },
        toolbox: {
          feature: {
            saveAsImage: {}
          }
        },
        legend: {},
        xAxis: {
          type: 'category',
          data: this.dates_list
        },
        yAxis: {
          type: 'value'
        },
        series: [
          {
            name: 'Portfolio Systemic Variance',
            type: 'line',
            data: this.risk_sysvols
          },
          {
            name: 'Portfolio Variance',
            type: 'line',
            data: this.risk_pfvols
          },
          {
            name: 'Portfolio Specific Variance',
            type: 'line',
            data: this.risk_pfspec
          }
        ]
      }
    },
    plotBeta () {
      this.chartOptionsLine = {
        xAxis: {
          data: this.dates_list
        },
        yAxis: {
          type: 'value'
        },
        series: [
          {
            type: 'line',
            data: this.betalist
          }
        ],
        title: {
          text: 'Portfolio Betas',
          x: 'center',
          textStyle: {
            fontSize: 24
          }
        },
        color: ['#127ac2']
      }
    }

  }
}
</script>

<style scoped>
form {
  margin: 2rem auto;
  max-width: 50rem;
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

input {
  width: 200px;
}

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
