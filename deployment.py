#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st


# In[3]:


from textblob import TextBlob


# In[4]:


def main():
    st.title("Sentimental Analysis App on Iphone 4s User Review")
    st.image('sentiment.jpg')
    st.write("Built with Streamlit and python")
    from_sent=st.text_input("Enter your review")
    if st.button("Analysis"):
        br=TextBlob(from_sent)
        result=br.sentiment.polarity
        if result==0:
            st.write("This is a Neutral Review")
        elif result>0:
            st.write("This is a Positive Review")
        else:
            st.write("This is a Negative Review")
    
    


# In[5]:


if __name__=="__main__":
    main()


# In[ ]:




