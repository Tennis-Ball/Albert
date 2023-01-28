# The main script which declares model architecture and trains
# !! SWITCHED TO PYTHON V3.8
# Test with 50% data, length 20, BS 128, 64->128 drop 0.2 for 100 eps: acc 0.7572, loss 0.0638
from process_data import process_data
from tf_utils import *
import tensorflow_datasets as tfds
import tensorflow as tf
assert tf.__version__.startswith('2')
tf.random.set_seed(1234)


# ds consts  # int = original value
BATCH_SIZE = 256  # 64
BUFFER_SIZE = 20000  # 20000
MAX_LENGTH = 40  # 2100
DATA_SIZE = 50  # percentage of data to use

# model consts
NUM_LAYERS = 2  # 2
D_MODEL = 128  # 256
NUM_HEADS = 8  # 8
UNITS = 256  # 512
DROPOUT = 0.2  # 0.1
learning_rate = CustomSchedule(D_MODEL)
optimizer = tf.keras.optimizers.Adam(
    learning_rate, beta_1=0.9, beta_2=0.98, epsilon=1e-9)
# Create a callback that saves the model's weights
cp_callback = tf.keras.callbacks.ModelCheckpoint(filepath="./saved/checkpoint/cp.ckpt",
                                                 save_weights_only=True,
                                                 verbose=1,
                                                 save_freq="epoch",
                                                 period=20)

# trainings consts
EPOCHS = 50
dataset, tokenizer, VOCAB_SIZE, START_TOKEN, END_TOKEN = initialize(
    BATCH_SIZE, BUFFER_SIZE, MAX_LENGTH, DATA_SIZE)
print(f"Vocab size: {VOCAB_SIZE}")

model = transformer(
    vocab_size=VOCAB_SIZE,
    num_layers=NUM_LAYERS,
    units=UNITS,
    d_model=D_MODEL,
    num_heads=NUM_HEADS,
    dropout=DROPOUT)
print(model.summary())


model.compile(optimizer=optimizer, loss=loss_function, metrics=[accuracy], run_eagerly=True)
model.fit(dataset, epochs=EPOCHS, callbacks=[cp_callback])
# model.save("./saved/full_model/model.h5")  # TODO: get model save to work

print(predict("Spkr1 Where have you been? Spkr2", model, tokenizer, START_TOKEN, END_TOKEN, MAX_LENGTH))
print(predict("Spkr1 Who is Abraham Lincoln? Spkr2", model, tokenizer, START_TOKEN, END_TOKEN, MAX_LENGTH))
print(predict("Spkr1 Hello, how are you? Spkr2", model, tokenizer, START_TOKEN, END_TOKEN, MAX_LENGTH))
