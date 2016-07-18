from timer.lib.track import Track


def test_is_fit_for_given_time_should_give_true_if_the_track_has_place_for_the_time_given():
    track = Track()
    assert track.is_fit_for_given_time(60)
    track.add_task("first task", 120)
    assert track.is_fit_for_given_time(60)
    track.add_task("second_task" , 30)
    assert track.is_fit_for_given_time(60)

def test_is_fit_for_given_time_should_give_false_if_the_track_not_has_place_for_the_time_given():
    track = Track()
    track.add_task("first task", 180)
    track.add_task("second task", 180)
    assert not track.is_fit_for_given_time(20)

def test_is_full_should_return_if_the_given_track_is_full():
    track = Track()
    track.add_task("first task", 180)
    assert not track.is_full()
    track.add_task("second_task", 180)
    assert track.is_full()

