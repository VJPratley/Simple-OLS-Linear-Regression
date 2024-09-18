# Simple OLS Regression

## Overview

Simple OLS Regression is a Python package for performing Ordinary Least Squares (OLS) regression. Written mainly to teach myself how to write a package and use git.

Pandas and NumPy are needed to run use this package.

## Installation
In the command line, type
```bash
pip install git+https://github.com/VJPratley/Simple-OLS-Regression.git
```

## Example Usage

```python
import pandas as pd
from OLS_Regression import ols_linear_regression

# Example DataFrame
data = {
    'Feature1': [1, 2, 3, 4, 5],
    'Feature2': [6, 3, 4, 5, 10],
    'Target': [13.149, 8.127, 11.240, 14.171, 25.117]
}
df = pd.DataFrame(data)

# Perform OLS linear regression
result = ols_linear_regression(df, 'Target', ['Feature1', 'Feature2'])

print(result)
```



## License
This project is licensed under the MIT License - see the LICENSE file for details.
