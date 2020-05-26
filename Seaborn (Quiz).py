#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# 1.สร้าง DataFrame ที่เก็บยอดขายของบริษัท A,B,C,D ของปี 2014,2015,2016,2017 โดยชื่อบริษัทเป็น index และปีเป็น column. สร้างคำสั่ง numpy สุ่มเลขแบบ float ให้เป็นรายได้ของบริษัทที่อยู่ในช่วง 50 – 500 (หน่วยล้านบาท) 

# In[121]:


import random
randomFloatList = []                            # Set a length of the list to 10
for i in range(0, 16):                          # any random float between 50 to 500
    x = round(random.uniform(50, 500), 2)       # don't use round() if you need number as it is
    randomFloatList.append(x)                  
randomFloatList


# In[126]:


data = np.array(randomFloatList).reshape(4,4)
data


# In[127]:


index = ['A','B','C','D']
columns = [2014, 2015, 2016, 2017]
df = pd.DataFrame(data, index = index,columns=columns)
df


# 2.ใช้ข้อมูลจาก DataFrame ด้านบนสร้าง Bar plot ให้แกน x เป็น ชื่อบริษัท ยอดขายเฉลี่ยเป็นแกน Y โดยสร้างกราฟแบบแนวตั้งและแนวนอน

# In[136]:


fig = plt.figure(figsize = (10,8))
sns.barplot(x = df.index, y =df.columns)


# In[137]:


fig = plt.figure(figsize = (10,8))
sns.barplot(x = df.columns, y =df.index)


# 3.ใช้ข้อมูลจาก DataFrame ด้านบนสร้าง Scatter plot ให้แกน x เป็น ชื่อบริษัท ยอดขายปี 2017 เป็นแกน Y โดยสร้างกราฟแบบแนวตั้งและแนวนอน

# In[140]:


fig = plt.figure(figsize = (10,8))
sns.scatterplot(x = df.index, y =df[2017]) 


# In[141]:


fig = plt.figure(figsize = (10,8))
sns.scatterplot(x = df[2017], y = df.index)


# ให้ import ไฟล์ titanic ไฟล์เดิมจากบทเรียน Pandas เข้าสู่ Jupyter Notebook สามารถใช้ Pandas มาร่วมทำด้วย

# In[29]:


df = pd.read_csv('../Desktop/DataCamp/train.csv')
df.head()


# 4. สร้าง count plot นับข้อมูล Embarked โดยสร้างกราฟแบบแนวตั้งและแนวนอน

# In[46]:


fig = plt.figure(figsize = (7,6))
sns.countplot(x = 'Embarked',data = df)


# In[42]:


fig = plt.figure(figsize = (7,6))
sns.countplot(y = 'Embarked',data = df)


# 5. สร้าง count plot นับข้อมูล Pclass โดยสร้างกราฟแบบแนวตั้งและแนวนอน

# In[43]:


fig = plt.figure(figsize = (7,6))
sns.countplot(x = 'Pclass',data = df)


# In[44]:


fig = plt.figure(figsize = (7,6))
sns.countplot(y = 'Pclass',data = df)


# 6. สร้าง box plot ให้แกน X เป็นเพศ และแกน Y เป็นราคา 

# In[49]:


fig = plt.figure(figsize = (13,6))
sns.boxplot(x = 'Sex', y='Fare',data = df)


# 7. สร้าง box plot ให้แกน X เป็นPclass และแกน Y เป็นราคา 

# In[51]:


fig = plt.figure(figsize = (13,6))
sns.boxplot(x ='Pclass', y='Fare',data = df)


# 8. สร้าง barplot โดยให้ แกน X เป็นจุดหมายปลายทางและแกน Y เป็นราคา

# In[52]:


fig = plt.figure(figsize = (13,6))
sns.barplot(x ='Embarked', y='Fare',data = df)


# 9. สร้าง barplot โดยให้ แกน X เป็นPclass และแกน Y เป็นอายุ

# In[53]:


fig = plt.figure(figsize = (13,6))
sns.barplot(x ='Pclass', y='Age',data = df)


# 10. สร้าง Stripplot โดยให้แกน X เป็น Pclass และ แกน Y เป็นราคา

# In[55]:


fig = plt.figure(figsize = (13,6))
sns.stripplot(x ='Pclass', y='Fare',data = df)


# 11. สร้าง Stripplot โดยให้ แกน X เป็น Survived แกน Y เป็นอายุ และ hue เป็นเพศM

# In[59]:


fig = plt.figure(figsize = (13,6))
sns.stripplot(x ='Survived', y='Age',data = df, hue = 'Sex')


# 12. สร้าง Swarmplot โดยให้ แกน X เป็นเพศและแกน Y เป็นอายุ

# In[61]:


fig = plt.figure(figsize = (13,6))
sns.swarmplot(x ='Sex', y='Age',data = df)


# 13. สร้าง HeatMap โดย crosstab กำหนดให้ index เป็น Pclass และ column เป็นเพศ 

# In[67]:


index = df['Pclass']
columns = df['Sex']
new_df = pd.crosstab(index,columns)
sns.heatmap(new_df,annot = True)


# 14. สร้าง HeatMap โดย pivot table กำหนดให้ index เป็น Pclass และ column เป็นเพศ และ values เป็น ราคา

# In[71]:


new_df = df.pivot_table(index='Pclass',columns='Sex',values='Fare')
sns.heatmap(new_df,annot = True)


# 15. สร้าง HeatMap โดย pivot table กำหนดให้ index เป็น Pclass และ column เป็นเพศ และ values เป็น ราคา และกำหนดเส้นสีขาวขนาด 2 เป็นเส้นแบ่ง

# In[76]:


new_df = df.pivot_table(index='Pclass',columns='Sex',values='Fare')
sns.heatmap(new_df,annot = True,linecolor = 'white',linewidth = 2)


# 16. สร้าง Heatmap โดย Correlation ของทั้ง DataFrame

# In[80]:


df_corr = df.corr()
sns.heatmap(df_corr,annot = True)


# 17. สร้าง Clustermap ของทั้ง DataFrame

# In[81]:


sns.clustermap(df_corr,cmap='coolwarm',annot = True)


# 18. พิจารณาจากข้อมูลที่มีความสัมพันธ์มากที่สุดมาสร้าง Scatterplot

# In[89]:


sns.scatterplot(x ='Parch',y = 'SibSp', data = df)


# In[88]:


df


# 19. พิจารณาจากข้อมูลที่มีความสัมพันธ์น้อยที่สุดมาสร้าง Scatterplot และให้ hue เป็นเพศ

# In[90]:


sns.scatterplot(x ='Pclass',y = 'Fare', data = df, hue = 'Sex')


# 20. สร้าง Distribution Plot ของราคาและอายุ

# In[94]:


sns.distplot(df['Fare'])


# In[95]:


sns.distplot(df['Age'])


# 21. สร้าง Pair Plot ของทั้ง DataFrame (หรือ column ที่น่าสนใจ)

# In[96]:


sns.pairplot(df)

