import pysubgroup as ps 
import pandas as pd 

from datasets import get_titanic_data, get_german_credit_data

feature = 'Risk'
data = get_german_credit_data()
target = ps.BinaryTarget(feature, True) 
searchspace = ps.create_selectors(data, ignore=['Risk']) 
task = ps.SubgroupDiscoveryTask(
    data, 
    target, 
    searchspace,
    result_set_size=5, 
    depth=2, 
    qf=ps.ChiSquaredQF()
    )
result = ps.BeamSearch().execute(task)
print(result.to_dataframe())