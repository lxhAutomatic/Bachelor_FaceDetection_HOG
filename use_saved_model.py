# import tf.keras api for build the model architecture
from tensorflow.keras import models
from lib.file_operate import read_np_lists
import numpy as np

data_x = read_np_lists('HOG_data/PHOG.txt')
amount = len(data_x) 
print("containing "+str(amount)+" positive samples")
 
train_x = data_x[0:int(amount*0.6)]
val_x = data_x[int(amount*0.6):amount]

train_y = np.array([1]*len(train_x))
val_y = np.array([1]*len(val_x))

hog_model = models.load_model("trained_models/nnet/best.h5")
predict = hog_model.predict(val_x)



