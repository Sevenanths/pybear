import numpy as np
import torch

def predict_direction(model, feature_vectors):
	previous_frame_vector = feature_vectors[-2]
	current_frame_vector = feature_vectors[-1]

	inference_vector = trim_feature_vector(previous_frame_vector) + \
					   trim_feature_vector(current_frame_vector)
	inference_vector = torch.from_numpy(np.array([ inference_vector ], dtype="float32"))

	prediction = model(inference_vector)

	predicted_direction = torch.max(prediction, 1).indices[0] + 1

	return predicted_direction

def trim_feature_vector(v):
	return v[0:2] + v[8:14]