#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask
from flask import request, render_template

from keras.models import load_model


# In[2]:


app = Flask(__name__)


# In[3]:


model = load_model('bankruptcy_model')


# In[4]:


@app.route('/', methods=['GET', 'POST'])

def index():
    if request.method == 'POST':
        NPTA = request.form.get('NP_TA')
        TLTA = request.form.get('TL_TA')
        WCTA = request.form.get('WC_TA')
        print(NPTA, TLTA, WCTA)
        pred = model.predict([[float(NPTA), float(TLTA), float(WCTA)]])
        s = 'the result is ' + str(pred[[0]])
        
        return(render_template('index.html', result = s))
    else:
        return(render_template('index.html', result = 'ready'))

    


# In[ ]:


if __name__ == '__main__':
    app.run()


# In[ ]:




