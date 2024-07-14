import pysubgroup as ps
import numpy as np
# Load the example dataset
from datasets import get_titanic_data, get_german_credit_data, get_categorical_german_credit_data


# Normal exploration
data = get_categorical_german_credit_data()
# data = data.drop(['Sex'], axis=1)
print(data)
target = ps.BinaryTarget ('label', True)
searchspace = ps.create_selectors(data, ignore=['label'])

task = ps.SubgroupDiscoveryTask (
    data,
    target,
    searchspace,
    result_set_size=4144,
    depth=3,
    qf=ps.StandardQF(a=1.0))

result = ps.DFS().execute(task)
df_result = result.to_dataframe()
df_result.to_csv(f'../unprocessed_DFS_descriptions.csv', index=False)
print(df_result)
print("\n", "\n", "\n")


# Split exploration
# df = get_german_credit_data()
# df = df.replace(np.nan, 'unknown', regex=True)
# data = df
# good_risk_data = data.loc[data['Risk'] == 1]
# bad_risk_data = data.loc[data['Risk'] == 0]
# print(good_risk_data['Checking account'].unique())


# # Positive
# target = ps.NumericTarget ('Checking account')
# searchspace = ps.create_selectors(good_risk_data, ignore=['Checking account'])
# task = ps.SubgroupDiscoveryTask (
#     good_risk_data,
#     target,
#     searchspace,
#     result_set_size=10,
#     depth=2,
#     qf=ps.StandardQF(a=0.5))

# result = ps.DFS().execute(task)
# print(result.to_dataframe())
