#!/usr/bin/env python
# coding: utf-8

# In[3]:


import matplotlib.pyplot as plt
hours_studied=[10,15,5,25,20,30,20,30]
exam_scores=[95,80,96,88,79,84,90,99]
plt.plot(hours_studied,exam_scores,marker='*',color='red',linestyle='-')
plt.xlabel('Hours Studied')
plt.ylabel('Score in Final Exam')
plt.title('Effect of Hours Studied on Exam Score')
plt.show()



# In[ ]:




