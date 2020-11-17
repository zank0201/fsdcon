
<template>
<!--    input date-->
<div>
  <!-- Image and text -->

  <b-form v-show="isShown" @submit.prevent="GetIcs">
      <b-form-group id="input-group-1"
  label="Please select a date:"
  label-for="rdate">
    <b-form-select
      name="rdate"
      id="rdate"
      v-model="rdate"
      :options="['2017-09', '2017-12', '2018-03', '2018-06', '2018-09', '2018-12', '2019-03', '2019-06', '2019-09', '2019-12', '2020-03', '2020-06']"
      required></b-form-select>
  </b-form-group>

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

     <b-row align-h="center">
      <button v-on:click="isShown = !isShown">Submit</button>
     </b-row>

</b-form>

<div v-show="!isShown">
<!--    Graphs-->
    <div class="row">
        <div class="col-md-6">
          <v-chart :options="ChartOptionsBar"></v-chart>
        </div>
        <div class="col-md-6">
            <v-chart :options="ChartOptionsPie"></v-chart>
        </div>
    </div>

<!--    Graphs of function 3 and 2-->

      <zing-grid
    ref="myGrid"
    caption="Portfolio Summary"
    layout="row"
    viewport-stop
    :data.prop="allbetas"
    filter sort pager
  >
    <zg-colgroup>
      <zg-column index="instrument" header="Share"></zg-column>
      <zg-column index="beta" header="Beta"></zg-column>
      <zg-column index="unique_risk" header="Unique Risk"></zg-column>
      <zg-column index = 'total_risk' header="Total Risk"></zg-column>

    </zg-colgroup>
  </zing-grid>

<!--      function 3-->

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

  <div class="container" v-show="showbutton">
       <div class="row justify-content-between">
          <div class="col-4">
       <button  @click.prevent="reset">Clear</button>
         </div>
         <div class="col-4">
      <button @click="downloadfiles">Download Files</button>
    </div>
       </div>

  <div>
</div>
  </div>
  </div>
</div>
</template>

<script>
// eslint-disable-next-line no-unused-vars
import Zingrid from 'zinggrid'
import axios from 'axios'
import 'echarts/lib/chart/bar'
import 'echarts/lib/chart/pie'
import ECharts from 'vue-echarts'
export default {
  components: {
    'v-chart': ECharts
  },

  data () {
    return {

      show: true,
      rdate: '2017-09',
      indexCode: 'ALSI',
      // mktIndex: 'J200',
      allbetas: [],
      statsvals: [],
      allweights: [],
      allalphas: [],
      alphaweights: [],
      ChartOptionsBar: {},
      ChartOptionsLine: {},
      ChartOptionsPie: {},
      isShown: true,
      showbutton: true

    }
  },
  mounted () {
    // this.$refs.myGrid.setData(this.allweights)
    // this.$refs.newGrids.setData(this.statsvals)
  },
  methods: {
    downloadfiles () {
      axios({url:
          'http://localhost:5000/getweights/getfiles',
      method: 'GET',
      responseType: 'blob'})
        .then((response) => {
          console.log(response.data)
          const url = window.URL.createObjectURL(new Blob([response.data]))
          const link = document.createElement('a')
          link.href = url
          link.setAttribute('download', 'Matrices.zip') // or any other extension
          document.body.appendChild(link)
          link.click()
        })
    },
    reset () {
      this.show = true
      this.rdate = '2017-09'
      this.indexCode = 'ALSI'
      // mktIndex: 'J200',
      this.allbetas = []
      this.statsvals = []
      this.allweights = []
      this.allalphas = []
      this.alphaweights = []
      this.ChartOptionsBar = {}
      this.ChartOptionsLine = {}
      this.ChartOptionsPie = {}
      this.isShown = true
      this.showbutton = true
    },
    getweights () {
      axios.get('http://localhost:5000/getweights/betas')
        .then((response) => {
          this.allweights = response.data
          this.getalphas()
        })
    },
    getalphas () {
      axios.get('http://localhost:5000/getweights/alpha')
        .then((response) => {
          this.allalphas = response.data
          this.getpie()
        })
    },
    getpie () {
      axios.get('http://localhost:5000/getweights/piechart')
        .then((response) => {
          this.alphaweights = response.data
          this.plotWeights()
        })
    },

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
        indexCode: this.indexCode
        // mktIndex: this.mktIndex

      }
      console.log(this.indexCode)
      axios.post('http://localhost:5000/getweights', formdata, {crossdomain: true})
        // eslint-disable-next-line no-unused-vars
        .then(response => {
          this.allbetas = response.data
          console.log(this.allbetas.beta)
          this.getstats()
          this.getweights()
          console.log(response)
          // return this.allweights
        })
        .catch(error => console.log(error))
    },

    plotWeights () {
      this.ChartOptionsBar = {
        tooltip: {
          trigger: 'axis'
        },
        xAxis: {
          // eslint-disable-next-line
          data: this.allalphas,
          type: 'category',
          axisLabel: {
            show: true,
            textStyle: {
              color: 'black'
            },
            interval: 0,
            rotate: 90
          }
        },
        yAxis: {
          type: 'value'
        },
        series: [{
          data: this.allweights,
          type: 'bar',
          align: 'center',
          color: '#0099FF',
          showBackground: true,
          backgroundStyle: {
            color: 'rgba(220, 220, 220, 0.8)'
          }

        }],
        title: {
          text: this.indexCode + ' Constituent Betas',
          x: 'center',
          textStyle: {
            fontSize: 24
          }
        }
      }

      this.ChartOptionsPie = {
        title: {
          text: this.indexCode + ' Constituent Weights',
          // left: 'center',
          x: 'center',
          textStyle: {
            fontSize: 24
          }
        },
        tooltip: {
          trigger: 'item',
          formatter: this.allalphas
        },
        // legend: {
        //   type: 'scroll',
        //   orient: 'vertical',
        //   show: true,
        //   right: 'auto',
        //   left: 'auto',
        //   top: 'auto',
        //   bottom: 'auto',
        //   data: this.alphaweights,
        //   selected: this.alphaweights.selected
        // },
        series: [
          {
            name: '',
            type: 'pie',
            radius: '40%',
            // radius: ['55%', '70%'],
            // avoidoverlap: false,
            center: ['40%', '60%'],
            data: this.alphaweights,
            // animation: true,
            emphasis: {
              itemStyle: {
                shadowBlur: 5,
                shadowOffsetX: 0,
                shadowColor: 'rgba(0, 0, 0, 0.5)'
              }
              // label: {
              //   show: true,
              //   fontSize: '10'
              //   // fontWeight: 'bold'
              // }
            },
            // labelLine: {
            //   show: false
            // },
            // label: {
            //   position: 'outer',
            //   alignTo: 'none',
            //   bleedMargin: 0,
            // },
            left: '40%',
            right: '40%',
            align: 'centre',
            top: 'auto',
            bottom: 'auto',
            height: 400,
            width: 400
          }
        ]
      }
    }
  }

}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
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
    margin-bottom: 5%;
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
</style>
