meta:
  id: ssamusat
  endian: be
  title: SSAMUSAT
doc-ref: 'https://amu-sat.github.io/'
doc: |
  :field preamble: ssamusat.preamble
  :field sync_word: ssamusat.sync_word
  :field data_field1: ssamusat.data_field1
  :field data_field2: ssamusat.data_field2
  :field crc: ssamusat.crc
  :field ax25_frame: ssamusat.data_field2.ax25_frame
  :field ax25_header: ssamusat.data_field2.ax25_frame.ax25_header
  :field dest_address: ssamusat.data_field2.ax25_frame.ax25_header.dest_address
  :field dest_ssid: ssamusat.data_field2.ax25_frame.ax25_header.dest_ssid
  :field src_address: ssamusat.data_field2.ax25_frame.ax25_header.src_address
  :field src_ssid: ssamusat.data_field2.ax25_frame.ax25_header.src_ssid
  :field control_id: ssamusat.data_field2.ax25_frame.ax25_header.control_id
  :field pid: ssamusat.data_field2.ax25_frame.ax25_header.pid
  :field information_field: ssamusat.data_field2.ax25_frame.information_field
  :field packet_type: ssamusat.data_field2.ax25_frame.information_field.packet_type
  :field telemetry_data_1: ssamusat.data_field2.ax25_frame.information_field.telemetry_data_1
  :field sensor1: ssamusat.data_field2.ax25_frame.information_field.telemetry_data_1.sensor1
  :field sensor2: ssamusat.data_field2.ax25_frame.information_field.telemetry_data_1.sensor2
  :field sensor3: ssamusat.data_field2.ax25_frame.information_field.telemetry_data_1.sensor3
  :field sensor4: ssamusat.data_field2.ax25_frame.information_field.telemetry_data_1.sensor4
  :field battery_voltage: ssamusat.data_field2.ax25_frame.information_field.telemetry_data_1.battery_voltage
  :field battery_temperature: ssamusat.data_field2.ax25_frame.information_field.telemetry_data_1.battery_temperature
  :field battery_soc: ssamusat.data_field2.ax25_frame.information_field.telemetry_data_1.battery_soc
  :field battery_current: ssamusat.data_field2.ax25_frame.information_field.telemetry_data_1.battery_current
  :field temp_in: ssamusat.data_field2.ax25_frame.information_field.telemetry_data_1.temp_in
  :field temp_out: ssamusat.data_field2.ax25_frame.information_field.telemetry_data_1.temp_out
  :field temp_3: ssamusat.data_field2.ax25_frame.information_field.telemetry_data_1.temp_3
  :field pl_temp: ssamusat.data_field2.ax25_frame.information_field.telemetry_data_1.pl_temp
  :field rtc: ssamusat.data_field2.ax25_frame.information_field.telemetry_data_1.rtc
  :field temp_out_l: ssamusat.data_field2.ax25_frame.information_field.telemetry_data_1.temp_out_l
  :field temp_out_h: ssamusat.data_field2.ax25_frame.information_field.telemetry_data_1.temp_out_h
  :field acceleration_x: ssamusat.data_field2.ax25_frame.information_field.telemetry_data_1.acceleration_x
  :field acceleration_y: ssamusat.data_field2.ax25_frame.information_field.telemetry_data_1.acceleration_y
  :field acceleration_z: ssamusat.data_field2.ax25_frame.information_field.telemetry_data_1.acceleration_z
  :field magnetic_field_x: ssamusat.data_field2.ax25_frame.information_field.telemetry_data_1.magnetic_field_x
  :field magnetic_field_y: ssamusat.data_field2.ax25_frame.information_field.telemetry_data_1.magnetic_field_y
  :field magnetic_field_z: ssamusat.data_field2.ax25_frame.information_field.telemetry_data_1.magnetic_field_z
  :field angular_rate_x: ssamusat.data_field2.ax25_frame.information_field.telemetry_data_1.angular_rate_x
  :field angular_rate_y: ssamusat.data_field2.ax25_frame.information_field.telemetry_data_1.angular_rate_y
  :field angular_rate_z: ssamusat.data_field2.ax25_frame.information_field.telemetry_data_1.angular_rate_z
  :field velocity: ssamusat.data_field2.ax25_frame.information_field.telemetry_data_1.velocity
  :field latitude: ssamusat.data_field2.ax25_frame.information_field.telemetry_data_1.latitude
  :field longitude: ssamusat.data_field2.ax25_frame.information_field.telemetry_data_1.longitude
  :field telemetry_data_2: ssamusat.data_field2.ax25_frame.information_field.telemetry_data_2
  :field gps_time: ssamusat.data_field2.ax25_frame.information_field.telemetry_data_2.gps_time
  :field solar_deployment_status: ssamusat.data_field2.ax25_frame.information_field.telemetry_data_2.solar_deployment_status
  :field eps_health_status: ssamusat.data_field2.ax25_frame.information_field.telemetry_data_2.eps_health_status
  :field adcs_health_status: ssamusat.data_field2.ax25_frame.information_field.telemetry_data_2.adcs_health_status
  :field payload_health_status: ssamusat.data_field2.ax25_frame.information_field.telemetry_data_2.payload_health_status
  :field com_health_status: ssamusat.data_field2.ax25_frame.information_field.telemetry_data_2.com_health_status
  :field battery1_health_status: ssamusat.data_field2.ax25_frame.information_field.telemetry_data_2.battery1_health_status
  :field battery2_health_status: ssamusat.data_field2.ax25_frame.information_field.telemetry_data_2.battery2_health_status
  :field image_data_0: ssamusat.data_field2.ax25_frame.information_field.image_data_0
  :field image_id: ssamusat.data_field2.ax25_frame.information_field.image_data_0.image_id
  :field payload_data: ssamusat.data_field2.ax25_frame.information_field.image_data_0.payload_data

seq:
  - id: preamble
    type: str
    size: 5
    encoding: ascii
    doc: "Preamble (5 bytes)"

  - id: sync_word
    type: u1
    doc: "Sync Word (1 byte)"

  - id: data_field1
    type: u2
    doc: "Length of Data Field 2 (2 bytes)"

  - id: data_field2
    type: data_field2_struct
    doc: "Data Field 2"

  - id: crc
    type: u2
    doc: "CRC (2 bytes)"

types:
  data_field2_struct:
    seq:
      - id: preamble
        type: str
        size: 8
        encoding: ascii
        doc: "Preamble in Data Field 2 (8 bytes)"

      - id: ax25_frame
        type: ax25_frame_struct
        doc: "AX.25 Frame"

      - id: postamble
        type: str
        size: 3
        encoding: ascii
        doc: "Postamble in Data Field 2 (3 bytes)"

  ax25_frame_struct:
    seq:
      - id: flag1
        type: u1
        doc: "AX.25 Flag 1 (1 byte)"

      - id: ax25_header
        type: ax25_header_struct
        doc: "AX.25 Header"

      - id: information_field
        type: information_field_struct
        doc: "Information Field"

      - id: fcs
        type: u2
        doc: "Frame Check Sequence (FCS) (2 bytes)"

      - id: flag2
        type: u1
        doc: "AX.25 Flag 2 (1 byte)"

  ax25_header_struct:
    seq:
      - id: dest_address
        type: str
        size: 7
        encoding: "ASCII"
        doc: "Destination address (7 bytes)"

      - id: dest_ssid
        type: u1
        doc: "Destination SSID (1 byte)"

      - id: src_address
        type: str
        size: 7
        encoding: "ASCII"
        doc: "Source address (7 bytes)"

      - id: src_ssid
        type: u1
        doc: "Source SSID (1 byte)"

      - id: control_id
        type: u1
        doc: "Control ID (1 byte)"

      - id: pid
        type: u1
        doc: "Packet ID (1 byte)"

  information_field_struct:
    seq:
      - id: packet_type
        type: u1
        doc: "Packet Type (1 byte)"

      - id: telemetry_data_1
        type: telemetry_data_struct_1
        doc: "Telemetry Data (Type 1)"
        if: packet_type == 1

      - id: telemetry_data_2
        type: telemetry_data_struct_2
        doc: "Telemetry Data (Type 2)"
        if: packet_type == 2

      - id: image_data_0
        type: image_data_struct_0
        doc: "Image Data (Type 0)"
        if: packet_type == 0

  telemetry_data_struct_1:
    seq:
      - id: sensor1
        type: f4
        doc: "CURRENT SENSOR_1 - Measures current (CURRENT)"

      - id: sensor2
        type: f4
        doc: "CURRENT SENSOR_2 - Measures current (CURRENT)"

      - id: sensor3
        type: f4
        doc: "CURRENT SENSOR_3 - Measures current (CURRENT)"

      - id: sensor4
        type: f4
        doc: "CURRENT SENSOR_4 - Measures current (CURRENT)"

      - id: battery_voltage
        type: f4
        doc: "BATTERY VOLT. FUEL GUAGE 1 - Battery voltage (CURRENT)"

      - id: battery_temperature
        type: f4
        doc: "BATTERY TEMP. FUEL GUAGE 1 - Temperature (CELSIUS)"

      - id: battery_soc
        type: f4
        doc: "BATTERY STATE OF CHARGE - SOC alarm level (percentage)"

      - id: battery_current
        type: f4
        doc: "BAT. CURRENT FUEL GUAGE 1 - Battery current (CURRENT)"

      - id: temp_in
        type: u1
        doc: "TEMP_IN - Temperature inside"

      - id: temp_out
        type: u1
        doc: "TEMP_OUT - Temperature outside"

      - id: temp_3
        type: u1
        doc: "TEMP_3 - Temperature data 2 LSB"

      - id: pl_temp
        type: u1
        doc: "PL_TEMP - Temperature payload"

      - id: rtc
        type: u8
        doc: "RTC - Seconds since Epoch time"

      - id: temp_out_l
        type: u1
        doc: "TEMP_OUT_L - Temperature data LSB"

      - id: temp_out_h
        type: u1
        doc: "TEMP_OUT_H - Temperature data MSB"

      - id: acceleration_x
        type: f4
        doc: "A_X - acceleration along X axis (m/s^2)"

      - id: acceleration_y
        type: f4
        doc: "A_Y - acceleration along Y axis (m/s^2)"

      - id: acceleration_z
        type: f4
        doc: "A_Z - acceleration along Z axis (m/s^2)"

      - id: magnetic_field_x
        type: f4
        doc: "MF_X - Magnetic field strength - X axis (uT)"

      - id: magnetic_field_y
        type: f4
        doc: "MF_Y - Magnetic field strength - Y axis (uT)"

      - id: magnetic_field_z
        type: f4
        doc: "MF_Z - Magnetic field strength - Z axis (uT)"

      - id: angular_rate_x
        type: f4
        doc: "AR_X - Angular rate along X-axis (dps)"

      - id: angular_rate_y
        type: f4
        doc: "AR_Y - Angular rate along Y-axis (dps)"

      - id: angular_rate_z
        type: f4
        doc: "AR_Z - Angular rate along Z-axis (dps)"

      - id: velocity
        type: f4
        doc: "VELOCITY - Velocity"

      - id: latitude
        type: f4
        doc: "LATITUDE - Latitude"

      - id: longitude
        type: f4
        doc: "LONGITUDE - Longitude"

  telemetry_data_struct_2:
    seq:
      - id: gps_time
        type: u8
        doc: "TIME - GPS Time"

      - id: solar_deployment_status
        type: b1
        doc: "SOLAR DEPLOYMENT STATUS - Binary"

      - id: eps_health_status
        type: b1
        doc: "EPS HEALTH STATUS - Binary"

      - id: adcs_health_status
        type: b1
        doc: "ADCS HEALTH STATUS - Binary"

      - id: payload_health_status
        type: b1
        doc: "PAYLOAD HEALTH STATUS - Binary"

      - id: com_health_status
        type: b1
        doc: "COM HEALTH STATUS - Binary"

      - id: battery1_health_status
        type: b1
        doc: "BATTERY 1 HEALTH STATUS - Binary"

      - id: battery2_health_status
        type: b1
        doc: "BATTERY 2 HEALTH STATUS - Binary"

  image_data_struct_0:
    seq:
      - id: image_id
        type: u1
        doc: "Image ID (1 byte)"

      - id: payload_data
        type: b93
        doc: "Image Payload Data (93 bytes)"
