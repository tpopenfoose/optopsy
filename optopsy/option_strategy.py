from optopsy.option_legs import *
from .enums import OptionType, OrderAction
from functools import reduce
import filter as f


leg_filters = {
    'abs_delta': (0.4, 0.5, 0.6),
    'leg_1_abs_delta': (0.1, 0.2, 0.3),
    'leg_2_abs_delta': (0.3, 0.4, 0.5),
    'leg_3_abs_delta': (0.5, 0.6, 0.7),
    'leg_4_abs_delta': (0.7, 0.8, 0.9),

    'dte': (
        Period.FOUR_WEEKS.value - 3,
        Period.FOUR_WEEKS.value,
        Period.FOUR_WEEKS.value + 3
    ),
    'leg_1_dte': (
        Period.FOUR_WEEKS.value - 3,
        Period.FOUR_WEEKS.value,
        Period.FOUR_WEEKS.value + 3
    ),
    'leg_2_dte': (
        Period.FOUR_WEEKS.value - 3,
        Period.FOUR_WEEKS.value,
        Period.FOUR_WEEKS.value + 3
    ),
    'leg_3_dte': (
        Period.FOUR_WEEKS.value - 3,
        Period.FOUR_WEEKS.value,
        Period.FOUR_WEEKS.value + 3
    ),
    'leg_4_dte': (
        Period.FOUR_WEEKS.value - 3,
        Period.FOUR_WEEKS.value,
        Period.FOUR_WEEKS.value + 3
    ),
}

spread_filters = {
    'price': None,
    'leg_1_leg_2_dist': None,
    'leg_2_leg_3_dist': None,
    'leg_3_leg_4_dist': None
}


def _create_spread(legs, valid_filters, **kwargs):
	
	l_filters = _process_filters(leg_filters, valid_filters, kwargs)
    filtered_legs = list(map(lambda l: _apply_entry_filters(l, l_filters), legs))
    
    spread = _build_spread(filtered_legs)
    
    s_filters = _process_filters(spread_filters, valid_filters, kwargs)
    return _apply_entry_filters(spread, s_filters)


def _process_filters(base, filters, **kwargs):
	f = {k: v for k, v in kwargs if k in filters}
	return _merged_filters(base, f)
	
# make sure this merges properly
def _merge_filters(base, filters):
	return {k: base[k] for k, v in filters if k[v] is None}


def _apply_entry_filters(leg, m_filters):
	return reduce(lambda k: leg.pipe(_do_apply_entry_filter, k=k, v=m_filters[k]), m_filters.keys())


def _build_spread(legs):
	pass
	
	
# this returns a dataframe
def _do_apply_entry_filters(l, k, v):
	return getattr(f, k)(l, v)


def long_call(data, **kwargs):
	valid_filters = ['abs_delta', 'dte', 'price']
    legs = create_legs(data, legs=[(OptionType.CALL, 1)])
    return OrderAction.BTO, _create_spread(legs, valid_filters, kwargs)


def short_call(data, **kwargs):
    valid_filters = ['abs_delta', 'dte', 'price']
    legs = create_legs(data, legs=[(OptionType.CALL, 1)])
    return OrderAction.STO, _create_spread(legs, valid_filters, kwargs)


def long_put(data, **kwargs):
    valid_filters = ['abs_delta', 'dte', 'price']
    legs = create_legs(data, legs=[(OptionType.PUT, 1)])
    return OrderAction.BTO, _create_spread(legs, valid_filters, kwargs)


def short_put(data, **kwargs):
    valid_filters = ['abs_delta', 'dte', 'price']
    legs = create_legs(data, legs=[(OptionType.PUT, 1)])
    return OrderAction.STO, _create_spread(legs, valid_filters, kwargs)


# debit
def long_call_spread(data, **kwargs):
    valid_filters = ['leg_1_abs_delta', 'leg_2_abs_delta', 'dte', 'price']
    legs = create_legs(data, legs=[(OptionType.CALL, 1), (OptionType.CALL, -1)])
    return OrderAction.BTO, _create_spread(legs, valid_filters, kwargs)


# credit
def short_call_spread(data, **kwargs):
	valid_filters = ['leg_1_abs_delta', 'leg_2_abs_delta', 'dte', 'price']
    legs = create_legs(data, legs=[(OptionType.CALL, -1), (OptionType.CALL, 1)])
    return OrderAction.STO, _create_spread(legs, valid_filters, kwargs)


# credit
def long_put_spread(data, **kwargs):
	valid_filters = ['leg_1_abs_delta', 'leg_2_abs_delta', 'dte', 'price']
    legs = create_legs(data, legs=[(OptionType.PUT, 1), (OptionType.PUT, -1)])
    return OrderAction.BTO, _create_spread(legs, valid_filters, kwargs)


# debit
def short_put_spread(data, **kwargs):
	valid_filters = ['leg_1_abs_delta', 'leg_2_abs_delta', 'dte', 'price']
    legs = create_legs(data, legs=[(OptionType.PUT, -1), (OptionType.PUT, 1)])
    return OrderAction.STO, _create_spread(legs, valid_filters, kwargs)


def long_iron_condor(data, **kwargs):
	valid_filters = ['leg_1_abs_delta', 'leg_2_abs_delta', 'leg_3_abs_delta',
 					'leg_4_abs_delta', 'dte', 'price', 'leg_1_leg_2_dist',
					 'leg_2_leg_3_dist', 'leg_3_leg_4_dist']
    legs = create_legs(data, legs=[(OptionType.PUT, 1), (OptionType.PUT, -1),
        (OptionType.CALL, -1), (OptionType.CALL, 1)])
    return OrderAction.BTO, _create_spread(legs, valid_filters, kwargs)


def short_iron_condor(data, **kwargs):
	valid_filters = ['leg_1_abs_delta', 'leg_2_abs_delta', 'leg_3_abs_delta',
 					'leg_4_abs_delta', 'dte', 'price', 'leg_1_leg_2_dist',
					 'leg_2_leg_3_dist', 'leg_3_leg_4_dist']
    legs = create_legs(data, legs=[(OptionType.PUT, 1), (OptionType.PUT, -1),
        (OptionType.CALL, -1), (OptionType.CALL, 1)])
    return OrderAction.STO, _create_spread(legs, valid_filters, kwargs)


def long_iron_butterfly(data, **kwargs):
	valid_filters = ['leg_1_abs_delta', 'leg_2_abs_delta', 'leg_3_abs_delta',
 					'leg_4_abs_delta', 'dte', 'price', 'leg_1_leg_2_dist',
					 'leg_3_leg_4_dist']
    legs = create_legs(data, legs=[(OptionType.PUT, 1), (OptionType.PUT, -1),
        (OptionType.CALL, -1), (OptionType.CALL, 1)])
    return OrderAction.BTO, _create_spread(legs, valid_filters, kwargs)


def short_iron_butterfly(data, **kwargs):
	valid_filters = ['leg_1_abs_delta', 'leg_2_abs_delta', 'leg_3_abs_delta',
 					'leg_4_abs_delta', 'dte', 'price', 'leg_1_leg_2_dist',
					 'leg_3_leg_4_dist']
    legs = create_legs(data, legs=[(OptionType.PUT, 1), (OptionType.PUT, -1),
        (OptionType.CALL, -1), (OptionType.CALL, 1)])
    return OrderAction.STO, _create_spread(legs, valid_filters, kwargs)
