#https://tykimos.github.io/index.html 참고

import numpy as np
import  keras as kr
from keras.models import Sequential
from keras.layers import Dense
import matplotlib.pyplot as plt
import os
import pickle

TESTPACK_PATH="E:\\data\\packing_detection\\test\\pack"
TESTNOPACK_PATH="E:\\data\\packing_detection\\test\\unpack"
TRAINPACK_PATH="E:\\data\\packing_detection\\train\\pack"
TRAINNOPACK_PATH="E:\\data\\packing_detection\\train\\unpack"


INPUTD = 512

x_train = list()
y_train = list()
trainpack_list = os.listdir(TRAINPACK_PATH)
for x in trainpack_list:
    x_train.append(pickle.load(open(os.path.join(TRAINPACK_PATH, x),'rb')))
    y_train.append(1)

trainnopack_list = os.listdir(TRAINNOPACK_PATH)
for x in trainnopack_list:
    x_train.append(pickle.load(open(os.path.join(TRAINNOPACK_PATH, x),'rb')))
    y_train.append(0)

x_test = list()
y_test = list()
testpack_list = os.listdir(TESTPACK_PATH)
for x in testpack_list:
    x_test.append(pickle.load(open(os.path.join(TESTPACK_PATH, x),'rb')))
    y_test.append(1)

testnopack_list = os.listdir(TESTNOPACK_PATH)
for x in testnopack_list:
    x_test.append(pickle.load(open(os.path.join(TESTNOPACK_PATH, x),'rb')))
    y_test.append(0)

x_train = np.array(x_train)
y_train = np.array(y_train)
x_test = np.array(x_test)
y_test = np.array(y_test)

print(x_train.shape)
print(y_train.shape)
print(x_test.shape)
print(y_test.shape)
print("데이터 입력완료")

model = Sequential()
model.add(Dense(512, input_dim=INPUTD, activation='relu'))
model.add(Dense(1024, activation='relu'))
model.add(Dense(512, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

adam = kr.optimizers.Adam(lr=0.001, beta_1=0.9, beta_2=0.999, epsilon=1e-8)
model.compile(optimizer=adam, loss='binary_crossentropy', metrics=['accuracy'])

hist = model.fit(x_train, y_train, epochs=10, batch_size=1000)

fig, loss_ax = plt.subplots()

acc_ax = loss_ax.twinx()

loss_ax.set_ylim([0.0, 1.0])
acc_ax.set_ylim([0.0, 1.0])

loss_ax.plot(hist.history['loss'], 'y', label='train loss')
acc_ax.plot(hist.history['acc'], 'b', label='train acc')

loss_ax.set_xlabel('epoch')
loss_ax.set_ylabel('loss')
acc_ax.set_ylabel('accuray')

loss_ax.legend(loc='upper left')
acc_ax.legend(loc='lower left')

plt.show()

loss_and_metrics = model.evaluate(x_test, y_test, batch_size=32)
print('loss_and_metrics : ' + str(loss_and_metrics))