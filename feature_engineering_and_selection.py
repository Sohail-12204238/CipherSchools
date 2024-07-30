# -*- coding: utf-8 -*-
"""Feature Engineering And Selection.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1LWh4uinaIpd4Ls_qSLUWQ-Q1L_xR3mYN

# 1. Handling Missing Values
"""

import pandas as pd
from sklearn.impute import SimpleImputer

# Sample Data
data = {
    'Feature1' : [1.0, 2.0, None, 4.0, 5.0],
    'Feature2' : [2.0, None, 4.0, 5.0, None],
    'Feature3' : [None, 3.0, 3.5, 4.0, 4.5]
}
df = pd.DataFrame(data)

# Handling missing values
imputer = SimpleImputer(strategy = 'mean')
df_imputed = pd.DataFrame(imputer.fit_transform(df), columns=df.columns)
print("After Imputation:\n", df_imputed)

"""# 2. Encoding Categorical Variables"""

import pandas as pd
from sklearn.preprocessing import OneHotEncoder

# Sample data
data = {
    'Color' : ['Red', 'Blue', 'Green', 'Blue',  'Red']
}
df = pd.DataFrame(data)

# Encoding categorical variables
encoder = OneHotEncoder(sparse = False)
encoded_categories = encoder.fit_transform(df[['Color']])
df_encoded = pd.DataFrame(encoded_categories, columns=encoder.get_feature_names_out(['Color']))
df = pd.concat([df, df_encoded], axis=1).drop('Color',axis=1)
print("After One-Hot Encoding:\n",df)

"""# 3. Feature Scaling"""

import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Sample data
data = {
    'Feature1' : [10, 20, 30, 40, 50],
    'Feature2' : [100, 200, 300, 400, 500]
}
df = pd.DataFrame(data)

# Feature Scaling
scaler = MinMaxScaler()
df_scaled = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)
print("After Min-Max Scaling: \n", df_scaled)

"""# 4. Feature Creation"""

import pandas as pd
from sklearn.preprocessing import PolynomialFeatures

data = {
    'Feature1' : [1,2,3,4,5],
    'Feature2' : [2,3,4,5,6]
}
df = pd.DataFrame(data)

# Feature creation
poly = PolynomialFeatures(degree=2, include_bias=False)
poly_features = poly.fit_transform(df)
df_poly = pd.DataFrame(poly_features, columns=poly.get_feature_names_out(['Feature1','Feature2']))
print("After Creating Polynomial Features:\n", df_poly)