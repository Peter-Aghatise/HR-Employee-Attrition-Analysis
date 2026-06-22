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


# -------------Visualization------------------------
import matplotlib.pyplot as plt
# Load the HR data
df = pd.read_csv('HR-Employee-Attrition-Cleaned-Data.csv')
# Which department has most attrition?
attrition_yes = df[df['Attrition'] == 'Yes']
department_counts = attrition_yes['Department'].value_counts()

# Create bar chart
department_counts.plot(kind='bar')

# Add labels
plt.title('Employee Attrition by Department')
plt.xlabel('Department')
plt.ylabel('Number of Employees who Left')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# What is the Gender distribution?
gender_counts = df['Gender'].value_counts()
gender_counts.plot(kind='pie', autopct='%1.1f%%')
plt.title('Gender Distribution Table')
plt.ylabel('')
plt.tight_layout()
plt.show()

# How are monthly incomes distributed?
df['MonthlyIncome'].plot(kind='hist', bins=10)
plt.title('Monthly Income Distribution')
plt.xlabel('Monthly Income')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# Does age affect attrition?
# Filter Data
attrition_yes = df[df['Attrition'] == 'Yes']
attrition_no = df[df['Attrition'] == 'No']

# Plot both on same chart
attrition_yes['Age'].plot(kind='hist', bins=15, alpha=0.5, label='left', color='deeppink')
attrition_no['Age'].plot(kind='hist', bins=15, alpha=0.5, label='Stayed', color='blue')
plt.title('Age to Attrition Distribution')
plt.xlabel('Age')
plt.ylabel('Number of Employees')
plt.legend()
plt.tight_layout()
plt.show()

# Now combine all 4 into one dashboard:
fig, axes = plt.subplots(2, 2, figsize=(16, 12))
attrition_yes = df[df['Attrition'] == 'Yes']
attrition_no = df[df['Attrition'] == 'No']

# Chart 1 Department with most Attrition
department_counts = attrition_yes['Department'].value_counts()
department_counts.plot(kind='bar', ax=axes[0,0])
axes[0,0].set_title('Employee Attrition by Department', fontsize=16, fontweight='bold')
axes[0,0].set_xlabel('Department', labelpad=15)
axes[0,0].set_ylabel('Number of Employees who Left')
axes[0,0].tick_params(axis='x', rotation=45)

# Chart 2 What is the Gender distribution?
gender_counts = attrition_yes['Gender'].value_counts()
gender_counts.plot(kind='pie', ax=axes[0,1], autopct='%1.1f%%', startangle=90)
axes[0,1].set_title('Employee Attrition by Gender', fontsize=14, fontweight='bold')

# Chart 3 How are monthly incomes distributed?
df['MonthlyIncome'].plot(kind='hist', ax=axes[1,0], bins=10)
axes[1,0].set_title('Monthly Income Distribution')
axes[1,0].set_xlabel('Monthly Income')
axes[1,0].set_ylabel('Frequency')

# Chart 4 Does age affect attrition?
axes[1,1].hist([attrition_yes['Age'], attrition_no['Age']],
              bins=15, color=['deeppink', 'darkblue'], label=['Left', 'Stayed'],
              alpha=0.7, rwidth=0.85) # rwidth=0.85 adds a crisp micro-gap between the bar groups for better readability
axes[1,1].set_title('Age to Attrition Distribution', fontsize=16, fontweight='bold')
axes[1,1].set_xlabel('Age')
axes[1,1].set_ylabel('Number of Employees')
axes[1,1].legend(loc='upper right')

plt.tight_layout(pad=3.0)
plt.savefig('HR_Dashboard.png', dpi=300, bbox_inches='tight')
plt.show()