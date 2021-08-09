import tensorflow as tf
from tensorflow import keras
import tensorflow.keras.layers as layers
import numpy as np

class ChessNNModel(tf.keras.Model):
    def __init__(self):
        super(ChessNNModel, self).__init__()
        self.d1 = layers.Dense(128, activation="relu")
        self.d2 = layers.Dense(128, activation="relu")
        self.d3 = layers.Dense(128, activation="relu")
        self.d4 = layers.Dense(128, activation="relu")
        self.d5 = layers.Dense(1, activation="sigmoid")

    def call(self, x):
        x = self.d1(x)
        x = self.d2(x)
        x = self.d3(x)
        x = self.d4(x)
        x = self.d5(x)
        return x
        