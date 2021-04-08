class LimitTable():

    """
    Class for creating a Limit Table object to show the results of a function as x approaches a certain number.

    Attributes:
        rows (integer) giving the number of rows in the Limit Table
        max_delta (percentage expressed as a decimal) giving the starting point for approaching the limit from both right and left
        x_approaches (float) giving the certain number that x is approaching, for which we want to find the limit
        func (a python function object) the function already defined by the user that must return a single value output (float) for each single input of x

    Methods:
        func_result - a way to find the output of the original function from within an instantiated instance of this class
        _generate_x_list_left - an internal class method to generate the list of x inputs as we approach from the left
        _generate_x_list_right - an internal class method to generate the list of x inputs as we approach from the right
        generate_fx_array - the main output method from this class - provides a 3 dimensional array showing the x inputs and corresponding fx outputs for all rows, split left and right

    """

    def __init__(self, rows, max_delta, x_approaches, func):
        """
        Instantiates an object of the class LimitTable
        """
        self.rows = rows
        self.max_delta = max_delta
        self.x_approaches = x_approaches
        self.func = func

    def func_result(self, x):
        """
        A class method for calculating the output of the function for any value of x
        """
        return self.func(x)


    def _generate_x_list_left(self):
        """
        An internal class method for generating the left sided list of x values to test as x approaches some number
        """
        x_list_left = []
        delta = self.x_approaches * self.max_delta
        x_list_left.append(self.x_approaches - delta)
        try:
            for n in range(self.rows - 1):
                delta = delta / 10
                x_list_left.append(self.x_approaches - delta)
        except:
            pass

        return x_list_left

    def _generate_x_list_right(self):
        """
        An internal class method for generating the right sided list of x values to test as x approaches some number
        """
        x_list_left = []
        delta = self.x_approaches * self.max_delta
        x_list_left.append(self.x_approaches + delta)
        try:
            for n in range(self.rows - 1):
                delta = delta / 10
                x_list_left.append(self.x_approaches + delta)
        except:
            pass

        return x_list_left

    def generate_fx_array(self):
        """
        The main output method for the LimitTable class.
        Generates a three dimensional array with rows as follows:
            x - left or right side of the Limit Table
            y - row number of the Limit Table
            z - two columns for x value tested and f(x) that results
            
        """
        fx_array = []
        x_list_left = self._generate_x_list_left()
        x_list_right = self._generate_x_list_right()

        fx_array_left = []
        for n in range(len(x_list_left)):
            fx = self.func_result(x_list_left[n])
            fx_array_left.append([x_list_left[n], fx])
        
        fx_array.append(fx_array_left)

        fx_array_right = []
        for n in range(len(x_list_right)):
            fx = self.func_result(x_list_right[n])
            fx_array_right.append([x_list_right[n], fx])

        fx_array.append(fx_array_right)

        return fx_array


    


    