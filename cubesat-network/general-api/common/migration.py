import sqlite3
import getpass
#from common.constants import script_dir
from secrets import token_hex
import subprocess
script_dir = str(subprocess.check_output(["pwd"])).replace("b'", "").replace("n'", "")[:-1]


class Sql:
    db_folder = "data"
    db_name = "data"
    db_path = f"{script_dir}/common/{db_folder}/{db_name}.db"

    table = ""

    def __init__(self):
        self.conn = sqlite3.connect(Sql.db_path)
        self.cursor = self.conn.cursor()

    def createDB(self):
        # num_gs = int(input("How many ground stations would you like to add? "))
        # lats = []
        # lngs = []
        # alts = []
        # transmit = []
        # is_satnogs = []
        # for i in range(num_gs):
        #     lats.append(float(getpass.getpass("Enter the decimal latitude for the ground station's location: ")))
        #     lngs.append(float(getpass.getpass("Enter the decimal longitude for the ground station's location: ")))
        #     lngs.append(float(getpass.getpass("Enter the decimal elevation in meters of the ground station: ")))
        #     can_transmit = getpass.getpass("Can this ground station transmit? (y/n) ").lower()
        #     if can_transmit == "y":
        #         transmit.append(1)
        #     else:
        #         transmit.append(0)
        #     satnogs_compatible = getpass.getpass("Will this ground station be used with the SatNogs network? (y/n) ").lower()
        #     if satnogs_compatible == "y":
        #         is_satnogs.append(1)
        #     else:
        #         is_satnogs.append(0)
        self.cursor.executescript(
            """
            DROP TABLE IF EXISTS telemtry;

            CREATE TABLE IF NOT EXISTS telemetry (
                satellite integer,
                timestamp integer,
                frame blob,
                station string
                );

            DROP TABLE IF EXISTS satellites;
            
            CREATE TABLE IF NOT EXISTS satellites (
                norad_id integer,
                name string,
                description string,
                launch_date string,
                deployment_date string,
                countries string,
                in_orbit int
                );

            CREATE TABLE IF NOT EXISTS groundstations (
                station_id str,
                name str,
                lat real,
                lng real,
                alt real,
                transmit int,
                satnogs int
            );

            CREATE TABLE IF NOT EXISTS keys (
                key_id str,
                satnogs_key str,
                n2yo_key str
            )
        """
        )

        # for i in range(num_gs):
        #     self.cursor.execute(  # fix later
        #         f"""
        #         INSERT INTO groundstations (station_id, lat, lng, alt, transmit, satnogs) VALUES ({token_hex(4)}, {lats[i]}, {lngs[i]}, {alts[i]} {can_transmit[i]}, {satnogs_compatible[i]})
        #         """)

        self.conn.commit()
        self.conn.close()

    def migrate(self):
        self.createDB()

    # def __del__(self):
    #     self.conn.close()


if __name__ == "__main__":
    Sql().migrate()


