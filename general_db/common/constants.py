import subprocess

# initialize script directory constant
script_dir = str(subprocess.check_output(["pwd"])).replace("b'", "").replace("n'", "")[:-1]
base_url = "http://127.0.0.1:5000"
# Hardcoded dictionary of decoders for each NORAD ID
NORAD_DECODERS = {
    46287: "Amicalsat"
    # Add more mappings as needed
}