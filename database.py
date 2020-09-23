
import pandas as pd
import numpy as np
from datetime import datetime
from pandas import DataFrame
from sqlalchemy import create_engine
import psycopg2
import matplotlib


def GetICsAndWeight(rDate, indexCode):
    # Load IC table
    tbl_Index_Constituents = pd.read_csv("../tbl_Index_Constituents.csv")
    # Remove timestamp from date column
    tbl_Index_Constituents["Quarter"] = pd.to_datetime(tbl_Index_Constituents["Date"]).dt.quarter
    tbl_Index_Constituents["Date"] = pd.to_datetime(tbl_Index_Constituents["Date"]).dt.strftime("%Y-%m")

    # Convert Rdate to datetime for comparison
    # Create dataframe which contains dates being looked for
    datetbl = (tbl_Index_Constituents[tbl_Index_Constituents["Date"] == rDate])
    newdata = datetbl[datetbl[indexCode + " New"] == indexCode]

    # Select column with Index Code
    total = newdata["Gross Market Capitalisation"].sum(axis=0)
    # return weights
    newdata["weights"] = newdata["Gross Market Capitalisation"] / total
    # newdata.fillna(0)
    # ICs = newdata[["Alpha"]]
    # weights = newdata[["weights"]]
    return newdata[["Alpha", "weights"]]


#portframe = GetICsAndWeight(rDate="2017-09", indexCode="TOPI")



def GetBetasMktAndSpecVols(rDate, ICs, mktIndexCode):
    Ba_Output = pd.read_csv("../tbl_BA_Beta_Output.csv")
    Ba_Output["Quarter"] = pd.to_datetime(Ba_Output["End Date"]).dt.quarter
    Ba_Output["End Date"] = pd.to_datetime(Ba_Output["End Date"]).dt.strftime("%Y-%m")

    datetbl = (Ba_Output[Ba_Output["End Date"] == rDate])
    frame = datetbl.loc[datetbl["Instrument"].isin(ICs)]
    betasframe = frame.loc[frame["Index"] == mktIndexCode]

    mktframe = datetbl.loc[datetbl["Instrument"] == mktIndexCode]
    mktVol = mktframe[["Total Risk"]].iloc[0]

    # print(mktVol)
    # create dataframe with instrument's beta values

    df = betasframe[["Instrument", "Beta", "Unique Risk", "Total Risk"]]

    return mktVol, df


#mktVol, df = GetBetasMktAndSpecVols(rDate="2017-09", ICs=portframe["Alpha"], mktIndexCode="J200")


# def CalcStats(weights, betas, mktVol, specVols):
#     # convert dataframe to array
#     nump_weights = np.array(weights)
#     nump_betas = np.array(betas)
#
#     nump_weights = nump_weights.reshape(len(nump_weights), 1)
#     nump_betas = nump_betas.reshape(len(nump_betas), 1)
#
#     weights_trans = nump_weights.transpose()
#
#     pfBetas = weights_trans.dot(nump_betas)
#
#     betas_trans = nump_betas.transpose()
#
#     m = np.array(mktVol)
#
#     # Systematic Covariance Matrix
#     sysCov = nump_betas.dot(betas_trans) * (m ** 2)
#
#     # Portfolio Systematic Variance
#     pfSysVol = (((weights_trans.dot(nump_betas)).dot(betas_trans)).dot(nump_weights)) * (m * 2)
#
#     # Specific CoVariance matrix
#     nump_specVols = np.array(df["Unique Risk"].fillna(0))
#     specCov = (np.diag(nump_specVols)) ** 2
#
#     # Portfolio specific variance
#     pfSpecVol = (weights_trans.dot(specCov)).dot(nump_weights)
#
#     # Total Covariance matrix
#
#     totCov = ((nump_betas.dot(betas_trans)) * (m ** 2)) + specCov
#
#     # Portfolio Variance
#     pfVol = ((((weights_trans.dot(nump_betas)).dot(betas_trans)).dot(nump_weights)) * (m ** 2)) + (
#         (weights_trans.dot(specCov)).dot(nump_weights))
#
#     # correlation matrix
#     D = np.array(df["Total Risk"])
#     nump_D = np.diag(D)
#     nump_D_inv = np.linalg.inv(nump_D)
#     CorrMat = nump_D_inv.dot((nump_betas.dot(betas_trans) * (m ** 2)) + specCov).dot(nump_D_inv)
#
#     return pfBetas, sysCov, pfSysVol, specCov, pfSpecVol, totCov, pfVol, CorrMat
#

# #weights_data = portframe.loc[portframe["Alpha"].isin(df["Instrument"])]["weights"]
# betas_data = df["Beta"].fillna(0)
#
# pfBetas, sysCov, pfSysVol, specCov, pfSpecVol, totCov, pfVol, CorrMat = CalcStats(weights_data, betas_data, mktVol,
                                                                                #  df["Unique Risk"])
