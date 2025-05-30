# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 9):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class Bugsat1(KaitaiStruct):
    """:field dest_callsign: ax25_frame.ax25_header.dest_callsign_raw.callsign_ror.callsign
    :field src_callsign: ax25_frame.ax25_header.src_callsign_raw.callsign_ror.callsign
    :field src_ssid: ax25_frame.ax25_header.src_ssid_raw.ssid
    :field dest_ssid: ax25_frame.ax25_header.dest_ssid_raw.ssid
    :field rpt_callsign: ax25_frame.ax25_header.repeater.rpt_instance[0].rpt_callsign_raw.callsign_ror.callsign
    :field ctl: ax25_frame.ax25_header.ctl
    :field pid: ax25_frame.payload.pid
    :field uptime_s: ax25_frame.payload.ax25_info.beacon_type.uptime_s
    :field rtc_s: ax25_frame.payload.ax25_info.beacon_type.rtc_s
    :field reset_count: ax25_frame.payload.ax25_info.beacon_type.reset_count_be
    :field current_mode: ax25_frame.payload.ax25_info.beacon_type.current_mode
    :field last_boot_reason: ax25_frame.payload.ax25_info.beacon_type.last_boot_reason
    :field free: ax25_frame.payload.ax25_info.beacon_type.free
    :field last_seen_sequence_number: ax25_frame.payload.ax25_info.beacon_type.last_seen_sequence_number
    :field antenna_deploy_status: ax25_frame.payload.ax25_info.beacon_type.antenna_deploy_status
    :field low_voltage_counter: ax25_frame.payload.ax25_info.beacon_type.low_voltage_counter
    :field nice_battery_mv: ax25_frame.payload.ax25_info.beacon_type.nice_battery_mv
    :field raw_battery_mv: ax25_frame.payload.ax25_info.beacon_type.raw_battery_mv
    :field battery_amps: ax25_frame.payload.ax25_info.beacon_type.battery_amps
    :field pcm_3v3_v: ax25_frame.payload.ax25_info.beacon_type.pcm_3v3_v
    :field pcm_3v3_a: ax25_frame.payload.ax25_info.beacon_type.pcm_3v3_a
    :field pcm_5v_v: ax25_frame.payload.ax25_info.beacon_type.pcm_5v_v
    :field pcm_5v_a: ax25_frame.payload.ax25_info.beacon_type.pcm_5v_a
    :field cpu_c: ax25_frame.payload.ax25_info.beacon_type.cpu_c
    :field mirror_cell_c: ax25_frame.payload.ax25_info.beacon_type.mirror_cell_c
    :field mode: ax25_frame.payload.ax25_info.beacon_type.mode
    :field sun_vector_x: ax25_frame.payload.ax25_info.beacon_type.sun_vector_x
    :field sun_vector_y: ax25_frame.payload.ax25_info.beacon_type.sun_vector_y
    :field sun_vector_z: ax25_frame.payload.ax25_info.beacon_type.sun_vector_z
    :field magnetometer_x_mg: ax25_frame.payload.ax25_info.beacon_type.magnetometer_x_mg
    :field magnetometer_y_mg: ax25_frame.payload.ax25_info.beacon_type.magnetometer_y_mg
    :field magnetometer_z_mg: ax25_frame.payload.ax25_info.beacon_type.magnetometer_z_mg
    :field gyro_x_dps: ax25_frame.payload.ax25_info.beacon_type.gyro_x_dps
    :field gyro_y_dps: ax25_frame.payload.ax25_info.beacon_type.gyro_y_dps
    :field gyro_z_dps: ax25_frame.payload.ax25_info.beacon_type.gyro_z_dps
    :field temperature_imu_c: ax25_frame.payload.ax25_info.beacon_type.temperature_imu_c
    :field fine_gyro_x_dps: ax25_frame.payload.ax25_info.beacon_type.fine_gyro_x_dps
    :field fine_gyro_y_dps: ax25_frame.payload.ax25_info.beacon_type.fine_gyro_y_dps
    :field fine_gyro_z_dps: ax25_frame.payload.ax25_info.beacon_type.fine_gyro_z_dps
    :field wheel_1_radsec: ax25_frame.payload.ax25_info.beacon_type.wheel_1_radsec
    :field wheel_2_radsec: ax25_frame.payload.ax25_info.beacon_type.wheel_2_radsec
    :field wheel_3_radsec: ax25_frame.payload.ax25_info.beacon_type.wheel_3_radsec
    :field wheel_4_radsec: ax25_frame.payload.ax25_info.beacon_type.wheel_4_radsec
    :field experiments_run: ax25_frame.payload.ax25_info.beacon_type.experiments_run
    :field experiments_failed: ax25_frame.payload.ax25_info.beacon_type.experiments_failed
    :field last_experiment_run: ax25_frame.payload.ax25_info.beacon_type.last_experiment_run
    :field current_state: ax25_frame.payload.ax25_info.beacon_type.current_state
    :field message: ax25_frame.payload.ax25_info.beacon_type.message
    
    Attention: `rpt_callsign` cannot be accessed because `rpt_instance` is an
    array of unknown size at the beginning of the parsing process! Left an
    example in here.
    """
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.ax25_frame = Bugsat1.Ax25Frame(self._io, self, self._root)

    class Ax25Frame(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.ax25_header = Bugsat1.Ax25Header(self._io, self, self._root)
            _on = (self.ax25_header.ctl & 19)
            if _on == 0:
                self.payload = Bugsat1.IFrame(self._io, self, self._root)
            elif _on == 3:
                self.payload = Bugsat1.UiFrame(self._io, self, self._root)
            elif _on == 19:
                self.payload = Bugsat1.UiFrame(self._io, self, self._root)
            elif _on == 16:
                self.payload = Bugsat1.IFrame(self._io, self, self._root)
            elif _on == 18:
                self.payload = Bugsat1.IFrame(self._io, self, self._root)
            elif _on == 2:
                self.payload = Bugsat1.IFrame(self._io, self, self._root)


    class Ax25Header(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.dest_callsign_raw = Bugsat1.CallsignRaw(self._io, self, self._root)
            self.dest_ssid_raw = Bugsat1.SsidMask(self._io, self, self._root)
            self.src_callsign_raw = Bugsat1.CallsignRaw(self._io, self, self._root)
            self.src_ssid_raw = Bugsat1.SsidMask(self._io, self, self._root)
            if (self.src_ssid_raw.ssid_mask & 1) == 0:
                self.repeater = Bugsat1.Repeater(self._io, self, self._root)

            self.ctl = self._io.read_u1()


    class UiFrame(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.pid = self._io.read_u1()
            self._raw_ax25_info = self._io.read_bytes_full()
            _io__raw_ax25_info = KaitaiStream(BytesIO(self._raw_ax25_info))
            self.ax25_info = Bugsat1.Ax25InfoData(_io__raw_ax25_info, self, self._root)


    class Callsign(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.callsign = (self._io.read_bytes(6)).decode(u"ASCII")


    class IFrame(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.pid = self._io.read_u1()
            self._raw_ax25_info = self._io.read_bytes_full()
            _io__raw_ax25_info = KaitaiStream(BytesIO(self._raw_ax25_info))
            self.ax25_info = Bugsat1.Ax25InfoData(_io__raw_ax25_info, self, self._root)


    class SsidMask(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.ssid_mask = self._io.read_u1()

        @property
        def ssid(self):
            if hasattr(self, '_m_ssid'):
                return self._m_ssid

            self._m_ssid = ((self.ssid_mask & 15) >> 1)
            return getattr(self, '_m_ssid', None)


    class Repeaters(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.rpt_callsign_raw = Bugsat1.CallsignRaw(self._io, self, self._root)
            self.rpt_ssid_raw = Bugsat1.SsidMask(self._io, self, self._root)


    class Repeater(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.rpt_instance = []
            i = 0
            while True:
                _ = Bugsat1.Repeaters(self._io, self, self._root)
                self.rpt_instance.append(_)
                if (_.rpt_ssid_raw.ssid_mask & 1) == 1:
                    break
                i += 1


    class Message(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.message = (self._io.read_bytes_full()).decode(u"utf-8")


    class CallsignRaw(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self._raw__raw_callsign_ror = self._io.read_bytes(6)
            self._raw_callsign_ror = KaitaiStream.process_rotate_left(self._raw__raw_callsign_ror, 8 - (1), 1)
            _io__raw_callsign_ror = KaitaiStream(BytesIO(self._raw_callsign_ror))
            self.callsign_ror = Bugsat1.Callsign(_io__raw_callsign_ror, self, self._root)


    class Ax25InfoData(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.beacon_id0 = self._io.read_u1()
            if self.beacon_id0 == 255:
                self.beacon_id1 = self._io.read_bytes(1)
                if not self.beacon_id1 == b"\xFF":
                    raise kaitaistruct.ValidationNotEqualError(b"\xFF", self.beacon_id1, self._io, u"/types/ax25_info_data/seq/1")

            if self.beacon_id0 == 255:
                self.beacon_id2 = self._io.read_bytes(1)
                if not self.beacon_id2 == b"\xF0":
                    raise kaitaistruct.ValidationNotEqualError(b"\xF0", self.beacon_id2, self._io, u"/types/ax25_info_data/seq/2")

            _on = self.beacon_id0
            if _on == 58:
                self.beacon_type = Bugsat1.Message(self._io, self, self._root)
            else:
                self.beacon_type = Bugsat1.Telemetry(self._io, self, self._root)


    class Telemetry(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.platform_id = self._io.read_bytes(2)
            if not self.platform_id == b"\x00\x01":
                raise kaitaistruct.ValidationNotEqualError(b"\x00\x01", self.platform_id, self._io, u"/types/telemetry/seq/0")
            self.uptime_s = self._io.read_u4be()
            self.rtc_s = self._io.read_u4be()
            self.rstcnt_b = []
            for i in range(3):
                self.rstcnt_b.append(self._io.read_u1())

            self.current_mode = self._io.read_u1()
            self.last_boot_reason = self._io.read_u4be()
            self.mem_tlm_id = self._io.read_bytes(2)
            if not self.mem_tlm_id == b"\x01\x01":
                raise kaitaistruct.ValidationNotEqualError(b"\x01\x01", self.mem_tlm_id, self._io, u"/types/telemetry/seq/6")
            self.free = self._io.read_u4be()
            self.cdh_id = self._io.read_bytes(2)
            if not self.cdh_id == b"\x02\x01":
                raise kaitaistruct.ValidationNotEqualError(b"\x02\x01", self.cdh_id, self._io, u"/types/telemetry/seq/8")
            self.last_seen_sequence_number = self._io.read_u4be()
            self.antenna_deploy_status = self._io.read_u1()
            self.pwr_tlm_id = self._io.read_bytes(2)
            if not self.pwr_tlm_id == b"\x03\x01":
                raise kaitaistruct.ValidationNotEqualError(b"\x03\x01", self.pwr_tlm_id, self._io, u"/types/telemetry/seq/11")
            self.low_voltage_counter = self._io.read_u2be()
            self.nice_battery_mv = self._io.read_u2be()
            self.raw_battery_mv = self._io.read_u2be()
            self.battery_amps = self._io.read_u2be()
            self.pcm_3v3_v = self._io.read_u2be()
            self.pcm_3v3_a = self._io.read_u2be()
            self.pcm_5v_v = self._io.read_u2be()
            self.pcm_5v_a = self._io.read_u2be()
            self.thermal_tlm_id = self._io.read_bytes(2)
            if not self.thermal_tlm_id == b"\x04\x01":
                raise kaitaistruct.ValidationNotEqualError(b"\x04\x01", self.thermal_tlm_id, self._io, u"/types/telemetry/seq/20")
            self.cpu_c = self._io.read_s2be()
            self.mirror_cell_c = self._io.read_s2be()
            self.aocs_tlm_id = self._io.read_bytes(2)
            if not self.aocs_tlm_id == b"\x05\x01":
                raise kaitaistruct.ValidationNotEqualError(b"\x05\x01", self.aocs_tlm_id, self._io, u"/types/telemetry/seq/23")
            self.mode = self._io.read_u4be()
            self.sun_vector_x = self._io.read_s2be()
            self.sun_vector_y = self._io.read_s2be()
            self.sun_vector_z = self._io.read_s2be()
            self.magnetometer_x_mg = self._io.read_s2be()
            self.magnetometer_y_mg = self._io.read_s2be()
            self.magnetometer_z_mg = self._io.read_s2be()
            self.gyro_x_dps = self._io.read_s2be()
            self.gyro_y_dps = self._io.read_s2be()
            self.gyro_z_dps = self._io.read_s2be()
            self.temperature_imu_c = self._io.read_s2be()
            self.fine_gyro_x_dps = self._io.read_s4be()
            self.fine_gyro_y_dps = self._io.read_s4be()
            self.fine_gyro_z_dps = self._io.read_s4be()
            self.wheel_1_radsec = self._io.read_s2be()
            self.wheel_2_radsec = self._io.read_s2be()
            self.wheel_3_radsec = self._io.read_s2be()
            self.wheel_4_radsec = self._io.read_s2be()
            self.payload_tlm_id = self._io.read_bytes(2)
            if not self.payload_tlm_id == b"\x06\x01":
                raise kaitaistruct.ValidationNotEqualError(b"\x06\x01", self.payload_tlm_id, self._io, u"/types/telemetry/seq/42")
            self.experiments_run = self._io.read_u2be()
            self.experiments_failed = self._io.read_u2be()
            self.last_experiment_run = self._io.read_s2be()
            self.current_state = self._io.read_u1()

        @property
        def reset_count_be(self):
            if hasattr(self, '_m_reset_count_be'):
                return self._m_reset_count_be

            self._m_reset_count_be = (((self.rstcnt_b[0] << 16) | (self.rstcnt_b[1] << 8)) | self.rstcnt_b[2])
            return getattr(self, '_m_reset_count_be', None)



