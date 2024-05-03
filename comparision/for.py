import time

array1 = [i for i in range(1000000)]

a=time.time()
print(sum(array1))
b=time.time()
c=b-a
print(f"Duration: {c}")


import tensorflow as tf

array_tf = tf.constant(array1, dtype=tf.float32)
a1=time.time()
print(tf.reduce_sum(array_tf).numpy())
b1=time.time()
d=b1-a1
print(f"Duration: {d}")

if c>d:
    print("tensor is fast")
else:
    print("tensor is slow")
