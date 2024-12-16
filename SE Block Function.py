import tensorflow as tf

def se_block(inputs, ratio=8):
    # 获取输入张量的通道数
    channels = inputs.shape[-1]
    # Squeeze操作，将通道维度压缩为1，形状变为[batch_size, 1, 1, channels]
    x = tf.keras.layers.GlobalAveragePooling2D()(inputs)
    # Excitation操作，引入一个全连接层，并使用ReLU作为激活函数，形状变为[batch_size, channels // ratio]
    x = tf.keras.layers.Dense(channels // ratio, activation='relu')(x)
    # Excitation操作，再次引入一个全连接层，并使用sigmoid作为激活函数，形状变为[batch_size, channels]
    x = tf.keras.layers.Dense(channels, activation='sigmoid')(x)
    # 重新塑造张量形状，使其与输入张量相同
    x = tf.keras.layers.Reshape((1, 1, channels))(x)
    # 乘以输入张量，引入注意力机制，得到输出张量
    outputs = inputs * x
    return outputs
