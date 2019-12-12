def display_output(output_rows_df):
    for index, output_row in output_rows_df.head().iterrows():
        print (output_row.to_string(header=None))
        print ("")