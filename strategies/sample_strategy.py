import optopsy as op

# Filters take a single value or a tuple as parameters,
# if a tuple is provided for a parameter, the simulation
# will run every possible combinations across all filters.
filters = {
    'strategy': 'long_call_spread',
    'start_date': '2016-12-01',
    'end_date': '2016-12-31',
    
    'entry_leg1_abs_delta': 0.2,
    'entry_leg1_abs_delta_min': 0.15,
    'entry_leg1_abs_delta_max': 0.25,
    
    'entry_leg2_abs_delta': 0.4,
    'entry_leg2_abs_delta_min': 0.35,
    'entry_leg2_abs_delta_max': 0.45,
    
    'entry_dte': 47,
    'entry_dte_min': 40,
    'entry_dte_max': 52,
    
    'exit_dte': 1
}


def run_strategy():
    # fetch the option chains from our data source
    data = op.data.get(
        'data/SPX.csv',
        struct=op.structs.cboe_struct,
        prompt=False
    )

    # test our strategy with our defined filter rules,
    # simulate function will return a dict with three dataframe items: summary, returns
    # and trades
    backtest = op.backtest.simulate('Weekly Verticals', data, filters)


if __name__ == '__main__':
    run_strategy()
