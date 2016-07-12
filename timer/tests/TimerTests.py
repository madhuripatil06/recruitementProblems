from timer.lib.conferrenceTimer import Timer


def test_when_there_is_only_one_task_in_the_input_then_also_timer_should_give_me_time():
    time = Timer({"Writing Fast Tests Against Enterprise Rails": 60}).get_time()
    assert time == {
            "track1":[
                "9.00AM Writing Fast Tests Against Enterprise Rails"
            ]
    }