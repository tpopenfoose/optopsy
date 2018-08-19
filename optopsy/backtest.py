from .option_strategy import *

default_filters = {
    'strategy': None,
    'start_date': None,
    'end_date': None,
    'entry_leg1_abs_delta': 0.2,
    'entry_leg1_abs_delta_min': 0.15,
    'entry_leg1_abs_delta_max': 0.25,
    'entry_leg2_abs_delta': 0.4,
    'entry_leg2_abs_delta_min': 0.35,
    'entry_leg2_abs_delta_max': 0.45,
    'entry_leg3_abs_delta': 0.6,
    'entry_leg3_abs_delta_min': 0.55,
    'entry_leg3_abs_delta_max': 0.65,
    'entry_leg4_abs_delta': 0.8,
    'entry_leg4_abs_delta_min': 0.75,
    'entry_leg4_abs_delta_max': 0.85,
    'entry_dte': Period.FOUR_WEEKS.value,
    'entry_dte_min': Period.FOUR_WEEKS.value - 3,
    'entry_dte_max': Period.FOUR_WEEKS.value + 3,
    'entry_spread_price': None,
    'exit_spread_price': None,
    'exit_dte': None,
    'exit_leg1_abs_delta': None,
    'exit_leg1_abs_delta_min': None,
    'exit_leg1_abs_delta_max': None,
    'exit_leg2_abs_delta': None,
    'exit_leg2_abs_delta_min': None,
    'exit_leg2_abs_delta_max': None,
    'exit_leg3_abs_delta': None,
    'exit_leg3_abs_delta_min': None,
    'exit_leg3_abs_delta_max': None,
    'exit_leg4_abs_delta': None,
    'exit_leg4_abs_delta_min': None,
    'exit_leg4_abs_delta_max': None,
    'leg_1_leg_2_dist': None,
    'leg_2_leg_3_dist': None,
    'leg_3_leg_4_dist': None
}


def _merge_filters(user_filters):
    cleaned = {k: k[v] for k, v in user_filters if k in default_filters.keys()}
    return {**default_filters, **cleaned}


def _apply_filters(data, filters):
    return



# this is the main function that runs the backtest engine
def simulate(title, data, filters):
    # merge user defined filter with defaults
    merged_filter = _merge_filters(filters)

    # call the appropriate option strategy function based on the 'strategy'
    # attribute of the filter
    


    # option strategy function will create option spreads that match the entry
    # filter's parameters

    # filter the main option chain for only the options that are used to create the spreads

    # search the main option chain for options that match the exit criteria

    # if exit criterion are met for all legs of the spread, simulate a sell action
    pass
