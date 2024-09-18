def ols_linear_regression(df, target, features):
    """
    Perform OLS linear regression.

    Parameters:
    df (pd.DataFrame): DataFrame containing the data.
    target (str): The name of the target variable (dependent variable).
    features (list of str): List of feature names (independent variables).

    Returns:
    dict: A dictionary containing the model coefficients and intercept.
    """
    import numpy as np
    import pandas as pd
    
    # Extract target and features from DataFrame. Each row is one set of data from a given observation.
    X = df[features]
    y = df[target]
    
    
    # Add a constant (intercept) to the features
    X = pd.concat([pd.Series(np.ones(len(X)), name='Intercept'), X], axis=1)

    # Calculate coefficients using the OLS formula: (X^T * X)^-1 * X^T * y
    X_matrix = X.values
    y_vector = y.values
    coefficients = np.linalg.inv(X_matrix.T @ X_matrix) @ X_matrix.T @ y_vector

    # Create a dictionary with feature names and their coefficients
    coef_dict = {'Intercept': coefficients[0]}
    for i, feature in enumerate(features):
        coef_dict[feature] = coefficients[i + 1]
    
    return coef_dict
