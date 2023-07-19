import cv2
import tkinter as Tk
from tensorflow import keras
import numpy as np
from PIL import ImageTk, Image
import pandas as pd
from tkinter import filedialog
from keras.models import load_model
from keras.utils.image_utils import img_to_array
import gradio as gr
import tensorflow as tf
import matplotlib.pyplot as plt



# Load model Nhận diện
model = load_model("CNN_BienBaoVN_new.h5")
#load nhãn cho model
classes = pd.read_csv('class.csv')
classes = list(classes)


#Hàm nhận diện biển báo
def predict_object(img):
  img = img_to_array(img)                                           #Chuyển đổi ảnh thành mảng
  img = img.reshape(1,64,64,3)                                      #Thay đổi hình dạng mảng img với batch=1 (số lượng 1 ảnh được xử lý)
  # tính toán giá trị dự đoán của mô hình trên tập hình ảnh images bằng cách sử dụng hàm predict() của model_h5
  # và lấy chỉ số của lớp có xác suất cao nhất bằng hàm argmax()
  print(classes[np.argmax(model.predict(img),axis=1)[0]])
  prediction= model.predict(img)[0]

  #Hiển thị thông tin loại biển báo
  cf = {classes[i]: float(prediction[i]) for i in range(121)}
  print(cf)
  return cf

#Hàm tạo giao diện trên Gradio
gr.Interface(fn = predict_object,
             inputs = gr.inputs.Image(shape = (64,64)),
             outputs = gr.outputs.Label(num_top_classes=3),
             interpretation='default'
             ).launch(debug = True)         #Launch là hàm để khởi tạo ứng dụng trước khi nó bắt đầu chạy