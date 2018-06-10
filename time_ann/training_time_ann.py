import tensorflow as tf
import numpy as np
import os, sys
import csv
import pickle
import time

MAL_PATH = 'D:\\패킹관련\\패킹\\pack_fh_everything\\trainningSet'
BENIGN_PATH = 'D:\\패킹관련\\패킹\\nopack_fh_everthing\\trainningSet'
BASE_PATH = 'D:\\패킹관련\\패킹학습결과\\'
TODAY = '20180610_trainning'

# for using tensorflow as hyper parameter
INPUT_SIZE = int(512)
OUTPUT_SIZE = int(2)
LEARNING_RATE = 1e-4
BATCH_SIZE = int(256)
EPOCH = int(10)
DROPOUT_PROB = 0.6


def collect_mal(mal_path_list,mal_path):
    mal_list = os.listdir(mal_path)
    for x in mal_list:
        mal_path_list.append(os.path.join(mal_path, x))
    return mal_path_list


def collect_benign(benign_path_list,benign_path):
    benign_list = os.listdir(benign_path)
    for x in benign_list:
        benign_path_list.append(os.path.join(benign_path, x))
    return benign_path_list


def get_mini_batch(benign_list,mal_list, batch_size):
    while True:
        np.random.shuffle(benign_list)
        np.random.shuffle(mal_list)

        half_batch_size = int(batch_size/2)
        batch_data_lists, batch_label_lists = list(), list()

        for x in benign_list[:half_batch_size]:
            batch_data_lists.append(pickle.load(open(x, 'rb')))

        for i in range(half_batch_size):
            batch_label_lists.append([1, 0]) # benign

        for x in mal_list[:half_batch_size]:
            batch_data_lists.append(pickle.load(open(x, 'rb')))

        for i in range(half_batch_size):
            batch_label_lists.append([0, 1])

        yield (batch_data_lists, batch_label_lists)


#  KISnet
def trainANN(benign_list,mal_list,save_model_name):
    tf.gfile.MkDir(save_model_name)
    tf.reset_default_graph()

    with tf.device('/gpu:0'):
        # ANN network architecture
        prob = tf.placeholder(tf.float32)

        x = tf.placeholder(tf.float32, shape=[None, INPUT_SIZE])
        y = tf.placeholder(tf.float32, shape=[None, OUTPUT_SIZE])

        dense_layer_1 = tf.layers.dense(inputs=x, units=2048, activation=tf.nn.relu)
        dense_drop_1 = tf.nn.dropout(dense_layer_1, prob)

        dense_layer_2 = tf.layers.dense(inputs=dense_drop_1, units=1024, activation=tf.nn.relu)
        dense_drop_2 = tf.nn.dropout(dense_layer_2, prob)

        dense_layer_3 = tf.layers.dense(inputs=dense_drop_2, units=512, activation=tf.nn.relu)
        dense_drop_3 = tf.nn.dropout(dense_layer_3, prob)

        dense_layer_4 = tf.layers.dense(inputs=dense_drop_3, units=256, activation=tf.nn.relu)
        dense_drop_4 = tf.nn.dropout(dense_layer_4, prob)

        dense_layer_5 = tf.layers.dense(inputs=dense_drop_4, units=128, activation=tf.nn.relu)
        dense_drop_5 = tf.nn.dropout(dense_layer_5, prob)

        y_ = tf.layers.dense(inputs=dense_drop_5, units=OUTPUT_SIZE)

        # loss function: softmax, cross-entropy
        cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=y_, labels=y))

        # optimizer: Adaptive momentum optimizer
        optimizer = tf.train.AdamOptimizer(LEARNING_RATE).minimize(cost)

    # predict
    prediction = tf.equal(tf.argmax(y_, 1), tf.argmax(y, 1))
    accuracy = tf.reduce_mean(tf.cast(prediction, tf.float32))

    # training session start
    init = tf.global_variables_initializer()
    model_saver = tf.train.Saver()
    train_iter = get_mini_batch(benign_list, mal_list, BATCH_SIZE)
    cycle = (int)((mal_list.__len__()+benign_list.__len__())/BATCH_SIZE * EPOCH)


    with tf.Session(config=tf.ConfigProto(allow_soft_placement=True, log_device_placement=True)) as sess:
        sess.run(init)

        print('learning start')
        for i in range(cycle):
            (training_data, training_label) = next(train_iter)
            sess.run(optimizer, feed_dict={x: training_data, y: training_label, prob: DROPOUT_PROB})
            if (i % 100 == 0):
                print(i, sess.run(accuracy, feed_dict={x: training_data, y: training_label, prob: DROPOUT_PROB}))
        print('------finish------')
        print("check2")
        print(save_model_name)
        model_saver.save(sess, os.path.normpath(save_model_name + '\\model.ckpt'))
    pass


def make_path(today):
    benign_list = list()
    benign_list = collect_benign(benign_list, BENIGN_PATH)
    mal_list = list()
    mal_list = collect_mal(mal_list, MAL_PATH)
    save_model_name = os.path.join(BASE_PATH, today)
    trainANN(benign_list, mal_list, save_model_name)

make_path(TODAY)
