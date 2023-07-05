
import pandas as pd

from zipline.data.bundles import register
from zipline.data.bundles.csvdir import csvdir_equities
register(
    'snp500',
    csvdir_equities(
        ['daily'],
        '/home/mehedi/Documents/snp500_backtest/snp_500_backtest/data'
    ),
    calendar_name='XNYS',
   
    
)


