import tensorflow as tf

a = tf.constant([1,2,3], dtype=tf.float32)
b = tf.constant([4,5,6], dtype=tf.float32)

add_tf = tf.add(a, b)
sub_tf = tf.subtract(a, b)

print(add_tf.numpy(), sub_tf.numpy())

