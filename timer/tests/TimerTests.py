from timer.lib.conferrenceTimer import ConferenceTimer


def test_when_there_is_only_one_task_in_the_input_then_also_timer_should_give_me_time():
    time = ConferenceTimer().get_time({"Writing Fast Tests Against Enterprise Rails": 60})
    assert time == {
            "Track1":
                "9.00AM Writing Fast Tests Against Enterprise Rails"
    }