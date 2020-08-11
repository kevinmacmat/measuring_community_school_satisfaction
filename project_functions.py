def check_for_string(data_frame, column_name, string):
    count = data_frame[column_name].str.contains(string).sum()
    if count > 0:
        print("There are {m} instances.".format(m = count))
    else:
        print("There are no instances.")

def cleanText(data_frame, column_name:str):
    data_frame = data_frame
    # Remove numbers
    data_frame[column_name] = data_frame[column_name].str.replace(r'[0-9]', '')
    # Remove punctuation
    data_frame[column_name] = data_frame[column_name].str.replace(r'[^\w\s]', '')    
    # Remove underscore
    data_frame[column_name] = data_frame[column_name].str.replace(r'[_]', '')
    # Remove whitespace
    data_frame[column_name] = data_frame[column_name].str.replace(r'\t', '')
    # Lowercase
    data_frame[column_name] = data_frame[column_name].str.lower()
