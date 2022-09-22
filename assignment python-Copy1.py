#!/usr/bin/env python
# coding: utf-8

# # Basic Python

# ## 1. Split this string

# In[ ]:


s = "Hi there Sam!"


# In[1]:


s="Hi there Sam!"
s=s.split()
print(s);


# *`italicized text`*## 2. Use .format() to print the following string. 
# 
# ### Output should be: The diameter of Earth is 12742 kilometers.

# In[ ]:


planet = "Earth"
diameter = 12742


# In[5]:


planet = "Earth"
diameter = 12742
print( 'The diameter of {} is {} kilometers.' .format(planet,diameter));


# ## 3. In this nest dictionary grab the word "hello"

# In[ ]:


d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}


# In[4]:


d['k1'][3]['tricky'][3]['target'][3]
Out[1]: 'hello'


# # Numpy

# In[3]:


import numpy as np


# ## 4.1 Create an array of 10 zeros? 
# ## 4.2 Create an array of 10 fives?

# In[7]:


import numpy as np
array=np.zeros(10)
print("An array of 10 zeros:")
print(array)


# In[8]:


array=np.ones(10)*5
print("An array of 10 fives:")
print(array)


# ## 5. Create an array of all the even integers from 20 to 35

# In[10]:


import numpy as np
array=np.arange(20,35,2)
print("Array of all the even integers from 20 to 35")
print(array)


# ## 6. Create a 3x3 matrix with values ranging from 0 to 8

# In[12]:


np.arange(0,9).reshape((3,3))


# ## 7. Concatinate a and b 
# ## a = np.array([1, 2, 3]), b = np.array([4, 5, 6])

# In[15]:


a = np.array([[1, 2, 3]])
b = np.array([[4, 5, 6]])
np.concatenate((a, b), axis=0)
array([[1, 2, 3],
       [4, 5, 6]])
np.concatenate((a, b.T), axis=1)
array([[1, 2, 5],
       [3, 4, 6]])
np.concatenate((a, b), axis=None)
array([1, 2, 3, 4, 5, 6])


# # Pandas

# ## 8. Create a dataframe with 3 rows and 2 columns

# In[ ]:


import pandas as pd


# In[11]:



# Import pandas library
import pandas as pd
  
# initialize list of lists
data = [['ram', 10], ['jam', 15], ['sam', 14]]
  
# Create the pandas DataFrame
df = pd.DataFrame(data, columns=['Name', 'Age'])
  
# print dataframe.
df


# ## 9. Generate the series of dates from 1st Jan, 2023 to 10th Feb, 2023

# In[6]:


import datetime
import pandas as pd
 
# initializing date
test_date = datetime.datetime.strptime("01-1-2023", "%d-%m-%Y")
 
# initializing K
K = 41
 
date_generated = pd.date_range(test_date, periods=K)
print(date_generated.strftime("%d-%m-%Y"))


# ## 10. Create 2D list to DataFrame
# 
# lists = [[1, 'aaa', 22],
#          [2, 'bbb', 25],
#          [3, 'ccc', 24]]

# In[ ]:


lists = [[1, 'aaa', 22], [2, 'bbb', 25], [3, 'ccc', 24]]


# In[8]:


import pandas as pd  
      
# List1  
lst = [[1, 'aaa', 22], [2, 'bbb', 25], [3, 'ccc', 24]], 
      
df = pd.DataFrame(lst, columns =['FName', 'LName', 'Age'],
                                           dtype = float) 
print(df)


# In[ ]:




