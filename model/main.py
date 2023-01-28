# The main script which declares model architecture and trains
# !! SWITCHED TO PYTHON V3.8
from process_data import process_data
from tf_utils import *
import tensorflow_datasets as tfds
import tensorflow as tf
assert tf.__version__.startswith('2')
tf.random.set_seed(1234)


# ds consts
BATCH_SIZE = 128  # 64
BUFFER_SIZE = 2100  # 20000
MAX_LENGTH = 2100
DATA_SIZE = 0.05  # percentage of data to use

# model consts
NUM_LAYERS = 2  # 2
D_MODEL = 16  # 256
NUM_HEADS = 8  # 8
UNITS = 32  # 512
DROPOUT = 0.5  # 0.1

# trainings consts
EPOCHS = 5

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

learning_rate = CustomSchedule(D_MODEL)
optimizer = tf.keras.optimizers.Adam(
    learning_rate, beta_1=0.9, beta_2=0.98, epsilon=1e-9)

model.compile(optimizer=optimizer, loss=loss_function, metrics=[accuracy], run_eagerly=True)
model.fit(dataset, epochs=EPOCHS)
