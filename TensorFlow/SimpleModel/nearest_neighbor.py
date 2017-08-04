import numpy as np
import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets('mnist_data/', one_hot=True)

Xtrain, Ytrain = mnist.train.next_batch(5000)
Xtest, Ytest = mnist.test.next_batch(200)
print('Xtrain.shape:', Xtrain.shape, 'Ytrain.shape:', Ytrain.shape)
print('Xtest.shape:', Xtest.shape, 'Ytest.shape:', Ytest.shape)