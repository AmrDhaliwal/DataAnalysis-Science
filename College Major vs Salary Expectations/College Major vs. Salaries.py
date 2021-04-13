import pandas as pd

df = pd.read_csv(r"C:\Users\Amrit\Desktop\VSCODE-Projects\Pandas-College Major\salaries_by_college_major.csv")

# Use df.head() to print first 5 rows of the dataframe
# print(df.head())

# Use df.shape to use numbers of rows and columns
# print(df.shape)

# Use df.columns to directly access column names
# print(df.columns)

# Use .isna() to find Nan values
# print(df.isna())

# Use df.tail() to print last 5 rows of dataframe
# print(df.tail())

# Use .dropna to drop Nan values and create a new dataframe
clean_df = df.dropna()
# clean_df.tail()

# Use clean_df["Starting Median Salary"].max() to find max starting median salary
clean_df["Starting Median Salary"].max()

# .idmax() gives the index row for highest salary for starting median salary
clean_df["Starting Median Salary"].idxmax()

# Use .loc[] to locate the name of the major
# with the highest starting salary
clean_df["Undergraduate Major"].loc[43]

# Use clean_df["Mid-Career Median Salary"].max() to find max mid-career median salary
clean_df["Mid-Career Median Salary"].max()

# .idmax() gives the index row for highest salary for mid-career median salary
clean_df["Mid-Career Median Salary"].idxmax()

# Use .loc[] to locate the name of the major
# with the highest mid-career salary
clean_df["Undergraduate Major"].loc[8]

# Use clean_df["Starting Median Salary"].min() to find min starting median salary
clean_df["Starting Median Salary"].min()

# .idmax() gives the index row for lowest salary for starting median salary
clean_df["Starting Median Salary"].idxmin()

# Use .loc[] to locate the name of the major
# with the lowest starting salary
clean_df["Undergraduate Major"].loc[49]

# Use code below to find lowest salary for mid-career salary
clean_df.loc[clean_df["Mid-Career Median Salary"].idxmin()]

# Calculating the earnings for the 10th and 90th percent tiles
# And insert it into the clean_df
spread_col = clean_df["Mid-Career 90th Percentile Salary"] - clean_df["Mid-Career 10th Percentile Salary"]
clean_df.insert(1, "Spread", spread_col)
clean_df.head()

# Finding the majors with the lowest salary risk
low_risk = clean_df.sort_values("Spread")
low_risk[["Undergraduate Major", "Spread"]].head()

# Finding the majors with the highest potential
highest_potential = clean_df.sort_values("Mid-Career 90th Percentile Salary", ascending=False)
highest_potential[["Undergraduate Major", "Mid-Career 90th Percentile Salary"]].head()

# Finding majors with the highest Spread
highest_spread = clean_df.sort_values("Spread", ascending=False)
highest_spread[["Undergraduate Major", "Spread"]].head()

# Use .groupby() to count all majors in Group
clean_df.groupby("Group").count()

# Use code below to find average salary by Group
pd.options.display.float_format = "{:,.2f}".format 
print(clean_df.groupby("Group").mean())

