from OLS_Regression.OLS_Linear_Regression import ols_linear_regression
import pandas as pd

def test_ols_regression():
    data = {
        'X1': [1, 2, 3, 4, 5],
        'X2': [6, 3, 4, 5, 10],
        'y': [13.14990385134946, 8.127537733933618, 11.240323459184067, 14.171663207243501, 25.117915262039194]
    }
    df = pd.DataFrame(data)
    target = 'y'
    features = ['X1', 'X2']
    
    result = ols_linear_regression(df, target, features)
    
    assert isinstance(result, dict)
    assert 'Intercept' in result
    assert 'X1' in result
    assert 'X2' in result
    assert isinstance(result['Intercept'], (int, float))
    assert isinstance(result['X1'], (int, float))
    assert isinstance(result['X2'], (int, float))
    return result

# Run the test
if __name__ == '__main__':
    result = test_ols_regression()
    print("All tests passed!")
