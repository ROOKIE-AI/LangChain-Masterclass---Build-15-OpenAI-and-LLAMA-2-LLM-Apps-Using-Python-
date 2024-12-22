#你好！看起来你想在Python中导入Streamlit库。Streamlit是一个强大的开源框架，用于构建具有交互式数据可视化和机器学习模型的Web应用程序。要导入Streamlit，你需要确保它已经在你的Python环境中安装。
#一旦你安装了Streamlit，你可以使用导入语句将其导入到你的Python脚本中。

import streamlit as st

#由于Langchain团队一直在积极改善该工具，我们可以看到每周都有很多变化，
#作为其一部分，下面的导入已被弃用
#from langchain.llms import OpenAI

#来自langchain的新导入，替代上述内容
from langchain_openai import OpenAI

#当部署在huggingface空间时，这个值必须使用变量和秘密设置传递，如视频中所示 :)
#import os
#os.environ["OPENAI_API_KEY"] = "sk-PLfFwPq6y24234234234FJ1Uc234234L8hVowXdt"

#返回响应的函数
def load_answer(question):
    # "text-davinci-003"模型已被弃用，因此使用最新的模型 https://platform.openai.com/docs/deprecations
    llm = OpenAI(model_name="gpt-3.5-turbo-instruct", temperature=0)

    #上周langchain建议为下面的内容使用invoke函数 :)
    answer = llm.invoke(question)
    return answer


#应用UI从这里开始
st.set_page_config(page_title="LangChain 演示", page_icon=":robot:")
st.header("LangChain 演示")

#获取用户输入
def get_text():
    input_text = st.text_input("你: ", key="input")
    return input_text


user_input = get_text()
response = load_answer(user_input)

submit = st.button('生成')  

#如果点击生成按钮
if submit:

    st.subheader("回答:")

    st.write(response)