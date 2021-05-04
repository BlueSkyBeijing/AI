import tensorflow as tf

#print tensorflow version
print(tf.__version__)

tf.compat.v1.disable_eager_execution()
hello = tf.constant('Hello, TensorFlow!')
sess = tf.compat.v1.Session()

print(sess.run(hello))