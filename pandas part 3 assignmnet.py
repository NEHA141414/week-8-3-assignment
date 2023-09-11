#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
course_name=['Data Science','Machin Learning','Big Data','Data Engineer']
duration=[2,3,6,4]
df=pd.DataFrame(data={'course_name': course_name, 'duration': duration})


# Q-1 Write a code to point the present in the second row of the dataframe, df.

# In[2]:


df


#  Q-2 What is the difference b/w the function loc and iloc in pandas.DataFrame ?

# Ans-2 Loc is typically used for label indexing and can access multiple columns, while Iloc is used for integer indexing

# Q-3 Reindex the given dataframe using a variable , reindex =[3,0,1,2] and store it in the variable row_df then find the output for both new_df.loc[2]  and new_df.iloc[2].

# In[10]:


import pandas as pd
course_name=['Data Science','Machin Learning','Big Data','Data Engineer']
duration=[2,3,6,4]
df1=pd.DataFrame(data={'course_name': course_name, 'duration': duration},index=['a','b','c','d'])


# In[11]:


df1


# In[12]:


df1.reindex([3,0,1,2])


# In[23]:


df1.loc[2]


# In[19]:


df1.iloc[2]


# In[1]:


import pandas as pd

import numpy as np

columns = ['column_1', 'column_2', 'column_3', 'column_4', 'column_5', 'column_6']

indices = [1,2,3,4,5,6]

#Creating a dataframe:

df1 = pd.DataFrame(np.random.rand(6,6), columns = columns, index = indices)


#  Q-4 Write a code to find the following statistical measurement for the above dataframe df1: 
#  1. mean of each and every column present in the dataframe.
#  2. standard deviation of column, column_2

# In[2]:


df1


# In[7]:


df1['column_1'].mean()


# In[8]:


df1['column_2'].mean()


# In[9]:


df1['column_3'].mean()


# In[10]:


df1['column_4'].mean()


# In[11]:


df1['column_5'].mean()


# In[12]:


df1['column_6'].mean()


# In[13]:


df1['column_1'].std()


# In[14]:


df1['column_2'].std()


# In[15]:


df1.std()


# Q5. Replace the data present in the second row of column, ‘column_2’ by a string variable then find the
# mean of column, column_2.
# 
# If you are getting errors in executing it then explain why.
# 
# [Hint: To replace the data use df1.loc[] and equate this to string data of your choice.]

# In[16]:


df1


# In[18]:


df1.loc[0:2]


# In[25]:


df1.at[2,'column_1']=2.234234
print(df1)


# In[24]:


df1.at[2,'column_2']=1.234567
print(df1)


# In[26]:


df1['column_1'].mean()


# In[27]:


df1['column_2'].mean()


# Q6. What do you understand about the windows function in pandas and list the types of windows
# functions?

# Ans-6 In pandas ,window function (also known as windowing and rolling function ) as a powerfull tool for performing calculations on a specific subset of data , known as a "window", as it moves through a dataframe or series . These functions allow you to compute aggregate statistics , apply transformations and more within a specified window of data.
# 
# TYPES OF WINDOW  FUNCTION :
#   
#   1. Rolling Functions: These functions perform calculations over a rolling window of data.
#   
#   2. Expanding Functions: These function calculate statistics that include all the data points up to the current point.
#   
#   3. Transform Function : These function apply a transformation to each element within the window . 
#   
#   4. Ranking Function: These function calculate cumulative values witin the window .
#                         

# Q7. Write a code to print only the current month and year at the time of answering this question.
# 
# [Hint: Use pandas.datetime function]

# In[30]:


from datetime import datetime

current_date=datetime.now()

current_month=current_date.month
current_year=current_date.year

print(f"current month:{current_month}")
print(f"current year:{current_year}")


# Q8. Write a Python program that takes in two dates as input (in the format YYYY-MM-DD) and
# calculates the difference between them in days, hours, and minutes using Pandas time delta. The
# program should prompt the user to enter the dates and display the result.

# In[32]:


import pandas as pd

date1_str=input("Enter the first date(YYYY-MM-DD):")
date2_str=input("Enter the second date(YYYY-MM-DD):")
date1=pd.to_datetime(date1_str)
date2=pd.to_datetime(date2_str)
time_difference =date2-date1

days=time_difference.days
hours=time_difference.seconds//3600
minutes=(time_difference.seconds//60)%60
print(f"time_difference:{days} days, {hours} hours, {minutes} minutes")

