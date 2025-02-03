# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 9):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class Lucky7(KaitaiStruct):
    """:field obc_id: obc_id
    :field mission_counter: mission_counter
    :field callsign_and_satellite_name: callsign_and_satellite_name
    :field total_reset_counter: total_reset_counter
    :field swap_reset_counter: swap_reset_counter
    :field battery_voltage: battery_voltage
    :field mcu_temperature: mcu_temperature
    :field pa_temperature: pa_temperature
    :field processor_current: processor_current
    :field mcu_voltage_3v3: mcu_voltage_3v3
    :field mcu_voltage_1v2: mcu_voltage_1v2
    :field angular_rate_x_axis: angular_rate_x_axis
    :field angular_rate_y_axis: angular_rate_y_axis
    :field angular_rate_z_axis: angular_rate_z_axis
    :field antenna_burnwire: antenna_burnwire
    """
    SEQ_FIELDS = ["obc_id", "mission_counter", "callsign_and_satellite_name", "total_reset_counter", "swap_reset_counter", "battery_voltage", "mcu_temperature", "pa_temperature", "processor_current", "mcu_voltage_3v3", "mcu_voltage_1v2", "angular_rate_x_axis", "angular_rate_y_axis", "angular_rate_z_axis", "antenna_burnwire"]
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._debug = collections.defaultdict(dict)

    def _read(self):
        self._debug['obc_id']['start'] = self._io.pos()
        self.obc_id = self._io.read_s2le()
        self._debug['obc_id']['end'] = self._io.pos()
        self._debug['mission_counter']['start'] = self._io.pos()
        self.mission_counter = self._io.read_u4be()
        self._debug['mission_counter']['end'] = self._io.pos()
        self._debug['callsign_and_satellite_name']['start'] = self._io.pos()
        self.callsign_and_satellite_name = (self._io.read_bytes(12)).decode(u"ASCII")
        self._debug['callsign_and_satellite_name']['end'] = self._io.pos()
        if not self.callsign_and_satellite_name == u"OK0SATLUCKY7":
            raise kaitaistruct.ValidationNotEqualError(u"OK0SATLUCKY7", self.callsign_and_satellite_name, self._io, u"/seq/2")
        self._debug['total_reset_counter']['start'] = self._io.pos()
        self.total_reset_counter = self._io.read_u2be()
        self._debug['total_reset_counter']['end'] = self._io.pos()
        self._debug['swap_reset_counter']['start'] = self._io.pos()
        self.swap_reset_counter = self._io.read_u2be()
        self._debug['swap_reset_counter']['end'] = self._io.pos()
        self._debug['battery_voltage']['start'] = self._io.pos()
        self.battery_voltage = self._io.read_u1()
        self._debug['battery_voltage']['end'] = self._io.pos()
        self._debug['mcu_temperature']['start'] = self._io.pos()
        self.mcu_temperature = self._io.read_s1()
        self._debug['mcu_temperature']['end'] = self._io.pos()
        self._debug['pa_temperature']['start'] = self._io.pos()
        self.pa_temperature = self._io.read_s1()
        self._debug['pa_temperature']['end'] = self._io.pos()
        self._debug['processor_current']['start'] = self._io.pos()
        self.processor_current = self._io.read_u1()
        self._debug['processor_current']['end'] = self._io.pos()
        self._debug['mcu_voltage_3v3']['start'] = self._io.pos()
        self.mcu_voltage_3v3 = self._io.read_u1()
        self._debug['mcu_voltage_3v3']['end'] = self._io.pos()
        self._debug['mcu_voltage_1v2']['start'] = self._io.pos()
        self.mcu_voltage_1v2 = self._io.read_u1()
        self._debug['mcu_voltage_1v2']['end'] = self._io.pos()
        self._debug['angular_rate_x_axis']['start'] = self._io.pos()
        self.angular_rate_x_axis = self._io.read_s2be()
        self._debug['angular_rate_x_axis']['end'] = self._io.pos()
        self._debug['angular_rate_y_axis']['start'] = self._io.pos()
        self.angular_rate_y_axis = self._io.read_s2be()
        self._debug['angular_rate_y_axis']['end'] = self._io.pos()
        self._debug['angular_rate_z_axis']['start'] = self._io.pos()
        self.angular_rate_z_axis = self._io.read_s2be()
        self._debug['angular_rate_z_axis']['end'] = self._io.pos()
        self._debug['antenna_burnwire']['start'] = self._io.pos()
        self.antenna_burnwire = self._io.read_u1()
        self._debug['antenna_burnwire']['end'] = self._io.pos()


