import pandas as pd
import numpy as np
from datetime import datetime
from pandas import DataFrame
from sqlalchemy import create_engine
import psycopg2
import matplotlib


def GetICsAndWeight(rDate, indexCode):
    '''

    :param rDate:
    :param indexCode:
    :return:
    '''
    # Load IC table
    tbl_Index_Constituents = pd.read_csv("tbl_Index_Constituents.csv")
    # Remove timestamp from date column
    tbl_Index_Constituents["Quarter"] = pd.to_datetime(tbl_Index_Constituents["Date"]).dt.quarter
    tbl_Index_Constituents["Date"] = pd.to_datetime(tbl_Index_Constituents["Date"]).dt.strftime("%Y-%m")
    # print(tbl_Index_Constituents.Date)
    # Convert Rdate to datetime for comparison
    # Create dataframe which contains dates being looked for
    datetbl = (tbl_Index_Constituents[tbl_Index_Constituents["Date"] == rDate])
    ics = ["LRGC", "MIDC", "SMLC"]
    if indexCode == "FLED":
        newindex = 'ALSI'
    elif indexCode in ics:
        newindex = 'Index'
    else:
        newindex = indexCode
    newdata = datetbl[datetbl[newindex + " New"] == newindex]

    # Get market index code from indexcode
    if indexCode == 'ALSI':
        mktIndexCode = 'J203'
    elif indexCode == 'TOPI':
        mktIndexCode = 'J200'
    elif indexCode == 'RESI':
        mktIndexCode = 'J258'
    elif indexCode == 'FINI':
        mktIndexCode = 'J250'
    elif indexCode == 'INDI':
        mktIndexCode = 'J257'

    # Select column with Index Code
    total = newdata["Gross Market Capitalisation"].sum(axis=0)
    # return weights
    newdata["weights"] = newdata["Gross Market Capitalisation"] / total
    # newdata.fillna(0)
    # ICs = newdata[["Alpha"]]
    # weights = newdata[["weights"]]

    portframe = newdata[["Alpha", "weights"]]
    portframe.rename(columns={'Alpha': 'Instrument'}, inplace=True)
    return portframe, mktIndexCode


# portframe = GetICsAndWeight(rDate="2017-09", indexCode="TOPI")


def GetBetasMktAndSpecVols(rDate, ICs, mktIndexCode, portframe):
    '''

    :param rDate:
    :param ICs:
    :param mktIndexCode:
    :return:
    '''
    Ba_Output = pd.read_csv("tbl_BA_Beta_Output.csv")
    Ba_Output["Quarter"] = pd.to_datetime(Ba_Output["End Date"]).dt.quarter
    Ba_Output["End Date"] = pd.to_datetime(Ba_Output["End Date"]).dt.strftime("%Y-%m")

    datetbl = (Ba_Output[Ba_Output["End Date"] == rDate])

    frame = datetbl.loc[datetbl["Instrument"].isin(ICs)]
    # print(frame)
    frame = pd.merge(frame, portframe, on='Instrument')
    betasframe = frame.loc[frame["Index"] == mktIndexCode]
    betasframe['Beta'] = betasframe['Beta'].fillna(0)

    betasframe['Unique Risk'] = betasframe['Unique Risk'].fillna(0)

    mktframe = datetbl.loc[datetbl["Instrument"] == mktIndexCode]

    mktVol = mktframe[["Total Risk"]].iloc[0]

    # print(mktVol)
    # create dataframe with instrument's beta values

    df = betasframe[["Instrument", "Beta", "Unique Risk", "Total Risk", "weights"]]
    # print(df)
    return mktVol, df


# mktVol, df = GetBetasMktAndSpecVols(rDate="2017-09", ICs=portframe["Alpha"], mktIndexCode="J200")


def CalcStats(weights, betas, mktVol, specVols, totalRisk):
    '''

    :param weights:
    :param betas:
    :param mktVol:
    :param specVols:
    :param totalRisk:
    :param portframe:
    :return:
    '''
    # convert dataframe to array
    nump_weights = np.array(weights)
    nump_betas = np.array(betas)

    nump_weights = nump_weights.reshape(len(nump_weights), 1)
    nump_betas = nump_betas.reshape(len(nump_betas), 1)
    weights_trans = nump_weights.transpose()
    # print(nump_betas.shape)

    pfBetas = weights_trans.dot(nump_betas)
    pfBetas = pfBetas[0][0]

    betas_trans = nump_betas.transpose()

    m = np.array(mktVol)

    # Systematic Covariance Matrix
    sysCov = nump_betas.dot(betas_trans) * (m ** 2)
    # convert matrix to dataframe

    # Portfolio Systematic Variance
    pfSysVol = (((weights_trans.dot(nump_betas)).dot(betas_trans)).dot(nump_weights)) * (m * 2)
    pfSysVol = pfSysVol[0][0]

    # Specific CoVariance matrix
    nump_specVols = np.array(specVols)
    specCov = (np.diag(nump_specVols)) ** 2

    # Portfolio specific variance
    pfSpecVol = (weights_trans.dot(specCov)).dot(nump_weights)
    pfSpecVol = pfSpecVol[0][0]

    # Total Covariance matrix
    totCov = ((nump_betas.dot(betas_trans)) * (m ** 2)) + specCov

    # Portfolio Variance
    pfVol = ((((weights_trans.dot(nump_betas)).dot(betas_trans)).dot(nump_weights)) * (m ** 2)) + (
        (weights_trans.dot(specCov)).dot(nump_weights))
    pfVol = pfVol[0][0]

    # correlation matrix
    D = np.array(totalRisk)
    nump_D = np.diag(D)
    nump_D_inv = np.linalg.inv(nump_D)
    CorrMat = nump_D_inv.dot((nump_betas.dot(betas_trans) * (m ** 2)) + specCov).dot(nump_D_inv)

    return pfBetas, sysCov, pfSysVol, specCov, pfSpecVol, totCov, pfVol, CorrMat


#
# pfBetas, sysCov, pfSysVol, specCov, pfSpecVol, totCov, pfVol, CorrMat = CalcStats(weights_data, betas_data, mktVol,
#  df["Unique Risk"])


def GetICSTime(indexCode):
    '''

    Function similar to function getICAndWeight but looks at all dates
    Dates are shown as year and quarter

    :param indexCode:
    :return: dateframe year, quarter and Alpha
    '''

    tbl_Index_Constituents = pd.read_csv("tbl_Index_Constituents.csv")
    # Remove timestamp from date column and return quarter and yar from date column
    tbl_Index_Constituents["Quarter"] = pd.to_datetime(tbl_Index_Constituents["Date"]).dt.quarter
    tbl_Index_Constituents["Date"] = pd.to_datetime(tbl_Index_Constituents["Date"]).dt.strftime("%Y-%m")
    tbl_Index_Constituents["Year"] = pd.DatetimeIndex(tbl_Index_Constituents["Date"]).year

    # Get ICS ensuring same membership

    ics = ["LRGC", "MIDC", "SMLC"]
    if indexCode == "FLED":
        newindex = 'ALSI'
    elif indexCode in ics:
        newindex = 'Index'
    else:
        newindex = indexCode
    newdata = tbl_Index_Constituents[tbl_Index_Constituents[newindex + " New"] == newindex]

    # Get market index code from indexcode
    if indexCode == 'ALSI':
        mktIndexCode = 'J203'
    elif indexCode == 'TOPI':
        mktIndexCode = 'J200'
    elif indexCode == 'RESI':
        mktIndexCode = 'J258'
    elif indexCode == 'FINI':
        mktIndexCode = 'J250'
    elif indexCode == 'INDI':
        mktIndexCode = 'J257'

    return newdata[["Year", "Quarter", "Alpha"]]


def PortfolioBetasMktAndSpecVols(ICs, weights, mktIndexCode):
    """

    :param ICs:
    :param weights:
    :param mktIndexCode:
    :return:
    """
    # read the data
    Ba_Output = pd.read_csv("tbl_BA_Beta_Output.csv")
    # Ba_Output = pd.read_csv("/content/drive/My Drive/Data/tbl_BA_Beta_Output.csv")
    # adding quarter info
    Ba_Output["Quarter"] = pd.to_datetime(Ba_Output["End Date"]).dt.quarter
    # converting the dates to quarters
    Ba_Output["Year"] = pd.DatetimeIndex(Ba_Output["End Date"]).year
    Ba_Output["End Date"] = pd.to_datetime(Ba_Output["End Date"]).dt.strftime("%Y-%m")

    datetbl = Ba_Output
    mktframe = datetbl.loc[datetbl["Instrument"] == mktIndexCode]
    mkt_val = pd.Series(mktframe['Total Risk'].unique())
    mkt_val = mkt_val.tolist()

    frame = datetbl.loc[datetbl["Instrument"].isin(ICs)]
    betasframe = frame.loc[frame["Index"] == mktIndexCode]
    datetbl = betasframe
    datetbl["New Date"] = datetbl["Year"].map(str) + " - Q" + datetbl["Quarter"].map(str)
    # create dataframe with instrument's beta values
    df = betasframe[["New Date", "Instrument", "Beta", "Unique Risk", "Total Risk"]]
    # df["New Date"] = pd.to_datetime(df["Date"]).dt.strftime("%Y-%m")

    dates = pd.Series(df['New Date'].unique())

    # Empty array of portfolio betas that we will append the portflio betas with the for-loop
    pfBetas = []

    for date, group in df.groupby('New Date'):
        # Instrument Betas per quarter
        nump_betas = np.array(group['Beta'])
        # Instrument Betas enetered by user - (Weights is defined in the previous cell)
        nump_weights = np.array(weights)

        # Calculation portfolio betas through time
        nump_weights = nump_weights.reshape(len(nump_weights), 1)
        nump_betas = nump_betas.reshape(len(nump_betas), 1)

        weights_trans = nump_weights.transpose()

        pfBeta = weights_trans.dot(nump_betas).flatten()[0]
        # Appending portfolio beta to an empty array pfBetas
        pfBetas.append(pfBeta)

    dict_list = {'Dates': dates, 'pfBeta': pfBetas}
    newframe = pd.DataFrame(dict_list)
    mkt_dict = {'Total Risk': mkt_val}
    mkt_dict = pd.DataFrame(mkt_dict)
    return newframe, mkt_dict


def PortfolioRisk(ICs, weights, mktIndexCode, mkt_val):
    # read the data
    Ba_Output = pd.read_csv("tbl_BA_Beta_Output.csv")

    # adding quarter info
    Ba_Output["Quarter"] = pd.to_datetime(Ba_Output["End Date"]).dt.quarter
    # converting the dates to quarters
    Ba_Output["Year"] = pd.DatetimeIndex(Ba_Output["End Date"]).year
    Ba_Output["End Date"] = pd.to_datetime(Ba_Output["End Date"]).dt.strftime("%Y-%m")

    datetbl = Ba_Output
    datetbl["New Date"] = datetbl["Year"].map(str) + " - Q" + datetbl["Quarter"].map(str)
    frame = datetbl.loc[datetbl["Instrument"].isin(ICs)]
    betasframe = frame.loc[frame["Index"] == mktIndexCode]

    # create dataframe with instrument's beta values
    df = betasframe[["New Date", "Instrument", "Beta", "Unique Risk", "Total Risk"]]

    dates = pd.Series(df['New Date'].unique())

    # Empty array of portfolio risk statistics that we will append the portflio betas with the for-loop
    pfSysVols = []
    pfSpecVols = []
    pfVols = []
    i = 0

    for date, group in df.groupby('New Date'):
        # Instrument Betas per quarter
        nump_betas = np.array(group['Beta'])
        # Instrument Betas enetered by user - (Weights is defined in the previous cell)
        nump_weights = np.array(weights)

        # Calculation portfolio betas through time
        nump_weights = nump_weights.reshape(len(nump_weights), 1)
        nump_betas = nump_betas.reshape(len(nump_betas), 1)

        weights_trans = nump_weights.transpose()

        pfBetas = weights_trans.dot(nump_betas)
        betas_trans = nump_betas.transpose()

        m = (mkt_val[i])

        # Systematic Covariance Matrix
        sysCov = nump_betas.dot(betas_trans) * (m ** 2)

        # Portfolio Systematic Variance
        pfSysVol = ((((weights_trans.dot(nump_betas)).dot(betas_trans)).dot(nump_weights)) * (m * 2)).flatten()[0]

        # Specific CoVariance matrix
        nump_specVols = np.array(group["Unique Risk"].fillna(0))
        specCov = (np.diag(nump_specVols)) ** 2

        # Portfolio specific variance
        pfSpecVol = ((weights_trans.dot(specCov)).dot(nump_weights)).flatten()[0]

        # Total Covariance matrix
        totCov = ((nump_betas.dot(betas_trans)) * (m ** 2)) + specCov

        # Portfolio Variance
        pfVol = (((((weights_trans.dot(nump_betas)).dot(betas_trans)).dot(nump_weights)) * (m ** 2)) + (
            (weights_trans.dot(specCov)).dot(nump_weights))).flatten()[0]

        # Appending portfolio beta to an empty array pfBetas

        pfSysVols.append(pfSysVol)
        pfSpecVols.append(pfSpecVol)
        pfVols.append(pfVol)
        i += 1

    return dates, pfSysVols, pfSpecVols, pfVols


def PortFolioIcs(mktIndexCode):
    """

    :param mktIndexCode:
    :return:
    """
    Ba_Output = pd.read_csv("tbl_BA_Beta_Output.csv")
    # Ba_Output = pd.read_csv("/content/drive/My Drive/Data/tbl_BA_Beta_Output.csv")
    # adding quarter info
    Ba_Output["Quarter"] = pd.to_datetime(Ba_Output["End Date"]).dt.quarter
    # converting the dates to quarters
    Ba_Output["Year"] = pd.DatetimeIndex(Ba_Output["End Date"]).year
    Ba_Output["End Date"] = pd.to_datetime(Ba_Output["End Date"]).dt.strftime("%Y-%m")

    datetbl = Ba_Output
    # frame = datetbl.loc[datetbl["Instrument"].isin(ICs)]
    betasframe = datetbl.loc[datetbl["Index"] == mktIndexCode]
    ics_list = betasframe.Instrument.unique().tolist()
    return ics_list


def GetICSTime(indexCode):
    tbl_Index_Constituents = pd.read_csv("tbl_Index_Constituents.csv")
    # Remove timestamp from date column and return quarter and yar from date column
    tbl_Index_Constituents["Quarter"] = pd.to_datetime(tbl_Index_Constituents["Date"]).dt.quarter
    tbl_Index_Constituents["Date"] = pd.to_datetime(tbl_Index_Constituents["Date"]).dt.strftime("%Y-%m")
    tbl_Index_Constituents["Year"] = pd.DatetimeIndex(tbl_Index_Constituents["Date"]).year

    # Get ICS ensuring same membership

    ics = ["LRGC", "MIDC", "SMLC"]
    if indexCode == "FLED":
        newindex = 'ALSI'
    elif indexCode in ics:
        newindex = 'Index'
    else:
        newindex = indexCode
    newdata = tbl_Index_Constituents[tbl_Index_Constituents[newindex + " New"] == newindex]

    # Get market index code from indexcode
    if indexCode == 'ALSI':
        mktIndexCode = 'J203'
    elif indexCode == 'TOPI':
        mktIndexCode = 'J200'
    elif indexCode == 'RESI':
        mktIndexCode = 'J258'
    elif indexCode == 'FINI':
        mktIndexCode = 'J250'
    elif indexCode == 'INDI':
        mktIndexCode = 'J257'

    # Select column with Index Code
    total = newdata["Gross Market Capitalisation"].sum(axis=0)
    # return weights
    newdata["weights"] = newdata["Gross Market Capitalisation"] / total
    # newdata.fillna(0)
    # ICs = newdata[["Alpha"]]
    # weights = newdata[["weights"]]

    icsFrame = newdata[["Alpha", "weights"]]
    icsFrame.rename(columns={'Alpha': 'Instrument'}, inplace=True)
    return icsFrame, mktIndexCode


def GetBetasTime(mktIndexCode, icsFrame):
    Ba_Output = pd.read_csv("tbl_BA_Beta_Output.csv")
    Ba_Output["Quarter"] = pd.to_datetime(Ba_Output["End Date"]).dt.quarter
    Ba_Output["End Date"] = pd.to_datetime(Ba_Output["End Date"]).dt.strftime("%Y-%m")
    Ba_Output["Year"] = pd.DatetimeIndex(Ba_Output["End Date"]).year

    datetbl = Ba_Output

    datetbl["New Date"] = datetbl["Year"].map(str) + " - Q" + datetbl["Quarter"].map(str)
    frame = datetbl.loc[datetbl["Instrument"].isin(icsFrame.Instrument)]

    frame = pd.merge(frame, icsFrame, on='Instrument')
    betasframe = frame.loc[frame["Index"] == mktIndexCode]

    betasframe['Beta'] = betasframe['Beta'].fillna(0)
    betasframe['Unique Risk'] = betasframe['Unique Risk'].fillna(0)
    dates = pd.Series(betasframe['New Date'].unique())

    new_frame = betasframe[["New Date", "Instrument", "Beta", "Unique Risk", "Total Risk", "weights"]]
    # print(df)
    mktframe = datetbl.loc[datetbl["Instrument"] == mktIndexCode]
    mkt_val = pd.Series(mktframe['Total Risk'].unique())
    mkt_val = mkt_val.tolist()
    return new_frame, mkt_val


def PortfolioBetasTime(new_frame):
    # read the data

    dates = pd.Series(new_frame['New Date'].unique())
    print(dates)

    # Empty array of portfolio betas that we will append the portflio betas with the for-loop
    pfBetas = []

    for date, group in new_frame.groupby('New Date'):
        # Instrument Betas per quarter
        nump_betas = np.array(group['Beta'])

        # Instrument Betas enetered by user - (Weights is defined in the previous cell)
        nump_weights = np.array(group['weights'])

        # Calculation portfolio betas through time
        nump_weights = nump_weights.reshape(len(nump_weights), 1)
        nump_betas = nump_betas.reshape(len(nump_betas), 1)

        weights_trans = nump_weights.transpose()

        pfBeta = weights_trans.dot(nump_betas).flatten()[0]
        # Appending portfolio beta to an empty array pfBetas
        pfBetas.append(pfBeta)

    dict_list = {'Dates': dates, 'pfBeta': pfBetas}
    betasframe = pd.DataFrame(dict_list)
    return betasframe



def RiskTime(new_frame, mkt_val):
    dates = pd.Series(new_frame['New Date'].unique())

    # Empty array of portfolio risk statistics that we will append the portflio betas with the for-loop
    pfSysVols = []
    pfSpecVols = []
    pfVols = []
    i = 0
    for date, group in new_frame.groupby('New Date'):
        # Instrument Betas per quarter
        nump_betas = np.array(group['Beta'])
        # Instrument Betas enetered by user - (Weights is defined in the previous cell)
        nump_weights = np.array(group['weights'])

        # Calculation portfolio betas through time
        nump_weights = nump_weights.reshape(len(nump_weights), 1)

        nump_betas = nump_betas.reshape(len(nump_betas), 1)

        weights_trans = nump_weights.transpose()

        pfBetas = weights_trans.dot(nump_betas)
        betas_trans = nump_betas.transpose()

        m = (mkt_val[i])

        i += 1

        # Systematic Covariance Matrix
        sysCov = nump_betas.dot(betas_trans) * (m ** 2)

        # Portfolio Systematic Variance
        pfSysVol = ((((weights_trans.dot(nump_betas)).dot(betas_trans)).dot(nump_weights)) * (m * 2)).flatten()[0]

        # Specific CoVariance matrix
        nump_specVols = np.array(group["Unique Risk"].fillna(0))
        specCov = (np.diag(nump_specVols)) ** 2

        # Portfolio specific variance
        pfSpecVol = ((weights_trans.dot(specCov)).dot(nump_weights)).flatten()[0]

        # Total Covariance matrix
        totCov = ((nump_betas.dot(betas_trans)) * (m ** 2)) + specCov

        # Portfolio Variance
        pfVol = (((((weights_trans.dot(nump_betas)).dot(betas_trans)).dot(nump_weights)) * (m ** 2)) + (
            (weights_trans.dot(specCov)).dot(nump_weights))).flatten()[0]

        # Appending portfolio beta to an empty array pfBetas

        pfSysVols.append(pfSysVol)
        pfSpecVols.append(pfSpecVol)
        pfVols.append(pfVol)

    # dict_list = {'Dates': dates, 'pfSysVols': pfSysVols, 'pfSpecVols': pfSpecVols, 'pfVols':pfVols}
    # RiskFrame = pd.DataFrame(dict_list)
    return dates, pfSysVols, pfSpecVols, pfVols
