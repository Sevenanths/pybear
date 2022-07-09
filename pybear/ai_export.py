import json
import os
import time

def get_feature_vector(obj_bear, objects):
	bear_coords = [ obj_bear.rect.x, obj_bear.rect.y ]
	stars_coords = []
	fires_coords = []

	for obj_object in objects:
		if obj_object.type == "star":
			stars_coords.append(obj_object.rect.x)
			stars_coords.append(obj_object.rect.y)
		elif obj_object.type == "fire":
			fires_coords.append(obj_object.rect.x)
			fires_coords.append(obj_object.rect.y)

	direction = [ obj_bear.direction ]

	feature_vector = bear_coords + stars_coords + fires_coords + direction

	return feature_vector

def export_feature_vectors(feature_vectors):
	feature_vectors = feature_vectors[:-120]

	output_directory = "ai_export/"

	if not os.path.exists(output_directory):
		os.makedirs(output_directory)

	timestamp = str(int(time.time()))
	filename = f"{output_directory}{timestamp}.json"

	with open(filename, "wt") as writer:
		writer.write(json.dumps(feature_vectors))