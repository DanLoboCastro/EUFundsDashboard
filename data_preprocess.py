import pandas as pd

# Load the dataset
df = pd.read_csv("C:/Users/Utilizador/Desktop/PowerBI_project/data/2021-2027_Planned_finances_detailed__categorisation__multi_funds__20250619.csv")

# Step 1: Select relevant columns
relevant_columns = [
    'ms_name_en',            # Country
    'fund',                  # Fund type
    'category_of_region',    # Region type
    'policy_objective_name', # Policy goal
    'eu_amount',             # EU funding
    'cofinancing_rate',     # Cofinancing rate   
    'total_amount',          # Total funding
]

df_selected = df[relevant_columns].copy()

# Step 2: Clean missing data
numeric_cols = ['eu_amount', 'total_amount', 'cofinancing_rate']
df_selected[numeric_cols] = df_selected[numeric_cols].fillna(0)


# Scale funding columns to millions
#df_selected['eu_amount_million'] = (df_selected['eu_amount'] / 1000000).round(2)
#df_selected['total_amount_million'] = (df_selected['total_amount'] / 1000000).round(2)

# Format EU share as a percentage (rounded to 2 decimals)
#df_selected['cofinancing_rate'] = (df_selected['cofinancing_rate']).round(2)

# Drop original unscaled columns
#df_selected = df_selected.drop(columns=['eu_amount', 'total_amount'])

df_selected = df_selected.fillna({
    'category_of_region': 'Not Specified',
    'policy_objective_name': 'Not Specified',
    'category_title_short': 'Not Specified'
})

# Rename remaining columns
df_selected = df_selected.rename(columns={
    'ms_name_en': 'Country',
    'fund': 'Fund',
    'category_of_region': 'Region Type',
    'policy_objective_name': 'Policy Objective'
})


# Save to CSV for Power BI import
df_selected.to_csv("C:/Users/Utilizador/Desktop/PowerBI_project/data/preprocessed_eu_funding_by_country.csv", index=False)
