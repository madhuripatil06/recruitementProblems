import collections

from timer.lib.conferrenceTimer import ConferenceTimer


def test_when_there_is_only_one_task_in_the_input_then_also_timer_should_give_me_time():
    time = ConferenceTimer().get_time({"Writing Fast Tests Against Enterprise Rails": 60})
    assert time == {
            "Track1":
                "\n9.0AM Writing Fast Tests Against Enterprise Rails"
    }

def test_when_there_are_many_task_in_the_input_then_also_timer_should_give_me_time():
    text = collections.OrderedDict()
    text["Writing Fast Tests Against Enterprise Rails"] = 60
    text["Ruby Errors from Mismatched Gem Versions"] = 45
    time = ConferenceTimer().get_time(text)
    assert time == {
            "Track1":
                "\n9.0AM Writing Fast Tests Against Enterprise Rails\n"
                "10.0AM Ruby Errors from Mismatched Gem Versions"
    }

def test_get_time():
    text = collections.OrderedDict()
    text["Writing Fast Tests Against Enterprise Rails"] = 60
    text["Ruby Errors from Mismatched Gem Versions"] = 45
    text["Lua for the Masses"] = 30
    text["Communicating Over Distance"] = 60
    print ConferenceTimer().get_time(text)
    # assert ConferenceTimer().get_time(text) == {
    #     "Track1":
    #         "\n9.0AM Writing Fast Tests Against Enterprise Rails\n"
    #         "10.0AM Ruby Errors from Mismatched Gem Versions\n"
    #         "10.45 Lua for the Masses\n"
    #         "11.15 Communicating Over Distance"
    # }



def test_time():
    text = collections.OrderedDict()
    text["Writing Fast Tests Against Enterprise Rails"] = 60
    text["Ruby Errors from Mismatched Gem Versions"] = 45
    text["Lua for the Masses"] = 30
    text["Communicating Over Distance"] = 60
    text["Communicating"] = 60
    print ConferenceTimer().get_time(text)
    # assert ConferenceTimer().get_time(text) == {
    #     "Track1":
    #         "\n9.0AM Writing Fast Tests Against Enterprise Rails\n"
    #         "10.0AM Ruby Errors from Mismatched Gem Versions\n"
    #         "10.45 Lua for the Masses\n"
    #         "11.15 Ruby Errors from Mismatched Gem Versions"
    # }



def test_test():
    text = collections.OrderedDict()
    text["Writing Fast Tests Against Enterprise Rails"] = 60
    text["Overdoing it in Python"] = 45
    text["Lua for the Masses"] =  30
    text["Ruby Errors from Mismatched Gem Versions"] = 45
    text["Common Ruby Errors"] = 45
    text["Rails for Python Developers lightning Communicating Over Distance"] = 60
    text["Accounting - Driven Development"] = 45
    text["Woah"] = 30
    text["Sit Down and Write"] = 30
    text["Pair Programming vs Noise"] = 45
    text["Rails Magic"] = 60
    text["Ruby on Rails: Why We Should Move On"] = 60
    text["Clojure Ate Scala(on my project)"] = 45
    text["Programming in the Boondocks of Seattle"] = 30
    text["Ruby vs.Clojure for Back - End Development"] =  30
    text["Ruby on Rails Legacy App Maintenance"] = 60
    text["A World Without HackerNews"] = 30
    text["User Interface CSS in Rails Apps"] = 30
    print ConferenceTimer().get_time(text)
