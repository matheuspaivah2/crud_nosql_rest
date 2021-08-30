

def check_valid_data(data):
    for key in data:
        if key != 'tags':
            if type(data[key]) != str:
                return False
        else:
            for k in data['tags']:
                if type(k) != str:
                    return False

    return True

