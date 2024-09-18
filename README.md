# Simple OLS Linear Regression

## Overview

Simple OLS Linear Regression is a Python package for performing Ordinary Least Squares (OLS) regression. Written mainly to teach me how to write a package and use git.

Pandas and NumPy are needed to run use this package.

## Installation
In the command line, type
```bash
pip install git+https://github.com/VJPratley/Simple-OLS-Linear-Regression.git
```

## Example Usage

```python
import pandas as pd
from OLS_Regression import ols_linear_regression

# Example DataFrame
data = {
    'Feature1': [1, 2, 3, 4, 5],
    'Feature2': [6, 3, 4, 5, 10],
    'Target': [13.14990385134946, 8.127537733933618, 11.240323459184067, 14.171663207243501, 25.117915262039194]
}
df = pd.DataFrame(data)

# Perform OLS linear regression
result = ols_linear_regression(df, 'Target', ['Feature1', 'Feature2'])

print(result)
```



## License
This project is licensed under the MIT License - see the LICENSE file for details.
