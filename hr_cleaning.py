# Step 1 LOADING DATA
import pandas as pd
HR_dataset = pd.read_csv('HR-Employee-Attrition.csv')

# ANALYSE PROBLEMS
# Step 2 Check the data
print(HR_dataset.shape)
print(HR_dataset.head())

# Step 3 deep check
print(HR_dataset.info())              #Gives more details about the file
print(HR_dataset.duplicated().sum())  #Shows no duplicate
print(HR_dataset.isnull().sum())      #Check for empty rows
print(HR_dataset.dtypes)              #Check for invalid data types

# Step 4 Check for inconsistency in text
text_columns = HR_dataset.select_dtypes(include='str').columns
for column in text_columns:                     # Loop through each text_columns one by one
    print(f'\n{column}:')                       # Print the column name as a header
    print(HR_dataset[column].value_counts())    # Show all unique values and how many times each appears

    total = HR_dataset[column].value_counts().sum()   # Automatically check if counts add up to total rows
    print(f'Total: {total}, out of {len(HR_dataset[column])}')

# Step 5 Check for unique values the is just 1 value across (Useless columns)
useless_columns = [column for column in HR_dataset.columns
                  if HR_dataset[column].nunique() == 1]
print(f'Useless columns found {useless_columns} - consider dropping it')  #if the above check is true the sentence here should be printed.

#==================== SOLUTIONS ======================

# SOLUTION TO THE ONLY ISSUE DETECTED WHICH IS THE LAST QUERY FOR USELESS COLUMNS
print(f'Shape before dropping useless_columns: {HR_dataset.shape}') #Before dropping useless_columns
HR_dataset = HR_dataset.drop(columns=useless_columns)       #To drop useless columns
print(f'Shape after dropping: {HR_dataset.shape}')

# TO SAVE THE DATA
HR_dataset.to_csv('HR-Employee-Attrition-Cleaned-Data.csv', index=False)
print(f'Clean Data Saved Successfully!')