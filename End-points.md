# Flask Restful-API

#### [Form input](#form-endpoints)
* [Add data to database](#add-data)

#### [Portfolio stats](#portfolio-stats)
* [Get Stats](#get-stats)

#### [Graph outputs](#graphs)
* [Create bar-graph](#create-bar-graph)
* [Create pie-graph](#create-pie-graph)

[> Back to `README.md`](https://github.com/zank0201/fsdcon/blob/master/README.md)

---
# Form input

## Add data to database
**GET** [http://localhost:5000/getweights/2017-09/J200/TOPI](http://localhost:5000/getweights/2017-09/J200/TOPI)
### Response
```
[
  {
    "beta": 1.087, 
    "id": 25186, 
    "instrument": "APN", 
    "mkt_vol": null, 
    "total_risk": 0.311, 
    "unique_risk": 0.286
  }, 
  {
    "beta": 0.674, 
    "id": 25188, 
    "instrument": "BAW", 
    "mkt_vol": null, 
    "total_risk": 0.3, 
    "unique_risk": 0.29
  }, 
  {
    "beta": 0.903, 
    "id": 25190, 
    "instrument": "BTI", 
    "mkt_vol": null, 
    "total_risk": 0.186, 
    "unique_risk": 0.155
  }, 
  {
    "beta": 1.118, 
    "id": 25192, 
    "instrument": "CFR", 
    "mkt_vol": null, 
    "total_risk": 0.226, 
    "unique_risk": 0.187
  }, 
  {
    "beta": 0.885, 
    "id": 25194, 
    "instrument": "IPL", 
    "mkt_vol": null, 
    "total_risk": 0.316, 
    "unique_risk": 0.299
  }, 
  {
    "beta": 1.035, 
    "id": 25196, 
    "instrument": "MEI", 
    "mkt_vol": null, 
    "total_risk": 0.286, 
    "unique_risk": 0.257
  }, 
  {
    "beta": 0.592, 
    "id": 25198, 
    "instrument": "MTN", 
    "mkt_vol": null, 
    "total_risk": 0.263, 
    "unique_risk": 0.254
  }, 
  {
    "beta": 0.712, 
    "id": 25200, 
    "instrument": "NTC", 
    "mkt_vol": null, 
    "total_risk": 0.224, 
    "unique_risk": 0.209
  }, 
  {
    "beta": 0.944, 
    "id": 25202, 
    "instrument": "PIK", 
    "mkt_vol": null, 
    "total_risk": 0.265, 
    "unique_risk": 0.242
  }, 
  {
    "beta": 0.486, 
    "id": 25204, 
    "instrument": "SHP", 
    "mkt_vol": null, 
    "total_risk": 0.259, 
    "unique_risk": 0.253
  }, 
  {
    "beta": 0.639, 
    "id": 25206, 
    "instrument": "TBS", 
    "mkt_vol": null, 
    "total_risk": 0.248, 
    "unique_risk": 0.237
  }, 
  {
    "beta": 0.604, 
    "id": 25208, 
    "instrument": "TRU", 
    "mkt_vol": null, 
    "total_risk": 0.276, 
    "unique_risk": 0.267
  }, 
  {
    "beta": 0.874, 
    "id": 25210, 
    "instrument": "WHL", 
    "mkt_vol": null, 
    "total_risk": 0.242, 
    "unique_risk": 0.221
  }, 
  {
    "beta": 0.789, 
    "id": 25211, 
    "instrument": "APN", 
    "mkt_vol": null, 
    "total_risk": 0.262, 
    "unique_risk": 0.244
  }, 
  {
    "beta": 0.35, 
    "id": 25212, 
    "instrument": "AVI", 
    "mkt_vol": null, 
    "total_risk": 0.18, 
    "unique_risk": 0.175
  }, 
  {
    "beta": 0.54, 
    "id": 25213, 
    "instrument": "BAW", 
    "mkt_vol": null, 
    "total_risk": 0.295, 
    "unique_risk": 0.288
  }, 
  {
    "beta": 0.757, 
    "id": 25214, 
    "instrument": "BID", 
    "mkt_vol": null, 
    "total_risk": 0.25, 
    "unique_risk": 0.234
  }, 
  {
    "beta": 0.706, 
    "id": 25215, 
    "instrument": "BTI", 
    "mkt_vol": null, 
    "total_risk": 0.17, 
    "unique_risk": 0.147
  }, 
  {
    "beta": 0.542, 
    "id": 25216, 
    "instrument": "BVT", 
    "mkt_vol": null, 
    "total_risk": 0.195, 
    "unique_risk": 0.184
  }, 
  {
    "beta": 1.216, 
    "id": 25217, 
    "instrument": "CFR", 
    "mkt_vol": null, 
    "total_risk": 0.245, 
    "unique_risk": 0.196
  }, 
  {
    "beta": 0.559, 
    "id": 25218, 
    "instrument": "CLS", 
    "mkt_vol": null, 
    "total_risk": 0.21, 
    "unique_risk": 0.199
  }, 
  {
    "beta": 0.796, 
    "id": 25219, 
    "instrument": "IPL", 
    "mkt_vol": null, 
    "total_risk": 0.288, 
    "unique_risk": 0.271
  }, 
  {
    "beta": 0.71, 
    "id": 25220, 
    "instrument": "LHC", 
    "mkt_vol": null, 
    "total_risk": 0.215, 
    "unique_risk": 0.197
  }, 
  {
    "beta": 1.012, 
    "id": 25221, 
    "instrument": "MEI", 
    "mkt_vol": null, 
    "total_risk": 0.269, 
    "unique_risk": 0.242
  }, 
  {
    "beta": 0.822, 
    "id": 25222, 
    "instrument": "MRP", 
    "mkt_vol": null, 
    "total_risk": 0.298, 
    "unique_risk": 0.281
  }, 
  {
    "beta": 0.598, 
    "id": 25223, 
    "instrument": "MTN", 
    "mkt_vol": null, 
    "total_risk": 0.236, 
    "unique_risk": 0.225
  }, 
  {
    "beta": 1.282, 
    "id": 25224, 
    "instrument": "NPN", 
    "mkt_vol": null, 
    "total_risk": 0.266, 
    "unique_risk": 0.217
  }, 
  {
    "beta": 0.69, 
    "id": 25225, 
    "instrument": "NTC", 
    "mkt_vol": null, 
    "total_risk": 0.208, 
    "unique_risk": 0.191
  }, 
  {
    "beta": 0.752, 
    "id": 25226, 
    "instrument": "PFG", 
    "mkt_vol": null, 
    "total_risk": 0.284, 
    "unique_risk": 0.269
  }, 
  {
    "beta": 0.666, 
    "id": 25227, 
    "instrument": "PIK", 
    "mkt_vol": null, 
    "total_risk": 0.256, 
    "unique_risk": 0.243
  }, 
  {
    "beta": 0.817, 
    "id": 25228, 
    "instrument": "REM", 
    "mkt_vol": null, 
    "total_risk": 0.173, 
    "unique_risk": 0.141
  }, 
  {
    "beta": 0.393, 
    "id": 25229, 
    "instrument": "SHP", 
    "mkt_vol": null, 
    "total_risk": 0.259, 
    "unique_risk": 0.255
  }, 
  {
    "beta": 0.52, 
    "id": 25230, 
    "instrument": "SPP", 
    "mkt_vol": null, 
    "total_risk": 0.207, 
    "unique_risk": 0.197
  }, 
  {
    "beta": 0.508, 
    "id": 25231, 
    "instrument": "TBS", 
    "mkt_vol": null, 
    "total_risk": 0.225, 
    "unique_risk": 0.217
  }, 
  {
    "beta": 0.669, 
    "id": 25232, 
    "instrument": "TFG", 
    "mkt_vol": null, 
    "total_risk": 0.303, 
    "unique_risk": 0.292
  }, 
  {
    "beta": 0.715, 
    "id": 25233, 
    "instrument": "TRU", 
    "mkt_vol": null, 
    "total_risk": 0.262, 
    "unique_risk": 0.247
  }, 
  {
    "beta": 0.983, 
    "id": 25234, 
    "instrument": "VOD", 
    "mkt_vol": null, 
    "total_risk": 0.214, 
    "unique_risk": 0.178
  }, 
  {
    "beta": 0.956, 
    "id": 25235, 
    "instrument": "WHL", 
    "mkt_vol": null, 
    "total_risk": 0.258, 
    "unique_risk": 0.23
  }, 
  {
    "beta": 0.582, 
    "id": 25187, 
    "instrument": "AVI", 
    "mkt_vol": null, 
    "total_risk": 0.203, 
    "unique_risk": 0.191
  }, 
  {
    "beta": 0.848, 
    "id": 25189, 
    "instrument": "BID", 
    "mkt_vol": null, 
    "total_risk": 0.244, 
    "unique_risk": 0.221
  }, 
  {
    "beta": 0.617, 
    "id": 25191, 
    "instrument": "BVT", 
    "mkt_vol": null, 
    "total_risk": 0.225, 
    "unique_risk": 0.214
  }, 
  {
    "beta": 0.633, 
    "id": 25193, 
    "instrument": "CLS", 
    "mkt_vol": null, 
    "total_risk": 0.213, 
    "unique_risk": 0.2
  }, 
  {
    "beta": 0.977, 
    "id": 25195, 
    "instrument": "LHC", 
    "mkt_vol": null, 
    "total_risk": 0.227, 
    "unique_risk": 0.198
  }, 
  {
    "beta": 0.802, 
    "id": 25197, 
    "instrument": "MRP", 
    "mkt_vol": null, 
    "total_risk": 0.316, 
    "unique_risk": 0.303
  }, 
  {
    "beta": 1.427, 
    "id": 25199, 
    "instrument": "NPN", 
    "mkt_vol": null, 
    "total_risk": 0.272, 
    "unique_risk": 0.218
  }, 
  {
    "beta": 0.862, 
    "id": 25201, 
    "instrument": "PFG", 
    "mkt_vol": null, 
    "total_risk": 0.277, 
    "unique_risk": 0.259
  }, 
  {
    "beta": 0.838, 
    "id": 25203, 
    "instrument": "REM", 
    "mkt_vol": null, 
    "total_risk": 0.185, 
    "unique_risk": 0.159
  }, 
  {
    "beta": 0.743, 
    "id": 25205, 
    "instrument": "SPP", 
    "mkt_vol": null, 
    "total_risk": 0.228, 
    "unique_risk": 0.212
  }, 
  {
    "beta": 0.619, 
    "id": 25207, 
    "instrument": "TFG", 
    "mkt_vol": null, 
    "total_risk": 0.32, 
    "unique_risk": 0.312
  }, 
  {
    "beta": 0.667, 
    "id": 25209, 
    "instrument": "VOD", 
    "mkt_vol": null, 
    "total_risk": 0.225, 
    "unique_risk": 0.211
  }, 
  {
    "beta": 0.789, 
    "id": 25236, 
    "instrument": "APN", 
    "mkt_vol": null, 
    "total_risk": 0.262, 
    "unique_risk": 0.244
  }, 
  {
    "beta": 0.35, 
    "id": 25237, 
    "instrument": "AVI", 
    "mkt_vol": null, 
    "total_risk": 0.18, 
    "unique_risk": 0.175
  }, 
  {
    "beta": 0.54, 
    "id": 25238, 
    "instrument": "BAW", 
    "mkt_vol": null, 
    "total_risk": 0.295, 
    "unique_risk": 0.288
  }, 
  {
    "beta": 0.757, 
    "id": 25239, 
    "instrument": "BID", 
    "mkt_vol": null, 
    "total_risk": 0.25, 
    "unique_risk": 0.234
  }, 
  {
    "beta": 0.706, 
    "id": 25240, 
    "instrument": "BTI", 
    "mkt_vol": null, 
    "total_risk": 0.17, 
    "unique_risk": 0.147
  }, 
  {
    "beta": 0.542, 
    "id": 25241, 
    "instrument": "BVT", 
    "mkt_vol": null, 
    "total_risk": 0.195, 
    "unique_risk": 0.184
  }, 
  {
    "beta": 1.216, 
    "id": 25242, 
    "instrument": "CFR", 
    "mkt_vol": null, 
    "total_risk": 0.245, 
    "unique_risk": 0.196
  }, 
  {
    "beta": 0.559, 
    "id": 25243, 
    "instrument": "CLS", 
    "mkt_vol": null, 
    "total_risk": 0.21, 
    "unique_risk": 0.199
  }, 
  {
    "beta": 0.796, 
    "id": 25244, 
    "instrument": "IPL", 
    "mkt_vol": null, 
    "total_risk": 0.288, 
    "unique_risk": 0.271
  }, 
  {
    "beta": 0.71, 
    "id": 25245, 
    "instrument": "LHC", 
    "mkt_vol": null, 
    "total_risk": 0.215, 
    "unique_risk": 0.197
  }, 
  {
    "beta": 1.012, 
    "id": 25246, 
    "instrument": "MEI", 
    "mkt_vol": null, 
    "total_risk": 0.269, 
    "unique_risk": 0.242
  }, 
  {
    "beta": 0.822, 
    "id": 25247, 
    "instrument": "MRP", 
    "mkt_vol": null, 
    "total_risk": 0.298, 
    "unique_risk": 0.281
  }, 
  {
    "beta": 0.598, 
    "id": 25248, 
    "instrument": "MTN", 
    "mkt_vol": null, 
    "total_risk": 0.236, 
    "unique_risk": 0.225
  }, 
  {
    "beta": 1.282, 
    "id": 25249, 
    "instrument": "NPN", 
    "mkt_vol": null, 
    "total_risk": 0.266, 
    "unique_risk": 0.217
  }, 
  {
    "beta": 0.69, 
    "id": 25250, 
    "instrument": "NTC", 
    "mkt_vol": null, 
    "total_risk": 0.208, 
    "unique_risk": 0.191
  }, 
  {
    "beta": 0.752, 
    "id": 25251, 
    "instrument": "PFG", 
    "mkt_vol": null, 
    "total_risk": 0.284, 
    "unique_risk": 0.269
  }, 
  {
    "beta": 0.666, 
    "id": 25252, 
    "instrument": "PIK", 
    "mkt_vol": null, 
    "total_risk": 0.256, 
    "unique_risk": 0.243
  }, 
  {
    "beta": 0.817, 
    "id": 25253, 
    "instrument": "REM", 
    "mkt_vol": null, 
    "total_risk": 0.173, 
    "unique_risk": 0.141
  }, 
  {
    "beta": 0.393, 
    "id": 25254, 
    "instrument": "SHP", 
    "mkt_vol": null, 
    "total_risk": 0.259, 
    "unique_risk": 0.255
  }, 
  {
    "beta": 0.52, 
    "id": 25255, 
    "instrument": "SPP", 
    "mkt_vol": null, 
    "total_risk": 0.207, 
    "unique_risk": 0.197
  }, 
  {
    "beta": 0.508, 
    "id": 25256, 
    "instrument": "TBS", 
    "mkt_vol": null, 
    "total_risk": 0.225, 
    "unique_risk": 0.217
  }, 
  {
    "beta": 0.669, 
    "id": 25257, 
    "instrument": "TFG", 
    "mkt_vol": null, 
    "total_risk": 0.303, 
    "unique_risk": 0.292
  }, 
  {
    "beta": 0.715, 
    "id": 25258, 
    "instrument": "TRU", 
    "mkt_vol": null, 
    "total_risk": 0.262, 
    "unique_risk": 0.247
  }, 
  {
    "beta": 0.983, 
    "id": 25259, 
    "instrument": "VOD", 
    "mkt_vol": null, 
    "total_risk": 0.214, 
    "unique_risk": 0.178
  }, 
  {
    "beta": 0.956, 
    "id": 25260, 
    "instrument": "WHL", 
    "mkt_vol": null, 
    "total_risk": 0.258, 
    "unique_risk": 0.23
  }
]

```
# Portfolio stats
Note, before these functions can be run, the post request above needs to be run.

## Get Stats
**GET** [http://localhost:5000/getweights/stats](http://localhost:5000/getweights/stats)

### Response:
```
[
  {
    "pfBetas": 0.9129, 
    "pfSpecVol": 0.0029, 
    "pfSysVol": 0.2017, 
    "pfVol": 0.0151
  }
]
```
# Graph outputs

## Create bar-graph
Note, before these functions can be run, the post request above needs to be run.

**GET** [http://localhost:5000/getweights/weights](http://localhost:5000/getweights/weights)
### Response:
```
[
  0.036577810063437216, 
  0.014793519059101114, 
  0.01222506817634425, 
  0.19430098772323076, 
  0.06972380653085901, 
  0.010946324503974184, 
  0.0049246119519301855, 
  0.005663081986525002, 
  0.00352122482785417, 
  0.006734937113200328, 
  0.010643954922016603, 
  0.01536069895606212, 
  0.027873092238387985, 
  0.15034391505893535, 
  0.004300030218193454, 
  0.007016399193233402, 
  0.013715447062230594, 
  0.005661631266079534, 
  0.014272339537224227, 
  0.032796940531848486, 
  0.00903636949754823, 
  0.008053781782019957, 
  0.0063500820469363055, 
  0.015017339386491264, 
  0.057851774811185926, 
  0.006832542973623049, 
  0.011846328876660197, 
  0.0023900610153996813, 
  0.036875621425599726, 
  0.008528435258925158, 
  0.007682882487842475, 
  0.004305655742329532, 
  0.0049516550047739635, 
  0.005381251221782871, 
  0.013193820032233185, 
  0.011894946184264336, 
  0.02015662241160608, 
  0.006434591821501664, 
  0.011051095050967234, 
  0.030950264308969074, 
  0.017738971390597, 
  0.030279193587032613, 
  0.03180089276104251
]
```

**GET** [http://localhost:5000/getweights/alpha](http://localhost:5000/getweights/alpha)
### Response:
```
[
  "AGL", 
  "APN", 
  "BID", 
  "BTI", 
  "CFR", 
  "DSY", 
  "FFB", 
  "GFI", 
  "INL", 
  "ITU", 
  "MEI", 
  "MNP", 
  "MTN", 
  "NPN", 
  "NTC", 
  "RDF", 
  "REM", 
  "SAP", 
  "SHP", 
  "SNH", 
  "TBS", 
  "WHL", 
  "ANG", 
  "BGA", 
  "BIL", 
  "BVT", 
  "CPI", 
  "FFA", 
  "FSR", 
  "GRT", 
  "INP", 
  "LHC", 
  "MND", 
  "MRP", 
  "NED", 
  "NRP", 
  "OML", 
  "REI", 
  "RMH", 
  "SBK", 
  "SLM", 
  "SOL", 
  "VOD"
]
```

## Create pie-graph

**GET** [http://localhost:5000/getweights/piechart](http://localhost:5000/getweights/piechart)

### Response:
```
[ { "name": "AGL", "value": 0.0365778101 }, { "name": "APN", "value": 0.0147935191 }, { "name": "BID", "value": 0.0122250682 }, { "name": "BTI", "value": 0.1943009877 }, { "name": "CFR", "value": 0.0697238065 }, { "name": "DSY", "value": 0.0109463245 }, { "name": "FFB", "value": 0.004924612 }, { "name": "GFI", "value": 0.005663082 }, { "name": "INL", "value": 0.0035212248 }, { "name": "ITU", "value": 0.0067349371 }, { "name": "MEI", "value": 0.0106439549 }, { "name": "MNP", "value": 0.015360699 }, { "name": "MTN", "value": 0.0278730922 }, { "name": "NPN", "value": 0.1503439151 }, { "name": "NTC", "value": 0.0043000302 }, { "name": "RDF", "value": 0.0070163992 }, { "name": "REM", "value": 0.0137154471 }, { "name": "SAP", "value": 0.0056616313 }, { "name": "SHP", "value": 0.0142723395 }, { "name": "SNH", "value": 0.0327969405 }, { "name": "TBS", "value": 0.0090363695 }, { "name": "WHL", "value": 0.0080537818 }, { "name": "ANG", "value": 0.006350082 }, { "name": "BGA", "value": 0.0150173394 }, { "name": "BIL", "value": 0.0578517748 }, { "name": "BVT", "value": 0.006832543 }, { "name": "CPI", "value": 0.0118463289 }, { "name": "FFA", "value": 0.002390061 }, { "name": "FSR", "value": 0.0368756214 }, { "name": "GRT", "value": 0.0085284353 }, { "name": "INP", "value": 0.0076828825 }, { "name": "LHC", "value": 0.0043056557 }, { "name": "MND", "value": 0.004951655 }, { "name": "MRP", "value": 0.0053812512 }, { "name": "NED", "value": 0.01319382 }, { "name": "NRP", "value": 0.0118949462 }, { "name": "OML", "value": 0.0201566224 }, { "name": "REI", "value": 0.0064345918 }, { "name": "RMH", "value": 0.0110510951 }, { "name": "SBK", "value": 0.0309502643 }, { "name": "SLM", "value": 0.0177389714 }, { "name": "SOL", "value": 0.0302791936 }, { "name": "VOD", "value": 0.0318008928 } ]
```









