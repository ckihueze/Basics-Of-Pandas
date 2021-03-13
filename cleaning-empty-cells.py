# Empty cells can potentially give you a wrong result when you analyze data.

# Remove Rows
# One way to deal with empty cells is to remove rows that contain empty cells.
# This is usually OK, since data sets can be very big, and removing a few rows will not have a big impact on the result.

# Example
# Return a new Data Frame with no empty cells:

import pandas as pd

abc = pd.read_csv("dirtydata.csv")
new_abc = abc.dropna()
print(new_abc.to_string())

# By default, the dropna() method returns a new DataFrame, and will not change the original.

print(abc)

# If you want to change the original DataFrame, use the inplace = True argument:

abc.dropna(inplace = True)
print(abc.to_string())
print(abc)

# Replace Empty Values
# Another way of dealing with empty cells is to insert a new value instead.
# This way you do not have to delete entire rows just because of some empty cells.
# The fillna() method allows us to replace empty cells with a value:

abc = pd.read_csv("dirtydata.csv")
abc.fillna(1, inplace = True)
print(abc.to_string())

# Replace Only For a Specified Columns
# The example above replaces all empty cells in the whole Data Frame.
# To only replace empty values for one column, specify the column name for the DataFrame:
# Example
# Replace NULL values in the "Calories" columns with the number 10:

abc = pd.read_csv("dirtydata.csv")
abc['Calories'].fillna(10, inplace = True)
print(abc.to_string())