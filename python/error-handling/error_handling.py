
import error_handling_test

def handle_error_by_throwing_exception():
    raise Exception("Failed while doing something")


def handle_error_by_returning_none(input_data):
    if input_data.isdigit():
        return int(input_data)
    else:
        return None


def handle_error_by_returning_tuple(input_data):
    if input_data.isdigit():
        return (True, int(input_data))
    else:
        return (False, input_data)


def filelike_objects_are_closed_on_exception(filelike_object):
    try:
        filelike_object.do_something()
    except Exception as err:
        if filelike_object.is_open():
            filelike_object.close()