#!/usr/bin/env python
# coding: utf-8

# In[10]:


# Example 1.1
x = int(input("::請輸入數字\n\t>>"))
print(f"::你輸入的是 {x}")


# In[11]:


# Example 1.2
# :try - except
try :
    x = int(input("::請輸入數字\n\t>>"))
    print(f"::你輸入的是 {x}")
except Exception as e:
    print(e)


# In[15]:


# Example 1.3
# :try - except with While
while True:
    try :
        x = int(input(":: 請輸入數字\n\t>>"))
        print(f":: 你輸入的是 {x}\n")
        break
    except Exception as e:
        print(e,"\n")
print("執行完成")


# In[17]:


# Example 2.1
# :try - raise - except
try: 
    x = int(input(":: 請輸入出生月份(1~12)\n\t>>"))
    if x >12 or x < 0:
        raise ValueError
    print(f":: 原來你是{x}月出生的寶寶\n")
except ValueError:
    print(":: 別以為我不知道一年只有12個月喔!\n")
print("執行完成")


# In[19]:


# Example 2.2
# :if 
x = int(input(":: 請輸入出生月份(1~12)\n\t>>"))
if x >12 or x < 0:
    print(":: 別以為我不知道一年只有12個月喔!\n")
else:
    print(f":: 原來你是{x}月出生的寶寶\n")
    
print("執行完成") 


# In[26]:


# Example 3
# :try - except - else - finally
try: 
    x = int(input(":: 請輸入出生月份(1~12)\n\t>>"))
    if x >12 or x < 0:
        raise ValueError
except ValueError:
    print(":: 別以為我不知道一年只有12個月喔!\n")
else:
    print(f":: 原來你是{x}月出生的寶寶\n")
finally:
    print(":: 執行完成")

