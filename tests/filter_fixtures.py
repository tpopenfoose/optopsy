import pytest
from optopsy.enums import Period


@pytest.fixture
def default_filters():
    return {
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

