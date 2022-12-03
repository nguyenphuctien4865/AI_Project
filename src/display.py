# from win32com.client import Dispatch
from keras.models import load_model
import cv2
import os
import random
from PIL import Image, ImageEnhance
import numpy as np
import streamlit as st
import warnings
import main as m
import pathlib
warnings.filterwarnings('ignore')

def main():
    st.title("Handwritten Digit Classification Web App")
    st.set_option('deprecation.showfileUploaderEncoding', False)
    activities = ["Program","Train-validate","Credits"]
    choices = st.sidebar.selectbox("Select Option", activities)
 
    if choices == "Program":
       
        st.subheader("Kindly upload file below")
        img_file = st.file_uploader("Upload File", type=['png', 'jpg', 'jpeg'])
        if img_file is not None:
            up_img = Image.open(img_file)
            st.image(up_img)
            print(img_file.name)
        else:
            folder=r"./data/sample"
            a=random.choice(os.listdir(folder))
            print(a)
            file = folder+'\\'+a           
            up_img = Image.open(file)
            st.image(up_img)
        if st.button("Predict Now"):
            # m.predix( img_file = up_img)
            str = m.predix(img_file = up_img)
            st.write('Recognized: ',str)
            


    elif choices == 'Train-validate':
        st.subheader("Training-Validate")
        fastmode = st.sidebar.checkbox("Fast")
        batchsize = st.sidebar.number_input('Batch Size',100)
        decoder = ["bestpath","beamsearch","wordbeamsearch"]
        choices_decoder = st.sidebar.selectbox("Decoder", decoder)
        path = "./data"
        f_path = pathlib.Path(path)
        
        st.subheader("Chuẩn bị dataset")
        st.write("- Đăng ký và tải bộ dữ liệu tại website: http://www.fki.inf.unibe.ch/databases/iam-handwriting-database")
        st.write("- Tải file words/words.tgz ")
        st.write("- Tải file ascii/words.txt ")
        st.write("- Đặt file word.txt vào đường dẫn data/gt")
        st.write("- Đặt file nội dung (các thư mục a01, a02, ...) của word.tgz vào đường dẫn data/img")

        st.subheader("Chạy tranning")
        st.write("- Xóa file từ thu mục model nếu muốn train từ đầu" )
        st.write("- Bộ IAM dataset được chia thành 95% training data và 5% validation data")
                
        if st.sidebar.button("Traning"):
            try:
                m.predix(mode="train",batch_size=batchsize, fast=fastmode,decoder=choices_decoder, data_dir=f_path)
                st.sidebar.write("Traning hoàn thành")

            except:
                st.sidebar.error("Có lỗi xảy ra, lại đường dẫn thư mục dữ liệu để train")
            
            

        
        
    elif choices == 'Credits':
        st.subheader("Đồ án Trí tuệ nhân tạo")
        st.write(
            "Nguyễn Phúc Tiền - 20110573 ")


if __name__ == '__main__':
    main()
