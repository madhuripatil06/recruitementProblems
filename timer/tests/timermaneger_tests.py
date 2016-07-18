from timer.lib.timemanager import Timer


def test_is_lunch_break_should_return_true_for_time_bet_12_to_1():
    timer = Timer(9.00)
    timer.add_time(60)
    timer.add_time(59)
    assert not timer.is_lunch_break(60)
    assert timer.is_lunch_break(61)

def test_add_time_should_add_the_given_number_of_min_to_the_timer():
    timer = Timer(9.00)
    time = timer.add_time(60)
    assert time == "10.0AM"
    assert timer.add_time(90) == "11.3AM"

def test_add_time_should_return_1_pm_if_add_to_the_lunch_break():
    timer = Timer(9.00)
    assert timer.update_available_time(180) == "1.0PM"

def test_get_the_next_mins_to_add_should_return_the_min_to_add():
    time =Timer(9.00)
    assert time.get_the_next_mins_to_add(60) == 60
    timer = Timer(9.45)
    assert timer.get_the_next_mins_to_add(60) == 105
