class AddrBookEntry(object):
	def __init__(self, nm, ph):
		self.name = nm
		self.phone = ph
		print 'add for',self.name
	def updatePhone(self, newph):
		self.phone = newph
		print 'Updated for#',self.name