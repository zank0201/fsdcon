<template>
     <div>
      <b-form v-show="step===1">
 <b-form-group id="input-group-2"
  label="Please select an index code:"
  label-for="indexcode">
    <b-form-select
      name="indexcode"
      id="indexcode"
      v-model="indexCode"
      :options="['ALSI', 'TOPI',
        'RESI', 'FINI', 'INDI']"
      required></b-form-select>

  </b-form-group>
        <div class="container">
       <div class="row justify-content-between">
      <div class="col-4">

      <button @click.prevent="riskDates">Next</button>
     </div>
     </div>
        </div>
   </b-form>
 <div class ="row justify-content-center" v-show="step===2">
          <v-chart :options="chartRisks"></v-chart>
          <div class="col-4" v-show="step===2">
       <button  @click.prevent="reset">Clear</button>
         </div>

</div>

     </div>
</template>

<script>
import axios from 'axios'
import ECharts from 'vue-echarts'
import 'echarts/lib/chart/line'
export default {
  components: {
    'v-chart': ECharts
  },

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
          // this.plotBeta()
        })
    },
    plotRisks () {
      this.chartRisks = {
        tooltip: {
          trigger: 'axis',
          axisPointer: {
            type: 'cross',
            label: {
              backgroundColor: '#6a7985'
            }
          }
        },
        color: ['#e5323e', '#BB33FF'],
        title: {
          text: 'Portfolio Risks',
          x: 'left',
          textStyle: {
            fontSize: 20
          }
        },

        grid: {
          left: '3%',
          right: '4%',
          bottom: '3%',
          containLabel: true
        },
        toolbox: {
          left: 'center',
          feature: {
            dataZoom: {
              yAxisIndex: 'none'
            },
            restore: {},
            saveAsImage: {}
          }
        },
        legend: {
          right: '0%',
          orient: 'vertical',
          data: ['Index Variance', 'Beta']
        },
        xAxis: {
          type: 'category',
          data: this.dates_list
        },
        yAxis: {
          type: 'value'
        },
        series: [
          {
            name: 'Index Variance',
            type: 'line',
            stack: 'portfolio',
            data: this.risk_sysvols
          },
          {
            name: 'Beta',
            type: 'line',
            stack: 'portfolio',
            data: this.betalist
          }

        ]
      }
    }

  }
}
</script>

<style scoped>
form {
  margin: 4rem auto;
  max-width: 30rem;
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
  margin-bottom: 2%;
  margin-top: 2%;
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
  width: auto;
  font: inherit;
  margin-top: 0.5rem;

}

  button {
  font: inherit;
  border: 1px solid #0076bb;
  background-color: #0076bb;
  color: white;
  cursor: pointer;
  padding: 0.75rem 2rem;
  border-radius: 30px;
    margin-top: 3%;
}

button:hover,
button:active {
  border-color: #002350;
  background-color: #002350;
}
/*jumbotron {*/
/*  text-align: center;*/
/*  align-items: center;*/
/*  alignment: center;*/
/*}*/
  .echarts {
    height: 700px;
    margin-top: 2%;
    margin-right: 15%;
    width: 900px;
  }
</style>
