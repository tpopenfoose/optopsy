from optopsy.option_legs import *
from .enums import OptionType, OrderAction, Period


def long_call(data):
    return OrderAction.BTO, create_legs(data, legs=[(OptionType.CALL, 1)])


def short_call(data):
    return OrderAction.STO, create_legs(data, legs=[(OptionType.CALL, 1)])


def long_put(data):
    return OrderAction.BTO, create_legs(data, legs=[(OptionType.PUT, 1)])


def short_put(data):
    return OrderAction.STO, create_legs(data, legs=[(OptionType.PUT, 1)])


# debit
def long_call_spread(data):
    return OrderAction.BTO, create_legs(data, legs=[(OptionType.CALL, 1), (OptionType.CALL, -1)])


# credit
def short_call_spread(data):
    return OrderAction.STO, create_legs(data, legs=[(OptionType.CALL, -1), (OptionType.CALL, 1)])


# credit
def long_put_spread(data):
    return OrderAction.BTO, create_legs(data, legs=[(OptionType.PUT, 1), (OptionType.PUT, -1)])


# debit
def short_put_spread(data):
    return OrderAction.STO, create_legs(data, legs=[(OptionType.PUT, -1), (OptionType.PUT, 1)])


def long_iron_condor(data):
    return OrderAction.BTO, create_legs(data, legs=[(OptionType.PUT, 1), (OptionType.PUT, -1),
                                                    (OptionType.CALL, -1), (OptionType.CALL, 1)])


def short_iron_condor(data):
    return OrderAction.STO, create_legs(data, legs=[(OptionType.PUT, 1), (OptionType.PUT, -1),
                                                    (OptionType.CALL, -1), (OptionType.CALL, 1)])


def long_iron_butterfly(data):
    return OrderAction.BTO, create_legs(data, legs=[(OptionType.PUT, 1), (OptionType.PUT, -1),
                                                    (OptionType.CALL, -1), (OptionType.CALL, 1)])


def short_iron_butterfly(data):
    return OrderAction.STO, create_legs(data, legs=[(OptionType.PUT, 1), (OptionType.PUT, -1),
                                                    (OptionType.CALL, -1), (OptionType.CALL, 1)])
