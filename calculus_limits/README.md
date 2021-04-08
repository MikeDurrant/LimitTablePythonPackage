# LimitTable

LimitTable is a Python library for dealing with finding limits in differential calculus.

## Installation

Use the package manager [pip](link to be added) to install LimitTable.

```bash
pip install 'to be add later'
```

## Usage

```python
import LimitTable

#First define the function you wish to apply to the Limit Table

func = def some_function(x):
    return some_number

# Instantiate a LimitTable object
my_limit_table = LimitTable(rows, max_delta, x_approaches, func)

# Methods available
LimitTable.generate_fx_array(self) # returns a 3d array based on the attributes of the object you created
LimitTable.func_result(x) # outputs the result of your original function

```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

This is my first package - any developmental feedback gratefully received.


## License
MIT License

Copyright (c) [2021] [Michael Durrant]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.