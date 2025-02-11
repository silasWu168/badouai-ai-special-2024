import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf

x_data = np.linspace(-0.5, 0.5, 200)[:, np.newaxis]
noise = np.random.normal(0, 0.02, x_data.shape)
y_data = np.square(x_data) + noise

x = tf.placeholder(tf.float32, [None, 1])
y = tf.placeholder(tf.float32, [None, 1])

weights_L1 = tf.Variable(tf.random_normal([1,10]))
biases_L1 = tf.Variable(tf.zeros([1,10]))
wx_plus_b_L1 = tf.matmul(x, weights_L1) + biases_L1
L1 = tf.nn.tanh(wx_plus_b_L1)

weights_L2 = tf.Variable(tf.random_normal([10,1]))
biases_L2 = tf.Variable(tf.zeros([1,1]))
wx_plus_b_L2 = tf.matmul(L1,weights_L2)+biases_L2
prediction = tf.nn.tanh(wx_plus_b_L2)

loss = tf.reduce_mean(tf.square(y - prediction))
train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for i in range(2000):
        sess.run(train_step, feed_dict={x:x_data, y:y_data})

    prediction_value = sess.run(prediction, feed_dict={x:x_data})

    plt.figure()
    plt.scatter(x_data, y_data)
    plt.plot(x_data,prediction_value,'r-',lw=5)   #曲线是预测值
    plt.show()
