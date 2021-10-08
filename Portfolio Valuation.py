#Portfolio Valuation

import sys
sys.path.append('A:\Lekan\Miscellaneous\python\modules\Portfolio')
import Port_Valfunc as PV

tick = 'AAPL,GE,GOOG,IBM,ADM,ABF,AAL'
start = '10 Jul 2012'
finish = '10 Jul 2020'

res = PV.Port_Valfunc(tick, start, finish)

print('Portfolio Return is ' + str(res[0] * 100) + ' %')
print('Portfolio Variance is ' + str(res[1]))
print('Portfolio Volatility is ' + str(res[2]))