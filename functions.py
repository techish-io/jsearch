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