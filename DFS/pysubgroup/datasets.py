from io import StringIO

import pandas as pd
import pkg_resources
from scipy.io import arff


def get_credit_data():
    s_io = StringIO(
        str(pkg_resources.resource_string("pysubgroup", "data/credit-g.arff"), "utf-8")
    )
    return pd.DataFrame(arff.loadarff(s_io)[0])


def get_titanic_data():
    s_io = StringIO(
        str(pkg_resources.resource_string("pysubgroup", "data/titanic.csv"), "utf-8")
    )
    return pd.read_csv(s_io, sep="\t", header=[0])

def get_german_credit_data():
    s_io = StringIO(
        str(pkg_resources.resource_string("pysubgroup", "data/german_credit_data.csv"), "utf-8")
    )

    # column_names = ["ID", "Age","Sex","Job","Housing","Saving accounts","Checking account",
                    # "Credit amount","Duration","Purpose","Risk"]

    return pd.read_csv(s_io, index_col=False)
    # return pd.read_csv("src/pysubgroup/data/german_credit_data.csv", sep="\t", header=[0])

def get_categorical_german_credit_data():
    s_io = StringIO(
        str(pkg_resources.resource_string("pysubgroup", "data/categorical_german_credit_data.csv"), "utf-8")
    )

    # column_names = ["ID", "Age","Sex","Job","Housing","Saving accounts","Checking account",
                    # "Credit amount","Duration","Purpose","Risk"]

    return pd.read_csv(s_io, index_col=False)
    # return pd.read_csv("src/pysubgroup/data/german_credit_data.csv", sep="\t", header=[0])
