"""autogenerated by genpy from camera_actuator/CameraInstruction.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import camera_actuator.msg

class CameraInstruction(genpy.Message):
  _md5sum = "4a0c0bb2cc9774dcd8d640551eabf6f0"
  _type = "camera_actuator/CameraInstruction"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """string type
IntArray value
string status
================================================================================
MSG: camera_actuator/IntArray
int16[] data
"""
  __slots__ = ['type','value','status']
  _slot_types = ['string','camera_actuator/IntArray','string']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       type,value,status

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(CameraInstruction, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.type is None:
        self.type = ''
      if self.value is None:
        self.value = camera_actuator.msg.IntArray()
      if self.status is None:
        self.status = ''
    else:
      self.type = ''
      self.value = camera_actuator.msg.IntArray()
      self.status = ''

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self.type
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      length = len(self.value.data)
      buff.write(_struct_I.pack(length))
      pattern = '<%sh'%length
      buff.write(struct.pack(pattern, *self.value.data))
      _x = self.status
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.value is None:
        self.value = camera_actuator.msg.IntArray()
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.type = str[start:end].decode('utf-8')
      else:
        self.type = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sh'%length
      start = end
      end += struct.calcsize(pattern)
      self.value.data = struct.unpack(pattern, str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.status = str[start:end].decode('utf-8')
      else:
        self.status = str[start:end]
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self.type
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      length = len(self.value.data)
      buff.write(_struct_I.pack(length))
      pattern = '<%sh'%length
      buff.write(self.value.data.tostring())
      _x = self.status
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.value is None:
        self.value = camera_actuator.msg.IntArray()
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.type = str[start:end].decode('utf-8')
      else:
        self.type = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sh'%length
      start = end
      end += struct.calcsize(pattern)
      self.value.data = numpy.frombuffer(str[start:end], dtype=numpy.int16, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.status = str[start:end].decode('utf-8')
      else:
        self.status = str[start:end]
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
