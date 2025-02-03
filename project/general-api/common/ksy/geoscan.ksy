---
meta:
  id: geoscan
  title: Geoscan Educational Platform Decoder Struct
  endian: le

doc: |
  :field callsign: ax25_frame.ax25_header.dest_callsign_raw.callsign_ror.callsign
  :field ssid_mask: ax25_frame.ax25_header.dest_ssid_raw.ssid_mask
  :field ssid: ax25_frame.ax25_header.dest_ssid_raw.ssid
  :field src_callsign_raw_callsign: ax25_frame.ax25_header.src_callsign_raw.callsign_ror.callsign
  :field src_ssid_raw_ssid_mask: ax25_frame.ax25_header.src_ssid_raw.ssid_mask
  :field src_ssid_raw_ssid: ax25_frame.ax25_header.src_ssid_raw.ssid
  :field ctl: ax25_frame.ax25_header.ctl
  :field pid: ax25_frame.ax25_header.pid
  :field beacon_id: ax25_frame.payload.beacon_id
  :field eps_timestamp: ax25_frame.payload.eps_timestamp
  :field eps_mode: ax25_frame.payload.eps_mode
  :field eps_switch_count: ax25_frame.payload.eps_switch_count
  :field eps_consumption_current: ax25_frame.payload.eps_consumption_current
  :field eps_system_current: ax25_frame.payload.eps_system_current
  :field eps_cell_voltage_half: ax25_frame.payload.eps_cell_voltage_half
  :field eps_cell_voltage_full: ax25_frame.payload.eps_cell_voltage_full
  :field eps_systems_status: ax25_frame.payload.eps_systems_status
  :field eps_temperature_cell1: ax25_frame.payload.eps_temperature_cell1
  :field eps_temperature_cell2: ax25_frame.payload.eps_temperature_cell2
  :field eps_boot_count: ax25_frame.payload.eps_boot_count
  :field eps_heater_mode: ax25_frame.payload.eps_heater_mode
  :field eps_reserved: ax25_frame.payload.eps_reserved
  :field obc_boot_count: ax25_frame.payload.obc_boot_count
  :field obc_active_status: ax25_frame.payload.obc_active_status
  :field obc_temperature_pos_x: ax25_frame.payload.obc_temperature_pos_x
  :field obc_temperature_neg_x: ax25_frame.payload.obc_temperature_neg_x
  :field obc_temperature_pos_y: ax25_frame.payload.obc_temperature_pos_y
  :field obc_temperature_neg_y: ax25_frame.payload.obc_temperature_neg_y
  :field gnss_sat_number: ax25_frame.payload.gnss_sat_number
  :field adcs_mode: ax25_frame.payload.adcs_mode
  :field adcs_reserved: ax25_frame.payload.adcs_reserved
  :field cam_photos_number: ax25_frame.payload.cam_photos_number
  :field cam_mode: ax25_frame.payload.cam_mode
  :field cam_reserved: ax25_frame.payload.cam_reserved
  :field comm_type: ax25_frame.payload.comm_type
  :field comm_bus_voltage: ax25_frame.payload.comm_bus_voltage
  :field comm_boot_count: ax25_frame.payload.comm_boot_count
  :field comm_rssi: ax25_frame.payload.comm_rssi
  :field comm_rssi_minimal: ax25_frame.payload.comm_rssi_minimal
  :field comm_received_valid_packets: ax25_frame.payload.comm_received_valid_packets
  :field comm_received_invalid_packets: ax25_frame.payload.comm_received_invalid_packets
  :field comm_sent_packets: ax25_frame.payload.comm_sent_packets
  :field comm_status: ax25_frame.payload.comm_status
  :field comm_mode: ax25_frame.payload.comm_mode
  :field comm_temperature: ax25_frame.payload.comm_temperature
  :field comm_qso_received: ax25_frame.payload.comm_qso_received
  :field comm_reserved: ax25_frame.payload.comm_reserved

seq:
  - id: ax25_frame
    type: ax25_frame
    doc-ref: 'https://www.tapr.org/pdf/AX25.2.2.pdf'
types:
  ax25_frame:
    seq:
      - id: ax25_header
        type: ax25_header
      - id: payload
        type: geoscan_beacon_tlm

  ax25_header:
    seq:
      - id: dest_callsign_raw
        type: callsign_raw
      - id: dest_ssid_raw
        type: ssid_mask
      - id: src_callsign_raw
        type: callsign_raw
      - id: src_ssid_raw
        type: ssid_mask
      - id: ctl
        type: u1
      - id: pid
        type: u1

  callsign_raw:
    seq:
      - id: callsign_ror
        process: ror(1)
        size: 6
        type: callsign

  callsign:
    seq:
      - id: callsign
        type: str
        encoding: ASCII
        size: 6

  ssid_mask:
    seq:
      - id: ssid_mask
        type: u1
    instances:
      ssid:
        value: (ssid_mask & 0x0f) >> 1

  geoscan_beacon_tlm:
    seq:
      - id: beacon_id
        type: u1
      - id: eps_timestamp
        type: u4
        doc: |
          OBC Time (Unix timestamp)
      - id: eps_mode
        type: u1
        doc: |
          0 - init, 1 - reserved, 2 - safe, 3 - normal
      - id: eps_switch_count
        type: u1
        doc: |
          Number of EPS switches
      - id: eps_consumption_current
        type: u2
        doc: |
          Current of consumption [mA]
      - id: eps_solar_cells_current
        type: u2
        doc: |
          Current from sun panels [mA]
      - id: eps_cell_voltage_half
        type: u2
        doc: |
          Voltage of one battery [mV]
      - id: eps_cell_voltage_full
        type: u2
        doc: |
          Voltage of both batteries [mV]
      - id: eps_systems_status
        type: u2
        doc: |
          Status of all systems [bitfield]
          0: COMMu1
          1: COMMu2
          2: OBC
          3: RWS
          4: COMMx
          5: PL1
          6: PL2
          7: PL3
          8: PL4
          9…15: Reserved
      - id: eps_temperature_cell1
        type: s1
        doc: |
          Temperature on battery cell 1 [°C]
      - id: eps_temperature_cell2
        type: s1
        doc: |
          Temperature on battery cell 2 [°C]
      - id: eps_boot_count
        type: u2
        doc: |
      - id: eps_heater_mode
        type: u1
        doc: |
          Bits 0 - 3:
          0 - Turned Off
          1 - Threshold
          2 - Manual
          Bits 4 - 6:
          0 - Middle D1 and D2
          1 - 1-Wire
          2 - Sensor 1
          3 - Sensor 2
          Bit 7:
          0 - Heater Tured Off
          1 - Heater Tured On
      - id: eps_reserved
        type: u2
        doc: |
      - id: obc_boot_count
        type: u2
        doc: |
          Total number of OBC reboots
      - id: obc_active_status
        type: u1
        doc: |
          0: RWS
          1: Torques
          2: INS
          3: Camera
          4: Panel Х+
          5: Panel Х-
          6: Panel Y+
          7: Panel Y-
      - id: obc_temperature_pos_x
        type: s1
        doc: |
          Temperature on panel X+ [°C]
      - id: obc_temperature_neg_x
        type: s1
        doc: |
          Temperature on panel X- [°C]
      - id: obc_temperature_pos_y
        type: s1
        doc: |
          Temperature on panel Y+ [°C]
      - id: obc_temperature_neg_y
        type: s1
        doc: |
          Temperature on panel Y- [°C]
      - id: gnss_sat_number
        type: u1
        doc: |
          Number of fixed satellites
      - id: adcs_mode
        type: u1
        doc: |
          0 - Turned Off
          1 - B-Dot
          2 - Three-axis
      - id: adcs_reserved
        type: u1
        doc: |
      - id: cam_photos_number
        type: u1
        doc: |
          Total number of made images
      - id: cam_mode
        type: u1
        doc: |
          0 - Waiting
          1 - Single Photo
          2 - Serial Photo
          3 - Video
          4 - Control
          255 - Turned Off
      - id: cam_reserved
        type: u4
      - id: comm_type
        type: u1
        doc: |
          3 - Comm #1
          13 - Comm #2
      - id: comm_bus_voltage
        type: u2
        doc: | 
          Voltage of VBUS [mV]
      - id: comm_boot_count
        type: u2
        doc: | 
          Total COMM boot count
      - id: comm_rssi
        type: s1
        doc: |
          COMM received signal strength indicator [dBm]
      - id: comm_rssi_minimal
        type: s1
        doc: |
          COMM received minimal signal strength indicator [dBm]
      - id: comm_received_valid_packets
        type: u1
        doc: |
          Number of received valid packets
      - id: comm_received_invalid_packets
        type: u1
        doc: |
          Number of received invalid packets
      - id: comm_sent_packets
        type: u1
        doc: |
          Number of sent packets
      - id: comm_status
        type: u1
        doc: |
          0: Antenna Detector
          1: Battery Status Detector
          2-7: Reserved
      - id: comm_mode
        type: u1
        doc: |
          0 - Mode I
          1 - Mode III
          2 - Mode II
          3-244 - Reserved
      - id: comm_temperature
        type: s1
        doc: |
          COMM board temperature [°C]
      - id: comm_qso_received
        type: u1
        doc: |
          Number of received QSO
      - id: comm_reserved
        type: u2

