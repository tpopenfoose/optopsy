from optopsy.option_legs import *
from .enums import OptionType, OrderAction
from .filter import apply_entry_filters


def long_call(data, u_filters):

    legs = create_legs(data, legs=[(OptionType.CALL, 1)])
    spread = list(map(lambda l: apply_entry_filters(l, u_filters), legs))
    return OrderAction.BTO, spread


def short_call(data, u_filters):
    legs = create_legs(data, legs=[(OptionType.CALL, 1)])
    spread = list(map(lambda l: apply_entry_filters(l, u_filters), legs))
    return OrderAction.STO, spread


def long_put(data, u_filters):
    legs = create_legs(data, legs=[(OptionType.PUT, 1)])
    spread = list(map(lambda l: apply_entry_filters(l, u_filters), legs))
    return OrderAction.BTO, spread


def short_put(data, u_filters):
    legs = create_legs(data, legs=[(OptionType.PUT, 1)])
    spread = list(map(lambda l: apply_entry_filters(l, u_filters), legs))
    return OrderAction.STO, spread


# debit
def long_call_spread(data, u_filters):
    return OrderAction.BTO, create_legs(data, legs=[(OptionType.CALL, 1), (OptionType.CALL, -1)])


# credit
def short_call_spread(data, u_filters):
    return OrderAction.STO, create_legs(data, legs=[(OptionType.CALL, -1), (OptionType.CALL, 1)])


# credit
def long_put_spread(data, u_filters):
    return OrderAction.BTO, create_legs(data, legs=[(OptionType.PUT, 1), (OptionType.PUT, -1)])


# debit
def short_put_spread(data, u_filters):
    return OrderAction.STO, create_legs(data, legs=[(OptionType.PUT, -1), (OptionType.PUT, 1)])


def long_iron_condor(data, u_filters):
    return OrderAction.BTO, create_legs(data, legs=[(OptionType.PUT, 1), (OptionType.PUT, -1),
                                                    (OptionType.CALL, -1), (OptionType.CALL, 1)])


def short_iron_condor(data, u_filters):
    return OrderAction.STO, create_legs(data, legs=[(OptionType.PUT, 1), (OptionType.PUT, -1),
                                                    (OptionType.CALL, -1), (OptionType.CALL, 1)])


def long_iron_butterfly(data, u_filters):
    return OrderAction.BTO, create_legs(data, legs=[(OptionType.PUT, 1), (OptionType.PUT, -1),
                                                    (OptionType.CALL, -1), (OptionType.CALL, 1)])


def short_iron_butterfly(data, u_filters):
    return OrderAction.STO, create_legs(data, legs=[(OptionType.PUT, 1), (OptionType.PUT, -1),
                                                    (OptionType.CALL, -1), (OptionType.CALL, 1)])
