import tensorflow as tf

a = tf.constant([1,4,9], dtype=tf.float32)
print(f"SQRT: {tf.math.sqrt(a).numpy()}")
print(f"EXP: {tf.math.exp(a).numpy()}")
print(f"LOG: {tf.math.log(a).numpy()}")
print(f"POW: {tf.math.pow(a, 2).numpy()}")
