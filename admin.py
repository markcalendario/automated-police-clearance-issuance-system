class admin_info:
  def __init__(self, name="Agent"):
    self.name = name
  
  def set_name(self, name):
    self.name = name
  
  def get_name(self):
    return self.name
    
admin = admin_info()