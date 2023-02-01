import tensorflow as tf


mode = 0  # 0=from checkpoint, 1=from last full save

if mode == 0:
    from train import *
    model.load_weights("./saved/checkpoint/cp.ckpt")
    print(predict("How many people are in the world today ?", model, tokenizer, START_TOKEN, END_TOKEN, MAX_LENGTH))
else:
    # Recreate the exact same model, including its weights and the optimizer
    model = tf.keras.models.load_model('my_model.h5')
    # Show the model architecture
    model.summary()
    print(predict("How many people are in the world today ?", model, tokenizer, START_TOKEN, END_TOKEN, MAX_LENGTH))
