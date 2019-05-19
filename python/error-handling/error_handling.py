def handle_error_by_throwing_exception():
    raise Exception("Error.")


def handle_error_by_returning_none(input_data):
    try:
        return int(input_data)
    except ValueError:
        return None


def handle_error_by_returning_tuple(input_data):
    try:
        return True, int(input_data)
    except ValueError:
        return False, input_data


def filelike_objects_are_closed_on_exception(filelike_object):
    try:
        if filelike_object.is_open is False:
            filelike_object.open()
        filelike_object.do_something()
    except Exception as err:
        raise err("filelike_object failed doing something.")
    finally:
        filelike_object.close()
