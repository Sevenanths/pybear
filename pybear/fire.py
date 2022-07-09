from .bear_object import BearObject

class Fire(BearObject):
	def __init__(self, obj_bear):
		super().__init__("fire", obj_bear)