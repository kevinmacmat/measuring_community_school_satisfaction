def check_for_string(data_frame, column_name, string):
    count = data_frame[column_name].str.contains(string).sum()
    if count > 0:
        print("There are {m} instances.".format(m = count))
    else:
        print("There are no instances.")

def cleanText(data_frame, column_name:str, new_column:str):
    data_frame[column_name] = data_frame[column_name].str.replace('<br />', ' ')
    data_frame[column_name] = data_frame[column_name].str.replace("'", '')    
    data_frame[column_name] = data_frame[column_name].str.replace('[^\w\s]', ' ')
    data_frame[column_name] = data_frame[column_name].str.replace('[0-9]', ' ')
    data_frame[column_name] = data_frame[column_name].str.replace('_', ' ')
    # Lowercase
    data_frame[column_name] = data_frame[column_name].str.lower()

def cleanColumn(data_frame, column_name:str):
    data_frame[column_name] = data_frame[column_name].str.replace('<br />', ' ')
    data_frame[column_name] = data_frame[column_name].str.replace("'", '')    
    data_frame[column_name] = data_frame[column_name].str.replace('[^\w\s]', ' ')
    data_frame[column_name] = data_frame[column_name].str.replace('[0-9]', ' ')
    data_frame[column_name] = data_frame[column_name].str.replace('_', ' ')
    # Lowercase
    data_frame[column_name] = data_frame[column_name].str.lower()