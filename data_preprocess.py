import pandas as pd

# Load the dataset
df = pd.read_csv("./2021-2027_Planned_finances_detailed__categorisation__multi_funds__20250619.csv")

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
df_selected.to_csv("./preprocessed_eu_funding_by_country.csv", index=False)
