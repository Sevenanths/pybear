from .bear_object import BearObject

class Star(BearObject):
	def __init__(self, obj_bear):
		super().__init__("star", obj_bear)