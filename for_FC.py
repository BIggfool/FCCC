import streamlit as st
from PIL import Image
import pickle
import numpy as np



def run():
    img1 = Image.open('线条小狗.jpg')
    img1 = img1.resize((300,200))
    st.image(img1,use_column_width=False)
    st.title("生日快乐！可爱的超超宝宝")


    ## Full Name
    fn = st.text_input('请输入你的爱称：（小宝、宝宝、乖乖宝、超超）')

    ## For Marital Status
    mar_display = ('有','有，而且甩也甩不掉','有一个爱宝宝一辈子的')
    mar_options = list(range(len(mar_display)))
    mar = st.selectbox("你是否有一个爱你的男人？", mar_options, format_func=lambda x: mar_display[x])

    ## For edu
    edu_display = ('是','不是，是连续好几辈子，一直粘着宝宝')
    edu_options = list(range(len(edu_display)))
    edu = st.selectbox("他是否会和宝宝在一起一辈子，永远陪着宝宝？",edu_options, format_func=lambda x: edu_display[x])

    ## For Property status
    prop_display = ('是', '他这辈子只喜欢宝宝一个女孩', '已经被宝宝迷死了')
    prop_options = list(range(len(prop_display)))
    prop = st.selectbox("他是否一辈子只爱宝宝一个人，永远被宝宝迷住", prop_options, format_func=lambda x: prop_display[x])



    if st.button("Submit"):
        if fn =='小宝':
            st.write("小宝，即使我老了，你也是我的宝宝，你永远都小小的，是我的心头肉，想亲亲你")
        if fn =='宝宝':
            st.write("宝宝，我最爱你啦，你是我心里最可爱最机灵最活泼的小宝宝啦，最最最喜欢你啦！")
        if fn == '乖乖宝':
            st.write("乖乖宝，我会陪你一辈子，你最乖啦，我的小可爱！")
        if fn == '超超':
            st.write("超超，虽然你会和我吵架，你会发小脾气，我也会对你生气，但是这些你的小淘气也是我的最爱，最喜欢你啦，我的活泼宝！")

run()