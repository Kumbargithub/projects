#!/usr/bin/env python
# coding: utf-8

# In[163]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[164]:


#now reading the orders file 
df_order_details = pd.read_csv(r'C:\\Users\\HPUSER\\Desktop\\Pizza sale-project\\order_details.csv')
df_order_details


# In[165]:


#Now checking the total number of orders placed in the entire year 2015
Total_pizza_sold = df_order_details['order_details_id'].count()
Total_pizza_sold


# In[166]:


#now reading the orders file to find out the number of orders we got in the entire year
orders_df = pd.read_csv(r'C:\\Users\\HPUSER\\Desktop\\Pizza sale-project\\orders.csv')
orders_df


# In[167]:


#now merging the two dataFrame to get the total orders placed 
orders_details_df = pd.merge(df_order_details, orders_df, on = ['order_id'], how = 'left')
orders_details_df


# In[168]:


#Now reading the pizzas file in the resturant 
pizzas = pd.read_csv(r'C:\\Users\\HPUSER\\Desktop\\Pizza sale-project\\pizzas.csv')
pizzas


# In[169]:


#now merging the dataFrame to findout which pizzas has been placed
orders_details_df = pd.merge(orders_details_df, pizzas, on = ['pizza_id'], how = 'left')
orders_details_df


# In[170]:


pizza_type = pd.read_csv(r'C:\\Users\\HPUSER\\Desktop\\Pizza sale-project\\pizza_types.csv', encoding= 'unicode_escape')
pizza_type


# In[171]:


orders_details_2015 = pd.merge(orders_details_df,pizza_type,on = ['pizza_type_id'], how = 'left')
orders_details_2015


# In[172]:


#Renaming the dataframe as df
df = orders_details_2015
df


# In[173]:


#here the date column is in object time it has been changed to datetime 
df['date'] =  pd.to_datetime(df['date'])


# In[174]:


#here in this step we are introducing the new 'month' column from an existing 'date' column
df['month'] = df['date'].dt.month_name()
df


# In[175]:


#now checking the month wise pizza sold in year 2015
month_wise_sale = pd.DataFrame(df.groupby("month")['order_id'].count().reset_index())
month_wise_sale


# In[176]:


average_monthly_pizza_sold = month_wise_sale['order_id'].mean()
average_monthly_pizza_sold


# In[177]:


month_wise_sale

values = month_wise_sale['order_id']
mylabel = ['Jan','Feb','march','April','May','June','July','Aug','Sep','Oct','Nov','Dec'] 
plt.pie(values,  labels = mylabel)

plt.show()


# In[178]:


best_worst_sold_pizza = pd.DataFrame(df.groupby(['name'])['order_id'].count().reset_index())
best_worst_sold_pizza


# In[179]:


best_worst_sold_pizza.sort_values(by=['order_id'], ascending=False).reset_index()


# In[180]:


top_least_sold = best_worst_sold_pizza.loc[(best_worst_sold_pizza['order_id'] >= 2370)].reset_index()
top_least_sold


# In[181]:


top_least_sold

x = top_least_sold['name']
y = top_least_sold['order_id']

plt.ylabel("Months from January - December",color = 'g')
plt.xlabel("Total pizzas sold ",color = 'g')
plt.barh(x,y)
plt.title("pizza sale in year 2015")

plt.show()


# In[182]:


#from above datafram we can say that the best sold pizza in the entire year is 'The Classic Deluxe Pizza'
#And the worst sold is 'The Brie Carre Pizza'


# In[183]:


# which category pizza got sold more in the entire year  
category = pd.DataFrame(df.groupby(['category'])['order_id'].count().reset_index())
category


# In[184]:


#now plotting the bar graph for category wise pizza sale
category


x = category['category']
y = category['order_id']

plt.xlabel("Category pizza sale from January - December",color = 'r')
plt.ylabel("Total pizzas sold ",color = 'r')
plt.bar(x,y, color = 'g')
plt.title("pizza sale in year 2015")

plt.show()


# In[185]:


#now here we can filter the data to do more analysis on classic pizza

classic_df = df[(df['category'] == 'Classic')]
classic_df


# In[186]:


#here grouping the data in month wise to check in which month the more classic pizza got sold
classic_sold_month = pd.DataFrame(classic_df.groupby('month')['order_id'].count().reset_index())
classic_sold_month


# In[187]:


name_df = pd.DataFrame(classic_df.groupby(['name','size'])['quantity'].sum().reset_index())
name_df


# In[188]:


july_month = classic_df[(classic_df['month'] == "July")]
july_month


# In[189]:


july_name_group = pd.DataFrame(july_month.groupby(['name','size'])['quantity'].sum().reset_index())
july_name_group


# In[190]:


#from dataframe we can say in entire year the in classic pizza the best sold are 'The Big Meat Pizza' and 'The Classic Deluxe Pizza'
#less sold pizzas in july month is 'The Greek Pizza'


# In[191]:


ORDERS_9AM_1PM = july_month[july_month["time"].between('09:00:00','13:00:00')]['order_id'].count()
print(ORDERS_9AM_1PM)


# In[192]:


ORDERS_1PM_5PM = july_month[july_month["time"].between('13:00:00','17:00:00')]['order_id'].count()
print(ORDERS_1PM_5PM)


# In[193]:


ORDERS_5PM_12PM = july_month[july_month["time"].between('17:00:00','23:59:59')]['order_id'].count()
print(ORDERS_5PM_12PM)


# In[194]:


output = pd.DataFrame(df.groupby(['category','name','size'])['quantity'].sum().reset_index())
output


# In[195]:


revenue_generated = pd.DataFrame(df.groupby(['category','name','size'])['price'].sum().reset_index())
revenue_generated


# In[196]:


final_output = pd.merge(output,revenue_generated,on = ['category','name','size'], how = 'left')
final_output


# In[197]:


#final_output.to_excel('C:\\Users\\HPUSER\\Desktop\\Pizza sale-project\\pizza_sale_output_category.xlsx')


# In[198]:


Chicken_df = df[(df['category'] == 'Chicken')]
Chicken_sold_month = pd.DataFrame(Chicken_df.groupby(['month'])['order_id'].count().reset_index())
Chicken_sold_month 


# In[199]:


Chicken_pizza_revenue = pd.DataFrame(Chicken_df.groupby('month')['price'].sum().reset_index())
Chicken_pizza_revenue


# In[200]:


Chicken_pizza_final_output = pd.merge(Chicken_sold_month,Chicken_pizza_revenue,on = ['month'], how = 'left')
Chicken_pizza_final_output


# In[201]:


Chicken_pizza_final_output.rename(columns = {'order_id': 'chicken_pizza_sold'},inplace = True)
Chicken_pizza_final_output.rename(columns = {'price': 'chicken_pizza_revenue'},inplace = True)


# In[202]:


Chicken_pizza_final_output


# In[203]:


#from above dataframe we can say chicken sold in the month of 'march' is high


# In[ ]:





# In[204]:


Supreme_df = df[(df['category'] == 'Supreme')]
Supreme_sold_month = pd.DataFrame(Supreme_df.groupby('month')['order_id'].count().reset_index())
Supreme_sold_month 


# In[205]:


Supreme_pizza_revenue = pd.DataFrame(Supreme_df.groupby('month')['price'].sum().reset_index())
Supreme_pizza_revenue


# In[206]:


Supreme_pizza_final_output = pd.merge(Supreme_sold_month,Supreme_pizza_revenue,on = ['month'], how = 'left')
Supreme_pizza_final_output


# In[207]:


Supreme_pizza_final_output.rename(columns = {'order_id': 'Supreme_pizza_sold'},inplace = True)
Supreme_pizza_final_output.rename(columns = {'price': 'Supreme_pizza_revenue'},inplace = True)


# In[208]:


Supreme_pizza_final_output


# In[209]:


#from above dataframe we can say supreme pizza sold in the month of 'November' is high


# In[210]:


Veggie_df = df[(df['category'] == 'Veggie')]
Veggie_sold_month = pd.DataFrame(Veggie_df.groupby('month')['order_id'].count().reset_index())
Veggie_sold_month


# In[211]:


Veggie_pizza_revenue = pd.DataFrame(Veggie_df.groupby('month')['price'].sum().reset_index())
Veggie_pizza_revenue


# In[212]:


Veggie_pizza_final_output = pd.merge(Veggie_sold_month,Veggie_pizza_revenue,on = ['month'], how = 'left')
Veggie_pizza_final_output


# In[213]:


Veggie_pizza_final_output.rename(columns = {'order_id': 'Veggie_pizza_sold'},inplace = True)
Veggie_pizza_final_output.rename(columns = {'price': 'Veggie_pizza_revenue'},inplace = True)


# In[214]:


Veggie_pizza_final_output


# In[215]:


Classic_df = df[(df['category'] == 'Classic')]
Classic_sold_month = pd.DataFrame(Classic_df.groupby('month')['order_id'].count().reset_index())
Classic_sold_month


# In[216]:


Classic_pizza_revenue = pd.DataFrame(Classic_df.groupby('month')['price'].sum().reset_index())
Classic_pizza_revenue


# In[217]:


Classic_pizza_final_output = pd.merge(Classic_sold_month,Classic_pizza_revenue,on = ['month'], how = 'left')
Classic_pizza_final_output


# In[218]:


Classic_pizza_final_output.rename(columns = {'order_id': 'Classic_pizza_sold'},inplace = True)
Classic_pizza_final_output.rename(columns = {'price': 'Classic_pizza_revenue'},inplace = True)


# In[219]:


Classic_pizza_final_output


# In[ ]:





# In[220]:


#from above dataframe we can say Veggie pizza sold in the month of 'July' is high


# In[221]:


Revenue_MTD_1 = Chicken_pizza_final_output.merge(Supreme_pizza_final_output,on =['month'])
Revenue_MTD_2 = Revenue_MTD_1.merge(Veggie_pizza_final_output,on =['month'])
Revenue_MTD_3 = Revenue_MTD_2.merge(Classic_pizza_final_output,on =['month'])


# In[222]:


Revenue_MTD_3


# In[223]:


Revenue_MTD_3


# In[ ]:





# In[224]:


#Revenue_MTD_3.to_excel('C:\\Users\\HPUSER\\Desktop\\Pizza sale-project\\pizza_sale_output.xlsx')


# In[ ]:




