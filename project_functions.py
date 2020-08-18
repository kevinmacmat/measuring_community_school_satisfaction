from random import randrange
import pandas 

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

def nanCheck(df, column_index):
    missing_count = []
    for x in df.iloc[:,column_index].isna():
        if x:
            missing_count.append(x)
        else:
            continue
    for x in df.iloc[:,column_index]:   
        if x == '.':
            missing_count.append(x)
        else:
            continue
    print(str(df.iloc[:,column_index].name) + ' contains '+ str(len(missing_count)) + ' missing values.')
    
def random_school(df):
    index = randrange(985)
    print('School: ' + str(df.loc[index]['school_name']))
    print('Borough: ' + str(df.loc[index]['borough']))
    print('Average SQR Ratings: ' + str((df.loc[index]['fam_comm_ties_rating']+df.loc[index]['trust_rating'])/2))
    print('Compound: ' + str(df.loc[index]['compound']))
    print('Pct Positive: ' + str(df.loc[index]['pos']))
    print('Pct Neutral: ' + str(df.loc[index]['neu']))
    print('Pct Negative: ' + str(df.loc[index]['neg']))