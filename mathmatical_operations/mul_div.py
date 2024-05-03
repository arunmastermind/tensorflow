import tensorflow as tf

a = tf.constant([4,8,6], dtype=tf.float32)
b = tf.constant([2,4,3], dtype=tf.float32)

print(tf.multiply(a,b).numpy())
print(tf.divide(a,b).numpy())
