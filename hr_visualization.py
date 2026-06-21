import matplotlib.pyplot as plt
import pandas as pd

# Load the HR data
df = pd.read_csv('HR-Employee-Attrition-Cleaned-Data.csv')

# Inspection of data
print(df.shape)
print(df.head())
print(df.describe())

# # Which department has most attrition?
# attrition_yes = df[df['Attrition'] == 'Yes']
# department_counts = attrition_yes['Department'].value_counts()
#
# # Create bar chart
# department_counts.plot(kind='bar')
#
# # Add labels
# plt.title('Employee Attrition by Department')
# plt.xlabel('Department')
# plt.ylabel('Number of Employees who Left')
# plt.xticks(rotation=45, ha='right')
# plt.tight_layout()
# plt.show()

# What is the Gender distribution?
# gender_counts = df['Gender'].value_counts()
# gender_counts.plot(kind='pie', autopct='%1.1f%%')
# plt.title('Gender Distribution Table')
# plt.ylabel('')
# plt.tight_layout()
# plt.show()

# How are monthly incomes distributed?
# df['MonthlyIncome'].plot(kind='hist', bins=10)
# plt.title('Monthly Income Distribution')
# plt.xlabel('Monthly Income')
# plt.ylabel('Frequency')
# plt.tight_layout()
# plt.show()

# Does age affect attrition?
# Filter Data
# attrition_yes = df[df['Attrition'] == 'Yes']
# attrition_no = df[df['Attrition'] == 'No']
#
# # Plot both on same chart
# attrition_yes['Age'].plot(kind='hist', bins=15, alpha=0.5, label='left', color='deeppink')
# attrition_no['Age'].plot(kind='hist', bins=15, alpha=0.5, label='Stayed', color='blue')
# plt.title('Age to Attrition Distribution')
# plt.xlabel('Age')
# plt.ylabel('Number of Employees')
# plt.legend()
# plt.tight_layout()
# plt.show()

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