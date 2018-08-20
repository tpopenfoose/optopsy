from optopsy.option_legs import *
from .enums import OptionType, OrderAction
from .filter import *


default_filters = {
    'abs_delta': [0.4, 0.5, 0.6],
    'leg_1_abs_delta': [0.4, 0.5, 0.6],
    'leg_2_abs_delta': [0.4, 0.5, 0.6],
    'leg_3_abs_delta': [0.4, 0.5, 0.6],
    'leg_4_abs_delta': [0.4, 0.5, 0.6],

    'dte': [
        Period.FOUR_WEEKS.value - 3,
        Period.FOUR_WEEKS.value,
        Period.FOUR_WEEKS.value + 3
    ],
    'leg_1_dte': [
        Period.FOUR_WEEKS.value - 3,
        Period.FOUR_WEEKS.value,
        Period.FOUR_WEEKS.value + 3
    ],
    'leg_2_dte': [
        Period.FOUR_WEEKS.value - 3,
        Period.FOUR_WEEKS.value,
        Period.FOUR_WEEKS.value + 3
    ],
    'leg_3_dte': [
        Period.FOUR_WEEKS.value - 3,
        Period.FOUR_WEEKS.value,
        Period.FOUR_WEEKS.value + 3
    ],
    'leg_4_dte': [
        Period.FOUR_WEEKS.value - 3,
        Period.FOUR_WEEKS.value,
        Period.FOUR_WEEKS.value + 3
    ],

    'price': None,

    'leg_1_leg_2_dist': None,
    'leg_2_leg_3_dist': None,
    'leg_3_leg_4_dist': None
}


def _merge_filters(u_filters):
    cleaned = {k: k[v] for k, v in u_filters if k in default_filters.keys()}
    return {**default_filters, **cleaned}


def _create_spread(legs, **kwargs):
    merged_filters = _merge_filters(**kwargs)
    return list(map(lambda l: _apply_entry_filters(l, merged_filters), legs))


def long_call(data, **kwargs):
    u_filters = {k: v for k, v in kwargs if k in ['abs_delta', 'dte', 'price']}
    legs = create_legs(data, legs=[(OptionType.CALL, 1)])
    return OrderAction.BTO, _create_spread(legs, u_filters)


def short_call(data, u_filters):
    u_filters = {k: v for k, v in kwargs if k in ['abs_delta', 'dte', 'price']}
    legs = create_legs(data, legs=[(OptionType.CALL, 1)])
    return OrderAction.STO, _create_spread(legs, u_filters)


def long_put(data, u_filters):
    u_filters = {k: v for k, v in kwargs if k in ['abs_delta', 'dte', 'price']}
    legs = create_legs(data, legs=[(OptionType.PUT, 1)])
    return OrderAction.BTO, _create_spread(legs, u_filters)


def short_put(data, u_filters):
    u_filters = {k: v for k, v in kwargs if k in ['abs_delta', 'dte', 'price']}
    legs = create_legs(data, legs=[(OptionType.PUT, 1)])
    return OrderAction.STO, _create_spread(legs, u_filters)


# debit
def long_call_spread(data, u_filters):
    u_filters = {k: v for k, v in kwargs if k in
                                            ['leg_1_abs_delta', 'leg_2_abs_delta', 'dte', 'price']}
    legs = create_legs(data, legs=[(OptionType.CALL, 1), (OptionType.CALL, -1)])
    return OrderAction.BTO, _create_spread(legs, u_filters)


# credit
def short_call_spread(data, u_filters):
    legs = create_legs(data, legs=[(OptionType.CALL, -1), (OptionType.CALL, 1)])
    return OrderAction.STO, _create_spread(legs, u_filters)


# credit
def long_put_spread(data, u_filters):
    legs = create_legs(data, legs=[(OptionType.PUT, 1), (OptionType.PUT, -1)])
    return OrderAction.BTO, _create_spread(legs, u_filters)


# debit
def short_put_spread(data, u_filters):
    legs = create_legs(data, legs=[(OptionType.PUT, -1), (OptionType.PUT, 1)])
    return OrderAction.STO, _create_spread(legs, u_filters)


def long_iron_condor(data, u_filters):
    legs = create_legs(data, legs=[(OptionType.PUT, 1), (OptionType.PUT, -1),
        (OptionType.CALL, -1), (OptionType.CALL, 1)])
    return OrderAction.BTO, _create_spread(legs, u_filters)


def short_iron_condor(data, u_filters):
    legs = create_legs(data, legs=[(OptionType.PUT, 1), (OptionType.PUT, -1),
        (OptionType.CALL, -1), (OptionType.CALL, 1)])
    return OrderAction.STO, _create_spread(legs, u_filters)


def long_iron_butterfly(data, u_filters):
    legs = create_legs(data, legs=[(OptionType.PUT, 1), (OptionType.PUT, -1),
        (OptionType.CALL, -1), (OptionType.CALL, 1)])
    return OrderAction.BTO, _create_spread(legs, u_filters)


def short_iron_butterfly(data, u_filters):
    legs = create_legs(data, legs=[(OptionType.PUT, 1), (OptionType.PUT, -1),
        (OptionType.CALL, -1), (OptionType.CALL, 1)])
    return OrderAction.STO, _create_spread(legs, u_filters)
