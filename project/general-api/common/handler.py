from common.constants import script_dir
from secrets import token_hex
from common.webbot import Webbot
from common.constants import NORAD_DECODERS
from queue import Queue
import time
import sqlite3
import os
import csv
import calendar
import requests
import common.mail as mail
import subprocess
import datetime
import sys
import binascii
import json
import importlib.util
import zipfile



db_folder = "data"
db_name = "data"
utilities_folder = "common"
db_path = f"{script_dir}/{utilities_folder}/{db_folder}/{db_name}.db"



def telemetryToZip(norad_id, telemetry_data):
        # Ensure the telemetry_cache folder exists
        telemetry_cache_dir = f'{script_dir}/common/telemetry_cache'
        if not os.path.exists(telemetry_cache_dir):
            os.makedirs(telemetry_cache_dir)

        # Create a JSON file for the telemetry data
        json_file_name = f"{norad_id}_frames_{int(time.time())}.json"
        json_file_path = f'{telemetry_cache_dir}/{json_file_name}'

        # Save the telemetry data as a JSON file
        with open(json_file_path, 'w') as json_file:
            json.dump(telemetry_data, json_file, indent=4)

        # Now, create a zip file containing the JSON file
        zip_file_name = f"{norad_id}_frames_{int(time.time())}.zip"
        zip_file_path = f'{telemetry_cache_dir}/{zip_file_name}'
        print(zip_file_path)
        # Create a zip file and add the JSON file
        with zipfile.ZipFile(zip_file_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            zipf.write(json_file_path, json_file_name)  # Add the JSON file to the zip

        # Delete the JSON file after creating the zip file
        os.remove(json_file_path)

        # Return the URL to the zip file
        return zip_file_name




# script_dir = str(subprocess.check_output(["pwd"])).replace("b'", "").replace("n'", "")[:-1]

csv.field_size_limit(1000000000000000000)

# todo: add delete satellite, add ground station, delete ground station

def readCSV(norad_id: int):
    """
    Reads the CSV file for the given NORAD ID, extracts the timestamps, frames, and station names,
    and returns them as lists. The file is deleted after processing.

    :param norad_id: The NORAD ID for which the data is stored in a CSV file.
    :return: Three lists: timestamps, frames, and station names, processed from the CSV file.
    """
    timestamps_raw = []
    frames_raw = []
    stations_raw = []  # To store the station names
    timestamps = []
    frames = []
    stations = []  # Final list for station names

    # Construct file path
    file_path = f"{script_dir}/common/csv_cache/{norad_id}_data.csv"

    try:
        # Open the CSV file for reading
        with open(file_path, mode="r") as file:
            print("Successfully opened the file")
            csvFile = csv.reader(file)

            # Read each line in the CSV
            for line in csvFile:
                # Split line by pipe (|) separator
                str_line = line[0]
                split_line = str_line.split("|")

                # Extract the timestamp, frame, and station name
                try:
                    timestamp = str(calendar.timegm(time.strptime(split_line[0], "%Y-%m-%d %H:%M:%S")))
                    # Check if station value exists
                    station = split_line[3] if len(split_line) > 3 and split_line[3] else None
                    #print(station)
                except ValueError:
                    print(f"Invalid timestamp or data format in line: {str_line}")
                    continue  # Skip lines with invalid timestamps or data

                # Append parsed data
                timestamps_raw.append(timestamp)
                frames_raw.append(split_line[1])
                stations_raw.append(station)  # Add station name to the raw list

            # Delete the CSV file after processing
            os.remove(file_path)
            
            # Process the raw data into final lists
            for i in range(len(frames_raw)):
                frames.append(frames_raw[i])
                timestamps.append(timestamps_raw[i])
                stations.append(stations_raw[i])  # Add station name to the final list

            # Reverse lists to go from the most recent to the earliest
            timestamps.reverse()
            frames.reverse()
            stations.reverse()  # Reverse the station list as well

        print(f"Processed {len(timestamps_raw)} timestamps, {len(frames_raw)} frames, and {len(stations_raw)} stations.")

        print(f"File {file_path} deleted after processing.")

    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
        return [], [], []  # Return empty lists in case of error
    except Exception as e:
        print(f"An error occurred: {e}")
        return [], [], []  # Return empty lists in case of error
    print(frames[146], timestamps[146], stations[146]) 

    return timestamps, frames, stations  # Return all three lists


def setupCronJob(norad_id, key_id, update_duration=7, offset=7):
        
        script_path = f"{script_dir}/common/update_frames.py"

        """
        Configures a cron job to run the given script one week from now and repeat weekly.
        
        Args:
            script_path (str): Full path to the Python script to execute.
            norad_id (int): NORAD ID of the satellite.
            update_duration (int): The span of days to fetch frames. Defaults to 7.
            offset (int): The date offset used to calculate timestamps. Defaults to 7.
            key_id (str): Key ID for SatNOGS access.
        """
        if not os.path.isfile(script_path):
            raise FileNotFoundError(f"The script '{script_path}' does not exist.")

        # Get the Python executable path for the current version
        python_path = sys.executable

        # Calculate start time one week from now
        start_time = datetime.datetime.now() + datetime.timedelta(weeks=1)
        minute = start_time.minute
        hour = start_time.hour
        day_of_week = start_time.weekday()  # Monday = 0, Sunday = 6

        # Build the script command with named arguments
        script_command = (
            f"{python_path} {script_path} --norad_id={norad_id} "
            f"--update_duration={update_duration} --offset={offset} --key_id={key_id}"
        )

        # Generate the cron command
        cron_command = f"{minute} {hour} * * {day_of_week} {script_command}"

        try:
            # Get existing crontab
            result = subprocess.run(["crontab", "-l"], capture_output=True, text=True, check=True)
            current_crontab = result.stdout.strip()
        except subprocess.CalledProcessError:
            # If crontab is empty or doesn't exist, initialize an empty one
            current_crontab = ""

        # Check if the cron job already exists
        if cron_command in current_crontab:
            print("Cron job already exists. No changes made.")
            return

        # Append the new cron job
        new_crontab = current_crontab + f"\n{cron_command}\n" if current_crontab else f"{cron_command}\n"

        try:
            # Write the updated crontab
            subprocess.run(["crontab", "-"], input=new_crontab, text=True, check=True)
            print(f"Cron job added: {cron_command}")
        except subprocess.CalledProcessError as e:
            print("Failed to update crontab:", e)
            raise RuntimeError("Failed to update the crontab.") from e
        
def deleteCronJob(norad_id):
    """
    Deletes the cron job associated with the given NORAD ID.

    Args:
        norad_id (int): NORAD ID of the satellite.
        script_dir (str): Directory where the script is located.
    """
    script_path = f"{script_dir}/common/update_frames.py"
    python_path = sys.executable

    # Construct the command part to identify the cron job
    script_command = f"{python_path} {script_path} --norad_id={norad_id}"

    try:
        # Get the current crontab
        result = subprocess.run(["crontab", "-l"], capture_output=True, text=True, check=True)
        current_crontab = result.stdout.strip()
    except subprocess.CalledProcessError:
        print("No existing crontab found.")
        return

    # Split the crontab into individual lines
    cron_lines = current_crontab.split("\n")

    # Filter out lines containing the specific script command
    updated_cron_lines = [line for line in cron_lines if script_command not in line]

    # Check if any lines were removed
    if len(cron_lines) == len(updated_cron_lines):
        print(f"No cron job found for NORAD ID {norad_id}.")
        return

    # Join the remaining lines and update the crontab
    new_crontab = "\n".join(updated_cron_lines)

    try:
        subprocess.run(["crontab", "-"], input=new_crontab, text=True, check=True)
        print(f"Cron job for NORAD ID {norad_id} has been deleted.")
    except subprocess.CalledProcessError as e:
        print("Failed to update crontab:", e)
        raise RuntimeError("Failed to update the crontab.") from e
# def compileDecoder()
        
def loadDecoder(norad_id):
    try:
        # Check if the NORAD ID exists in the dictionary
        print(NORAD_DECODERS)
        print(NORAD_DECODERS[46287])
        
        if norad_id not in NORAD_DECODERS:
            raise ValueError(f"No decoder found for NORAD ID: {norad_id}")

        # Get the decoder module name from the dictionary
        decoder_module_name = NORAD_DECODERS[norad_id]

        # Create the file path based on the module name (e.g., "Amicalsat" -> "amicalsat.py")
        file_name = f"{decoder_module_name[0].lower()}{decoder_module_name[1:]}.py"  # Lowercase the first letter of the module name
        module_name = decoder_module_name  # This will be used for the import

        # Assuming all decoder files are in a 'decoders' directory
        decoder_file_path = f"{script_dir}/common/decoders/{file_name}"
        print(decoder_file_path)

        # Check if the decoder file exists
        if not os.path.exists(decoder_file_path):
            raise FileNotFoundError(f"Decoder file '{file_name}' not found for NORAD ID: {norad_id}")

        # Dynamically import the module
        spec = importlib.util.spec_from_file_location(module_name, decoder_file_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        # Access the class from the module
        decoder_class = getattr(module, decoder_module_name)

        # Return the loaded class
        return False, decoder_class, ""

    except (ModuleNotFoundError, FileNotFoundError) as e:
        return True, f"Error loading module for NORAD ID {norad_id}: {str(e)}", ""
    except Exception as e:
        print(f"Error: {e}")
        return True, f"An error occured: {e}",""

def kaitaiToDict(obj):
    try:
        """Recursively converts a Kaitai Struct object to a Python dictionary."""
        if hasattr(obj, "__dict__"):
            result = {}
            for key, value in obj.__dict__.items():
                if not key.startswith('_'):
                    if hasattr(value, 'switch_on_field') and hasattr(value, 'cases'):
                        switch_value = getattr(value, 'switch_on_field')
                        for case_value, case_type in value.cases.items():
                            if switch_value == case_value:
                                result[key] = kaitaiToDict(getattr(value, case_type))
                                break
                    elif isinstance(value, list):
                        result[key] = [kaitaiToDict(item) for item in value]
                    elif hasattr(value, 'bitfield_field'):
                        bitfield = getattr(value, 'bitfield_field')
                        result[key] = ''.join(f'{bitfield:08b}')
                    elif hasattr(value, 'ror_field'):
                        ror_value = getattr(value, 'ror_field')
                        result[key] = (ror_value >> 1) | ((ror_value & 1) << 7)
                    else:
                        result[key] = kaitaiToDict(value)
        elif isinstance(obj, bytes):
            result = binascii.hexlify(obj).decode("utf-8")
        elif isinstance(obj, (int, str)):
            result = obj
        else:
            result = str(obj)
        
        return result 
    except Exception as e:
        return {"message": f"Error converting Kaitai object: {e}"}
    
def parseFrame(norad_id, telemetry, decode_frames: bool = False):
    if decode_frames:
        error, DecoderClass, message = loadDecoder(norad_id)
        if error:
            return True, message
        
    for i in range(len(telemetry)):
            if not decode_frames:
                del telemetry[i]["decoded_frame"]
            if decode_frames:
                print(i)
                hex_frame=telemetry[i]["raw_frame"]
                # Convert hex string to binary
                binary_frame = binascii.unhexlify(hex_frame)
                # Decode the frame data
                try:
                    kaitai_obj = DecoderClass.from_bytes(binary_frame)
                except:
                    telemetry[i]["decoded_frame"] = {"message": "Frame could not be parsed."}

                telemetry[i]["decoded_frame"] = kaitaiToDict(kaitai_obj)
    return False, telemetry


# Connection Pool for thread-safe database access
class ConnectionPool:
    def __init__(self, db_path, pool_size=10):
        self.db_path = db_path
        self.pool = Queue(maxsize=pool_size)
        for _ in range(pool_size):
            conn = sqlite3.connect(self.db_path, check_same_thread=False)
            conn.execute("PRAGMA journal_mode=WAL;")
            conn.execute("PRAGMA busy_timeout=5000;")
            self.pool.put(conn)

    def get_connection(self, timeout=5):
        try:
            print("Attempting to get connection from pool with timeout")
            conn = self.pool.get(timeout=timeout)
            print(f"Connection acquired: {conn}")
            return conn
        except Exception as e:
            print(f"Error getting connection: {e}")
            raise

    def release_connection(self, conn):
        print(f"Releasing connection: {conn}")
        try:
            if self.pool.full():
                print("Connection pool is full, discarding connection.")
                conn.close()  # Discard the connection
                return
            self.pool.put(conn, timeout=2)  # Use timeout to detect blocking
            print(f"Connection released back to pool: {conn}")
        except Exception as e:
            print(f"Error releasing connection: {e}")

    def close_all(self):
        print("Closing all connections in the pool")
        while not self.pool.empty():
            conn = self.pool.get()
            try:
                conn.close()
                print(f"Connection closed: {conn}")
            except Exception as e:
                print(f"Error closing connection: {e}")



# Global connection pool
connection_pool = ConnectionPool(db_path, pool_size=10)





class Sql:

    def __init__(self):
        # Fetch a connection from the pool
        self.conn = connection_pool.get_connection()
        self.cursor = self.conn.cursor()

    def __del__(self):
        # Release the connection back to the pool
        if self.conn:
            connection_pool.release_connection(self.conn)

    def satelliteExists(self, norad_id):
        """Check if the satellite exists in the database."""
        self.cursor.execute("SELECT 1 FROM satellites WHERE norad_id = ?", (norad_id,))
        result = self.cursor.fetchone()  # Get the first result

        if result is None:
            print(f"Satellite {norad_id} does NOT exist.")
            return False  # Satellite not found

        print(f"Satellite {norad_id} exists.")
        return True  # Satellite found


    table = ""


    def getTelemetry(self, norad_id: int = None, start_time: int = None, end_time: int = None, station: str = None, return_metadata: bool = False):
        telemetry = []
        query = "SELECT * FROM telemetry WHERE 1=1"  # Base query
        params = []

        try:
            # Add conditions to the query based on the provided parameters
            if norad_id is not None:
                query += " AND satellite = ?"
                params.append(norad_id)
        
            if station is not None:
                query += " AND station = ?"
                params.append(station)
        
            if start_time is not None:
                query += " AND timestamp >= ?"
                params.append(start_time)
        
            if end_time is not None:
                query += " AND timestamp <= ?"
                params.append(end_time)

            # Execute the query with the collected parameters
            self.cursor.execute(query, params)
            data = self.cursor.fetchall()

            # Process the data based on return_metadata flag
            for row in data:
                timestamp = int(row[1])  # Assuming the timestamp is in the second column
                if return_metadata:
                    # order: norad_id, timestamp, frames, station
                    telemetry.append({'norad_id': row[0], 'timestamp': timestamp, 'raw_frame': row[2], 'station': row[3], 'decoded_frame': None})  # Append all metadata
                else:
                    telemetry.append({'timestamp': timestamp, 'raw_frame': row[2], 'decoded_frame': None})  # Append limited data

            # Handle no errors found
            if telemetry:
                # Sort telemetry by timestamp (index 1 for metadata, index 0 otherwise)
                #telemetry.sort(key=operator.itemgetter(1) if return_metadata else operator.itemgetter(0))
                telemetry.sort(key=lambda x: x['timestamp'])

                # Convert timestamps to human-readable format
                for i in range(len(telemetry)):
                    # if return_metadata:
                    telemetry[i]["timestamp"] = datetime.datetime.utcfromtimestamp(telemetry[i]["timestamp"]).strftime("%Y-%m-%d %H:%M:%S")
                    # else:
                    #     telemetry[i][0] = datetime.datetime.utcfromtimestamp(telemetry[i][0]).strftime("%Y-%m-%d %H:%M:%S")
            
            print(telemetry)
            return False, "Successfully retrived telemetry",  telemetry

        except Exception as e:
            print(f"Error: {e}")
            return True, f"An error occured: {e}", {}
        finally:
            if self.conn:
                connection_pool.release_connection(self.conn)
    def getSatInfo(
        self,
        # filters for query
        norad_id: int = None,
        name: str = None,
        country: str = None,
        # filters for returning information
        return_all: bool = True,
        return_launchinfo: bool = False,
        return_name: bool = False,
        return_id: bool = False,
        return_description: bool = False,
    ):
        try:
            # Base query and parameters for filtering
            query = "SELECT * FROM satellites WHERE 1=1"
            params = []

            # Add filters
            if norad_id is not None:
                query += " AND norad_id = ?"
                params.append(norad_id)
            if name is not None:
                query += " AND name = ?"
                params.append(name)
            if country is not None:
                query += " AND countries LIKE ?"
                params.append(f"%{country}%")

            # Execute query
            self.cursor.execute(query, params)
            rows = self.cursor.fetchall()

            # Get column names dynamically
            column_names = [desc[0] for desc in self.cursor.description]
            column_mapping = {i: column for i, column in enumerate(column_names)}

            # Build the result
            info = {'data': []}

            if return_all:
                # Map all columns
                for row in rows:
                    info['data'].append(
                        {column_mapping[i]: row[i] for i in range(len(row))}
                    )
            else:
                # Select specific columns
                selected_columns = []
                if return_launchinfo:
                    selected_columns.extend([3, 4])  # launch_date and deployment_date indices
                if return_name:
                    selected_columns.append(1)  # name index
                if return_id:
                    selected_columns.append(0)  # norad_id index
                if return_description:
                    selected_columns.append(2)  # description index

                for row in rows:
                    filtered_row = {column_mapping[col]: row[col] for col in selected_columns}
                    info['data'].append(filtered_row)

            # Return success response
            return False, "Query executed successfully.", info

        except Exception as e:
            # Return error response
            return True, f"An error occurred: {e}", {}

        finally:
            if self.conn:
                connection_pool.release_connection(self.conn)
    def listGroundStations(
        self
        ):
        error_message = ""
        info = {
            'number_of_stations': 0,
            'stations': []
        }

        try:



            # Query the groundstations table
            self.cursor.execute(
                "SELECT station_id, name, lat, lng, alt, transmit, satnogs FROM groundstations"
            )
            data = self.cursor.fetchall()

            if data:
                print(f"\n\n{data}")
                station_counter = 0
                stations = []
                for row in data:
                    # Build a dictionary for each ground station
                    station = {
                        'station_id': row[0],
                        'name': row[1],
                        'latitude': row[2],
                        'longitude': row[3],
                        'altitude': row[4],
                        'can_transmit': bool(row[5]),
                        'is_satnogs': bool(row[6]),
                    }
                    stations.append(station)
                    station_counter += 1
                info['stations'] = stations
                info['number_of_stations'] = station_counter

            else:
                return True, "No ground stations found in the database.", info

        except Exception as e:
            error_message = f"An error occurred: {e}"
            return True, error_message, info

        finally:
            if self.conn:
                connection_pool.release_connection(self.conn)        
        return False, error_message, info


    def appendTelemetry(self, norad_id: int, timestamps: list, frames: list, stations: list = None):
        try:
            # If stations is not provided, create a list with None for each timestamp
            if stations is None:
                stations = [None] * len(timestamps)

            #print(stations)
            updated_list = []
        
            # Prepare a list of tuples for the insert operation (to do it in bulk later)
            insert_data = [
                (int(norad_id), int(timestamps[i]), frames[i], str(stations[i]))
                for i in range(len(frames))
            ]
        
            # Use a bulk insert to reduce the number of commits
            self.cursor.executemany(
                """INSERT INTO telemetry (satellite, timestamp, frame, station) VALUES (?, ?, ?, ?)""",
                insert_data
            )
            # Commit the transaction after all the insertions
            self.conn.commit()
        
            # Store the updated list for logging or further use
            updated_list.extend(insert_data)
        
            print("Bulk insert complete.")

            # time taken will be processed in general.py
            return False, "Success.", {'time_taken': time.time(), 'frame_count': len(frames)}

        except Exception as e:
            return True, f"An error occurred: {e}", {}
    
        finally:
            # Close the connection if it exists
            if self.conn:
                self.conn.close()
    
    def appendKeys(self, key_id, n2yo_key, satnogs_key):
        try:
            self.cursor.execute(
                """INSERT INTO keys (key_id, satnogs_key, n2yo_key) VALUES (?, ?, ?)""",
                (key_id, n2yo_key, satnogs_key),
            )
            print(key_id, n2yo_key, satnogs_key)
            self.conn.commit()

            return False, f"Successfully added keys for ID {key_id}."

        except Exception as e:
            print(f"Error: {e}")
            return True, f"An error occured: {e}"
        finally:
            if self.conn:
                connection_pool.release_connection(self.conn)
    def addSatellite(
        self, norad_id: int, name: str, description: str = None, launch_date: str = None, deployment_date: str = None, countries: str = None
    ):
        try: 
            # get rid of spaces
            self.cursor.execute(
                """INSERT INTO satellites (norad_id, name, description, launch_date, deployment_date, countries, in_orbit) VALUES (?, ?, ?, ?, ?, ?, 1)""",
                (norad_id, name, description, launch_date, deployment_date, countries),
            )
            print(norad_id, name, description, launch_date, deployment_date, countries)
            self.conn.commit()

            return False, "Successfully added satellite information to database."
        except Exception as e:
            print(f"Error: {e}")
            return True, f"An error occured: {e}"
        finally:
            if self.conn:
                connection_pool.release_connection(self.conn)
    def notInOrbit(self, norad_id: int):
        self.cursor.execute(f"""UPDATE satellites SET in_orbit=0 WHERE norad_id={norad_id}""")
        #add stuff to remove update command from cron file later

    # helper function for addSatellite()
    def buildTelemetry(self, norad_id: str, satnogs_cookies: str, email: str, email_passwd: str):
        print(norad_id)
        if Sql().satelliteExists(norad_id):
            return True, "The satellite already exists in the database.", {}
        try:
            try:
                mail.markEmailsAsRead(email=email, passwd=email_passwd)
            except:
                return True, "Your email credentials are invalid. Please update them.", {}
            webbot = Webbot()
            print("clicking link\n")
            try:
                webbot.clicker(norad_id, satnogs_cookies)
                time.sleep(20)
            except:
                return True, "Your Satnogs cookies have expired. Please renew them and try again.", {}
            print("fetching link\n")
            max_trials = 12     
            for attempt in range(max_trials):
                try:
                    link = mail.fetchLinks(email, email_passwd)
                    print("downloading csv\n")
                    mail.download(link, norad_id)
                    # If successful, break out of the loop
                    break
                except Exception as e:
                    print(f"Attempt {attempt + 1} failed: {e}")
                    # If this is the 12th attempt, return the error message
                    if attempt == max_trials - 1:
                        return True, "The satnogs database is not responding. Please try again later.", {}
            print("reading csv\n")
            timestamps, frames, stations = readCSV(norad_id)
            print(timestamps)
            print("done reading\n")
            print("appending to sql db\n")
            error, message, info = Sql().appendTelemetry(norad_id=norad_id, timestamps=timestamps, frames=frames, stations=stations)
            print("finished")
        except Exception as e:
            print(f"Error: {e}")
            return True, f"An error occured: {e}", {}
        if not error:
            message = "Successfully added satellite telemetry."
        return error, message, info

    # helper function for pass scheduler function, check notebook for details
    # Not finished
    # this data will not leave the general db container/server, and will not be transmitted over the api
    # therefore, it will not be converted into json
    def getTrackerInfo(self, station_id: str = None):
        if station_id == None:
            station_id = "*"
        self.cursor.execute(f"""select lat, lng, alt from groundstations where station_id=?""", (station_id,))
        data = self.cursor.fetchall()
        for row in data:
            info = [data[0][0], data[0][1], data[0][2]]
    
    # this data will not leave the general db container/server, and will not be transmitted over the api
    # therefore, it will not be converted into json
    # helper function for update_frames, and pass scheduler function (not started yet)
    def getKey(self, key_id: str, satnogs_key: bool = False, n2yo_key: bool = False):
        try:
            if satnogs_key:
                self.cursor.execute(f"""select satnogs_key from keys where key_id=?""", (key_id,))
                data = self.cursor.fetchall()
                info = data[0][0]
            if n2yo_key:
                self.cursor.execute(f"""select n2yo_key from keys where key_id=?""", (key_id,))
                data = self.cursor.fetchall()
                info = data[0][0]
            return info
        except Exception as e:
            print(f"Error: {e}") # Change this to use log file
        finally:
            if self.conn:
                connection_pool.release_connection(self.conn)
    def addGroundstation(
                self,
                name: str,
                lat: float,
                lng: float,
                alt: float,
                transmit: bool,
                satnogs: bool
        ):
            try:

                self.cursor.execute(
                    """INSERT INTO groundstations (station_id, name, lat, lng, alt, transmit, satnogs) VALUES (?, ?, ?, ?, ?, ?, ?)""",
                    (token_hex(4), name, lat, lng, alt, int(transmit), int(satnogs)),
                )
                self.conn.commit()
                return False, "Successfully added groundstation."
            except Exception as e:
                print(f"Error: {e}")
                return True, f"An error occured: {e}"
        
        

    # def buildSatInfoTest(self, norad_id: int, satnogs_key):
    #     decoders = [None]
    #     deframers = [None]
    #     url = f"https://db-dev.satnogs.org/api/satellites/?norad_cat_id={norad_id}"
    #     response = requests.get(url=url, headers={"Authorization": f"Token{satnogs_key}"})
    #     data = response.json()[0]
    #     description = f"User Entry: {input('Enter a description for the satellite: ')} \n\n Website: {data['website']}"
    #     if data["launched"] == None:
    #         if input("Do you want to manually enter a launch date? (y/n) ").strip().lower() == "y":
    #             launch_date = input("Enter a launch date (YYYY-MM-DDTHH:MM:SSZ): ")
    #         else:
    #             launch_date = None
    #     else:
    #         launch_date = data["launched"]
    #     if data["deployed"] == None:
    #         if input("Do you want to manually enter a deployment date? (y/n) ").strip().lower() == "y":
    #             deployment_date = input("Enter a deployment date (YYYY-MM-DDTHH:MM:SSZ): ")
    #         else:
    #             deployment_date = None
    #     else:
    #         deployment_date = data["deployed"]
    #     done = True
    #     while done:
    #         try:
    #             for i in range(len(deframers)):
    #                 print(f"{i+1}: {deframers[i]}")
    #             deframer = deframers[int(input("Choose a deframer: ")) - 1]
    #             done = False
    #         except:
    #             print("Enter the number corresponding to the option you want")
    #     done = True
    #     while done:
    #         try:
    #             for i in range(len(decoders)):
    #                 print(f"{i+1}: {decoders[i]}")
    #             decoder = decoders[int(input("Choose a decoder: ")) - 1]
    #             done = False
    #         except:
    #             print("Enter the number corresponding to the option you want")
        
    #     tracking = input("Would you like Woodson CubeSat ground stations to track this satellite? (y/n) ")
    #     if tracking.lower().strip() == "y":
    #         pass 
    #         #create priority system for satellite tracking 
    #     sql().appendSatellite(
    #         norad_id=norad_id, description=description, launch_date=launch_date, deployment_date=deployment_date, deframer=deframer, decoder=decoder, countries=data["countries"], name=data["name"]
    #     )

    def buildSatInfo(self, satnogs_key, norad_id: int, description: str = None, launch_date: str = None, deployment_date: str = None
        ):
        try:
            url = f"https://db-dev.satnogs.org/api/satellites/?norad_cat_id={norad_id}"
            response = requests.get(url=url, headers={"Authorization": f"Token{satnogs_key}"})

            try:
                data = response.json()[0]
                print("response:",response.json()[0])
            except:
                data = {'countries': None, 'name': None, 'website': None}
            description = f"User Entry: {description} \n\n Website: {data['website']}"
            Sql().addSatellite(
                norad_id=norad_id, description=description, launch_date=launch_date, deployment_date=deployment_date, countries=data["countries"], name=data["name"]
                )
            
            return False, "Successfully added satellite information to database."
        
        except Exception as e:
            print(f"Error: {e}")
            return True, f"An error occured: {e}"
        
    def deleteSatellite(self, norad_id):
        try: 
            # get rid of spaces
            self.cursor.execute(
                """DELETE FROM satellites WHERE norad_id = ? """,
                (norad_id,)
            )
            self.cursor.execute(
                """DELETE FROM telemetry WHERE satellite = ? """,
                (norad_id,)
            )
            print(norad_id)
            self.conn.commit()

            deleteCronJob(norad_id)

            print(f"Successfully deleted satellite {norad_id} and its corresponding telemetry from the database.")
            return False, f"Successfully deleted satellite {norad_id} and its corresponding telemetry from the database."
        except Exception as e:
            print(f"Error: {e}")
            return True, f"An error occured: {e}"
        finally:
            if self.conn:
                connection_pool.release_connection(self.conn)


    def __del__(self):
        self.conn.close()




# anything beyond this point is for testing

# print(timestamps)
# print(frames)

"""
"""
"""
sql().appendTelemetry(
    norad_id=25544,
    timestamps=[1700859867, 1700859868, 1700859869, 1700859870, 1700859871, 1700859872, 1700859873, 1700859874],
    frames=[
        "60A060A0A66C609C8262A6A640E082A0A4A682A86103F02776261C6C201C53495D41524953532D49535320504D323D0D",
        "60A060A0A66C609C8262A6A640E082A0A4A682A86103F02776261C6C201C53495D41524953532D49535320504D323D0D",
        "60A060A0A66C609C8262A6A640E082A0A4A682A86103F02776261C6C201C53495D41524953532D49535320504D323D0D",
        "60A060A0A66C609C8262A6A640E082A0A4A682A86103F02776261C6C201C53495D41524953532D49535320504D323D0D",
        "60A060A0A66C609C8262A6A640E082A0A4A682A86103F02776261C6C201C53495D41524953532D49535320504D323D0D",
        "60A060A0A66C609C8262A6A640E082A0A4A682A86103F02776261C6C201C53495D41524953532D49535320504D323D0D",
        "60A060A0A66C609C8262A6A640E082A0A4A682A86103F02776261C6C201C53495D41524953532D49535320504D323D0D",
        "60A060A0A66C609C8262A6A640E082A0A4A682A86103F02776261C6C201C53495D41524953532D49535320504D323D0D",
    ],
    stations=["plat0-3a-EN61cn", "9V1KG-OJ11xi", "M0EYT / 2E0NOG-IO80xs", "M0EYT / 2E0NOG-IO80xs", "M0EYT / 2E0NOG-IO80xs", "M0EYT / 2E0NOG-IO80xs", "M0EYT / 2E0NOG-IO80xs", "M0EYT / 2E0NOG-IO80xs"],
)

sql().appendSatellite(
    norad_id=25544,
    name="ISS",
    description="The International Space Station is a partnership between the US and Russia. It is made of mutiple modules, and houses astronauts from multiple countries",
    countries="US, Ru",
)
"""


"""
# cursor.get(1693464165, 1693541620)


# cursor.get(1530633289, 1688256077)
# cursor.append("", 96.42)


# conn = sqlite3.connect(f"dbs/{norad_id}.db")
# c = conn.cursor()
"""
