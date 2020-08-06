def check_for_string(data_frame, column_name, string):
    count = data_frame[column_name].str.contains(string).sum()
    if count > 0:
        print("There are {m} instances.".format(m = count))
    else:
        print("There are no instances.")