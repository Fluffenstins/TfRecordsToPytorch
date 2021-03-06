import numpy
import tensorflow as tf
import torch
from FuncTools import TFRecordDataset

# tfrecord_path = "train-0000" + str(1) + "-of-00008"
# index_path = None
# description = {"global_view": "float", "campaign": "int", "local_view": "float", "tce_planet_num": "int", "tce_depth": "float", "av_training_set": "byte", 
# "tce_impact": "float", "tce_time0bk": "float", "tce_period": "float", "tce_duration": "float"}#{"image": "byte", "label": "float"}
# dataset = TFRecordDataset(tfrecord_path, index_path, description)
# loader = torch.utils.data.DataLoader(dataset, batch_size=10**5) # batch size is just set to a number we know is larger than the dimension of the TfRecord

# data = next(iter(loader))

# FullData = [data["global_view"].numpy(),
#             data["campaign"].numpy(),
#             data["local_view"].numpy(),
#             data["tce_planet_num"].numpy(),
#             data["tce_depth"].numpy(),
#             data["av_training_set"].numpy(),
#             data["tce_impact"].numpy(),
#             data["tce_time0bk"].numpy(),
#             data["tce_period"].numpy(),
#             data["tce_duration"].numpy()]



for Feature in ["global_view", "campaign", "local_view", "tce_planet_num", "tce_depth", "av_training_set", "tce_impact", "tce_time0bk", "tce_period", "tce_duration"]:
    tfrecord_path = "train-00000-of-00008"
    index_path = None
    description = {"global_view": "float", "campaign": "int", "local_view": "float", "tce_planet_num": "int", "tce_depth": "float", "av_training_set": "byte", 
    "tce_impact": "float", "tce_time0bk": "float", "tce_period": "float", "tce_duration": "float"}#{"image": "byte", "label": "float"}
    dataset = TFRecordDataset(tfrecord_path, index_path, description)
    loader = torch.utils.data.DataLoader(dataset, batch_size=10**5)

    FullData = next(iter(loader))[Feature].numpy()

    for i in range(7):
        Index=i+1
        tfrecord_path = "train-0000" + str(Index) + "-of-00008"
        index_path = None
        description = {"global_view": "float", "campaign": "int", "local_view": "float", "tce_planet_num": "int", "tce_depth": "float", "av_training_set": "byte", 
        "tce_impact": "float", "tce_time0bk": "float", "tce_period": "float", "tce_duration": "float"}#{"image": "byte", "label": "float"}
        dataset = TFRecordDataset(tfrecord_path, index_path, description)
        loader = torch.utils.data.DataLoader(dataset, batch_size=10**5)

        data = next(iter(loader))

        ThisData = data[Feature].numpy()

        FullData = numpy.concatenate((FullData, ThisData))
    print("Done building " + Feature + " with a shape of: " + str(FullData.shape))

    numpy.save("NpyData/" + Feature, FullData)
