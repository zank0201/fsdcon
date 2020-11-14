<template>
 <div>
      <b-form v-show="step===1" @submit.prevent="GetIcs">
   <b-form-group id="input-group-1"
  label="Please select the market index code"
  label-for="mktIndex">
    <b-form-select
      name="mktIndex"
      id="mktIndex"
      v-model="mktIndex"
      :options="['J200', 'J203',
        'J250', 'J257', 'J258']"
      required></b-form-select>
  </b-form-group>
        <div>
              <button>Next</button>
     </div>
   </b-form>

   <b-form v-show="step===2">
      <b-form-group id="input-group-2"
  label="Please select a Share"
  label-for="shareCode">
    <b-form-select
      name="sharecode"
      id="sharecode"
      v-model="selected"
      :options= "shareCode"
      multiple :select-size="4"
      required></b-form-select>
        <div class="mt-3">Selected: <strong>{{ selected }}</strong></div>

  </b-form-group>
     <div class="mt-3">
      <div>
      <button @click.prevent="next">Next</button>
     </div>
     </div>
     <div class="mt-3">
     <div>
      <button @click.prevent="prev">Back</button>
     </div>
     </div>

   </b-form>
   <b-form v-show="step===3" >
     <div v-show="this.addList<this.selected.length">
     <b-form-input v-model.number="weightsVals"
     type="float"
     placeholder="Please insert a weight"
     aria-describedby="input-live-help">
     </b-form-input>
     </div>
     <p v-show="incorrect===true">The weights do not add up to zero, please enter the correct weights</p>
           <div>
      <button v-show="this.addList<this.selected.length" @click="addWeights">Add</button>
             <div class="mt-3">Selected ShareCode: <strong>{{selected}}</strong></div>
             <div class="mt-3">Added weights: <strong>{{weightslist}}</strong></div>
     </div>

       <div class="mt-3">
    <div class="col-4">
     <button @click.prevent="prev">Back</button>
    </div>
       </div>
<div class="mt-3">
         <div>
           <button v-show="this.addList===this.selected.length" @click.prevent="checkweights">Done</button>
         </div>
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
import PortfolioTime from './PortfolioTime'

export default {
  name: 'Portfolio',
  components: {
    PortfolioTime
  },
  data () {
    return {
      selected: [],
      betalist: [],
      dates_list: [],
      title: 'Betas',
      shareCode: [],
      nextId: 1,
      weightslist: [],
      weightsVals: '',
      mktIndex: 'J200',
      addList: 0,
      step: 1,
      incorrect: false,
      chartOptionsLine: {},
      chartRisks: {},
      risk_dates: [],
      showbutton: true,
      risk_sysvols: [],
      risk_pfvols: [],
      risk_pfspec: [],
      allbetas: []

    }
  },
  methods: {
    GetIcs () {
      this.step++
      const formdata = {
        mktIndex: this.mktIndex
        // mktIndex: this.mktIndex

      }
      console.log(formdata)
      console.log(this.mktIndex)
      axios.post('http://localhost:5000/getweights/ics', formdata, {crossdomain: true})
        // eslint-disable-next-line no-unused-vars
        .then(response => {
          console.log(response)
          this.shareCode = response.data
          // this.shareCode = this.shareCode.replace(/"/g, "'")
          // return this.allweights
        })
    },
    // previous page method
    prev () {
      this.step--
      if (this.step === 2) {
        this.weightslist = []
        this.selected = []
      } else if (this.step === 1) {
        this.selected = []
        this.shareCode = 'J200'
      }
    },
    // next page method
    next () {
      this.step++
    },
    GetIndex () {

    },
    reset () {
      this.selected = []
      this.betalist = []
      this.dates_list = []
      this.shareCode = []
      this.nextId = 1
      this.weightslist = []
      this.weightsVals = ''
      this.mktIndex = 'J200'
      this.addList = 0
      this.step = 1
      this.incorrect = false
      this.chartOptionsLine = {}
      this.chartRisks = {}
      this.risk_dates = []
      this.showbutton = true
      this.risk_sysvols = []
      this.risk_pfvols = []
      this.risk_pfspec = []
    },
    addWeights () {
      // check number of weights added
      console.log('weights: ' + this.weightslist)
      this.addList++
      this.weightslist.push(
        this.weightsVals)
      this.weightsVals = ''
    },
    checkweights () {
      const total = this.weightslist.reduce((a, b) => a + b, 0)
      console.log(total)
      // eslint-disable-next-line eqeqeq
      if (total == 1) {
        this.step++
        this.portfolioBeta()
      } else {
        this.weightslist = []
        this.addList = 0
        this.incorrect = true
      }
    },
    portfolioBeta () {
      const formdata = {
        mktIndex: this.mktIndex,
        weightslist: this.weightslist,
        selected: this.selected
      }
      axios.post('http://localhost:5000/getweights/ics/' + this.mktIndex, formdata, {crossdomain: true})
        .then(response => {
          this.betalist = response.data
          this.portfolioDates()
        })
    },
    portfolioDates () {
      axios.get('http://localhost:5000/getweights/ics/dates')
        .then(response => {
          this.dates_list = response.data
          this.incorrect = false
          this.riskDates()
          this.plotBeta()
        })
    },
    riskDates () {
      axios.post('http://localhost:5000/getweights/ics/risk/' + this.mktIndex, {crossdomain: true})
        .then(response => {
          console.log(response.data)
          this.risk_dates = response.data
          this.riskSysVol()
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
          data: this.risk_dates
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
