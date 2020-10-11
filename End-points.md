# Flask Restful-API

#### [Form input](#form-endpoints)
* [Add data to database](#add-data)

#### [Wallet endpoints](#wallet-endpoints)
* [Create wallet](#create-wallet)

### [OTP endpoints](#otp-endpoints)
* [Confirm OTP](#confirm-otp)
* [Resend OTP](#resend-otp)

### [Add Test Results Endpoints](#add-test-results-endpoints)
* [Add test result](#add-test-result)
* [Get Wallet Status](#get-wallet-status)

[> Back to `README.md`](https://github.com/zank0201/fsdcon/new/master/README.md)

---
# Form input

## Add data to database
**GET** [http://localhost:5000/getweights/2017-09/J200/TOPI](http://localhost:5000/getweights/2017-09/J200/TOPI)

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



