import tensorflow as tf

a = tf.constant([[1,2,3],[4,5,6]], dtype=tf.float32)

print(f"sum:{tf.reduce_sum(a).numpy()}")
print(f"Row Mean: {tf.reduce_mean(a, axis=0).numpy()}")
print(f"Col Mean: {tf.reduce_mean(a, axis=1).numpy()}")

print(f"Min: {tf.reduce_min(a).numpy()}")
print(f"Max: {tf.reduce_max(a).numpy()}")
