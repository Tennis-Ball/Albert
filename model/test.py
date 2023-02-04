import tensorflow as tf
from train import *


mode = 3  # 0=predict from checkpoint, 1=predict from last full save, 2=continue training from ckpt, 3=continue training from last full save
EPOCHS = 20

if mode == 0:
    model.load_weights("./saved/checkpoint/")
    while True:
        print(predict(input("Prompt: "), model, tokenizer, START_TOKEN, END_TOKEN, MAX_LENGTH))
elif mode == 1:
    model.load_weights("./saved/full_model/")
    while True:
        print(predict(input("Prompt: "), model, tokenizer, START_TOKEN, END_TOKEN, MAX_LENGTH))
elif mode == 2:
    model.load_weights("./saved/checkpoint/")
    model.compile(optimizer=optimizer, loss=loss_function, metrics=[accuracy], run_eagerly=True)
    model.fit(dataset, epochs=EPOCHS, callbacks=[cp_callback])
    # model.fit(dataset, epochs=EPOCHS)
    model.save_weights("./saved/full_model/")  # TODO: get model save to work

    print(predict("Where have you been ?", model, tokenizer, START_TOKEN, END_TOKEN, MAX_LENGTH))
    print(predict("Who is Abraham Lincoln ?", model, tokenizer, START_TOKEN, END_TOKEN, MAX_LENGTH))
    print(predict("Hello .", model, tokenizer, START_TOKEN, END_TOKEN, MAX_LENGTH))
elif mode == 3:
    model.load_weights("./saved/full_model/")
    model.compile(optimizer=optimizer, loss=loss_function, metrics=[accuracy], run_eagerly=True)
    model.fit(dataset, epochs=EPOCHS, callbacks=[cp_callback])
    # model.fit(dataset, epochs=EPOCHS)
    model.save_weights("./saved/full_model/")  # TODO: get model save to work

    print(predict("Where have you been ?", model, tokenizer, START_TOKEN, END_TOKEN, MAX_LENGTH))
    print(predict("Who is Abraham Lincoln ?", model, tokenizer, START_TOKEN, END_TOKEN, MAX_LENGTH))
    print(predict("Hello .", model, tokenizer, START_TOKEN, END_TOKEN, MAX_LENGTH))
