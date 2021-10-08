#Portfolio Valuation

def Port_Valfunc(Comp, Stat, Fini):
    from datetime import datetime as dt
    import pandas as pd
    import pandas_datareader as pdr
    import matplotlib.pyplot as plt
    import matplotlib as mpl
    import numpy as np
    
    result= []
    
    tickers = Comp.split(',')
        
    beg = dt.strptime(Stat, '%d %b %Y')
    fin = dt.strptime(Fini, '%d %b %Y')

    df = pdr.get_data_yahoo(tickers, start=beg, end=fin)['Adj Close']

    returns = df / df.shift(1) - 1  # to obtain the returns of the stock

    mean = returns.mean() # average of returns

    VarianceCo = df.cov() # Variance Covariance of returns
    Components = np.full(len(tickers), 1 / len(tickers))

    TransComponent = Components.transpose()

    PortReturn = np.dot(TransComponent, mean)
    PortVariance = np.dot(np.dot(TransComponent, VarianceCo),TransComponent)
    PortVolatility = PortVariance ** 0.5

    result.append(PortReturn)
    result.append(PortVariance)
    result.append(PortVolatility)
    
    return result
    