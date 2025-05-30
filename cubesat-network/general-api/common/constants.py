import subprocess

# initialize script directory constant
script_dir = str(subprocess.check_output(["pwd"])).replace("b'", "").replace("n'", "")[:-1]
base_url = "https://api.woodsoncubesat.org"
# Expiration time for telemetry download files in seconds
expiration_time = 24*60*60
# Parameters for Gunicorn
WORKERS = 2
THREADS = 4
BIND = '0.0.0.0:5500'
SELENIUM_REMOTE_URL = "http://selenium:4444/wd/hub"  # Connect to Selenium inside Docker


# Hardcoded dictionary of decoders for each NORAD ID, these Kaitai Struct files have been sourced from satnogs decoders
NORAD_DECODERS = {
    44352: "Armadillo",      # armadillo.ksy
    51025: "Grizu263a",      # grizu263a.ksy
    55098: "Bdsat2",         # bdsat2.ksy
    47984: "Co65",           # co65.ksy
    61502: "Dora",           # dora.ksy
    47964: "Grbalpha",       # grbalpha.ksy
    49069: "LedSat",         # ledsat.ksy
    52017: "Oresat0",        # oresat0.ksy
    52898: "Randev",         # randev.ksy
    39090: "Strand",         # strand.ksy
    39429: "Aausat4",        # aausat4.ksy
    35933: "Beesat",         # beesat.ksy
    45059: "Connectat11",    # connectat11.ksy
    44878: "Duchifat3",      # duchifat3.ksy
    47965: "Grbbeta",        # grbbeta.ksy
    47980: "Lightsail2",     # lightsail2.ksy
    60525: "Oresat05",      # oresat0_5.ksy
    51030: "Rhoksat",        # rhoksat.ksy
    57167: "Stratosattk1",   # stratosattk1.ksy
    44397: "Acrux1",         # acrux1.ksy
    39136: "Beesat2",        # beesat2.ksy
    49327: "Cosmogirlsat",   # cosmogirlsat.ksy
    47970: "Eirsat1",        # eirsat1.ksy
    47966: "Greencube",      # greencube.ksy
    47981: "Lucky7",         # lucky7.ksy
    43933: "Origamisat1",    # origamisat1.ksy
    56212: "Roseycubesat1",  # roseycubesat1.ksy
    52192: "Suchai2",        # suchai2.ksy
    47952: "Aepex",          # aepex.ksy
    43725: "Bisonsat",       # bisonsat.ksy
    40968: "Crocube",        # crocube.ksy
    47967: "Gt1",            # gt1.ksy
    47982: "Meznsat",        # meznsat.ksy
    44365: "Painani",        # painani.ksy
    10516: "Sakura",         # sakura.ksy
    51440: "Targit",         # targit.ksy
    41790: "Alsat1n",        # alsat1n.ksy
    46829: "Bobcat1",        # bobcat1.ksy
    43715: "Csim",           # csim.ksy
    47968: "Hadesd",         # hadesd.ksy
    47983: "Minxss",         # minxss.ksy
    51048: "Pegasus",        # pegasus.ksy
    51049: "Salsat",         # salsat.ksy
    48900: "Tubin",          # tubin.ksy
    46287: "Amicalsat",      # amicalsat.ksy
    43777: "Bugsat1",        # bugsat1.ksy
    47309: "Cspheader",      # cspheader.ksy
    58470: "Enso",           # enso.ksy
    47969: "Inspiresat1",    # inspiresat1.ksy
    47985: "Mirsat1",        # mirsat1.ksy
    43132: "Picsat",         # picsat.ksy
    51043: "Sanosat1",       # sanosat1.ksy
    51044: "Us6",            # us6.ksy
    39676: "Cape1",          # cape1.ksy
    53255: "Ctim",           # ctim.ksy
    43780: "Entrysat",       # entrysat.ksy
    51045: "Io86",           # io86.ksy
    47986: "Mitee1",         # mitee1.ksy
    51046: "Planetum1",      # planetum1.ksy
    51047: "Selfiesat",      # selfiesat.ksy
    42706: "Uwe4",           # uwe4.ksy
    43687: "Cas4",           # cas4.ksy
    43873: "Cas5a",          # cas5a.ksy
    48267: "Casaasat",       # casaasat.ksy
    49263: "Cute",           # cute.ksy
    48275: "Chomptt",        # chomptt.ksy
    48044: "Catsat",         # catsat.ksy
    51051: "Veronika",       # veronika.ksy
    43714: "Cubebel1",       # cubebel1.ksy
    43552: "Cubebel2",       # cubebel2.ksy
    53106: "Cubesatsim",     # cubesatsim.ksy
    44881: "Estcube2",       # estcube2.ksy
    25544: "Iss",            # iss.ksy
    47972: "Irazu",          # irazu.ksy
    47973: "Irvine01",       # irvine.ksy
    47988: "Mysat1",         # mysat.ksy
    47989: "Netsat",         # netsat.ksy
    51052: "Qarman",         # qarman.ksy
    41789: "Skcube",         # skcube.ksy
    51053: "Siriussat",      # siriussat.ksy
    51054: "Vzlusat2",       # vzlusat2.ksy
    51055: "Yomogi",         # yomogi.ksy
    51056: "Snet",           # snet.ksy
    48044: "Catsat",          # catsat.ksy
    47867: "Delfin3xt",       # delfin3xt.ksy
    40909: "Fox",             # fox.ksy
    47975: "Kashiwa",         # kashiwa.ksy
    46923: "Neutron1",        # neutron1.ksy
    60476: "Qube",            # qube.ksy
    46920: "Spoc",            # spoc.ksy
    46289: "Azaadisat2",      # azaadisat2.ksy
    44832: "Celesta",         # celesta.ksy
    48276: "Delfipq",         # delfipq.ksy
    47961: "Gaspacs",         # gaspacs.ksy
    47976: "Kosen1",          # kosen1.ksy
    27607: "No44",            # no44.ksy
    51054: "Qubik",           # qubik.ksy
    51055: "Sputnixusp",      # sputnixusp.ksy
    48275: "Chomptt",         # chomptt.ksy
    46120: "Dhabisat",        # dhabisat.ksy
    47962: "Geoscan",         # geoscan.ksy
    47977: "Ksu",             # ksu.ksy
    51057: "Nutsat1",         # nutsat1.ksy
    51058: "Quetzal1",        # quetzal1.ksy
    51059: "Sr0",             # sr0.ksy
    48274: "Bdsat",           # bdsat.ksy
    48078: "Cirbe",           # cirbe.ksy
    46921: "Diy1",            # diy1.ksy
    47963: "Geoscanedelveis", # geoscanedelveis.ksy
    47978: "Lasarsat",        # lasarsat.ksy
    45126: "Opssat1",         # opssat1.ksy
    51060: "Ramsat",          # ramsat.ksy
    51061: "Ssamusat"       # ssamusat.ksy
}