def display_output(output_rows_df):
    for index, output_row in output_rows_df.head().iterrows():
        print (output_row.to_string(header=None))
        print ("")

def add_data(input_df, output_df, input_col, output_col_prefix):
    i=0
    for index, input_df_row in input_df.iterrows():
        output_df[output_col_prefix + "_" + str(i)] = input_df_row[input_col]
        i = i + 1
    return output_df    

def type_cast(col, val):
    if col.dtype == "str" or col.dtype == "object":
        return str(val)
    elif col.dtype == "int64" or col.dtype == "int32" or col.dtype == "int":
        return int(val)
    elif col.dtype == "float":
        return float(val)
    elif col.dtype == "bool":
        return bool(val)
def print_search_terms(df, lable):
    print ("--------------------------------")
    print ("Search " +lable+ " with")
    for col in df.columns: 
        print(col)
    print ("")    
