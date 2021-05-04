import tensorflow as tf
from tensorflow.keras import layers

print("tensorflow version: ", tf.__version__)

print("keras version: ", tf.keras.__version__)

tf.compat.v1.disable_eager_execution()
hello = tf.constant('Hello, TensorFlow!')
sess = tf.compat.v1.Session()

print(sess.run(hello))
