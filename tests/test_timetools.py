# TEST FOR MODULE TIMETOOLS.PY

# Lets import moduleto to be tested
import timetools

# UNIT TESTS DEFINITIONS

# Test if datediff function calculates correct and absolute values
def test_datediff():
    assert timetools.datediff('2023-04-28', '2023-04-10') == 18
    assert timetools.datediff('2023-04-10', '2023-04-28') == 18

# Test if datediff function calculates correct and absolute values
def test_timediff():
    assert round(timetools.timediff('11:30:15', '10:10:05'), 4) == 1.3361
    assert round(timetools.timediff('10:10:05', '11:30:15'), 4) == 1.3361

# Test if dateTimeDiff works correctly 
def test_dateTimeDiff():
    assert timetools.dateTimeDiff('2023-04-27 10:00:00', '2023-04-28 12:30:00') == 26.5

def test_datediff2():
    assert timetools.datediff2('2023-04-10', '2023-04-12', 'day') == 2
    assert timetools.datediff2('2023-04-10', '2023-06-9', 'month') == 2
    assert timetools.datediff2('2023-04-10', '2025-04-10', 'year') == 2

