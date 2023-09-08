import streamlit as st
from PIL import Image
import pickle
import numpy as np



def run():
    img1 = Image.open('线条小狗.jpg')
    img1 = img1.resize((250,200))
    st.image(img1,use_column_width=False)
    st.title("致我最爱的超超宝宝——生日快乐！剩下的79年，我也一直陪着你")


    ## Full Name
    fn = st.text_input('请输入你的爱称：')

    ## For Marital Status
    mar_display = ('Of course','Yes')
    mar_options = list(range(len(mar_display)))
    mar = st.selectbox("你是否有一个爱你的男人？", mar_options, format_func=lambda x: mar_display[x])

    ## For edu
    edu_display = ('Yes','Yesssss!')
    edu_options = list(range(len(edu_display)))
    edu = st.selectbox("他是否会和宝宝在一起一辈子，永远陪着宝宝？",edu_options, format_func=lambda x: edu_display[x])

    ## For Property status
    prop_display = ('Yes', 'Of-course', 'Forever')
    prop_options = list(range(len(prop_display)))
    prop = st.selectbox("他是否一辈子只爱宝宝一个人，永远被宝宝迷住", prop_options, format_func=lambda x: prop_display[x])



    if st.button("Submit"):
        if fn =='宝宝':
            st.write("宝宝，我最爱你啦，你是我心里最可爱最机灵最活泼的小宝宝啦，最最最喜欢你啦！")
        if fn == '乖乖宝':
            st.write("乖乖宝，我会陪你一辈子，你最乖啦，我的小可爱！")
        if fn == '超超':
            st.write("超超，虽然你会和我吵架，你会发小脾气，我也会对你生气，但是这些你的小淘气也是我的最爱，最喜欢你啦，我的活泼宝！")

run()