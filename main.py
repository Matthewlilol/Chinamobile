import pandas as pd 
import matplotlib.pyplot as plt
df = pd.read_csv("/home/workspace/output/测试集A/test_a_x.csv") 





############  elderly

filtered_df = df[(df['FLAG_AGE'] >= 3) & ((df['TYPE1_1_MONTH'] >= 3) |(df['TYPE1_3_MONTH'] >= 5))
                 &((df['FLAG_PHONE_CALL_ZC'] == 1) | (df['FLAG_PHONE_NET_ZC'] == 1)| (df['ZWFW_3_ACCT1'] == 1))]
# age=2, (1month_type1 >3 or 3month_type1 >5),  complained
# Sort the filtered DataFrame by the specified column
sorted_filtered_df = filtered_df.sort_values(by='FLAG_AGE', ascending=True)  # Use ascending=False for descending order

# Display the sorted and filtered data
print("\ELDERLY Data:")
print(len(sorted_filtered_df))
########### teenagers
filtered_3df = df[(df['FLAG_AGE'] == 1) & ((df['TYPE2_1_MONTH'] >= 2) & (df['TYPE3_1_MONTH'] >= 4))&
                  ((df['FLAG_CQ_CT'] == 1) & (df['FLAG_OVER_GPRS'] == 1)& (df['FLOW_BHD'] >= 70))]
#(df['FLAG_OVER_GPRS'] == 1)

# Sort the filtered DataFrame by the specified column
sorted_filtered_3df = filtered_3df.sort_values(by='FLAG_AGE', ascending=True)  # Use ascending=False for descending order

# Display the sorted and filtered data
print("\nTeen Data:")
print(len(sorted_filtered_3df))


##############  middle age
filtered_2df = df[(df['FLAG_AGE'] == 2)&((df['TYPE3_3_MONTH'] >= 3)|(df['TYPE2_1_MONTH'] >= 3))&
                  ((df['FLOW_BHD'] >= 60)&(df['FLAG_YSF'] == 1)&(df['FLAG_FLOW_OVER'] == 1))& ((df['FLAG_OVER_GPRS'] == 1)|(df['FLAG_OF_CALL'] == 1))
                  |((df['ZWFW_3_ACCT1'] == 1)|(df['ZWFW_1_ACCT1'] == 1))&(df['FLAG_PHONE_ZC'] == 1)]

# Sort the filtered DataFrame by the specified column
sorted_filtered_2df = filtered_2df.sort_values(by='FLAG_AGE', ascending=True)  # Use ascending=False for descending order

# Display the sorted and filtered data
print("\nMID AGE Data:")
print(len(sorted_filtered_2df))

combined_df = pd.concat([sorted_filtered_df,sorted_filtered_2df, sorted_filtered_3df], ignore_index=True)

## Display the combined data
print("\nCombined Data:")
print(len(combined_df))

new_column_data = [1] * len(combined_df)  # Replace with your actual data as needed

# Add the new column to the DataFrame
  # Replace 'new_column' with your desired column name

# Display the updated DataFrame

# Add the new column to the DataFrame
combined_df['FLAG_USER'] = new_column_data  # Replace 'new_column' with your desired column name

# Save the updated DataFrame to a new CSV file
output_file = 'output_df.csv'  # Replace with your desired output file name
combined_df.to_csv(output_file, index=False)

#############
output_1_df= df.iloc[:, [0]]
output_1_df['FLAG_USER'] = '0'
output_1_df.to_csv('output_1_df.csv', index=False)

filter_user_ids = set(combined_df['USER_ID_MD5'])

# Update the 'FLAG_USER' column where 'USER_ID' is in the filter_user_ids set and currently 0
output_1_df['FLAG_USER'] = output_1_df.apply(
    lambda row: 1 if row['USER_ID_MD5'] in filter_user_ids else row['FLAG_USER'], 
    axis=1
)

# Save the updated DataFrame to a new CSV file
output_file_2 = 'output_1_df.csv'  # Replace with your desired output file name
output_1_df.to_csv(output_file_2, index=False) 

print(output_1_df)
