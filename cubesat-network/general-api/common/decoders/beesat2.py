# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 9):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class Beesat2(KaitaiStruct):
    """:field contrl: masterframe.contrl
    :field calsgn: masterframe.calsgn
    :field crcsgn: masterframe.crcsgn
    :field asm: masterframe.transferframe0.asm
    :field raw: masterframe.transferframe0.tfvn.raw
    :field value: masterframe.transferframe0.tfvn.value
    :field scid_raw: masterframe.transferframe0.scid.raw
    :field scid_value: masterframe.transferframe0.scid.value
    :field vcidb_raw: masterframe.transferframe0.vcidb.raw
    :field vcidb_value: masterframe.transferframe0.vcidb.value
    :field ocff: masterframe.transferframe0.ocff
    :field mcfc: masterframe.transferframe0.mcfc
    :field vcfc: masterframe.transferframe0.vcfc
    :field tf_shf: masterframe.transferframe0.tf_shf
    :field synchflag: masterframe.transferframe0.synchflag
    :field pof: masterframe.transferframe0.pof
    :field slid_raw: masterframe.transferframe0.slid.raw
    :field slid_value: masterframe.transferframe0.slid.value
    :field fhp_raw: masterframe.transferframe0.fhp.raw
    :field fhp_value: masterframe.transferframe0.fhp.value
    :field source_pvn_raw: masterframe.transferframe0.source.pvn.raw
    :field source_pvn_value: masterframe.transferframe0.source.pvn.value
    :field pt: masterframe.transferframe0.source.pt
    :field shf: masterframe.transferframe0.source.shf
    :field source_apid_raw: masterframe.transferframe0.source.apid.raw
    :field source_apid_value: masterframe.transferframe0.source.apid.value
    :field source_seqflag_raw: masterframe.transferframe0.source.seqflag.raw
    :field source_seqflag_value: masterframe.transferframe0.source.seqflag.value
    :field source_psc_raw: masterframe.transferframe0.source.psc.raw
    :field source_psc_value: masterframe.transferframe0.source.psc.value
    :field pdl: masterframe.transferframe0.source.pdl
    :field telemetry_cstutc_raw: masterframe.transferframe0.telemetry.cstutc.raw
    :field telemetry_cstutc_value: masterframe.transferframe0.telemetry.cstutc.value
    :field telemetry_csaxp_raw: masterframe.transferframe0.telemetry.csaxp.raw
    :field telemetry_csaxp_value: masterframe.transferframe0.telemetry.csaxp.value
    :field telemetry_csaxn_raw: masterframe.transferframe0.telemetry.csaxn.raw
    :field telemetry_csaxn_value: masterframe.transferframe0.telemetry.csaxn.value
    :field telemetry_csayp_raw: masterframe.transferframe0.telemetry.csayp.raw
    :field telemetry_csayp_value: masterframe.transferframe0.telemetry.csayp.value
    :field telemetry_csayn_raw: masterframe.transferframe0.telemetry.csayn.raw
    :field telemetry_csayn_value: masterframe.transferframe0.telemetry.csayn.value
    :field telemetry_csazp_raw: masterframe.transferframe0.telemetry.csazp.raw
    :field telemetry_csazp_value: masterframe.transferframe0.telemetry.csazp.value
    :field telemetry_csazn_raw: masterframe.transferframe0.telemetry.csazn.raw
    :field telemetry_csazn_value: masterframe.transferframe0.telemetry.csazn.value
    :field telemetry_vsabus_raw: masterframe.transferframe0.telemetry.vsabus.raw
    :field telemetry_vsabus_value: masterframe.transferframe0.telemetry.vsabus.value
    :field telemetry_cc0in_raw: masterframe.transferframe0.telemetry.cc0in.raw
    :field telemetry_cc0in_value: masterframe.transferframe0.telemetry.cc0in.value
    :field telemetry_cc1in_raw: masterframe.transferframe0.telemetry.cc1in.raw
    :field telemetry_cc1in_value: masterframe.transferframe0.telemetry.cc1in.value
    :field telemetry_vbat0_raw: masterframe.transferframe0.telemetry.vbat0.raw
    :field telemetry_vbat0_value: masterframe.transferframe0.telemetry.vbat0.value
    :field telemetry_vbat1_raw: masterframe.transferframe0.telemetry.vbat1.raw
    :field telemetry_vbat1_value: masterframe.transferframe0.telemetry.vbat1.value
    :field telemetry_cc0out_raw: masterframe.transferframe0.telemetry.cc0out.raw
    :field telemetry_cc0out_value: masterframe.transferframe0.telemetry.cc0out.value
    :field telemetry_cc1out_raw: masterframe.transferframe0.telemetry.cc1out.raw
    :field telemetry_cc1out_value: masterframe.transferframe0.telemetry.cc1out.value
    :field telemetry_v50bus_raw: masterframe.transferframe0.telemetry.v50bus.raw
    :field telemetry_v50bus_value: masterframe.transferframe0.telemetry.v50bus.value
    :field telemetry_v33bus_raw: masterframe.transferframe0.telemetry.v33bus.raw
    :field telemetry_v33bus_value: masterframe.transferframe0.telemetry.v33bus.value
    :field telemetry_cpcu_raw: masterframe.transferframe0.telemetry.cpcu.raw
    :field telemetry_cpcu_value: masterframe.transferframe0.telemetry.cpcu.value
    :field telemetry_cobc0_raw: masterframe.transferframe0.telemetry.cobc0.raw
    :field telemetry_cobc0_value: masterframe.transferframe0.telemetry.cobc0.value
    :field telemetry_cobc1_raw: masterframe.transferframe0.telemetry.cobc1.raw
    :field telemetry_cobc1_value: masterframe.transferframe0.telemetry.cobc1.value
    :field telemetry_ctnc0_raw: masterframe.transferframe0.telemetry.ctnc0.raw
    :field telemetry_ctnc0_value: masterframe.transferframe0.telemetry.ctnc0.value
    :field telemetry_ctnc1_raw: masterframe.transferframe0.telemetry.ctnc1.raw
    :field telemetry_ctnc1_value: masterframe.transferframe0.telemetry.ctnc1.value
    :field telemetry_ctrx0_raw: masterframe.transferframe0.telemetry.ctrx0.raw
    :field telemetry_ctrx0_value: masterframe.transferframe0.telemetry.ctrx0.value
    :field telemetry_ctrx1_raw: masterframe.transferframe0.telemetry.ctrx1.raw
    :field telemetry_ctrx1_value: masterframe.transferframe0.telemetry.ctrx1.value
    :field telemetry_cpdh_raw: masterframe.transferframe0.telemetry.cpdh.raw
    :field telemetry_cpdh_value: masterframe.transferframe0.telemetry.cpdh.value
    :field telemetry_ccam_raw: masterframe.transferframe0.telemetry.ccam.raw
    :field telemetry_ccam_value: masterframe.transferframe0.telemetry.ccam.value
    :field telemetry_csss_raw: masterframe.transferframe0.telemetry.csss.raw
    :field telemetry_csss_value: masterframe.transferframe0.telemetry.csss.value
    :field telemetry_cmfs0_raw: masterframe.transferframe0.telemetry.cmfs0.raw
    :field telemetry_cmfs0_value: masterframe.transferframe0.telemetry.cmfs0.value
    :field telemetry_cmfs1_raw: masterframe.transferframe0.telemetry.cmfs1.raw
    :field telemetry_cmfs1_value: masterframe.transferframe0.telemetry.cmfs1.value
    :field telemetry_cgyr0_raw: masterframe.transferframe0.telemetry.cgyr0.raw
    :field telemetry_cgyr0_value: masterframe.transferframe0.telemetry.cgyr0.value
    :field telemetry_cmcs_raw: masterframe.transferframe0.telemetry.cmcs.raw
    :field telemetry_cmcs_value: masterframe.transferframe0.telemetry.cmcs.value
    :field telemetry_cwhl_raw: masterframe.transferframe0.telemetry.cwhl.raw
    :field telemetry_cwhl_value: masterframe.transferframe0.telemetry.cwhl.value
    :field telemetry_ccan0_raw: masterframe.transferframe0.telemetry.ccan0.raw
    :field telemetry_ccan0_value: masterframe.transferframe0.telemetry.ccan0.value
    :field telemetry_ccan1_raw: masterframe.transferframe0.telemetry.ccan1.raw
    :field telemetry_ccan1_value: masterframe.transferframe0.telemetry.ccan1.value
    :field telemetry_vmfs0_raw: masterframe.transferframe0.telemetry.vmfs0.raw
    :field telemetry_vmfs0_value: masterframe.transferframe0.telemetry.vmfs0.value
    :field telemetry_vmfs1_raw: masterframe.transferframe0.telemetry.vmfs1.raw
    :field telemetry_vmfs1_value: masterframe.transferframe0.telemetry.vmfs1.value
    :field telemetry_cmcsxp_raw: masterframe.transferframe0.telemetry.cmcsxp.raw
    :field telemetry_cmcsxp_value: masterframe.transferframe0.telemetry.cmcsxp.value
    :field telemetry_cmcsxn_raw: masterframe.transferframe0.telemetry.cmcsxn.raw
    :field telemetry_cmcsxn_value: masterframe.transferframe0.telemetry.cmcsxn.value
    :field telemetry_cmcsyp_raw: masterframe.transferframe0.telemetry.cmcsyp.raw
    :field telemetry_cmcsyp_value: masterframe.transferframe0.telemetry.cmcsyp.value
    :field telemetry_cmcsyn_raw: masterframe.transferframe0.telemetry.cmcsyn.raw
    :field telemetry_cmcsyn_value: masterframe.transferframe0.telemetry.cmcsyn.value
    :field telemetry_cmcszp_raw: masterframe.transferframe0.telemetry.cmcszp.raw
    :field telemetry_cmcszp_value: masterframe.transferframe0.telemetry.cmcszp.value
    :field telemetry_cmcszn_raw: masterframe.transferframe0.telemetry.cmcszn.raw
    :field telemetry_cmcszn_value: masterframe.transferframe0.telemetry.cmcszn.value
    :field telemetry_cobcmcu_raw: masterframe.transferframe0.telemetry.cobcmcu.raw
    :field telemetry_cobcmcu_value: masterframe.transferframe0.telemetry.cobcmcu.value
    :field telemetry_cobcext_raw: masterframe.transferframe0.telemetry.cobcext.raw
    :field telemetry_cobcext_value: masterframe.transferframe0.telemetry.cobcext.value
    :field telemetry_ttrx1_raw: masterframe.transferframe0.telemetry.ttrx1.raw
    :field telemetry_ttrx1_value: masterframe.transferframe0.telemetry.ttrx1.value
    :field telemetry_cpdh2_raw: masterframe.transferframe0.telemetry.cpdh2.raw
    :field telemetry_cpdh2_value: masterframe.transferframe0.telemetry.cpdh2.value
    :field telemetry_ccam2_raw: masterframe.transferframe0.telemetry.ccam2.raw
    :field telemetry_ccam2_value: masterframe.transferframe0.telemetry.ccam2.value
    :field asstop: masterframe.transferframe0.telemetry.asstop
    :field assintv: masterframe.transferframe0.telemetry.assintv
    :field ascest: masterframe.transferframe0.telemetry.ascest
    :field asactv: masterframe.transferframe0.telemetry.asactv
    :field reserve2: masterframe.transferframe0.telemetry.reserve2
    :field reserve1: masterframe.transferframe0.telemetry.reserve1
    :field telemetry_tsaxp_raw: masterframe.transferframe0.telemetry.tsaxp.raw
    :field telemetry_tsaxp_value: masterframe.transferframe0.telemetry.tsaxp.value
    :field telemetry_tsaxn_raw: masterframe.transferframe0.telemetry.tsaxn.raw
    :field telemetry_tsaxn_value: masterframe.transferframe0.telemetry.tsaxn.value
    :field telemetry_tsayp_raw: masterframe.transferframe0.telemetry.tsayp.raw
    :field telemetry_tsayp_value: masterframe.transferframe0.telemetry.tsayp.value
    :field telemetry_tsayn_raw: masterframe.transferframe0.telemetry.tsayn.raw
    :field telemetry_tsayn_value: masterframe.transferframe0.telemetry.tsayn.value
    :field telemetry_tsazp_raw: masterframe.transferframe0.telemetry.tsazp.raw
    :field telemetry_tsazp_value: masterframe.transferframe0.telemetry.tsazp.value
    :field telemetry_tsazn_raw: masterframe.transferframe0.telemetry.tsazn.raw
    :field telemetry_tsazn_value: masterframe.transferframe0.telemetry.tsazn.value
    :field telemetry_tbat0_raw: masterframe.transferframe0.telemetry.tbat0.raw
    :field telemetry_tbat0_value: masterframe.transferframe0.telemetry.tbat0.value
    :field telemetry_tbat1_raw: masterframe.transferframe0.telemetry.tbat1.raw
    :field telemetry_tbat1_value: masterframe.transferframe0.telemetry.tbat1.value
    :field telemetry_tpcu00_raw: masterframe.transferframe0.telemetry.tpcu00.raw
    :field telemetry_tpcu00_value: masterframe.transferframe0.telemetry.tpcu00.value
    :field telemetry_tpcu01_raw: masterframe.transferframe0.telemetry.tpcu01.raw
    :field telemetry_tpcu01_value: masterframe.transferframe0.telemetry.tpcu01.value
    :field telemetry_tmfs0_raw: masterframe.transferframe0.telemetry.tmfs0.raw
    :field telemetry_tmfs0_value: masterframe.transferframe0.telemetry.tmfs0.value
    :field telemetry_tmfs1_raw: masterframe.transferframe0.telemetry.tmfs1.raw
    :field telemetry_tmfs1_value: masterframe.transferframe0.telemetry.tmfs1.value
    :field telemetry_twhlx_raw: masterframe.transferframe0.telemetry.twhlx.raw
    :field telemetry_twhlx_value: masterframe.transferframe0.telemetry.twhlx.value
    :field telemetry_twhly_raw: masterframe.transferframe0.telemetry.twhly.raw
    :field telemetry_twhly_value: masterframe.transferframe0.telemetry.twhly.value
    :field telemetry_twhlz_raw: masterframe.transferframe0.telemetry.twhlz.raw
    :field telemetry_twhlz_value: masterframe.transferframe0.telemetry.twhlz.value
    :field telemetry_tgyrox_raw: masterframe.transferframe0.telemetry.tgyrox.raw
    :field telemetry_tgyrox_value: masterframe.transferframe0.telemetry.tgyrox.value
    :field telemetry_tgyroy_raw: masterframe.transferframe0.telemetry.tgyroy.raw
    :field telemetry_tgyroy_value: masterframe.transferframe0.telemetry.tgyroy.value
    :field telemetry_tgyroz_raw: masterframe.transferframe0.telemetry.tgyroz.raw
    :field telemetry_tgyroz_value: masterframe.transferframe0.telemetry.tgyroz.value
    :field telemetry_tobc00_raw: masterframe.transferframe0.telemetry.tobc00.raw
    :field telemetry_tobc00_value: masterframe.transferframe0.telemetry.tobc00.value
    :field telemetry_tobc01_raw: masterframe.transferframe0.telemetry.tobc01.raw
    :field telemetry_tobc01_value: masterframe.transferframe0.telemetry.tobc01.value
    :field telemetry_tobc02_raw: masterframe.transferframe0.telemetry.tobc02.raw
    :field telemetry_tobc02_value: masterframe.transferframe0.telemetry.tobc02.value
    :field telemetry_ttrx0_raw: masterframe.transferframe0.telemetry.ttrx0.raw
    :field telemetry_ttrx0_value: masterframe.transferframe0.telemetry.ttrx0.value
    :field reserve: masterframe.transferframe0.telemetry.reserve
    :field telemetry_acssuxpx0_raw: masterframe.transferframe0.telemetry.acssuxpx0.raw
    :field telemetry_acssuxpx0_value: masterframe.transferframe0.telemetry.acssuxpx0.value
    :field telemetry_acssuxpx1_raw: masterframe.transferframe0.telemetry.acssuxpx1.raw
    :field telemetry_acssuxpx1_value: masterframe.transferframe0.telemetry.acssuxpx1.value
    :field telemetry_acssuxpy0_raw: masterframe.transferframe0.telemetry.acssuxpy0.raw
    :field telemetry_acssuxpy0_value: masterframe.transferframe0.telemetry.acssuxpy0.value
    :field telemetry_acssuxpy1_raw: masterframe.transferframe0.telemetry.acssuxpy1.raw
    :field telemetry_acssuxpy1_value: masterframe.transferframe0.telemetry.acssuxpy1.value
    :field telemetry_acssuxnx0_raw: masterframe.transferframe0.telemetry.acssuxnx0.raw
    :field telemetry_acssuxnx0_value: masterframe.transferframe0.telemetry.acssuxnx0.value
    :field telemetry_acssuxnx1_raw: masterframe.transferframe0.telemetry.acssuxnx1.raw
    :field telemetry_acssuxnx1_value: masterframe.transferframe0.telemetry.acssuxnx1.value
    :field telemetry_acssuxny0_raw: masterframe.transferframe0.telemetry.acssuxny0.raw
    :field telemetry_acssuxny0_value: masterframe.transferframe0.telemetry.acssuxny0.value
    :field telemetry_acssuxny1_raw: masterframe.transferframe0.telemetry.acssuxny1.raw
    :field telemetry_acssuxny1_value: masterframe.transferframe0.telemetry.acssuxny1.value
    :field telemetry_acssuypx0_raw: masterframe.transferframe0.telemetry.acssuypx0.raw
    :field telemetry_acssuypx0_value: masterframe.transferframe0.telemetry.acssuypx0.value
    :field telemetry_acssuypx1_raw: masterframe.transferframe0.telemetry.acssuypx1.raw
    :field telemetry_acssuypx1_value: masterframe.transferframe0.telemetry.acssuypx1.value
    :field telemetry_acssuypy0_raw: masterframe.transferframe0.telemetry.acssuypy0.raw
    :field telemetry_acssuypy0_value: masterframe.transferframe0.telemetry.acssuypy0.value
    :field telemetry_acssuypy1_raw: masterframe.transferframe0.telemetry.acssuypy1.raw
    :field telemetry_acssuypy1_value: masterframe.transferframe0.telemetry.acssuypy1.value
    :field telemetry_acssuynx0_raw: masterframe.transferframe0.telemetry.acssuynx0.raw
    :field telemetry_acssuynx0_value: masterframe.transferframe0.telemetry.acssuynx0.value
    :field telemetry_acssuynx1_raw: masterframe.transferframe0.telemetry.acssuynx1.raw
    :field telemetry_acssuynx1_value: masterframe.transferframe0.telemetry.acssuynx1.value
    :field telemetry_acssuyny0_raw: masterframe.transferframe0.telemetry.acssuyny0.raw
    :field telemetry_acssuyny0_value: masterframe.transferframe0.telemetry.acssuyny0.value
    :field telemetry_acssuyny1_raw: masterframe.transferframe0.telemetry.acssuyny1.raw
    :field telemetry_acssuyny1_value: masterframe.transferframe0.telemetry.acssuyny1.value
    :field telemetry_acssuzpx0_raw: masterframe.transferframe0.telemetry.acssuzpx0.raw
    :field telemetry_acssuzpx0_value: masterframe.transferframe0.telemetry.acssuzpx0.value
    :field telemetry_acssuzpx1_raw: masterframe.transferframe0.telemetry.acssuzpx1.raw
    :field telemetry_acssuzpx1_value: masterframe.transferframe0.telemetry.acssuzpx1.value
    :field telemetry_acssuzpy0_raw: masterframe.transferframe0.telemetry.acssuzpy0.raw
    :field telemetry_acssuzpy0_value: masterframe.transferframe0.telemetry.acssuzpy0.value
    :field telemetry_acssuzpy1_raw: masterframe.transferframe0.telemetry.acssuzpy1.raw
    :field telemetry_acssuzpy1_value: masterframe.transferframe0.telemetry.acssuzpy1.value
    :field telemetry_acssuznx0_raw: masterframe.transferframe0.telemetry.acssuznx0.raw
    :field telemetry_acssuznx0_value: masterframe.transferframe0.telemetry.acssuznx0.value
    :field telemetry_acssuznx1_raw: masterframe.transferframe0.telemetry.acssuznx1.raw
    :field telemetry_acssuznx1_value: masterframe.transferframe0.telemetry.acssuznx1.value
    :field telemetry_acssuzny0_raw: masterframe.transferframe0.telemetry.acssuzny0.raw
    :field telemetry_acssuzny0_value: masterframe.transferframe0.telemetry.acssuzny0.value
    :field telemetry_acssuzny1_raw: masterframe.transferframe0.telemetry.acssuzny1.raw
    :field telemetry_acssuzny1_value: masterframe.transferframe0.telemetry.acssuzny1.value
    :field telemetry_cmfs0x_raw: masterframe.transferframe0.telemetry.cmfs0x.raw
    :field telemetry_cmfs0x_value: masterframe.transferframe0.telemetry.cmfs0x.value
    :field telemetry_cmfs0y_raw: masterframe.transferframe0.telemetry.cmfs0y.raw
    :field telemetry_cmfs0y_value: masterframe.transferframe0.telemetry.cmfs0y.value
    :field telemetry_cmfs0z_raw: masterframe.transferframe0.telemetry.cmfs0z.raw
    :field telemetry_cmfs0z_value: masterframe.transferframe0.telemetry.cmfs0z.value
    :field telemetry_cmfs1x_raw: masterframe.transferframe0.telemetry.cmfs1x.raw
    :field telemetry_cmfs1x_value: masterframe.transferframe0.telemetry.cmfs1x.value
    :field telemetry_cmfs1y_raw: masterframe.transferframe0.telemetry.cmfs1y.raw
    :field telemetry_cmfs1y_value: masterframe.transferframe0.telemetry.cmfs1y.value
    :field telemetry_cmfs1z_raw: masterframe.transferframe0.telemetry.cmfs1z.raw
    :field telemetry_cmfs1z_value: masterframe.transferframe0.telemetry.cmfs1z.value
    :field telemetry_acsgy0x_raw: masterframe.transferframe0.telemetry.acsgy0x.raw
    :field telemetry_acsgy0x_value: masterframe.transferframe0.telemetry.acsgy0x.value
    :field telemetry_acsgy0y_raw: masterframe.transferframe0.telemetry.acsgy0y.raw
    :field telemetry_acsgy0y_value: masterframe.transferframe0.telemetry.acsgy0y.value
    :field telemetry_acsgy0z_raw: masterframe.transferframe0.telemetry.acsgy0z.raw
    :field telemetry_acsgy0z_value: masterframe.transferframe0.telemetry.acsgy0z.value
    :field telemetry_reserve1_raw: masterframe.transferframe0.telemetry.reserve1.raw
    :field telemetry_reserve1_value: masterframe.transferframe0.telemetry.reserve1.value
    :field psant0: masterframe.transferframe0.telemetry.psant0
    :field psant1: masterframe.transferframe0.telemetry.psant1
    :field psgyr1: masterframe.transferframe0.telemetry.psgyr1
    :field pscom1: masterframe.transferframe0.telemetry.pscom1
    :field psuhf0: masterframe.transferframe0.telemetry.psuhf0
    :field psuhf1: masterframe.transferframe0.telemetry.psuhf1
    :field pstnc0: masterframe.transferframe0.telemetry.pstnc0
    :field pstnc1: masterframe.transferframe0.telemetry.pstnc1
    :field psgyr0: masterframe.transferframe0.telemetry.psgyr0
    :field psmcsx: masterframe.transferframe0.telemetry.psmcsx
    :field psmcsy: masterframe.transferframe0.telemetry.psmcsy
    :field psmcsz: masterframe.transferframe0.telemetry.psmcsz
    :field pswhls: masterframe.transferframe0.telemetry.pswhls
    :field psobc0: masterframe.transferframe0.telemetry.psobc0
    :field psobc1: masterframe.transferframe0.telemetry.psobc1
    :field pspdh0: masterframe.transferframe0.telemetry.pspdh0
    :field pscam0: masterframe.transferframe0.telemetry.pscam0
    :field pssuns: masterframe.transferframe0.telemetry.pssuns
    :field psmfs0: masterframe.transferframe0.telemetry.psmfs0
    :field psms1: masterframe.transferframe0.telemetry.psms1
    :field pstemp: masterframe.transferframe0.telemetry.pstemp
    :field pscan0: masterframe.transferframe0.telemetry.pscan0
    :field pscan1: masterframe.transferframe0.telemetry.pscan1
    :field psccw0: masterframe.transferframe0.telemetry.psccw0
    :field psccw1: masterframe.transferframe0.telemetry.psccw1
    :field ps5vcn: masterframe.transferframe0.telemetry.ps5vcn
    :field pcuaid: masterframe.transferframe0.telemetry.pcuaid
    :field pcbobc: masterframe.transferframe0.telemetry.pcbobc
    :field pcbext: masterframe.transferframe0.telemetry.pcbext
    :field pcch00: masterframe.transferframe0.telemetry.pcch00
    :field pcch01: masterframe.transferframe0.telemetry.pcch01
    :field pccho2: masterframe.transferframe0.telemetry.pccho2
    :field pcch03: masterframe.transferframe0.telemetry.pcch03
    :field pcch04: masterframe.transferframe0.telemetry.pcch04
    :field pcch05: masterframe.transferframe0.telemetry.pcch05
    :field pcch06: masterframe.transferframe0.telemetry.pcch06
    :field telemetry_rxsig0_raw: masterframe.transferframe0.telemetry.rxsig0.raw
    :field telemetry_rxsig0_value: masterframe.transferframe0.telemetry.rxsig0.value
    :field pcch07: masterframe.transferframe0.telemetry.pcch07
    :field pcch08: masterframe.transferframe0.telemetry.pcch08
    :field pcch09: masterframe.transferframe0.telemetry.pcch09
    :field pcch10: masterframe.transferframe0.telemetry.pcch10
    :field telemetry_rxsig1_raw: masterframe.transferframe0.telemetry.rxsig1.raw
    :field telemetry_rxsig1_value: masterframe.transferframe0.telemetry.rxsig1.value
    :field pcch11: masterframe.transferframe0.telemetry.pcch11
    :field pcch12: masterframe.transferframe0.telemetry.pcch12
    :field pcch13: masterframe.transferframe0.telemetry.pcch13
    :field pcch14: masterframe.transferframe0.telemetry.pcch14
    :field pcch15: masterframe.transferframe0.telemetry.pcch15
    :field pcch16: masterframe.transferframe0.telemetry.pcch16
    :field pcch17: masterframe.transferframe0.telemetry.pcch17
    :field pcch18: masterframe.transferframe0.telemetry.pcch18
    :field pcch19: masterframe.transferframe0.telemetry.pcch19
    :field pcch20: masterframe.transferframe0.telemetry.pcch20
    :field pcch21: masterframe.transferframe0.telemetry.pcch21
    :field pcch22: masterframe.transferframe0.telemetry.pcch22
    :field pcch23: masterframe.transferframe0.telemetry.pcch23
    :field pcch24: masterframe.transferframe0.telemetry.pcch24
    :field pcch25: masterframe.transferframe0.telemetry.pcch25
    :field pcch26: masterframe.transferframe0.telemetry.pcch26
    :field tcrxid: masterframe.transferframe0.telemetry.tcrxid
    :field obcaid: masterframe.transferframe0.telemetry.obcaid
    :field tmtxrt: masterframe.transferframe0.telemetry.tmtxrt
    :field pcch27: masterframe.transferframe0.telemetry.pcch27
    :field pcch28: masterframe.transferframe0.telemetry.pcch28
    :field pcch29: masterframe.transferframe0.telemetry.pcch29
    :field pcch30: masterframe.transferframe0.telemetry.pcch30
    :field pcch31: masterframe.transferframe0.telemetry.pcch31
    :field cctcic: masterframe.transferframe0.telemetry.cctcic
    :field cctctt: masterframe.transferframe0.telemetry.cctctt
    :field ccetcs: masterframe.transferframe0.telemetry.ccetcs
    :field cceimc: masterframe.transferframe0.telemetry.cceimc
    :field ccettc: masterframe.transferframe0.telemetry.ccettc
    :field ccettg: masterframe.transferframe0.telemetry.ccettg
    :field ccetcc: masterframe.transferframe0.telemetry.ccetcc
    :field telemetry_tcrxqu_raw: masterframe.transferframe0.telemetry.tcrxqu.raw
    :field telemetry_tcrxqu_value: masterframe.transferframe0.telemetry.tcrxqu.value
    :field telemetry_tcfrcp_raw: masterframe.transferframe0.telemetry.tcfrcp.raw
    :field telemetry_tcfrcp_value: masterframe.transferframe0.telemetry.tcfrcp.value
    :field telemetry_tmhkur_raw: masterframe.transferframe0.telemetry.tmhkur.raw
    :field telemetry_tmhkur_value: masterframe.transferframe0.telemetry.tmhkur.value
    :field telemetry_cstsys_raw: masterframe.transferframe0.telemetry.cstsys.raw
    :field telemetry_cstsys_value: masterframe.transferframe0.telemetry.cstsys.value
    :field mcxpol: masterframe.transferframe0.telemetry.mcxpol
    :field mcypol: masterframe.transferframe0.telemetry.mcypol
    :field mczpol: masterframe.transferframe0.telemetry.mczpol
    :field telemetry_obcbad_raw: masterframe.transferframe0.telemetry.obcbad.raw
    :field telemetry_obcbad_value: masterframe.transferframe0.telemetry.obcbad.value
    :field ceswmc: masterframe.transferframe0.telemetry.ceswmc
    :field beacon: masterframe.transferframe0.telemetry.beacon
    :field telemetry_reserve3_raw: masterframe.transferframe0.telemetry.reserve3.raw
    :field telemetry_reserve3_value: masterframe.transferframe0.telemetry.reserve3.value
    :field telemetry_modcom_raw: masterframe.transferframe0.telemetry.modcom.raw
    :field telemetry_modcom_value: masterframe.transferframe0.telemetry.modcom.value
    :field obcabc: masterframe.transferframe0.telemetry.obcabc
    :field modobc: masterframe.transferframe0.telemetry.modobc
    :field ccecan: masterframe.transferframe0.telemetry.ccecan
    :field obccan: masterframe.transferframe0.telemetry.obccan
    :field telemetry_pcsyst_raw: masterframe.transferframe0.telemetry.pcsyst.raw
    :field telemetry_pcsyst_value: masterframe.transferframe0.telemetry.pcsyst.value
    :field pcbcnt: masterframe.transferframe0.telemetry.pcbcnt
    :field pctxec: masterframe.transferframe0.telemetry.pctxec
    :field pcrxec: masterframe.transferframe0.telemetry.pcrxec
    :field pcoffc: masterframe.transferframe0.telemetry.pcoffc
    :field pcackc: masterframe.transferframe0.telemetry.pcackc
    :field pcch32: masterframe.transferframe0.telemetry.pcch32
    :field pcch33: masterframe.transferframe0.telemetry.pcch33
    :field pcch34: masterframe.transferframe0.telemetry.pcch34
    :field pcch35: masterframe.transferframe0.telemetry.pcch35
    :field pcch36: masterframe.transferframe0.telemetry.pcch36
    :field pcch37: masterframe.transferframe0.telemetry.pcch37
    :field pcch38: masterframe.transferframe0.telemetry.pcch38
    :field pcch39: masterframe.transferframe0.telemetry.pcch39
    :field pcch40: masterframe.transferframe0.telemetry.pcch40
    :field pcch41: masterframe.transferframe0.telemetry.pcch41
    :field telemetry_reserve4_raw: masterframe.transferframe0.telemetry.reserve4.raw
    :field telemetry_reserve4_value: masterframe.transferframe0.telemetry.reserve4.value
    :field telemetry_reserve5_raw: masterframe.transferframe0.telemetry.reserve5.raw
    :field telemetry_reserve5_value: masterframe.transferframe0.telemetry.reserve5.value
    :field telemetry_reserve6_raw: masterframe.transferframe0.telemetry.reserve6.raw
    :field telemetry_reserve6_value: masterframe.transferframe0.telemetry.reserve6.value
    :field telemetry_reserve7_raw: masterframe.transferframe0.telemetry.reserve7.raw
    :field telemetry_reserve7_value: masterframe.transferframe0.telemetry.reserve7.value
    :field telemetry_acswhx_raw: masterframe.transferframe0.telemetry.acswhx.raw
    :field telemetry_acswhx_value: masterframe.transferframe0.telemetry.acswhx.value
    :field telemetry_acswhy_raw: masterframe.transferframe0.telemetry.acswhy.raw
    :field telemetry_acswhy_value: masterframe.transferframe0.telemetry.acswhy.value
    :field telemetry_acswhz_raw: masterframe.transferframe0.telemetry.acswhz.raw
    :field telemetry_acswhz_value: masterframe.transferframe0.telemetry.acswhz.value
    :field telemetry_acsq00_raw: masterframe.transferframe0.telemetry.acsq00.raw
    :field telemetry_acsq00_value: masterframe.transferframe0.telemetry.acsq00.value
    :field telemetry_acsq01_raw: masterframe.transferframe0.telemetry.acsq01.raw
    :field telemetry_acsq01_value: masterframe.transferframe0.telemetry.acsq01.value
    :field telemetry_acsq02_raw: masterframe.transferframe0.telemetry.acsq02.raw
    :field telemetry_acsq02_value: masterframe.transferframe0.telemetry.acsq02.value
    :field telemetry_acsq03_raw: masterframe.transferframe0.telemetry.acsq03.raw
    :field telemetry_acsq03_value: masterframe.transferframe0.telemetry.acsq03.value
    :field telemetry_acssux_raw: masterframe.transferframe0.telemetry.acssux.raw
    :field telemetry_acssux_value: masterframe.transferframe0.telemetry.acssux.value
    :field telemetry_acssuy_raw: masterframe.transferframe0.telemetry.acssuy.raw
    :field telemetry_acssuy_value: masterframe.transferframe0.telemetry.acssuy.value
    :field telemetry_acssuz_raw: masterframe.transferframe0.telemetry.acssuz.raw
    :field telemetry_acssuz_value: masterframe.transferframe0.telemetry.acssuz.value
    :field telemetry_acsmox_raw: masterframe.transferframe0.telemetry.acsmox.raw
    :field telemetry_acsmox_value: masterframe.transferframe0.telemetry.acsmox.value
    :field telemetry_acsmoy_raw: masterframe.transferframe0.telemetry.acsmoy.raw
    :field telemetry_acsmoy_value: masterframe.transferframe0.telemetry.acsmoy.value
    :field telemetry_acsmoz_raw: masterframe.transferframe0.telemetry.acsmoz.raw
    :field telemetry_acsmoz_value: masterframe.transferframe0.telemetry.acsmoz.value
    :field telemetry_acsm1x_raw: masterframe.transferframe0.telemetry.acsm1x.raw
    :field telemetry_acsm1x_value: masterframe.transferframe0.telemetry.acsm1x.value
    :field telemetry_acsm1y_raw: masterframe.transferframe0.telemetry.acsm1y.raw
    :field telemetry_acsm1y_value: masterframe.transferframe0.telemetry.acsm1y.value
    :field telemetry_acsm1z_raw: masterframe.transferframe0.telemetry.acsm1z.raw
    :field telemetry_acsm1z_value: masterframe.transferframe0.telemetry.acsm1z.value
    :field telemetry_modacs_raw: masterframe.transferframe0.telemetry.modacs.raw
    :field telemetry_modacs_value: masterframe.transferframe0.telemetry.modacs.value
    :field acsgsc: masterframe.transferframe0.telemetry.acsgsc
    :field acsshd: masterframe.transferframe0.telemetry.acsshd
    :field telemetry_reserve8_raw: masterframe.transferframe0.telemetry.reserve8.raw
    :field telemetry_reserve8_value: masterframe.transferframe0.telemetry.reserve8.value
    :field acserr: masterframe.transferframe0.telemetry.acserr
    :field telemetry_acsg1y_raw: masterframe.transferframe0.telemetry.acsg1y.raw
    :field telemetry_acsg1y_value: masterframe.transferframe0.telemetry.acsg1y.value
    :field telemetry_acsg1z_raw: masterframe.transferframe0.telemetry.acsg1z.raw
    :field telemetry_acsg1z_value: masterframe.transferframe0.telemetry.acsg1z.value
    :field telemetry_acsg1x_raw: masterframe.transferframe0.telemetry.acsg1x.raw
    :field telemetry_acsg1x_value: masterframe.transferframe0.telemetry.acsg1x.value
    :field telemetry_reserve9_raw: masterframe.transferframe0.telemetry.reserve9.raw
    :field telemetry_reserve9_value: masterframe.transferframe0.telemetry.reserve9.value
    :field telemetry_reserve10_raw: masterframe.transferframe0.telemetry.reserve10.raw
    :field telemetry_reserve10_value: masterframe.transferframe0.telemetry.reserve10.value
    :field crc000: masterframe.transferframe0.telemetry.crc000
    :field crc001: masterframe.transferframe0.telemetry.crc001
    :field crc002: masterframe.transferframe0.telemetry.crc002
    :field crc003: masterframe.transferframe0.telemetry.crc003
    :field crc004: masterframe.transferframe0.telemetry.crc004
    :field crc005: masterframe.transferframe0.telemetry.crc005
    :field crc006: masterframe.transferframe0.telemetry.crc006
    :field crc007: masterframe.transferframe0.telemetry.crc007
    :field crc008: masterframe.transferframe0.telemetry.crc008
    :field crc009: masterframe.transferframe0.telemetry.crc009
    :field crc010: masterframe.transferframe0.telemetry.crc010
    :field crc011: masterframe.transferframe0.telemetry.crc011
    :field crc012: masterframe.transferframe0.telemetry.crc012
    :field crc013: masterframe.transferframe0.telemetry.crc013
    :field crc014: masterframe.transferframe0.telemetry.crc014
    :field crc015: masterframe.transferframe0.telemetry.crc015
    :field crc016: masterframe.transferframe0.telemetry.crc016
    :field crc017: masterframe.transferframe0.telemetry.crc017
    :field crc018: masterframe.transferframe0.telemetry.crc018
    :field crc019: masterframe.transferframe0.telemetry.crc019
    :field crc020: masterframe.transferframe0.telemetry.crc020
    :field crc021: masterframe.transferframe0.telemetry.crc021
    :field crc022: masterframe.transferframe0.telemetry.crc022
    :field crc023: masterframe.transferframe0.telemetry.crc023
    :field crc024: masterframe.transferframe0.telemetry.crc024
    :field crc025: masterframe.transferframe0.telemetry.crc025
    :field crc026: masterframe.transferframe0.telemetry.crc026
    :field crc027: masterframe.transferframe0.telemetry.crc027
    :field crc028: masterframe.transferframe0.telemetry.crc028
    :field crc029: masterframe.transferframe0.telemetry.crc029
    :field crc030: masterframe.transferframe0.telemetry.crc030
    :field dummy: masterframe.transferframe0.telemetry.dummy
    :field imhd00: masterframe.transferframe0.telemetry.imhd00
    :field imhd01: masterframe.transferframe0.telemetry.imhd01
    :field imhd02: masterframe.transferframe0.telemetry.imhd02
    :field imhd03: masterframe.transferframe0.telemetry.imhd03
    :field imhd04: masterframe.transferframe0.telemetry.imhd04
    :field imhd10: masterframe.transferframe0.telemetry.imhd10
    :field imhd11: masterframe.transferframe0.telemetry.imhd11
    :field imhd12: masterframe.transferframe0.telemetry.imhd12
    :field imhd13: masterframe.transferframe0.telemetry.imhd13
    :field imhd14: masterframe.transferframe0.telemetry.imhd14
    :field imhd20: masterframe.transferframe0.telemetry.imhd20
    :field imhd21: masterframe.transferframe0.telemetry.imhd21
    :field imhd22: masterframe.transferframe0.telemetry.imhd22
    :field imhd23: masterframe.transferframe0.telemetry.imhd23
    :field imhd24: masterframe.transferframe0.telemetry.imhd24
    :field imhd30: masterframe.transferframe0.telemetry.imhd30
    :field imhd31: masterframe.transferframe0.telemetry.imhd31
    :field imhd32: masterframe.transferframe0.telemetry.imhd32
    :field imhd33: masterframe.transferframe0.telemetry.imhd33
    :field imhd34: masterframe.transferframe0.telemetry.imhd34
    :field reserver20: masterframe.transferframe0.telemetry.reserver20
    :field image_id: masterframe.transferframe0.telemetry.image_id
    :field pdh_image: masterframe.transferframe0.telemetry.pdh_image
    :field telemetry_cpdhmcu_raw: masterframe.transferframe0.telemetry.cpdhmcu.raw
    :field telemetry_cpdhmcu_value: masterframe.transferframe0.telemetry.cpdhmcu.value
    :field telemetry_cpdhcam_raw: masterframe.transferframe0.telemetry.cpdhcam.raw
    :field telemetry_cpdhcam_value: masterframe.transferframe0.telemetry.cpdhcam.value
    :field tpdhcam: masterframe.transferframe0.telemetry.tpdhcam
    :field pdhceccm: masterframe.transferframe0.telemetry.pdhceccm
    :field pdhcectc: masterframe.transferframe0.telemetry.pdhcectc
    :field pdhcetlii: masterframe.transferframe0.telemetry.pdhcetlii
    :field pdhcetlc: masterframe.transferframe0.telemetry.pdhcetlc
    :field pdhti: masterframe.transferframe0.telemetry.pdhti
    :field pdhth: masterframe.transferframe0.telemetry.pdhth
    :field pdhceisi: masterframe.transferframe0.telemetry.pdhceisi
    :field pdhceici: masterframe.transferframe0.telemetry.pdhceici
    :field pdhceids: masterframe.transferframe0.telemetry.pdhceids
    :field pdhmode: masterframe.transferframe0.telemetry.pdhmode
    :field pdhcii: masterframe.transferframe0.telemetry.pdhcii
    :field pdhcih: masterframe.transferframe0.telemetry.pdhcih
    :field pdhcescm: masterframe.transferframe0.telemetry.pdhcescm
    :field pdhcessm: masterframe.transferframe0.telemetry.pdhcessm
    :field pdhcescb: masterframe.transferframe0.telemetry.pdhcescb
    :field pdhceslb: masterframe.transferframe0.telemetry.pdhceslb
    :field pdhcesss: masterframe.transferframe0.telemetry.pdhcesss
    :field pdhcessb: masterframe.transferframe0.telemetry.pdhcessb
    :field pdhceseb: masterframe.transferframe0.telemetry.pdhceseb
    :field pdhcesci: masterframe.transferframe0.telemetry.pdhcesci
    :field pdhcsi: masterframe.transferframe0.telemetry.pdhcsi
    :field pdhcsh: masterframe.transferframe0.telemetry.pdhcsh
    :field pdhbtimg: masterframe.transferframe0.telemetry.pdhbtimg
    :field pdhswversion: masterframe.transferframe0.telemetry.pdhswversion
    :field pdhcstsys: masterframe.transferframe0.telemetry.pdhcstsys
    :field pdhctstutc: masterframe.transferframe0.telemetry.pdhctstutc
    :field pdh_reserve: masterframe.transferframe0.telemetry.pdh_reserve
    :field pdhcrc000: masterframe.transferframe0.telemetry.pdhcrc000
    :field pdhcrc001: masterframe.transferframe0.telemetry.pdhcrc001
    :field pdhcrc002: masterframe.transferframe0.telemetry.pdhcrc002
    :field pdhcrc003: masterframe.transferframe0.telemetry.pdhcrc003
    :field pdhcrc004: masterframe.transferframe0.telemetry.pdhcrc004
    :field pdhcrc005: masterframe.transferframe0.telemetry.pdhcrc005
    :field pdhcrc006: masterframe.transferframe0.telemetry.pdhcrc006
    :field pdhcrc007: masterframe.transferframe0.telemetry.pdhcrc007
    :field pdhcrc008: masterframe.transferframe0.telemetry.pdhcrc008
    :field pdhcrc009: masterframe.transferframe0.telemetry.pdhcrc009
    :field pdhcrc010: masterframe.transferframe0.telemetry.pdhcrc010
    :field pdhcrc011: masterframe.transferframe0.telemetry.pdhcrc011
    :field pdhcrc012: masterframe.transferframe0.telemetry.pdhcrc012
    :field pdhcrc013: masterframe.transferframe0.telemetry.pdhcrc013
    :field pdhcrc014: masterframe.transferframe0.telemetry.pdhcrc014
    :field pdhcrc015: masterframe.transferframe0.telemetry.pdhcrc015
    :field pdhcrc016: masterframe.transferframe0.telemetry.pdhcrc016
    :field pdhcrc017: masterframe.transferframe0.telemetry.pdhcrc017
    :field pdhcrc018: masterframe.transferframe0.telemetry.pdhcrc018
    :field pdhcrc019: masterframe.transferframe0.telemetry.pdhcrc019
    :field pdhcrc020: masterframe.transferframe0.telemetry.pdhcrc020
    :field pdhcrc021: masterframe.transferframe0.telemetry.pdhcrc021
    :field pdhcrc022: masterframe.transferframe0.telemetry.pdhcrc022
    :field pdhcrc023: masterframe.transferframe0.telemetry.pdhcrc023
    :field pdhcrc024: masterframe.transferframe0.telemetry.pdhcrc024
    :field pdhcrc025: masterframe.transferframe0.telemetry.pdhcrc025
    :field pdhcrc026: masterframe.transferframe0.telemetry.pdhcrc026
    :field pdhcrc027: masterframe.transferframe0.telemetry.pdhcrc027
    :field pdhcrc028: masterframe.transferframe0.telemetry.pdhcrc028
    :field pdhcrc029: masterframe.transferframe0.telemetry.pdhcrc029
    :field pdhcrc030: masterframe.transferframe0.telemetry.pdhcrc030
    :field pdhcrccmask00: masterframe.transferframe0.telemetry.pdhcrccmask00
    :field acswhx: masterframe.transferframe0.telemetry.acswhx
    :field telemetry_acsm0x_raw: masterframe.transferframe0.telemetry.acsm0x.raw
    :field telemetry_acsm0x_value: masterframe.transferframe0.telemetry.acsm0x.value
    :field telemetry_acsm0y_raw: masterframe.transferframe0.telemetry.acsm0y.raw
    :field telemetry_acsm0y_value: masterframe.transferframe0.telemetry.acsm0y.value
    :field telemetry_acsm0z_raw: masterframe.transferframe0.telemetry.acsm0z.raw
    :field telemetry_acsm0z_value: masterframe.transferframe0.telemetry.acsm0z.value
    :field reserveacsgr: masterframe.transferframe0.telemetry.reserveacsgr
    :field acstemex: masterframe.transferframe0.telemetry.acstemex
    :field acstemey: masterframe.transferframe0.telemetry.acstemey
    :field acstemez: masterframe.transferframe0.telemetry.acstemez
    :field telemetry_acstemevelx_raw: masterframe.transferframe0.telemetry.acstemevelx.raw
    :field telemetry_acstemevelx_value: masterframe.transferframe0.telemetry.acstemevelx.value
    :field telemetry_acstemevely_raw: masterframe.transferframe0.telemetry.acstemevely.raw
    :field telemetry_acstemevely_value: masterframe.transferframe0.telemetry.acstemevely.value
    :field telemetry_acstemevelz_raw: masterframe.transferframe0.telemetry.acstemevelz.raw
    :field telemetry_acstemevelz_value: masterframe.transferframe0.telemetry.acstemevelz.value
    :field acsefx: masterframe.transferframe0.telemetry.acsefx
    :field acsefy: masterframe.transferframe0.telemetry.acsefy
    :field acsefz: masterframe.transferframe0.telemetry.acsefz
    :field telemetry_acsmagifx_raw: masterframe.transferframe0.telemetry.acsmagifx.raw
    :field telemetry_acsmagifx_value: masterframe.transferframe0.telemetry.acsmagifx.value
    :field telemetry_acsmagify_raw: masterframe.transferframe0.telemetry.acsmagify.raw
    :field telemetry_acsmagify_value: masterframe.transferframe0.telemetry.acsmagify.value
    :field telemetry_acsmagifz_raw: masterframe.transferframe0.telemetry.acsmagifz.raw
    :field telemetry_acsmagifz_value: masterframe.transferframe0.telemetry.acsmagifz.value
    :field telemetry_acssunifx_raw: masterframe.transferframe0.telemetry.acssunifx.raw
    :field telemetry_acssunifx_value: masterframe.transferframe0.telemetry.acssunifx.value
    :field telemetry_acssunify_raw: masterframe.transferframe0.telemetry.acssunify.raw
    :field telemetry_acssunify_value: masterframe.transferframe0.telemetry.acssunify.value
    :field telemetry_acssunifz_raw: masterframe.transferframe0.telemetry.acssunifz.raw
    :field telemetry_acssunifz_value: masterframe.transferframe0.telemetry.acssunifz.value
    :field telemetry_acsqdes00_raw: masterframe.transferframe0.telemetry.acsqdes00.raw
    :field telemetry_acsqdes00_value: masterframe.transferframe0.telemetry.acsqdes00.value
    :field telemetry_acsqdes01_raw: masterframe.transferframe0.telemetry.acsqdes01.raw
    :field telemetry_acsqdes01_value: masterframe.transferframe0.telemetry.acsqdes01.value
    :field telemetry_acsqdes02_raw: masterframe.transferframe0.telemetry.acsqdes02.raw
    :field telemetry_acsqdes02_value: masterframe.transferframe0.telemetry.acsqdes02.value
    :field telemetry_acsqdes03_raw: masterframe.transferframe0.telemetry.acsqdes03.raw
    :field telemetry_acsqdes03_value: masterframe.transferframe0.telemetry.acsqdes03.value
    :field telemetry_acswcx_raw: masterframe.transferframe0.telemetry.acswcx.raw
    :field telemetry_acswcx_value: masterframe.transferframe0.telemetry.acswcx.value
    :field telemetry_acswcy_raw: masterframe.transferframe0.telemetry.acswcy.raw
    :field telemetry_acswcy_value: masterframe.transferframe0.telemetry.acswcy.value
    :field telemetry_acswcz_raw: masterframe.transferframe0.telemetry.acswcz.raw
    :field telemetry_acswcz_value: masterframe.transferframe0.telemetry.acswcz.value
    :field telemetry_acswu0_raw: masterframe.transferframe0.telemetry.acswu0.raw
    :field telemetry_acswu0_value: masterframe.transferframe0.telemetry.acswu0.value
    :field telemetry_acswu1_raw: masterframe.transferframe0.telemetry.acswu1.raw
    :field telemetry_acswu1_value: masterframe.transferframe0.telemetry.acswu1.value
    :field telemetry_acswu2_raw: masterframe.transferframe0.telemetry.acswu2.raw
    :field telemetry_acswu2_value: masterframe.transferframe0.telemetry.acswu2.value
    :field telemetry_acswq0_raw: masterframe.transferframe0.telemetry.acswq0.raw
    :field telemetry_acswq0_value: masterframe.transferframe0.telemetry.acswq0.value
    :field telemetry_acswq1_raw: masterframe.transferframe0.telemetry.acswq1.raw
    :field telemetry_acswq1_value: masterframe.transferframe0.telemetry.acswq1.value
    :field telemetry_acswq2_raw: masterframe.transferframe0.telemetry.acswq2.raw
    :field telemetry_acswq2_value: masterframe.transferframe0.telemetry.acswq2.value
    :field telemetry_acswq3_raw: masterframe.transferframe0.telemetry.acswq3.raw
    :field telemetry_acswq3_value: masterframe.transferframe0.telemetry.acswq3.value
    :field acswa0: masterframe.transferframe0.telemetry.acswa0
    :field acswa1: masterframe.transferframe0.telemetry.acswa1
    :field acswa2: masterframe.transferframe0.telemetry.acswa2
    :field acs_tm_vecs_res: masterframe.transferframe0.telemetry.acs_tm_vecs_res
    :field psmfs1: masterframe.transferframe0.telemetry.psmfs1
    :field pcch02: masterframe.transferframe0.telemetry.pcch02
    :field tcfrcp: masterframe.transferframe0.telemetry.tcfrcp
    :field tmhkur: masterframe.transferframe0.telemetry.tmhkur
    :field cstutc: masterframe.transferframe0.telemetry.cstutc
    :field cstsys: masterframe.transferframe0.telemetry.cstsys
    :field pcsyst: masterframe.transferframe0.telemetry.pcsyst
    :field acswhy: masterframe.transferframe0.telemetry.acswhy
    :field acswhz: masterframe.transferframe0.telemetry.acswhz
    :field telemetry_acg1ym_raw: masterframe.transferframe0.telemetry.acg1ym.raw
    :field telemetry_acg1ym_value: masterframe.transferframe0.telemetry.acg1ym.value
    :field telemetry_acg1zm_raw: masterframe.transferframe0.telemetry.acg1zm.raw
    :field telemetry_acg1zm_value: masterframe.transferframe0.telemetry.acg1zm.value
    :field telemetry_acg1xm_raw: masterframe.transferframe0.telemetry.acg1xm.raw
    :field telemetry_acg1xm_value: masterframe.transferframe0.telemetry.acg1xm.value
    :field obctmffp: masterframe.transferframe0.telemetry.obctmffp
    :field obcswversion: masterframe.transferframe0.telemetry.obcswversion
    :field telemetry_acscmod_raw: masterframe.transferframe0.telemetry.acscmod.raw
    :field telemetry_acscmod_value: masterframe.transferframe0.telemetry.acscmod.value
    :field cctccp: masterframe.transferframe0.telemetry.cctccp
    :field telemetry_b2_tm_reserve_raw: masterframe.transferframe0.telemetry.b2_tm_reserve.raw
    :field telemetry_b2_tm_reserve_value: masterframe.transferframe0.telemetry.b2_tm_reserve.value
    :field tledoy: masterframe.transferframe0.telemetry.tledoy
    :field telemetry_tlemem_raw: masterframe.transferframe0.telemetry.tlemem.raw
    :field telemetry_tlemem_value: masterframe.transferframe0.telemetry.tlemem.value
    :field tleecc: masterframe.transferframe0.telemetry.tleecc
    :field telemetry_tleinc_raw: masterframe.transferframe0.telemetry.tleinc.raw
    :field telemetry_tleinc_value: masterframe.transferframe0.telemetry.tleinc.value
    :field telemetry_tleaop_raw: masterframe.transferframe0.telemetry.tleaop.raw
    :field telemetry_tleaop_value: masterframe.transferframe0.telemetry.tleaop.value
    :field telemetry_tleraa_raw: masterframe.transferframe0.telemetry.tleraa.raw
    :field telemetry_tleraa_value: masterframe.transferframe0.telemetry.tleraa.value
    :field telemetry_tleman_raw: masterframe.transferframe0.telemetry.tleman.raw
    :field telemetry_tleman_value: masterframe.transferframe0.telemetry.tleman.value
    :field tledrt: masterframe.transferframe0.telemetry.tledrt
    :field tlexpc: masterframe.transferframe0.telemetry.tlexpc
    :field tleypc: masterframe.transferframe0.telemetry.tleypc
    :field tlettd: masterframe.transferframe0.telemetry.tlettd
    :field tleutd: masterframe.transferframe0.telemetry.tleutd
    :field tledep: masterframe.transferframe0.telemetry.tledep
    :field tledps: masterframe.transferframe0.telemetry.tledps
    :field tleyea: masterframe.transferframe0.telemetry.tleyea
    :field tle_placeholder: masterframe.transferframe0.telemetry.tle_placeholder
    :field fecfd: masterframe.transferframe0.fecfd
    :field transferframe1_asm: masterframe.transferframe1.asm
    :field transferframe1_raw: masterframe.transferframe1.tfvn.raw
    :field transferframe1_value: masterframe.transferframe1.tfvn.value
    :field transferframe1_scid_raw: masterframe.transferframe1.scid.raw
    :field transferframe1_scid_value: masterframe.transferframe1.scid.value
    :field transferframe1_vcidb_raw: masterframe.transferframe1.vcidb.raw
    :field transferframe1_vcidb_value: masterframe.transferframe1.vcidb.value
    :field transferframe1_ocff: masterframe.transferframe1.ocff
    :field transferframe1_mcfc: masterframe.transferframe1.mcfc
    :field transferframe1_vcfc: masterframe.transferframe1.vcfc
    :field transferframe1_tf_shf: masterframe.transferframe1.tf_shf
    :field transferframe1_synchflag: masterframe.transferframe1.synchflag
    :field transferframe1_pof: masterframe.transferframe1.pof
    :field transferframe1_slid_raw: masterframe.transferframe1.slid.raw
    :field transferframe1_slid_value: masterframe.transferframe1.slid.value
    :field transferframe1_fhp_raw: masterframe.transferframe1.fhp.raw
    :field transferframe1_fhp_value: masterframe.transferframe1.fhp.value
    :field transferframe1_source_pvn_raw: masterframe.transferframe1.source.pvn.raw
    :field transferframe1_source_pvn_value: masterframe.transferframe1.source.pvn.value
    :field transferframe1_pt: masterframe.transferframe1.source.pt
    :field transferframe1_shf: masterframe.transferframe1.source.shf
    :field transferframe1_source_apid_raw: masterframe.transferframe1.source.apid.raw
    :field transferframe1_source_apid_value: masterframe.transferframe1.source.apid.value
    :field transferframe1_source_seqflag_raw: masterframe.transferframe1.source.seqflag.raw
    :field transferframe1_source_seqflag_value: masterframe.transferframe1.source.seqflag.value
    :field transferframe1_source_psc_raw: masterframe.transferframe1.source.psc.raw
    :field transferframe1_source_psc_value: masterframe.transferframe1.source.psc.value
    :field transferframe1_pdl: masterframe.transferframe1.source.pdl
    :field transferframe1_telemetry_cstutc_raw: masterframe.transferframe1.telemetry.cstutc.raw
    :field transferframe1_telemetry_cstutc_value: masterframe.transferframe1.telemetry.cstutc.value
    :field transferframe1_telemetry_csaxp_raw: masterframe.transferframe1.telemetry.csaxp.raw
    :field transferframe1_telemetry_csaxp_value: masterframe.transferframe1.telemetry.csaxp.value
    :field transferframe1_telemetry_csaxn_raw: masterframe.transferframe1.telemetry.csaxn.raw
    :field transferframe1_telemetry_csaxn_value: masterframe.transferframe1.telemetry.csaxn.value
    :field transferframe1_telemetry_csayp_raw: masterframe.transferframe1.telemetry.csayp.raw
    :field transferframe1_telemetry_csayp_value: masterframe.transferframe1.telemetry.csayp.value
    :field transferframe1_telemetry_csayn_raw: masterframe.transferframe1.telemetry.csayn.raw
    :field transferframe1_telemetry_csayn_value: masterframe.transferframe1.telemetry.csayn.value
    :field transferframe1_telemetry_csazp_raw: masterframe.transferframe1.telemetry.csazp.raw
    :field transferframe1_telemetry_csazp_value: masterframe.transferframe1.telemetry.csazp.value
    :field transferframe1_telemetry_csazn_raw: masterframe.transferframe1.telemetry.csazn.raw
    :field transferframe1_telemetry_csazn_value: masterframe.transferframe1.telemetry.csazn.value
    :field transferframe1_telemetry_vsabus_raw: masterframe.transferframe1.telemetry.vsabus.raw
    :field transferframe1_telemetry_vsabus_value: masterframe.transferframe1.telemetry.vsabus.value
    :field transferframe1_telemetry_cc0in_raw: masterframe.transferframe1.telemetry.cc0in.raw
    :field transferframe1_telemetry_cc0in_value: masterframe.transferframe1.telemetry.cc0in.value
    :field transferframe1_telemetry_cc1in_raw: masterframe.transferframe1.telemetry.cc1in.raw
    :field transferframe1_telemetry_cc1in_value: masterframe.transferframe1.telemetry.cc1in.value
    :field transferframe1_telemetry_vbat0_raw: masterframe.transferframe1.telemetry.vbat0.raw
    :field transferframe1_telemetry_vbat0_value: masterframe.transferframe1.telemetry.vbat0.value
    :field transferframe1_telemetry_vbat1_raw: masterframe.transferframe1.telemetry.vbat1.raw
    :field transferframe1_telemetry_vbat1_value: masterframe.transferframe1.telemetry.vbat1.value
    :field transferframe1_telemetry_cc0out_raw: masterframe.transferframe1.telemetry.cc0out.raw
    :field transferframe1_telemetry_cc0out_value: masterframe.transferframe1.telemetry.cc0out.value
    :field transferframe1_telemetry_cc1out_raw: masterframe.transferframe1.telemetry.cc1out.raw
    :field transferframe1_telemetry_cc1out_value: masterframe.transferframe1.telemetry.cc1out.value
    :field transferframe1_telemetry_v50bus_raw: masterframe.transferframe1.telemetry.v50bus.raw
    :field transferframe1_telemetry_v50bus_value: masterframe.transferframe1.telemetry.v50bus.value
    :field transferframe1_telemetry_v33bus_raw: masterframe.transferframe1.telemetry.v33bus.raw
    :field transferframe1_telemetry_v33bus_value: masterframe.transferframe1.telemetry.v33bus.value
    :field transferframe1_telemetry_cpcu_raw: masterframe.transferframe1.telemetry.cpcu.raw
    :field transferframe1_telemetry_cpcu_value: masterframe.transferframe1.telemetry.cpcu.value
    :field transferframe1_telemetry_cobc0_raw: masterframe.transferframe1.telemetry.cobc0.raw
    :field transferframe1_telemetry_cobc0_value: masterframe.transferframe1.telemetry.cobc0.value
    :field transferframe1_telemetry_cobc1_raw: masterframe.transferframe1.telemetry.cobc1.raw
    :field transferframe1_telemetry_cobc1_value: masterframe.transferframe1.telemetry.cobc1.value
    :field transferframe1_telemetry_ctnc0_raw: masterframe.transferframe1.telemetry.ctnc0.raw
    :field transferframe1_telemetry_ctnc0_value: masterframe.transferframe1.telemetry.ctnc0.value
    :field transferframe1_telemetry_ctnc1_raw: masterframe.transferframe1.telemetry.ctnc1.raw
    :field transferframe1_telemetry_ctnc1_value: masterframe.transferframe1.telemetry.ctnc1.value
    :field transferframe1_telemetry_ctrx0_raw: masterframe.transferframe1.telemetry.ctrx0.raw
    :field transferframe1_telemetry_ctrx0_value: masterframe.transferframe1.telemetry.ctrx0.value
    :field transferframe1_telemetry_ctrx1_raw: masterframe.transferframe1.telemetry.ctrx1.raw
    :field transferframe1_telemetry_ctrx1_value: masterframe.transferframe1.telemetry.ctrx1.value
    :field transferframe1_telemetry_cpdh_raw: masterframe.transferframe1.telemetry.cpdh.raw
    :field transferframe1_telemetry_cpdh_value: masterframe.transferframe1.telemetry.cpdh.value
    :field transferframe1_telemetry_ccam_raw: masterframe.transferframe1.telemetry.ccam.raw
    :field transferframe1_telemetry_ccam_value: masterframe.transferframe1.telemetry.ccam.value
    :field transferframe1_telemetry_csss_raw: masterframe.transferframe1.telemetry.csss.raw
    :field transferframe1_telemetry_csss_value: masterframe.transferframe1.telemetry.csss.value
    :field transferframe1_telemetry_cmfs0_raw: masterframe.transferframe1.telemetry.cmfs0.raw
    :field transferframe1_telemetry_cmfs0_value: masterframe.transferframe1.telemetry.cmfs0.value
    :field transferframe1_telemetry_cmfs1_raw: masterframe.transferframe1.telemetry.cmfs1.raw
    :field transferframe1_telemetry_cmfs1_value: masterframe.transferframe1.telemetry.cmfs1.value
    :field transferframe1_telemetry_cgyr0_raw: masterframe.transferframe1.telemetry.cgyr0.raw
    :field transferframe1_telemetry_cgyr0_value: masterframe.transferframe1.telemetry.cgyr0.value
    :field transferframe1_telemetry_cmcs_raw: masterframe.transferframe1.telemetry.cmcs.raw
    :field transferframe1_telemetry_cmcs_value: masterframe.transferframe1.telemetry.cmcs.value
    :field transferframe1_telemetry_cwhl_raw: masterframe.transferframe1.telemetry.cwhl.raw
    :field transferframe1_telemetry_cwhl_value: masterframe.transferframe1.telemetry.cwhl.value
    :field transferframe1_telemetry_ccan0_raw: masterframe.transferframe1.telemetry.ccan0.raw
    :field transferframe1_telemetry_ccan0_value: masterframe.transferframe1.telemetry.ccan0.value
    :field transferframe1_telemetry_ccan1_raw: masterframe.transferframe1.telemetry.ccan1.raw
    :field transferframe1_telemetry_ccan1_value: masterframe.transferframe1.telemetry.ccan1.value
    :field transferframe1_telemetry_vmfs0_raw: masterframe.transferframe1.telemetry.vmfs0.raw
    :field transferframe1_telemetry_vmfs0_value: masterframe.transferframe1.telemetry.vmfs0.value
    :field transferframe1_telemetry_vmfs1_raw: masterframe.transferframe1.telemetry.vmfs1.raw
    :field transferframe1_telemetry_vmfs1_value: masterframe.transferframe1.telemetry.vmfs1.value
    :field transferframe1_telemetry_cmcsxp_raw: masterframe.transferframe1.telemetry.cmcsxp.raw
    :field transferframe1_telemetry_cmcsxp_value: masterframe.transferframe1.telemetry.cmcsxp.value
    :field transferframe1_telemetry_cmcsxn_raw: masterframe.transferframe1.telemetry.cmcsxn.raw
    :field transferframe1_telemetry_cmcsxn_value: masterframe.transferframe1.telemetry.cmcsxn.value
    :field transferframe1_telemetry_cmcsyp_raw: masterframe.transferframe1.telemetry.cmcsyp.raw
    :field transferframe1_telemetry_cmcsyp_value: masterframe.transferframe1.telemetry.cmcsyp.value
    :field transferframe1_telemetry_cmcsyn_raw: masterframe.transferframe1.telemetry.cmcsyn.raw
    :field transferframe1_telemetry_cmcsyn_value: masterframe.transferframe1.telemetry.cmcsyn.value
    :field transferframe1_telemetry_cmcszp_raw: masterframe.transferframe1.telemetry.cmcszp.raw
    :field transferframe1_telemetry_cmcszp_value: masterframe.transferframe1.telemetry.cmcszp.value
    :field transferframe1_telemetry_cmcszn_raw: masterframe.transferframe1.telemetry.cmcszn.raw
    :field transferframe1_telemetry_cmcszn_value: masterframe.transferframe1.telemetry.cmcszn.value
    :field transferframe1_telemetry_cobcmcu_raw: masterframe.transferframe1.telemetry.cobcmcu.raw
    :field transferframe1_telemetry_cobcmcu_value: masterframe.transferframe1.telemetry.cobcmcu.value
    :field transferframe1_telemetry_cobcext_raw: masterframe.transferframe1.telemetry.cobcext.raw
    :field transferframe1_telemetry_cobcext_value: masterframe.transferframe1.telemetry.cobcext.value
    :field transferframe1_telemetry_ttrx1_raw: masterframe.transferframe1.telemetry.ttrx1.raw
    :field transferframe1_telemetry_ttrx1_value: masterframe.transferframe1.telemetry.ttrx1.value
    :field transferframe1_telemetry_cpdh2_raw: masterframe.transferframe1.telemetry.cpdh2.raw
    :field transferframe1_telemetry_cpdh2_value: masterframe.transferframe1.telemetry.cpdh2.value
    :field transferframe1_telemetry_ccam2_raw: masterframe.transferframe1.telemetry.ccam2.raw
    :field transferframe1_telemetry_ccam2_value: masterframe.transferframe1.telemetry.ccam2.value
    :field transferframe1_asstop: masterframe.transferframe1.telemetry.asstop
    :field transferframe1_assintv: masterframe.transferframe1.telemetry.assintv
    :field transferframe1_ascest: masterframe.transferframe1.telemetry.ascest
    :field transferframe1_asactv: masterframe.transferframe1.telemetry.asactv
    :field transferframe1_reserve2: masterframe.transferframe1.telemetry.reserve2
    :field transferframe1_reserve1: masterframe.transferframe1.telemetry.reserve1
    :field transferframe1_telemetry_tsaxp_raw: masterframe.transferframe1.telemetry.tsaxp.raw
    :field transferframe1_telemetry_tsaxp_value: masterframe.transferframe1.telemetry.tsaxp.value
    :field transferframe1_telemetry_tsaxn_raw: masterframe.transferframe1.telemetry.tsaxn.raw
    :field transferframe1_telemetry_tsaxn_value: masterframe.transferframe1.telemetry.tsaxn.value
    :field transferframe1_telemetry_tsayp_raw: masterframe.transferframe1.telemetry.tsayp.raw
    :field transferframe1_telemetry_tsayp_value: masterframe.transferframe1.telemetry.tsayp.value
    :field transferframe1_telemetry_tsayn_raw: masterframe.transferframe1.telemetry.tsayn.raw
    :field transferframe1_telemetry_tsayn_value: masterframe.transferframe1.telemetry.tsayn.value
    :field transferframe1_telemetry_tsazp_raw: masterframe.transferframe1.telemetry.tsazp.raw
    :field transferframe1_telemetry_tsazp_value: masterframe.transferframe1.telemetry.tsazp.value
    :field transferframe1_telemetry_tsazn_raw: masterframe.transferframe1.telemetry.tsazn.raw
    :field transferframe1_telemetry_tsazn_value: masterframe.transferframe1.telemetry.tsazn.value
    :field transferframe1_telemetry_tbat0_raw: masterframe.transferframe1.telemetry.tbat0.raw
    :field transferframe1_telemetry_tbat0_value: masterframe.transferframe1.telemetry.tbat0.value
    :field transferframe1_telemetry_tbat1_raw: masterframe.transferframe1.telemetry.tbat1.raw
    :field transferframe1_telemetry_tbat1_value: masterframe.transferframe1.telemetry.tbat1.value
    :field transferframe1_telemetry_tpcu00_raw: masterframe.transferframe1.telemetry.tpcu00.raw
    :field transferframe1_telemetry_tpcu00_value: masterframe.transferframe1.telemetry.tpcu00.value
    :field transferframe1_telemetry_tpcu01_raw: masterframe.transferframe1.telemetry.tpcu01.raw
    :field transferframe1_telemetry_tpcu01_value: masterframe.transferframe1.telemetry.tpcu01.value
    :field transferframe1_telemetry_tmfs0_raw: masterframe.transferframe1.telemetry.tmfs0.raw
    :field transferframe1_telemetry_tmfs0_value: masterframe.transferframe1.telemetry.tmfs0.value
    :field transferframe1_telemetry_tmfs1_raw: masterframe.transferframe1.telemetry.tmfs1.raw
    :field transferframe1_telemetry_tmfs1_value: masterframe.transferframe1.telemetry.tmfs1.value
    :field transferframe1_telemetry_twhlx_raw: masterframe.transferframe1.telemetry.twhlx.raw
    :field transferframe1_telemetry_twhlx_value: masterframe.transferframe1.telemetry.twhlx.value
    :field transferframe1_telemetry_twhly_raw: masterframe.transferframe1.telemetry.twhly.raw
    :field transferframe1_telemetry_twhly_value: masterframe.transferframe1.telemetry.twhly.value
    :field transferframe1_telemetry_twhlz_raw: masterframe.transferframe1.telemetry.twhlz.raw
    :field transferframe1_telemetry_twhlz_value: masterframe.transferframe1.telemetry.twhlz.value
    :field transferframe1_telemetry_tgyrox_raw: masterframe.transferframe1.telemetry.tgyrox.raw
    :field transferframe1_telemetry_tgyrox_value: masterframe.transferframe1.telemetry.tgyrox.value
    :field transferframe1_telemetry_tgyroy_raw: masterframe.transferframe1.telemetry.tgyroy.raw
    :field transferframe1_telemetry_tgyroy_value: masterframe.transferframe1.telemetry.tgyroy.value
    :field transferframe1_telemetry_tgyroz_raw: masterframe.transferframe1.telemetry.tgyroz.raw
    :field transferframe1_telemetry_tgyroz_value: masterframe.transferframe1.telemetry.tgyroz.value
    :field transferframe1_telemetry_tobc00_raw: masterframe.transferframe1.telemetry.tobc00.raw
    :field transferframe1_telemetry_tobc00_value: masterframe.transferframe1.telemetry.tobc00.value
    :field transferframe1_telemetry_tobc01_raw: masterframe.transferframe1.telemetry.tobc01.raw
    :field transferframe1_telemetry_tobc01_value: masterframe.transferframe1.telemetry.tobc01.value
    :field transferframe1_telemetry_tobc02_raw: masterframe.transferframe1.telemetry.tobc02.raw
    :field transferframe1_telemetry_tobc02_value: masterframe.transferframe1.telemetry.tobc02.value
    :field transferframe1_telemetry_ttrx0_raw: masterframe.transferframe1.telemetry.ttrx0.raw
    :field transferframe1_telemetry_ttrx0_value: masterframe.transferframe1.telemetry.ttrx0.value
    :field transferframe1_reserve: masterframe.transferframe1.telemetry.reserve
    :field transferframe1_telemetry_acssuxpx0_raw: masterframe.transferframe1.telemetry.acssuxpx0.raw
    :field transferframe1_telemetry_acssuxpx0_value: masterframe.transferframe1.telemetry.acssuxpx0.value
    :field transferframe1_telemetry_acssuxpx1_raw: masterframe.transferframe1.telemetry.acssuxpx1.raw
    :field transferframe1_telemetry_acssuxpx1_value: masterframe.transferframe1.telemetry.acssuxpx1.value
    :field transferframe1_telemetry_acssuxpy0_raw: masterframe.transferframe1.telemetry.acssuxpy0.raw
    :field transferframe1_telemetry_acssuxpy0_value: masterframe.transferframe1.telemetry.acssuxpy0.value
    :field transferframe1_telemetry_acssuxpy1_raw: masterframe.transferframe1.telemetry.acssuxpy1.raw
    :field transferframe1_telemetry_acssuxpy1_value: masterframe.transferframe1.telemetry.acssuxpy1.value
    :field transferframe1_telemetry_acssuxnx0_raw: masterframe.transferframe1.telemetry.acssuxnx0.raw
    :field transferframe1_telemetry_acssuxnx0_value: masterframe.transferframe1.telemetry.acssuxnx0.value
    :field transferframe1_telemetry_acssuxnx1_raw: masterframe.transferframe1.telemetry.acssuxnx1.raw
    :field transferframe1_telemetry_acssuxnx1_value: masterframe.transferframe1.telemetry.acssuxnx1.value
    :field transferframe1_telemetry_acssuxny0_raw: masterframe.transferframe1.telemetry.acssuxny0.raw
    :field transferframe1_telemetry_acssuxny0_value: masterframe.transferframe1.telemetry.acssuxny0.value
    :field transferframe1_telemetry_acssuxny1_raw: masterframe.transferframe1.telemetry.acssuxny1.raw
    :field transferframe1_telemetry_acssuxny1_value: masterframe.transferframe1.telemetry.acssuxny1.value
    :field transferframe1_telemetry_acssuypx0_raw: masterframe.transferframe1.telemetry.acssuypx0.raw
    :field transferframe1_telemetry_acssuypx0_value: masterframe.transferframe1.telemetry.acssuypx0.value
    :field transferframe1_telemetry_acssuypx1_raw: masterframe.transferframe1.telemetry.acssuypx1.raw
    :field transferframe1_telemetry_acssuypx1_value: masterframe.transferframe1.telemetry.acssuypx1.value
    :field transferframe1_telemetry_acssuypy0_raw: masterframe.transferframe1.telemetry.acssuypy0.raw
    :field transferframe1_telemetry_acssuypy0_value: masterframe.transferframe1.telemetry.acssuypy0.value
    :field transferframe1_telemetry_acssuypy1_raw: masterframe.transferframe1.telemetry.acssuypy1.raw
    :field transferframe1_telemetry_acssuypy1_value: masterframe.transferframe1.telemetry.acssuypy1.value
    :field transferframe1_telemetry_acssuynx0_raw: masterframe.transferframe1.telemetry.acssuynx0.raw
    :field transferframe1_telemetry_acssuynx0_value: masterframe.transferframe1.telemetry.acssuynx0.value
    :field transferframe1_telemetry_acssuynx1_raw: masterframe.transferframe1.telemetry.acssuynx1.raw
    :field transferframe1_telemetry_acssuynx1_value: masterframe.transferframe1.telemetry.acssuynx1.value
    :field transferframe1_telemetry_acssuyny0_raw: masterframe.transferframe1.telemetry.acssuyny0.raw
    :field transferframe1_telemetry_acssuyny0_value: masterframe.transferframe1.telemetry.acssuyny0.value
    :field transferframe1_telemetry_acssuyny1_raw: masterframe.transferframe1.telemetry.acssuyny1.raw
    :field transferframe1_telemetry_acssuyny1_value: masterframe.transferframe1.telemetry.acssuyny1.value
    :field transferframe1_telemetry_acssuzpx0_raw: masterframe.transferframe1.telemetry.acssuzpx0.raw
    :field transferframe1_telemetry_acssuzpx0_value: masterframe.transferframe1.telemetry.acssuzpx0.value
    :field transferframe1_telemetry_acssuzpx1_raw: masterframe.transferframe1.telemetry.acssuzpx1.raw
    :field transferframe1_telemetry_acssuzpx1_value: masterframe.transferframe1.telemetry.acssuzpx1.value
    :field transferframe1_telemetry_acssuzpy0_raw: masterframe.transferframe1.telemetry.acssuzpy0.raw
    :field transferframe1_telemetry_acssuzpy0_value: masterframe.transferframe1.telemetry.acssuzpy0.value
    :field transferframe1_telemetry_acssuzpy1_raw: masterframe.transferframe1.telemetry.acssuzpy1.raw
    :field transferframe1_telemetry_acssuzpy1_value: masterframe.transferframe1.telemetry.acssuzpy1.value
    :field transferframe1_telemetry_acssuznx0_raw: masterframe.transferframe1.telemetry.acssuznx0.raw
    :field transferframe1_telemetry_acssuznx0_value: masterframe.transferframe1.telemetry.acssuznx0.value
    :field transferframe1_telemetry_acssuznx1_raw: masterframe.transferframe1.telemetry.acssuznx1.raw
    :field transferframe1_telemetry_acssuznx1_value: masterframe.transferframe1.telemetry.acssuznx1.value
    :field transferframe1_telemetry_acssuzny0_raw: masterframe.transferframe1.telemetry.acssuzny0.raw
    :field transferframe1_telemetry_acssuzny0_value: masterframe.transferframe1.telemetry.acssuzny0.value
    :field transferframe1_telemetry_acssuzny1_raw: masterframe.transferframe1.telemetry.acssuzny1.raw
    :field transferframe1_telemetry_acssuzny1_value: masterframe.transferframe1.telemetry.acssuzny1.value
    :field transferframe1_telemetry_cmfs0x_raw: masterframe.transferframe1.telemetry.cmfs0x.raw
    :field transferframe1_telemetry_cmfs0x_value: masterframe.transferframe1.telemetry.cmfs0x.value
    :field transferframe1_telemetry_cmfs0y_raw: masterframe.transferframe1.telemetry.cmfs0y.raw
    :field transferframe1_telemetry_cmfs0y_value: masterframe.transferframe1.telemetry.cmfs0y.value
    :field transferframe1_telemetry_cmfs0z_raw: masterframe.transferframe1.telemetry.cmfs0z.raw
    :field transferframe1_telemetry_cmfs0z_value: masterframe.transferframe1.telemetry.cmfs0z.value
    :field transferframe1_telemetry_cmfs1x_raw: masterframe.transferframe1.telemetry.cmfs1x.raw
    :field transferframe1_telemetry_cmfs1x_value: masterframe.transferframe1.telemetry.cmfs1x.value
    :field transferframe1_telemetry_cmfs1y_raw: masterframe.transferframe1.telemetry.cmfs1y.raw
    :field transferframe1_telemetry_cmfs1y_value: masterframe.transferframe1.telemetry.cmfs1y.value
    :field transferframe1_telemetry_cmfs1z_raw: masterframe.transferframe1.telemetry.cmfs1z.raw
    :field transferframe1_telemetry_cmfs1z_value: masterframe.transferframe1.telemetry.cmfs1z.value
    :field transferframe1_telemetry_acsgy0x_raw: masterframe.transferframe1.telemetry.acsgy0x.raw
    :field transferframe1_telemetry_acsgy0x_value: masterframe.transferframe1.telemetry.acsgy0x.value
    :field transferframe1_telemetry_acsgy0y_raw: masterframe.transferframe1.telemetry.acsgy0y.raw
    :field transferframe1_telemetry_acsgy0y_value: masterframe.transferframe1.telemetry.acsgy0y.value
    :field transferframe1_telemetry_acsgy0z_raw: masterframe.transferframe1.telemetry.acsgy0z.raw
    :field transferframe1_telemetry_acsgy0z_value: masterframe.transferframe1.telemetry.acsgy0z.value
    :field transferframe1_telemetry_reserve1_raw: masterframe.transferframe1.telemetry.reserve1.raw
    :field transferframe1_telemetry_reserve1_value: masterframe.transferframe1.telemetry.reserve1.value
    :field transferframe1_psant0: masterframe.transferframe1.telemetry.psant0
    :field transferframe1_psant1: masterframe.transferframe1.telemetry.psant1
    :field transferframe1_psgyr1: masterframe.transferframe1.telemetry.psgyr1
    :field transferframe1_pscom1: masterframe.transferframe1.telemetry.pscom1
    :field transferframe1_psuhf0: masterframe.transferframe1.telemetry.psuhf0
    :field transferframe1_psuhf1: masterframe.transferframe1.telemetry.psuhf1
    :field transferframe1_pstnc0: masterframe.transferframe1.telemetry.pstnc0
    :field transferframe1_pstnc1: masterframe.transferframe1.telemetry.pstnc1
    :field transferframe1_psgyr0: masterframe.transferframe1.telemetry.psgyr0
    :field transferframe1_psmcsx: masterframe.transferframe1.telemetry.psmcsx
    :field transferframe1_psmcsy: masterframe.transferframe1.telemetry.psmcsy
    :field transferframe1_psmcsz: masterframe.transferframe1.telemetry.psmcsz
    :field transferframe1_pswhls: masterframe.transferframe1.telemetry.pswhls
    :field transferframe1_psobc0: masterframe.transferframe1.telemetry.psobc0
    :field transferframe1_psobc1: masterframe.transferframe1.telemetry.psobc1
    :field transferframe1_pspdh0: masterframe.transferframe1.telemetry.pspdh0
    :field transferframe1_pscam0: masterframe.transferframe1.telemetry.pscam0
    :field transferframe1_pssuns: masterframe.transferframe1.telemetry.pssuns
    :field transferframe1_psmfs0: masterframe.transferframe1.telemetry.psmfs0
    :field transferframe1_psms1: masterframe.transferframe1.telemetry.psms1
    :field transferframe1_pstemp: masterframe.transferframe1.telemetry.pstemp
    :field transferframe1_pscan0: masterframe.transferframe1.telemetry.pscan0
    :field transferframe1_pscan1: masterframe.transferframe1.telemetry.pscan1
    :field transferframe1_psccw0: masterframe.transferframe1.telemetry.psccw0
    :field transferframe1_psccw1: masterframe.transferframe1.telemetry.psccw1
    :field transferframe1_ps5vcn: masterframe.transferframe1.telemetry.ps5vcn
    :field transferframe1_pcuaid: masterframe.transferframe1.telemetry.pcuaid
    :field transferframe1_pcbobc: masterframe.transferframe1.telemetry.pcbobc
    :field transferframe1_pcbext: masterframe.transferframe1.telemetry.pcbext
    :field transferframe1_pcch00: masterframe.transferframe1.telemetry.pcch00
    :field transferframe1_pcch01: masterframe.transferframe1.telemetry.pcch01
    :field transferframe1_pccho2: masterframe.transferframe1.telemetry.pccho2
    :field transferframe1_pcch03: masterframe.transferframe1.telemetry.pcch03
    :field transferframe1_pcch04: masterframe.transferframe1.telemetry.pcch04
    :field transferframe1_pcch05: masterframe.transferframe1.telemetry.pcch05
    :field transferframe1_pcch06: masterframe.transferframe1.telemetry.pcch06
    :field transferframe1_telemetry_rxsig0_raw: masterframe.transferframe1.telemetry.rxsig0.raw
    :field transferframe1_telemetry_rxsig0_value: masterframe.transferframe1.telemetry.rxsig0.value
    :field transferframe1_pcch07: masterframe.transferframe1.telemetry.pcch07
    :field transferframe1_pcch08: masterframe.transferframe1.telemetry.pcch08
    :field transferframe1_pcch09: masterframe.transferframe1.telemetry.pcch09
    :field transferframe1_pcch10: masterframe.transferframe1.telemetry.pcch10
    :field transferframe1_telemetry_rxsig1_raw: masterframe.transferframe1.telemetry.rxsig1.raw
    :field transferframe1_telemetry_rxsig1_value: masterframe.transferframe1.telemetry.rxsig1.value
    :field transferframe1_pcch11: masterframe.transferframe1.telemetry.pcch11
    :field transferframe1_pcch12: masterframe.transferframe1.telemetry.pcch12
    :field transferframe1_pcch13: masterframe.transferframe1.telemetry.pcch13
    :field transferframe1_pcch14: masterframe.transferframe1.telemetry.pcch14
    :field transferframe1_pcch15: masterframe.transferframe1.telemetry.pcch15
    :field transferframe1_pcch16: masterframe.transferframe1.telemetry.pcch16
    :field transferframe1_pcch17: masterframe.transferframe1.telemetry.pcch17
    :field transferframe1_pcch18: masterframe.transferframe1.telemetry.pcch18
    :field transferframe1_pcch19: masterframe.transferframe1.telemetry.pcch19
    :field transferframe1_pcch20: masterframe.transferframe1.telemetry.pcch20
    :field transferframe1_pcch21: masterframe.transferframe1.telemetry.pcch21
    :field transferframe1_pcch22: masterframe.transferframe1.telemetry.pcch22
    :field transferframe1_pcch23: masterframe.transferframe1.telemetry.pcch23
    :field transferframe1_pcch24: masterframe.transferframe1.telemetry.pcch24
    :field transferframe1_pcch25: masterframe.transferframe1.telemetry.pcch25
    :field transferframe1_pcch26: masterframe.transferframe1.telemetry.pcch26
    :field transferframe1_tcrxid: masterframe.transferframe1.telemetry.tcrxid
    :field transferframe1_obcaid: masterframe.transferframe1.telemetry.obcaid
    :field transferframe1_tmtxrt: masterframe.transferframe1.telemetry.tmtxrt
    :field transferframe1_pcch27: masterframe.transferframe1.telemetry.pcch27
    :field transferframe1_pcch28: masterframe.transferframe1.telemetry.pcch28
    :field transferframe1_pcch29: masterframe.transferframe1.telemetry.pcch29
    :field transferframe1_pcch30: masterframe.transferframe1.telemetry.pcch30
    :field transferframe1_pcch31: masterframe.transferframe1.telemetry.pcch31
    :field transferframe1_cctcic: masterframe.transferframe1.telemetry.cctcic
    :field transferframe1_cctctt: masterframe.transferframe1.telemetry.cctctt
    :field transferframe1_ccetcs: masterframe.transferframe1.telemetry.ccetcs
    :field transferframe1_cceimc: masterframe.transferframe1.telemetry.cceimc
    :field transferframe1_ccettc: masterframe.transferframe1.telemetry.ccettc
    :field transferframe1_ccettg: masterframe.transferframe1.telemetry.ccettg
    :field transferframe1_ccetcc: masterframe.transferframe1.telemetry.ccetcc
    :field transferframe1_telemetry_tcrxqu_raw: masterframe.transferframe1.telemetry.tcrxqu.raw
    :field transferframe1_telemetry_tcrxqu_value: masterframe.transferframe1.telemetry.tcrxqu.value
    :field transferframe1_telemetry_tcfrcp_raw: masterframe.transferframe1.telemetry.tcfrcp.raw
    :field transferframe1_telemetry_tcfrcp_value: masterframe.transferframe1.telemetry.tcfrcp.value
    :field transferframe1_telemetry_tmhkur_raw: masterframe.transferframe1.telemetry.tmhkur.raw
    :field transferframe1_telemetry_tmhkur_value: masterframe.transferframe1.telemetry.tmhkur.value
    :field transferframe1_telemetry_cstsys_raw: masterframe.transferframe1.telemetry.cstsys.raw
    :field transferframe1_telemetry_cstsys_value: masterframe.transferframe1.telemetry.cstsys.value
    :field transferframe1_mcxpol: masterframe.transferframe1.telemetry.mcxpol
    :field transferframe1_mcypol: masterframe.transferframe1.telemetry.mcypol
    :field transferframe1_mczpol: masterframe.transferframe1.telemetry.mczpol
    :field transferframe1_telemetry_obcbad_raw: masterframe.transferframe1.telemetry.obcbad.raw
    :field transferframe1_telemetry_obcbad_value: masterframe.transferframe1.telemetry.obcbad.value
    :field transferframe1_ceswmc: masterframe.transferframe1.telemetry.ceswmc
    :field transferframe1_beacon: masterframe.transferframe1.telemetry.beacon
    :field transferframe1_telemetry_reserve3_raw: masterframe.transferframe1.telemetry.reserve3.raw
    :field transferframe1_telemetry_reserve3_value: masterframe.transferframe1.telemetry.reserve3.value
    :field transferframe1_telemetry_modcom_raw: masterframe.transferframe1.telemetry.modcom.raw
    :field transferframe1_telemetry_modcom_value: masterframe.transferframe1.telemetry.modcom.value
    :field transferframe1_obcabc: masterframe.transferframe1.telemetry.obcabc
    :field transferframe1_modobc: masterframe.transferframe1.telemetry.modobc
    :field transferframe1_ccecan: masterframe.transferframe1.telemetry.ccecan
    :field transferframe1_obccan: masterframe.transferframe1.telemetry.obccan
    :field transferframe1_telemetry_pcsyst_raw: masterframe.transferframe1.telemetry.pcsyst.raw
    :field transferframe1_telemetry_pcsyst_value: masterframe.transferframe1.telemetry.pcsyst.value
    :field transferframe1_pcbcnt: masterframe.transferframe1.telemetry.pcbcnt
    :field transferframe1_pctxec: masterframe.transferframe1.telemetry.pctxec
    :field transferframe1_pcrxec: masterframe.transferframe1.telemetry.pcrxec
    :field transferframe1_pcoffc: masterframe.transferframe1.telemetry.pcoffc
    :field transferframe1_pcackc: masterframe.transferframe1.telemetry.pcackc
    :field transferframe1_pcch32: masterframe.transferframe1.telemetry.pcch32
    :field transferframe1_pcch33: masterframe.transferframe1.telemetry.pcch33
    :field transferframe1_pcch34: masterframe.transferframe1.telemetry.pcch34
    :field transferframe1_pcch35: masterframe.transferframe1.telemetry.pcch35
    :field transferframe1_pcch36: masterframe.transferframe1.telemetry.pcch36
    :field transferframe1_pcch37: masterframe.transferframe1.telemetry.pcch37
    :field transferframe1_pcch38: masterframe.transferframe1.telemetry.pcch38
    :field transferframe1_pcch39: masterframe.transferframe1.telemetry.pcch39
    :field transferframe1_pcch40: masterframe.transferframe1.telemetry.pcch40
    :field transferframe1_pcch41: masterframe.transferframe1.telemetry.pcch41
    :field transferframe1_telemetry_reserve4_raw: masterframe.transferframe1.telemetry.reserve4.raw
    :field transferframe1_telemetry_reserve4_value: masterframe.transferframe1.telemetry.reserve4.value
    :field transferframe1_telemetry_reserve5_raw: masterframe.transferframe1.telemetry.reserve5.raw
    :field transferframe1_telemetry_reserve5_value: masterframe.transferframe1.telemetry.reserve5.value
    :field transferframe1_telemetry_reserve6_raw: masterframe.transferframe1.telemetry.reserve6.raw
    :field transferframe1_telemetry_reserve6_value: masterframe.transferframe1.telemetry.reserve6.value
    :field transferframe1_telemetry_reserve7_raw: masterframe.transferframe1.telemetry.reserve7.raw
    :field transferframe1_telemetry_reserve7_value: masterframe.transferframe1.telemetry.reserve7.value
    :field transferframe1_telemetry_acswhx_raw: masterframe.transferframe1.telemetry.acswhx.raw
    :field transferframe1_telemetry_acswhx_value: masterframe.transferframe1.telemetry.acswhx.value
    :field transferframe1_telemetry_acswhy_raw: masterframe.transferframe1.telemetry.acswhy.raw
    :field transferframe1_telemetry_acswhy_value: masterframe.transferframe1.telemetry.acswhy.value
    :field transferframe1_telemetry_acswhz_raw: masterframe.transferframe1.telemetry.acswhz.raw
    :field transferframe1_telemetry_acswhz_value: masterframe.transferframe1.telemetry.acswhz.value
    :field transferframe1_telemetry_acsq00_raw: masterframe.transferframe1.telemetry.acsq00.raw
    :field transferframe1_telemetry_acsq00_value: masterframe.transferframe1.telemetry.acsq00.value
    :field transferframe1_telemetry_acsq01_raw: masterframe.transferframe1.telemetry.acsq01.raw
    :field transferframe1_telemetry_acsq01_value: masterframe.transferframe1.telemetry.acsq01.value
    :field transferframe1_telemetry_acsq02_raw: masterframe.transferframe1.telemetry.acsq02.raw
    :field transferframe1_telemetry_acsq02_value: masterframe.transferframe1.telemetry.acsq02.value
    :field transferframe1_telemetry_acsq03_raw: masterframe.transferframe1.telemetry.acsq03.raw
    :field transferframe1_telemetry_acsq03_value: masterframe.transferframe1.telemetry.acsq03.value
    :field transferframe1_telemetry_acssux_raw: masterframe.transferframe1.telemetry.acssux.raw
    :field transferframe1_telemetry_acssux_value: masterframe.transferframe1.telemetry.acssux.value
    :field transferframe1_telemetry_acssuy_raw: masterframe.transferframe1.telemetry.acssuy.raw
    :field transferframe1_telemetry_acssuy_value: masterframe.transferframe1.telemetry.acssuy.value
    :field transferframe1_telemetry_acssuz_raw: masterframe.transferframe1.telemetry.acssuz.raw
    :field transferframe1_telemetry_acssuz_value: masterframe.transferframe1.telemetry.acssuz.value
    :field transferframe1_telemetry_acsmox_raw: masterframe.transferframe1.telemetry.acsmox.raw
    :field transferframe1_telemetry_acsmox_value: masterframe.transferframe1.telemetry.acsmox.value
    :field transferframe1_telemetry_acsmoy_raw: masterframe.transferframe1.telemetry.acsmoy.raw
    :field transferframe1_telemetry_acsmoy_value: masterframe.transferframe1.telemetry.acsmoy.value
    :field transferframe1_telemetry_acsmoz_raw: masterframe.transferframe1.telemetry.acsmoz.raw
    :field transferframe1_telemetry_acsmoz_value: masterframe.transferframe1.telemetry.acsmoz.value
    :field transferframe1_telemetry_acsm1x_raw: masterframe.transferframe1.telemetry.acsm1x.raw
    :field transferframe1_telemetry_acsm1x_value: masterframe.transferframe1.telemetry.acsm1x.value
    :field transferframe1_telemetry_acsm1y_raw: masterframe.transferframe1.telemetry.acsm1y.raw
    :field transferframe1_telemetry_acsm1y_value: masterframe.transferframe1.telemetry.acsm1y.value
    :field transferframe1_telemetry_acsm1z_raw: masterframe.transferframe1.telemetry.acsm1z.raw
    :field transferframe1_telemetry_acsm1z_value: masterframe.transferframe1.telemetry.acsm1z.value
    :field transferframe1_telemetry_modacs_raw: masterframe.transferframe1.telemetry.modacs.raw
    :field transferframe1_telemetry_modacs_value: masterframe.transferframe1.telemetry.modacs.value
    :field transferframe1_acsgsc: masterframe.transferframe1.telemetry.acsgsc
    :field transferframe1_acsshd: masterframe.transferframe1.telemetry.acsshd
    :field transferframe1_telemetry_reserve8_raw: masterframe.transferframe1.telemetry.reserve8.raw
    :field transferframe1_telemetry_reserve8_value: masterframe.transferframe1.telemetry.reserve8.value
    :field transferframe1_acserr: masterframe.transferframe1.telemetry.acserr
    :field transferframe1_telemetry_acsg1y_raw: masterframe.transferframe1.telemetry.acsg1y.raw
    :field transferframe1_telemetry_acsg1y_value: masterframe.transferframe1.telemetry.acsg1y.value
    :field transferframe1_telemetry_acsg1z_raw: masterframe.transferframe1.telemetry.acsg1z.raw
    :field transferframe1_telemetry_acsg1z_value: masterframe.transferframe1.telemetry.acsg1z.value
    :field transferframe1_telemetry_acsg1x_raw: masterframe.transferframe1.telemetry.acsg1x.raw
    :field transferframe1_telemetry_acsg1x_value: masterframe.transferframe1.telemetry.acsg1x.value
    :field transferframe1_telemetry_reserve9_raw: masterframe.transferframe1.telemetry.reserve9.raw
    :field transferframe1_telemetry_reserve9_value: masterframe.transferframe1.telemetry.reserve9.value
    :field transferframe1_telemetry_reserve10_raw: masterframe.transferframe1.telemetry.reserve10.raw
    :field transferframe1_telemetry_reserve10_value: masterframe.transferframe1.telemetry.reserve10.value
    :field transferframe1_crc000: masterframe.transferframe1.telemetry.crc000
    :field transferframe1_crc001: masterframe.transferframe1.telemetry.crc001
    :field transferframe1_crc002: masterframe.transferframe1.telemetry.crc002
    :field transferframe1_crc003: masterframe.transferframe1.telemetry.crc003
    :field transferframe1_crc004: masterframe.transferframe1.telemetry.crc004
    :field transferframe1_crc005: masterframe.transferframe1.telemetry.crc005
    :field transferframe1_crc006: masterframe.transferframe1.telemetry.crc006
    :field transferframe1_crc007: masterframe.transferframe1.telemetry.crc007
    :field transferframe1_crc008: masterframe.transferframe1.telemetry.crc008
    :field transferframe1_crc009: masterframe.transferframe1.telemetry.crc009
    :field transferframe1_crc010: masterframe.transferframe1.telemetry.crc010
    :field transferframe1_crc011: masterframe.transferframe1.telemetry.crc011
    :field transferframe1_crc012: masterframe.transferframe1.telemetry.crc012
    :field transferframe1_crc013: masterframe.transferframe1.telemetry.crc013
    :field transferframe1_crc014: masterframe.transferframe1.telemetry.crc014
    :field transferframe1_crc015: masterframe.transferframe1.telemetry.crc015
    :field transferframe1_crc016: masterframe.transferframe1.telemetry.crc016
    :field transferframe1_crc017: masterframe.transferframe1.telemetry.crc017
    :field transferframe1_crc018: masterframe.transferframe1.telemetry.crc018
    :field transferframe1_crc019: masterframe.transferframe1.telemetry.crc019
    :field transferframe1_crc020: masterframe.transferframe1.telemetry.crc020
    :field transferframe1_crc021: masterframe.transferframe1.telemetry.crc021
    :field transferframe1_crc022: masterframe.transferframe1.telemetry.crc022
    :field transferframe1_crc023: masterframe.transferframe1.telemetry.crc023
    :field transferframe1_crc024: masterframe.transferframe1.telemetry.crc024
    :field transferframe1_crc025: masterframe.transferframe1.telemetry.crc025
    :field transferframe1_crc026: masterframe.transferframe1.telemetry.crc026
    :field transferframe1_crc027: masterframe.transferframe1.telemetry.crc027
    :field transferframe1_crc028: masterframe.transferframe1.telemetry.crc028
    :field transferframe1_crc029: masterframe.transferframe1.telemetry.crc029
    :field transferframe1_crc030: masterframe.transferframe1.telemetry.crc030
    :field transferframe1_dummy: masterframe.transferframe1.telemetry.dummy
    :field transferframe1_imhd00: masterframe.transferframe1.telemetry.imhd00
    :field transferframe1_imhd01: masterframe.transferframe1.telemetry.imhd01
    :field transferframe1_imhd02: masterframe.transferframe1.telemetry.imhd02
    :field transferframe1_imhd03: masterframe.transferframe1.telemetry.imhd03
    :field transferframe1_imhd04: masterframe.transferframe1.telemetry.imhd04
    :field transferframe1_imhd10: masterframe.transferframe1.telemetry.imhd10
    :field transferframe1_imhd11: masterframe.transferframe1.telemetry.imhd11
    :field transferframe1_imhd12: masterframe.transferframe1.telemetry.imhd12
    :field transferframe1_imhd13: masterframe.transferframe1.telemetry.imhd13
    :field transferframe1_imhd14: masterframe.transferframe1.telemetry.imhd14
    :field transferframe1_imhd20: masterframe.transferframe1.telemetry.imhd20
    :field transferframe1_imhd21: masterframe.transferframe1.telemetry.imhd21
    :field transferframe1_imhd22: masterframe.transferframe1.telemetry.imhd22
    :field transferframe1_imhd23: masterframe.transferframe1.telemetry.imhd23
    :field transferframe1_imhd24: masterframe.transferframe1.telemetry.imhd24
    :field transferframe1_imhd30: masterframe.transferframe1.telemetry.imhd30
    :field transferframe1_imhd31: masterframe.transferframe1.telemetry.imhd31
    :field transferframe1_imhd32: masterframe.transferframe1.telemetry.imhd32
    :field transferframe1_imhd33: masterframe.transferframe1.telemetry.imhd33
    :field transferframe1_imhd34: masterframe.transferframe1.telemetry.imhd34
    :field transferframe1_reserver20: masterframe.transferframe1.telemetry.reserver20
    :field transferframe1_image_id: masterframe.transferframe1.telemetry.image_id
    :field transferframe1_pdh_image: masterframe.transferframe1.telemetry.pdh_image
    :field transferframe1_telemetry_cpdhmcu_raw: masterframe.transferframe1.telemetry.cpdhmcu.raw
    :field transferframe1_telemetry_cpdhmcu_value: masterframe.transferframe1.telemetry.cpdhmcu.value
    :field transferframe1_telemetry_cpdhcam_raw: masterframe.transferframe1.telemetry.cpdhcam.raw
    :field transferframe1_telemetry_cpdhcam_value: masterframe.transferframe1.telemetry.cpdhcam.value
    :field transferframe1_tpdhcam: masterframe.transferframe1.telemetry.tpdhcam
    :field transferframe1_pdhceccm: masterframe.transferframe1.telemetry.pdhceccm
    :field transferframe1_pdhcectc: masterframe.transferframe1.telemetry.pdhcectc
    :field transferframe1_pdhcetlii: masterframe.transferframe1.telemetry.pdhcetlii
    :field transferframe1_pdhcetlc: masterframe.transferframe1.telemetry.pdhcetlc
    :field transferframe1_pdhti: masterframe.transferframe1.telemetry.pdhti
    :field transferframe1_pdhth: masterframe.transferframe1.telemetry.pdhth
    :field transferframe1_pdhceisi: masterframe.transferframe1.telemetry.pdhceisi
    :field transferframe1_pdhceici: masterframe.transferframe1.telemetry.pdhceici
    :field transferframe1_pdhceids: masterframe.transferframe1.telemetry.pdhceids
    :field transferframe1_pdhmode: masterframe.transferframe1.telemetry.pdhmode
    :field transferframe1_pdhcii: masterframe.transferframe1.telemetry.pdhcii
    :field transferframe1_pdhcih: masterframe.transferframe1.telemetry.pdhcih
    :field transferframe1_pdhcescm: masterframe.transferframe1.telemetry.pdhcescm
    :field transferframe1_pdhcessm: masterframe.transferframe1.telemetry.pdhcessm
    :field transferframe1_pdhcescb: masterframe.transferframe1.telemetry.pdhcescb
    :field transferframe1_pdhceslb: masterframe.transferframe1.telemetry.pdhceslb
    :field transferframe1_pdhcesss: masterframe.transferframe1.telemetry.pdhcesss
    :field transferframe1_pdhcessb: masterframe.transferframe1.telemetry.pdhcessb
    :field transferframe1_pdhceseb: masterframe.transferframe1.telemetry.pdhceseb
    :field transferframe1_pdhcesci: masterframe.transferframe1.telemetry.pdhcesci
    :field transferframe1_pdhcsi: masterframe.transferframe1.telemetry.pdhcsi
    :field transferframe1_pdhcsh: masterframe.transferframe1.telemetry.pdhcsh
    :field transferframe1_pdhbtimg: masterframe.transferframe1.telemetry.pdhbtimg
    :field transferframe1_pdhswversion: masterframe.transferframe1.telemetry.pdhswversion
    :field transferframe1_pdhcstsys: masterframe.transferframe1.telemetry.pdhcstsys
    :field transferframe1_pdhctstutc: masterframe.transferframe1.telemetry.pdhctstutc
    :field transferframe1_pdh_reserve: masterframe.transferframe1.telemetry.pdh_reserve
    :field transferframe1_pdhcrc000: masterframe.transferframe1.telemetry.pdhcrc000
    :field transferframe1_pdhcrc001: masterframe.transferframe1.telemetry.pdhcrc001
    :field transferframe1_pdhcrc002: masterframe.transferframe1.telemetry.pdhcrc002
    :field transferframe1_pdhcrc003: masterframe.transferframe1.telemetry.pdhcrc003
    :field transferframe1_pdhcrc004: masterframe.transferframe1.telemetry.pdhcrc004
    :field transferframe1_pdhcrc005: masterframe.transferframe1.telemetry.pdhcrc005
    :field transferframe1_pdhcrc006: masterframe.transferframe1.telemetry.pdhcrc006
    :field transferframe1_pdhcrc007: masterframe.transferframe1.telemetry.pdhcrc007
    :field transferframe1_pdhcrc008: masterframe.transferframe1.telemetry.pdhcrc008
    :field transferframe1_pdhcrc009: masterframe.transferframe1.telemetry.pdhcrc009
    :field transferframe1_pdhcrc010: masterframe.transferframe1.telemetry.pdhcrc010
    :field transferframe1_pdhcrc011: masterframe.transferframe1.telemetry.pdhcrc011
    :field transferframe1_pdhcrc012: masterframe.transferframe1.telemetry.pdhcrc012
    :field transferframe1_pdhcrc013: masterframe.transferframe1.telemetry.pdhcrc013
    :field transferframe1_pdhcrc014: masterframe.transferframe1.telemetry.pdhcrc014
    :field transferframe1_pdhcrc015: masterframe.transferframe1.telemetry.pdhcrc015
    :field transferframe1_pdhcrc016: masterframe.transferframe1.telemetry.pdhcrc016
    :field transferframe1_pdhcrc017: masterframe.transferframe1.telemetry.pdhcrc017
    :field transferframe1_pdhcrc018: masterframe.transferframe1.telemetry.pdhcrc018
    :field transferframe1_pdhcrc019: masterframe.transferframe1.telemetry.pdhcrc019
    :field transferframe1_pdhcrc020: masterframe.transferframe1.telemetry.pdhcrc020
    :field transferframe1_pdhcrc021: masterframe.transferframe1.telemetry.pdhcrc021
    :field transferframe1_pdhcrc022: masterframe.transferframe1.telemetry.pdhcrc022
    :field transferframe1_pdhcrc023: masterframe.transferframe1.telemetry.pdhcrc023
    :field transferframe1_pdhcrc024: masterframe.transferframe1.telemetry.pdhcrc024
    :field transferframe1_pdhcrc025: masterframe.transferframe1.telemetry.pdhcrc025
    :field transferframe1_pdhcrc026: masterframe.transferframe1.telemetry.pdhcrc026
    :field transferframe1_pdhcrc027: masterframe.transferframe1.telemetry.pdhcrc027
    :field transferframe1_pdhcrc028: masterframe.transferframe1.telemetry.pdhcrc028
    :field transferframe1_pdhcrc029: masterframe.transferframe1.telemetry.pdhcrc029
    :field transferframe1_pdhcrc030: masterframe.transferframe1.telemetry.pdhcrc030
    :field transferframe1_pdhcrccmask00: masterframe.transferframe1.telemetry.pdhcrccmask00
    :field transferframe1_acswhx: masterframe.transferframe1.telemetry.acswhx
    :field transferframe1_telemetry_acsm0x_raw: masterframe.transferframe1.telemetry.acsm0x.raw
    :field transferframe1_telemetry_acsm0x_value: masterframe.transferframe1.telemetry.acsm0x.value
    :field transferframe1_telemetry_acsm0y_raw: masterframe.transferframe1.telemetry.acsm0y.raw
    :field transferframe1_telemetry_acsm0y_value: masterframe.transferframe1.telemetry.acsm0y.value
    :field transferframe1_telemetry_acsm0z_raw: masterframe.transferframe1.telemetry.acsm0z.raw
    :field transferframe1_telemetry_acsm0z_value: masterframe.transferframe1.telemetry.acsm0z.value
    :field transferframe1_reserveacsgr: masterframe.transferframe1.telemetry.reserveacsgr
    :field transferframe1_acstemex: masterframe.transferframe1.telemetry.acstemex
    :field transferframe1_acstemey: masterframe.transferframe1.telemetry.acstemey
    :field transferframe1_acstemez: masterframe.transferframe1.telemetry.acstemez
    :field transferframe1_telemetry_acstemevelx_raw: masterframe.transferframe1.telemetry.acstemevelx.raw
    :field transferframe1_telemetry_acstemevelx_value: masterframe.transferframe1.telemetry.acstemevelx.value
    :field transferframe1_telemetry_acstemevely_raw: masterframe.transferframe1.telemetry.acstemevely.raw
    :field transferframe1_telemetry_acstemevely_value: masterframe.transferframe1.telemetry.acstemevely.value
    :field transferframe1_telemetry_acstemevelz_raw: masterframe.transferframe1.telemetry.acstemevelz.raw
    :field transferframe1_telemetry_acstemevelz_value: masterframe.transferframe1.telemetry.acstemevelz.value
    :field transferframe1_acsefx: masterframe.transferframe1.telemetry.acsefx
    :field transferframe1_acsefy: masterframe.transferframe1.telemetry.acsefy
    :field transferframe1_acsefz: masterframe.transferframe1.telemetry.acsefz
    :field transferframe1_telemetry_acsmagifx_raw: masterframe.transferframe1.telemetry.acsmagifx.raw
    :field transferframe1_telemetry_acsmagifx_value: masterframe.transferframe1.telemetry.acsmagifx.value
    :field transferframe1_telemetry_acsmagify_raw: masterframe.transferframe1.telemetry.acsmagify.raw
    :field transferframe1_telemetry_acsmagify_value: masterframe.transferframe1.telemetry.acsmagify.value
    :field transferframe1_telemetry_acsmagifz_raw: masterframe.transferframe1.telemetry.acsmagifz.raw
    :field transferframe1_telemetry_acsmagifz_value: masterframe.transferframe1.telemetry.acsmagifz.value
    :field transferframe1_telemetry_acssunifx_raw: masterframe.transferframe1.telemetry.acssunifx.raw
    :field transferframe1_telemetry_acssunifx_value: masterframe.transferframe1.telemetry.acssunifx.value
    :field transferframe1_telemetry_acssunify_raw: masterframe.transferframe1.telemetry.acssunify.raw
    :field transferframe1_telemetry_acssunify_value: masterframe.transferframe1.telemetry.acssunify.value
    :field transferframe1_telemetry_acssunifz_raw: masterframe.transferframe1.telemetry.acssunifz.raw
    :field transferframe1_telemetry_acssunifz_value: masterframe.transferframe1.telemetry.acssunifz.value
    :field transferframe1_telemetry_acsqdes00_raw: masterframe.transferframe1.telemetry.acsqdes00.raw
    :field transferframe1_telemetry_acsqdes00_value: masterframe.transferframe1.telemetry.acsqdes00.value
    :field transferframe1_telemetry_acsqdes01_raw: masterframe.transferframe1.telemetry.acsqdes01.raw
    :field transferframe1_telemetry_acsqdes01_value: masterframe.transferframe1.telemetry.acsqdes01.value
    :field transferframe1_telemetry_acsqdes02_raw: masterframe.transferframe1.telemetry.acsqdes02.raw
    :field transferframe1_telemetry_acsqdes02_value: masterframe.transferframe1.telemetry.acsqdes02.value
    :field transferframe1_telemetry_acsqdes03_raw: masterframe.transferframe1.telemetry.acsqdes03.raw
    :field transferframe1_telemetry_acsqdes03_value: masterframe.transferframe1.telemetry.acsqdes03.value
    :field transferframe1_telemetry_acswcx_raw: masterframe.transferframe1.telemetry.acswcx.raw
    :field transferframe1_telemetry_acswcx_value: masterframe.transferframe1.telemetry.acswcx.value
    :field transferframe1_telemetry_acswcy_raw: masterframe.transferframe1.telemetry.acswcy.raw
    :field transferframe1_telemetry_acswcy_value: masterframe.transferframe1.telemetry.acswcy.value
    :field transferframe1_telemetry_acswcz_raw: masterframe.transferframe1.telemetry.acswcz.raw
    :field transferframe1_telemetry_acswcz_value: masterframe.transferframe1.telemetry.acswcz.value
    :field transferframe1_telemetry_acswu0_raw: masterframe.transferframe1.telemetry.acswu0.raw
    :field transferframe1_telemetry_acswu0_value: masterframe.transferframe1.telemetry.acswu0.value
    :field transferframe1_telemetry_acswu1_raw: masterframe.transferframe1.telemetry.acswu1.raw
    :field transferframe1_telemetry_acswu1_value: masterframe.transferframe1.telemetry.acswu1.value
    :field transferframe1_telemetry_acswu2_raw: masterframe.transferframe1.telemetry.acswu2.raw
    :field transferframe1_telemetry_acswu2_value: masterframe.transferframe1.telemetry.acswu2.value
    :field transferframe1_telemetry_acswq0_raw: masterframe.transferframe1.telemetry.acswq0.raw
    :field transferframe1_telemetry_acswq0_value: masterframe.transferframe1.telemetry.acswq0.value
    :field transferframe1_telemetry_acswq1_raw: masterframe.transferframe1.telemetry.acswq1.raw
    :field transferframe1_telemetry_acswq1_value: masterframe.transferframe1.telemetry.acswq1.value
    :field transferframe1_telemetry_acswq2_raw: masterframe.transferframe1.telemetry.acswq2.raw
    :field transferframe1_telemetry_acswq2_value: masterframe.transferframe1.telemetry.acswq2.value
    :field transferframe1_telemetry_acswq3_raw: masterframe.transferframe1.telemetry.acswq3.raw
    :field transferframe1_telemetry_acswq3_value: masterframe.transferframe1.telemetry.acswq3.value
    :field transferframe1_acswa0: masterframe.transferframe1.telemetry.acswa0
    :field transferframe1_acswa1: masterframe.transferframe1.telemetry.acswa1
    :field transferframe1_acswa2: masterframe.transferframe1.telemetry.acswa2
    :field transferframe1_acs_tm_vecs_res: masterframe.transferframe1.telemetry.acs_tm_vecs_res
    :field transferframe1_psmfs1: masterframe.transferframe1.telemetry.psmfs1
    :field transferframe1_pcch02: masterframe.transferframe1.telemetry.pcch02
    :field transferframe1_tcfrcp: masterframe.transferframe1.telemetry.tcfrcp
    :field transferframe1_tmhkur: masterframe.transferframe1.telemetry.tmhkur
    :field transferframe1_cstutc: masterframe.transferframe1.telemetry.cstutc
    :field transferframe1_cstsys: masterframe.transferframe1.telemetry.cstsys
    :field transferframe1_pcsyst: masterframe.transferframe1.telemetry.pcsyst
    :field transferframe1_acswhy: masterframe.transferframe1.telemetry.acswhy
    :field transferframe1_acswhz: masterframe.transferframe1.telemetry.acswhz
    :field transferframe1_telemetry_acg1ym_raw: masterframe.transferframe1.telemetry.acg1ym.raw
    :field transferframe1_telemetry_acg1ym_value: masterframe.transferframe1.telemetry.acg1ym.value
    :field transferframe1_telemetry_acg1zm_raw: masterframe.transferframe1.telemetry.acg1zm.raw
    :field transferframe1_telemetry_acg1zm_value: masterframe.transferframe1.telemetry.acg1zm.value
    :field transferframe1_telemetry_acg1xm_raw: masterframe.transferframe1.telemetry.acg1xm.raw
    :field transferframe1_telemetry_acg1xm_value: masterframe.transferframe1.telemetry.acg1xm.value
    :field transferframe1_obctmffp: masterframe.transferframe1.telemetry.obctmffp
    :field transferframe1_obcswversion: masterframe.transferframe1.telemetry.obcswversion
    :field transferframe1_telemetry_acscmod_raw: masterframe.transferframe1.telemetry.acscmod.raw
    :field transferframe1_telemetry_acscmod_value: masterframe.transferframe1.telemetry.acscmod.value
    :field transferframe1_cctccp: masterframe.transferframe1.telemetry.cctccp
    :field transferframe1_telemetry_b2_tm_reserve_raw: masterframe.transferframe1.telemetry.b2_tm_reserve.raw
    :field transferframe1_telemetry_b2_tm_reserve_value: masterframe.transferframe1.telemetry.b2_tm_reserve.value
    :field transferframe1_tledoy: masterframe.transferframe1.telemetry.tledoy
    :field transferframe1_telemetry_tlemem_raw: masterframe.transferframe1.telemetry.tlemem.raw
    :field transferframe1_telemetry_tlemem_value: masterframe.transferframe1.telemetry.tlemem.value
    :field transferframe1_tleecc: masterframe.transferframe1.telemetry.tleecc
    :field transferframe1_telemetry_tleinc_raw: masterframe.transferframe1.telemetry.tleinc.raw
    :field transferframe1_telemetry_tleinc_value: masterframe.transferframe1.telemetry.tleinc.value
    :field transferframe1_telemetry_tleaop_raw: masterframe.transferframe1.telemetry.tleaop.raw
    :field transferframe1_telemetry_tleaop_value: masterframe.transferframe1.telemetry.tleaop.value
    :field transferframe1_telemetry_tleraa_raw: masterframe.transferframe1.telemetry.tleraa.raw
    :field transferframe1_telemetry_tleraa_value: masterframe.transferframe1.telemetry.tleraa.value
    :field transferframe1_telemetry_tleman_raw: masterframe.transferframe1.telemetry.tleman.raw
    :field transferframe1_telemetry_tleman_value: masterframe.transferframe1.telemetry.tleman.value
    :field transferframe1_tledrt: masterframe.transferframe1.telemetry.tledrt
    :field transferframe1_tlexpc: masterframe.transferframe1.telemetry.tlexpc
    :field transferframe1_tleypc: masterframe.transferframe1.telemetry.tleypc
    :field transferframe1_tlettd: masterframe.transferframe1.telemetry.tlettd
    :field transferframe1_tleutd: masterframe.transferframe1.telemetry.tleutd
    :field transferframe1_tledep: masterframe.transferframe1.telemetry.tledep
    :field transferframe1_tledps: masterframe.transferframe1.telemetry.tledps
    :field transferframe1_tleyea: masterframe.transferframe1.telemetry.tleyea
    :field transferframe1_tle_placeholder: masterframe.transferframe1.telemetry.tle_placeholder
    :field transferframe1_fecfd: masterframe.transferframe1.fecfd
    :field transferframe2_asm: masterframe.transferframe2.asm
    :field transferframe2_raw: masterframe.transferframe2.tfvn.raw
    :field transferframe2_value: masterframe.transferframe2.tfvn.value
    :field transferframe2_scid_raw: masterframe.transferframe2.scid.raw
    :field transferframe2_scid_value: masterframe.transferframe2.scid.value
    :field transferframe2_vcidb_raw: masterframe.transferframe2.vcidb.raw
    :field transferframe2_vcidb_value: masterframe.transferframe2.vcidb.value
    :field transferframe2_ocff: masterframe.transferframe2.ocff
    :field transferframe2_mcfc: masterframe.transferframe2.mcfc
    :field transferframe2_vcfc: masterframe.transferframe2.vcfc
    :field transferframe2_tf_shf: masterframe.transferframe2.tf_shf
    :field transferframe2_synchflag: masterframe.transferframe2.synchflag
    :field transferframe2_pof: masterframe.transferframe2.pof
    :field transferframe2_slid_raw: masterframe.transferframe2.slid.raw
    :field transferframe2_slid_value: masterframe.transferframe2.slid.value
    :field transferframe2_fhp_raw: masterframe.transferframe2.fhp.raw
    :field transferframe2_fhp_value: masterframe.transferframe2.fhp.value
    :field transferframe2_source_pvn_raw: masterframe.transferframe2.source.pvn.raw
    :field transferframe2_source_pvn_value: masterframe.transferframe2.source.pvn.value
    :field transferframe2_pt: masterframe.transferframe2.source.pt
    :field transferframe2_shf: masterframe.transferframe2.source.shf
    :field transferframe2_source_apid_raw: masterframe.transferframe2.source.apid.raw
    :field transferframe2_source_apid_value: masterframe.transferframe2.source.apid.value
    :field transferframe2_source_seqflag_raw: masterframe.transferframe2.source.seqflag.raw
    :field transferframe2_source_seqflag_value: masterframe.transferframe2.source.seqflag.value
    :field transferframe2_source_psc_raw: masterframe.transferframe2.source.psc.raw
    :field transferframe2_source_psc_value: masterframe.transferframe2.source.psc.value
    :field transferframe2_pdl: masterframe.transferframe2.source.pdl
    :field transferframe2_telemetry_cstutc_raw: masterframe.transferframe2.telemetry.cstutc.raw
    :field transferframe2_telemetry_cstutc_value: masterframe.transferframe2.telemetry.cstutc.value
    :field transferframe2_telemetry_csaxp_raw: masterframe.transferframe2.telemetry.csaxp.raw
    :field transferframe2_telemetry_csaxp_value: masterframe.transferframe2.telemetry.csaxp.value
    :field transferframe2_telemetry_csaxn_raw: masterframe.transferframe2.telemetry.csaxn.raw
    :field transferframe2_telemetry_csaxn_value: masterframe.transferframe2.telemetry.csaxn.value
    :field transferframe2_telemetry_csayp_raw: masterframe.transferframe2.telemetry.csayp.raw
    :field transferframe2_telemetry_csayp_value: masterframe.transferframe2.telemetry.csayp.value
    :field transferframe2_telemetry_csayn_raw: masterframe.transferframe2.telemetry.csayn.raw
    :field transferframe2_telemetry_csayn_value: masterframe.transferframe2.telemetry.csayn.value
    :field transferframe2_telemetry_csazp_raw: masterframe.transferframe2.telemetry.csazp.raw
    :field transferframe2_telemetry_csazp_value: masterframe.transferframe2.telemetry.csazp.value
    :field transferframe2_telemetry_csazn_raw: masterframe.transferframe2.telemetry.csazn.raw
    :field transferframe2_telemetry_csazn_value: masterframe.transferframe2.telemetry.csazn.value
    :field transferframe2_telemetry_vsabus_raw: masterframe.transferframe2.telemetry.vsabus.raw
    :field transferframe2_telemetry_vsabus_value: masterframe.transferframe2.telemetry.vsabus.value
    :field transferframe2_telemetry_cc0in_raw: masterframe.transferframe2.telemetry.cc0in.raw
    :field transferframe2_telemetry_cc0in_value: masterframe.transferframe2.telemetry.cc0in.value
    :field transferframe2_telemetry_cc1in_raw: masterframe.transferframe2.telemetry.cc1in.raw
    :field transferframe2_telemetry_cc1in_value: masterframe.transferframe2.telemetry.cc1in.value
    :field transferframe2_telemetry_vbat0_raw: masterframe.transferframe2.telemetry.vbat0.raw
    :field transferframe2_telemetry_vbat0_value: masterframe.transferframe2.telemetry.vbat0.value
    :field transferframe2_telemetry_vbat1_raw: masterframe.transferframe2.telemetry.vbat1.raw
    :field transferframe2_telemetry_vbat1_value: masterframe.transferframe2.telemetry.vbat1.value
    :field transferframe2_telemetry_cc0out_raw: masterframe.transferframe2.telemetry.cc0out.raw
    :field transferframe2_telemetry_cc0out_value: masterframe.transferframe2.telemetry.cc0out.value
    :field transferframe2_telemetry_cc1out_raw: masterframe.transferframe2.telemetry.cc1out.raw
    :field transferframe2_telemetry_cc1out_value: masterframe.transferframe2.telemetry.cc1out.value
    :field transferframe2_telemetry_v50bus_raw: masterframe.transferframe2.telemetry.v50bus.raw
    :field transferframe2_telemetry_v50bus_value: masterframe.transferframe2.telemetry.v50bus.value
    :field transferframe2_telemetry_v33bus_raw: masterframe.transferframe2.telemetry.v33bus.raw
    :field transferframe2_telemetry_v33bus_value: masterframe.transferframe2.telemetry.v33bus.value
    :field transferframe2_telemetry_cpcu_raw: masterframe.transferframe2.telemetry.cpcu.raw
    :field transferframe2_telemetry_cpcu_value: masterframe.transferframe2.telemetry.cpcu.value
    :field transferframe2_telemetry_cobc0_raw: masterframe.transferframe2.telemetry.cobc0.raw
    :field transferframe2_telemetry_cobc0_value: masterframe.transferframe2.telemetry.cobc0.value
    :field transferframe2_telemetry_cobc1_raw: masterframe.transferframe2.telemetry.cobc1.raw
    :field transferframe2_telemetry_cobc1_value: masterframe.transferframe2.telemetry.cobc1.value
    :field transferframe2_telemetry_ctnc0_raw: masterframe.transferframe2.telemetry.ctnc0.raw
    :field transferframe2_telemetry_ctnc0_value: masterframe.transferframe2.telemetry.ctnc0.value
    :field transferframe2_telemetry_ctnc1_raw: masterframe.transferframe2.telemetry.ctnc1.raw
    :field transferframe2_telemetry_ctnc1_value: masterframe.transferframe2.telemetry.ctnc1.value
    :field transferframe2_telemetry_ctrx0_raw: masterframe.transferframe2.telemetry.ctrx0.raw
    :field transferframe2_telemetry_ctrx0_value: masterframe.transferframe2.telemetry.ctrx0.value
    :field transferframe2_telemetry_ctrx1_raw: masterframe.transferframe2.telemetry.ctrx1.raw
    :field transferframe2_telemetry_ctrx1_value: masterframe.transferframe2.telemetry.ctrx1.value
    :field transferframe2_telemetry_cpdh_raw: masterframe.transferframe2.telemetry.cpdh.raw
    :field transferframe2_telemetry_cpdh_value: masterframe.transferframe2.telemetry.cpdh.value
    :field transferframe2_telemetry_ccam_raw: masterframe.transferframe2.telemetry.ccam.raw
    :field transferframe2_telemetry_ccam_value: masterframe.transferframe2.telemetry.ccam.value
    :field transferframe2_telemetry_csss_raw: masterframe.transferframe2.telemetry.csss.raw
    :field transferframe2_telemetry_csss_value: masterframe.transferframe2.telemetry.csss.value
    :field transferframe2_telemetry_cmfs0_raw: masterframe.transferframe2.telemetry.cmfs0.raw
    :field transferframe2_telemetry_cmfs0_value: masterframe.transferframe2.telemetry.cmfs0.value
    :field transferframe2_telemetry_cmfs1_raw: masterframe.transferframe2.telemetry.cmfs1.raw
    :field transferframe2_telemetry_cmfs1_value: masterframe.transferframe2.telemetry.cmfs1.value
    :field transferframe2_telemetry_cgyr0_raw: masterframe.transferframe2.telemetry.cgyr0.raw
    :field transferframe2_telemetry_cgyr0_value: masterframe.transferframe2.telemetry.cgyr0.value
    :field transferframe2_telemetry_cmcs_raw: masterframe.transferframe2.telemetry.cmcs.raw
    :field transferframe2_telemetry_cmcs_value: masterframe.transferframe2.telemetry.cmcs.value
    :field transferframe2_telemetry_cwhl_raw: masterframe.transferframe2.telemetry.cwhl.raw
    :field transferframe2_telemetry_cwhl_value: masterframe.transferframe2.telemetry.cwhl.value
    :field transferframe2_telemetry_ccan0_raw: masterframe.transferframe2.telemetry.ccan0.raw
    :field transferframe2_telemetry_ccan0_value: masterframe.transferframe2.telemetry.ccan0.value
    :field transferframe2_telemetry_ccan1_raw: masterframe.transferframe2.telemetry.ccan1.raw
    :field transferframe2_telemetry_ccan1_value: masterframe.transferframe2.telemetry.ccan1.value
    :field transferframe2_telemetry_vmfs0_raw: masterframe.transferframe2.telemetry.vmfs0.raw
    :field transferframe2_telemetry_vmfs0_value: masterframe.transferframe2.telemetry.vmfs0.value
    :field transferframe2_telemetry_vmfs1_raw: masterframe.transferframe2.telemetry.vmfs1.raw
    :field transferframe2_telemetry_vmfs1_value: masterframe.transferframe2.telemetry.vmfs1.value
    :field transferframe2_telemetry_cmcsxp_raw: masterframe.transferframe2.telemetry.cmcsxp.raw
    :field transferframe2_telemetry_cmcsxp_value: masterframe.transferframe2.telemetry.cmcsxp.value
    :field transferframe2_telemetry_cmcsxn_raw: masterframe.transferframe2.telemetry.cmcsxn.raw
    :field transferframe2_telemetry_cmcsxn_value: masterframe.transferframe2.telemetry.cmcsxn.value
    :field transferframe2_telemetry_cmcsyp_raw: masterframe.transferframe2.telemetry.cmcsyp.raw
    :field transferframe2_telemetry_cmcsyp_value: masterframe.transferframe2.telemetry.cmcsyp.value
    :field transferframe2_telemetry_cmcsyn_raw: masterframe.transferframe2.telemetry.cmcsyn.raw
    :field transferframe2_telemetry_cmcsyn_value: masterframe.transferframe2.telemetry.cmcsyn.value
    :field transferframe2_telemetry_cmcszp_raw: masterframe.transferframe2.telemetry.cmcszp.raw
    :field transferframe2_telemetry_cmcszp_value: masterframe.transferframe2.telemetry.cmcszp.value
    :field transferframe2_telemetry_cmcszn_raw: masterframe.transferframe2.telemetry.cmcszn.raw
    :field transferframe2_telemetry_cmcszn_value: masterframe.transferframe2.telemetry.cmcszn.value
    :field transferframe2_telemetry_cobcmcu_raw: masterframe.transferframe2.telemetry.cobcmcu.raw
    :field transferframe2_telemetry_cobcmcu_value: masterframe.transferframe2.telemetry.cobcmcu.value
    :field transferframe2_telemetry_cobcext_raw: masterframe.transferframe2.telemetry.cobcext.raw
    :field transferframe2_telemetry_cobcext_value: masterframe.transferframe2.telemetry.cobcext.value
    :field transferframe2_telemetry_ttrx1_raw: masterframe.transferframe2.telemetry.ttrx1.raw
    :field transferframe2_telemetry_ttrx1_value: masterframe.transferframe2.telemetry.ttrx1.value
    :field transferframe2_telemetry_cpdh2_raw: masterframe.transferframe2.telemetry.cpdh2.raw
    :field transferframe2_telemetry_cpdh2_value: masterframe.transferframe2.telemetry.cpdh2.value
    :field transferframe2_telemetry_ccam2_raw: masterframe.transferframe2.telemetry.ccam2.raw
    :field transferframe2_telemetry_ccam2_value: masterframe.transferframe2.telemetry.ccam2.value
    :field transferframe2_asstop: masterframe.transferframe2.telemetry.asstop
    :field transferframe2_assintv: masterframe.transferframe2.telemetry.assintv
    :field transferframe2_ascest: masterframe.transferframe2.telemetry.ascest
    :field transferframe2_asactv: masterframe.transferframe2.telemetry.asactv
    :field transferframe2_reserve2: masterframe.transferframe2.telemetry.reserve2
    :field transferframe2_reserve1: masterframe.transferframe2.telemetry.reserve1
    :field transferframe2_telemetry_tsaxp_raw: masterframe.transferframe2.telemetry.tsaxp.raw
    :field transferframe2_telemetry_tsaxp_value: masterframe.transferframe2.telemetry.tsaxp.value
    :field transferframe2_telemetry_tsaxn_raw: masterframe.transferframe2.telemetry.tsaxn.raw
    :field transferframe2_telemetry_tsaxn_value: masterframe.transferframe2.telemetry.tsaxn.value
    :field transferframe2_telemetry_tsayp_raw: masterframe.transferframe2.telemetry.tsayp.raw
    :field transferframe2_telemetry_tsayp_value: masterframe.transferframe2.telemetry.tsayp.value
    :field transferframe2_telemetry_tsayn_raw: masterframe.transferframe2.telemetry.tsayn.raw
    :field transferframe2_telemetry_tsayn_value: masterframe.transferframe2.telemetry.tsayn.value
    :field transferframe2_telemetry_tsazp_raw: masterframe.transferframe2.telemetry.tsazp.raw
    :field transferframe2_telemetry_tsazp_value: masterframe.transferframe2.telemetry.tsazp.value
    :field transferframe2_telemetry_tsazn_raw: masterframe.transferframe2.telemetry.tsazn.raw
    :field transferframe2_telemetry_tsazn_value: masterframe.transferframe2.telemetry.tsazn.value
    :field transferframe2_telemetry_tbat0_raw: masterframe.transferframe2.telemetry.tbat0.raw
    :field transferframe2_telemetry_tbat0_value: masterframe.transferframe2.telemetry.tbat0.value
    :field transferframe2_telemetry_tbat1_raw: masterframe.transferframe2.telemetry.tbat1.raw
    :field transferframe2_telemetry_tbat1_value: masterframe.transferframe2.telemetry.tbat1.value
    :field transferframe2_telemetry_tpcu00_raw: masterframe.transferframe2.telemetry.tpcu00.raw
    :field transferframe2_telemetry_tpcu00_value: masterframe.transferframe2.telemetry.tpcu00.value
    :field transferframe2_telemetry_tpcu01_raw: masterframe.transferframe2.telemetry.tpcu01.raw
    :field transferframe2_telemetry_tpcu01_value: masterframe.transferframe2.telemetry.tpcu01.value
    :field transferframe2_telemetry_tmfs0_raw: masterframe.transferframe2.telemetry.tmfs0.raw
    :field transferframe2_telemetry_tmfs0_value: masterframe.transferframe2.telemetry.tmfs0.value
    :field transferframe2_telemetry_tmfs1_raw: masterframe.transferframe2.telemetry.tmfs1.raw
    :field transferframe2_telemetry_tmfs1_value: masterframe.transferframe2.telemetry.tmfs1.value
    :field transferframe2_telemetry_twhlx_raw: masterframe.transferframe2.telemetry.twhlx.raw
    :field transferframe2_telemetry_twhlx_value: masterframe.transferframe2.telemetry.twhlx.value
    :field transferframe2_telemetry_twhly_raw: masterframe.transferframe2.telemetry.twhly.raw
    :field transferframe2_telemetry_twhly_value: masterframe.transferframe2.telemetry.twhly.value
    :field transferframe2_telemetry_twhlz_raw: masterframe.transferframe2.telemetry.twhlz.raw
    :field transferframe2_telemetry_twhlz_value: masterframe.transferframe2.telemetry.twhlz.value
    :field transferframe2_telemetry_tgyrox_raw: masterframe.transferframe2.telemetry.tgyrox.raw
    :field transferframe2_telemetry_tgyrox_value: masterframe.transferframe2.telemetry.tgyrox.value
    :field transferframe2_telemetry_tgyroy_raw: masterframe.transferframe2.telemetry.tgyroy.raw
    :field transferframe2_telemetry_tgyroy_value: masterframe.transferframe2.telemetry.tgyroy.value
    :field transferframe2_telemetry_tgyroz_raw: masterframe.transferframe2.telemetry.tgyroz.raw
    :field transferframe2_telemetry_tgyroz_value: masterframe.transferframe2.telemetry.tgyroz.value
    :field transferframe2_telemetry_tobc00_raw: masterframe.transferframe2.telemetry.tobc00.raw
    :field transferframe2_telemetry_tobc00_value: masterframe.transferframe2.telemetry.tobc00.value
    :field transferframe2_telemetry_tobc01_raw: masterframe.transferframe2.telemetry.tobc01.raw
    :field transferframe2_telemetry_tobc01_value: masterframe.transferframe2.telemetry.tobc01.value
    :field transferframe2_telemetry_tobc02_raw: masterframe.transferframe2.telemetry.tobc02.raw
    :field transferframe2_telemetry_tobc02_value: masterframe.transferframe2.telemetry.tobc02.value
    :field transferframe2_telemetry_ttrx0_raw: masterframe.transferframe2.telemetry.ttrx0.raw
    :field transferframe2_telemetry_ttrx0_value: masterframe.transferframe2.telemetry.ttrx0.value
    :field transferframe2_reserve: masterframe.transferframe2.telemetry.reserve
    :field transferframe2_telemetry_acssuxpx0_raw: masterframe.transferframe2.telemetry.acssuxpx0.raw
    :field transferframe2_telemetry_acssuxpx0_value: masterframe.transferframe2.telemetry.acssuxpx0.value
    :field transferframe2_telemetry_acssuxpx1_raw: masterframe.transferframe2.telemetry.acssuxpx1.raw
    :field transferframe2_telemetry_acssuxpx1_value: masterframe.transferframe2.telemetry.acssuxpx1.value
    :field transferframe2_telemetry_acssuxpy0_raw: masterframe.transferframe2.telemetry.acssuxpy0.raw
    :field transferframe2_telemetry_acssuxpy0_value: masterframe.transferframe2.telemetry.acssuxpy0.value
    :field transferframe2_telemetry_acssuxpy1_raw: masterframe.transferframe2.telemetry.acssuxpy1.raw
    :field transferframe2_telemetry_acssuxpy1_value: masterframe.transferframe2.telemetry.acssuxpy1.value
    :field transferframe2_telemetry_acssuxnx0_raw: masterframe.transferframe2.telemetry.acssuxnx0.raw
    :field transferframe2_telemetry_acssuxnx0_value: masterframe.transferframe2.telemetry.acssuxnx0.value
    :field transferframe2_telemetry_acssuxnx1_raw: masterframe.transferframe2.telemetry.acssuxnx1.raw
    :field transferframe2_telemetry_acssuxnx1_value: masterframe.transferframe2.telemetry.acssuxnx1.value
    :field transferframe2_telemetry_acssuxny0_raw: masterframe.transferframe2.telemetry.acssuxny0.raw
    :field transferframe2_telemetry_acssuxny0_value: masterframe.transferframe2.telemetry.acssuxny0.value
    :field transferframe2_telemetry_acssuxny1_raw: masterframe.transferframe2.telemetry.acssuxny1.raw
    :field transferframe2_telemetry_acssuxny1_value: masterframe.transferframe2.telemetry.acssuxny1.value
    :field transferframe2_telemetry_acssuypx0_raw: masterframe.transferframe2.telemetry.acssuypx0.raw
    :field transferframe2_telemetry_acssuypx0_value: masterframe.transferframe2.telemetry.acssuypx0.value
    :field transferframe2_telemetry_acssuypx1_raw: masterframe.transferframe2.telemetry.acssuypx1.raw
    :field transferframe2_telemetry_acssuypx1_value: masterframe.transferframe2.telemetry.acssuypx1.value
    :field transferframe2_telemetry_acssuypy0_raw: masterframe.transferframe2.telemetry.acssuypy0.raw
    :field transferframe2_telemetry_acssuypy0_value: masterframe.transferframe2.telemetry.acssuypy0.value
    :field transferframe2_telemetry_acssuypy1_raw: masterframe.transferframe2.telemetry.acssuypy1.raw
    :field transferframe2_telemetry_acssuypy1_value: masterframe.transferframe2.telemetry.acssuypy1.value
    :field transferframe2_telemetry_acssuynx0_raw: masterframe.transferframe2.telemetry.acssuynx0.raw
    :field transferframe2_telemetry_acssuynx0_value: masterframe.transferframe2.telemetry.acssuynx0.value
    :field transferframe2_telemetry_acssuynx1_raw: masterframe.transferframe2.telemetry.acssuynx1.raw
    :field transferframe2_telemetry_acssuynx1_value: masterframe.transferframe2.telemetry.acssuynx1.value
    :field transferframe2_telemetry_acssuyny0_raw: masterframe.transferframe2.telemetry.acssuyny0.raw
    :field transferframe2_telemetry_acssuyny0_value: masterframe.transferframe2.telemetry.acssuyny0.value
    :field transferframe2_telemetry_acssuyny1_raw: masterframe.transferframe2.telemetry.acssuyny1.raw
    :field transferframe2_telemetry_acssuyny1_value: masterframe.transferframe2.telemetry.acssuyny1.value
    :field transferframe2_telemetry_acssuzpx0_raw: masterframe.transferframe2.telemetry.acssuzpx0.raw
    :field transferframe2_telemetry_acssuzpx0_value: masterframe.transferframe2.telemetry.acssuzpx0.value
    :field transferframe2_telemetry_acssuzpx1_raw: masterframe.transferframe2.telemetry.acssuzpx1.raw
    :field transferframe2_telemetry_acssuzpx1_value: masterframe.transferframe2.telemetry.acssuzpx1.value
    :field transferframe2_telemetry_acssuzpy0_raw: masterframe.transferframe2.telemetry.acssuzpy0.raw
    :field transferframe2_telemetry_acssuzpy0_value: masterframe.transferframe2.telemetry.acssuzpy0.value
    :field transferframe2_telemetry_acssuzpy1_raw: masterframe.transferframe2.telemetry.acssuzpy1.raw
    :field transferframe2_telemetry_acssuzpy1_value: masterframe.transferframe2.telemetry.acssuzpy1.value
    :field transferframe2_telemetry_acssuznx0_raw: masterframe.transferframe2.telemetry.acssuznx0.raw
    :field transferframe2_telemetry_acssuznx0_value: masterframe.transferframe2.telemetry.acssuznx0.value
    :field transferframe2_telemetry_acssuznx1_raw: masterframe.transferframe2.telemetry.acssuznx1.raw
    :field transferframe2_telemetry_acssuznx1_value: masterframe.transferframe2.telemetry.acssuznx1.value
    :field transferframe2_telemetry_acssuzny0_raw: masterframe.transferframe2.telemetry.acssuzny0.raw
    :field transferframe2_telemetry_acssuzny0_value: masterframe.transferframe2.telemetry.acssuzny0.value
    :field transferframe2_telemetry_acssuzny1_raw: masterframe.transferframe2.telemetry.acssuzny1.raw
    :field transferframe2_telemetry_acssuzny1_value: masterframe.transferframe2.telemetry.acssuzny1.value
    :field transferframe2_telemetry_cmfs0x_raw: masterframe.transferframe2.telemetry.cmfs0x.raw
    :field transferframe2_telemetry_cmfs0x_value: masterframe.transferframe2.telemetry.cmfs0x.value
    :field transferframe2_telemetry_cmfs0y_raw: masterframe.transferframe2.telemetry.cmfs0y.raw
    :field transferframe2_telemetry_cmfs0y_value: masterframe.transferframe2.telemetry.cmfs0y.value
    :field transferframe2_telemetry_cmfs0z_raw: masterframe.transferframe2.telemetry.cmfs0z.raw
    :field transferframe2_telemetry_cmfs0z_value: masterframe.transferframe2.telemetry.cmfs0z.value
    :field transferframe2_telemetry_cmfs1x_raw: masterframe.transferframe2.telemetry.cmfs1x.raw
    :field transferframe2_telemetry_cmfs1x_value: masterframe.transferframe2.telemetry.cmfs1x.value
    :field transferframe2_telemetry_cmfs1y_raw: masterframe.transferframe2.telemetry.cmfs1y.raw
    :field transferframe2_telemetry_cmfs1y_value: masterframe.transferframe2.telemetry.cmfs1y.value
    :field transferframe2_telemetry_cmfs1z_raw: masterframe.transferframe2.telemetry.cmfs1z.raw
    :field transferframe2_telemetry_cmfs1z_value: masterframe.transferframe2.telemetry.cmfs1z.value
    :field transferframe2_telemetry_acsgy0x_raw: masterframe.transferframe2.telemetry.acsgy0x.raw
    :field transferframe2_telemetry_acsgy0x_value: masterframe.transferframe2.telemetry.acsgy0x.value
    :field transferframe2_telemetry_acsgy0y_raw: masterframe.transferframe2.telemetry.acsgy0y.raw
    :field transferframe2_telemetry_acsgy0y_value: masterframe.transferframe2.telemetry.acsgy0y.value
    :field transferframe2_telemetry_acsgy0z_raw: masterframe.transferframe2.telemetry.acsgy0z.raw
    :field transferframe2_telemetry_acsgy0z_value: masterframe.transferframe2.telemetry.acsgy0z.value
    :field transferframe2_telemetry_reserve1_raw: masterframe.transferframe2.telemetry.reserve1.raw
    :field transferframe2_telemetry_reserve1_value: masterframe.transferframe2.telemetry.reserve1.value
    :field transferframe2_psant0: masterframe.transferframe2.telemetry.psant0
    :field transferframe2_psant1: masterframe.transferframe2.telemetry.psant1
    :field transferframe2_psgyr1: masterframe.transferframe2.telemetry.psgyr1
    :field transferframe2_pscom1: masterframe.transferframe2.telemetry.pscom1
    :field transferframe2_psuhf0: masterframe.transferframe2.telemetry.psuhf0
    :field transferframe2_psuhf1: masterframe.transferframe2.telemetry.psuhf1
    :field transferframe2_pstnc0: masterframe.transferframe2.telemetry.pstnc0
    :field transferframe2_pstnc1: masterframe.transferframe2.telemetry.pstnc1
    :field transferframe2_psgyr0: masterframe.transferframe2.telemetry.psgyr0
    :field transferframe2_psmcsx: masterframe.transferframe2.telemetry.psmcsx
    :field transferframe2_psmcsy: masterframe.transferframe2.telemetry.psmcsy
    :field transferframe2_psmcsz: masterframe.transferframe2.telemetry.psmcsz
    :field transferframe2_pswhls: masterframe.transferframe2.telemetry.pswhls
    :field transferframe2_psobc0: masterframe.transferframe2.telemetry.psobc0
    :field transferframe2_psobc1: masterframe.transferframe2.telemetry.psobc1
    :field transferframe2_pspdh0: masterframe.transferframe2.telemetry.pspdh0
    :field transferframe2_pscam0: masterframe.transferframe2.telemetry.pscam0
    :field transferframe2_pssuns: masterframe.transferframe2.telemetry.pssuns
    :field transferframe2_psmfs0: masterframe.transferframe2.telemetry.psmfs0
    :field transferframe2_psms1: masterframe.transferframe2.telemetry.psms1
    :field transferframe2_pstemp: masterframe.transferframe2.telemetry.pstemp
    :field transferframe2_pscan0: masterframe.transferframe2.telemetry.pscan0
    :field transferframe2_pscan1: masterframe.transferframe2.telemetry.pscan1
    :field transferframe2_psccw0: masterframe.transferframe2.telemetry.psccw0
    :field transferframe2_psccw1: masterframe.transferframe2.telemetry.psccw1
    :field transferframe2_ps5vcn: masterframe.transferframe2.telemetry.ps5vcn
    :field transferframe2_pcuaid: masterframe.transferframe2.telemetry.pcuaid
    :field transferframe2_pcbobc: masterframe.transferframe2.telemetry.pcbobc
    :field transferframe2_pcbext: masterframe.transferframe2.telemetry.pcbext
    :field transferframe2_pcch00: masterframe.transferframe2.telemetry.pcch00
    :field transferframe2_pcch01: masterframe.transferframe2.telemetry.pcch01
    :field transferframe2_pccho2: masterframe.transferframe2.telemetry.pccho2
    :field transferframe2_pcch03: masterframe.transferframe2.telemetry.pcch03
    :field transferframe2_pcch04: masterframe.transferframe2.telemetry.pcch04
    :field transferframe2_pcch05: masterframe.transferframe2.telemetry.pcch05
    :field transferframe2_pcch06: masterframe.transferframe2.telemetry.pcch06
    :field transferframe2_telemetry_rxsig0_raw: masterframe.transferframe2.telemetry.rxsig0.raw
    :field transferframe2_telemetry_rxsig0_value: masterframe.transferframe2.telemetry.rxsig0.value
    :field transferframe2_pcch07: masterframe.transferframe2.telemetry.pcch07
    :field transferframe2_pcch08: masterframe.transferframe2.telemetry.pcch08
    :field transferframe2_pcch09: masterframe.transferframe2.telemetry.pcch09
    :field transferframe2_pcch10: masterframe.transferframe2.telemetry.pcch10
    :field transferframe2_telemetry_rxsig1_raw: masterframe.transferframe2.telemetry.rxsig1.raw
    :field transferframe2_telemetry_rxsig1_value: masterframe.transferframe2.telemetry.rxsig1.value
    :field transferframe2_pcch11: masterframe.transferframe2.telemetry.pcch11
    :field transferframe2_pcch12: masterframe.transferframe2.telemetry.pcch12
    :field transferframe2_pcch13: masterframe.transferframe2.telemetry.pcch13
    :field transferframe2_pcch14: masterframe.transferframe2.telemetry.pcch14
    :field transferframe2_pcch15: masterframe.transferframe2.telemetry.pcch15
    :field transferframe2_pcch16: masterframe.transferframe2.telemetry.pcch16
    :field transferframe2_pcch17: masterframe.transferframe2.telemetry.pcch17
    :field transferframe2_pcch18: masterframe.transferframe2.telemetry.pcch18
    :field transferframe2_pcch19: masterframe.transferframe2.telemetry.pcch19
    :field transferframe2_pcch20: masterframe.transferframe2.telemetry.pcch20
    :field transferframe2_pcch21: masterframe.transferframe2.telemetry.pcch21
    :field transferframe2_pcch22: masterframe.transferframe2.telemetry.pcch22
    :field transferframe2_pcch23: masterframe.transferframe2.telemetry.pcch23
    :field transferframe2_pcch24: masterframe.transferframe2.telemetry.pcch24
    :field transferframe2_pcch25: masterframe.transferframe2.telemetry.pcch25
    :field transferframe2_pcch26: masterframe.transferframe2.telemetry.pcch26
    :field transferframe2_tcrxid: masterframe.transferframe2.telemetry.tcrxid
    :field transferframe2_obcaid: masterframe.transferframe2.telemetry.obcaid
    :field transferframe2_tmtxrt: masterframe.transferframe2.telemetry.tmtxrt
    :field transferframe2_pcch27: masterframe.transferframe2.telemetry.pcch27
    :field transferframe2_pcch28: masterframe.transferframe2.telemetry.pcch28
    :field transferframe2_pcch29: masterframe.transferframe2.telemetry.pcch29
    :field transferframe2_pcch30: masterframe.transferframe2.telemetry.pcch30
    :field transferframe2_pcch31: masterframe.transferframe2.telemetry.pcch31
    :field transferframe2_cctcic: masterframe.transferframe2.telemetry.cctcic
    :field transferframe2_cctctt: masterframe.transferframe2.telemetry.cctctt
    :field transferframe2_ccetcs: masterframe.transferframe2.telemetry.ccetcs
    :field transferframe2_cceimc: masterframe.transferframe2.telemetry.cceimc
    :field transferframe2_ccettc: masterframe.transferframe2.telemetry.ccettc
    :field transferframe2_ccettg: masterframe.transferframe2.telemetry.ccettg
    :field transferframe2_ccetcc: masterframe.transferframe2.telemetry.ccetcc
    :field transferframe2_telemetry_tcrxqu_raw: masterframe.transferframe2.telemetry.tcrxqu.raw
    :field transferframe2_telemetry_tcrxqu_value: masterframe.transferframe2.telemetry.tcrxqu.value
    :field transferframe2_telemetry_tcfrcp_raw: masterframe.transferframe2.telemetry.tcfrcp.raw
    :field transferframe2_telemetry_tcfrcp_value: masterframe.transferframe2.telemetry.tcfrcp.value
    :field transferframe2_telemetry_tmhkur_raw: masterframe.transferframe2.telemetry.tmhkur.raw
    :field transferframe2_telemetry_tmhkur_value: masterframe.transferframe2.telemetry.tmhkur.value
    :field transferframe2_telemetry_cstsys_raw: masterframe.transferframe2.telemetry.cstsys.raw
    :field transferframe2_telemetry_cstsys_value: masterframe.transferframe2.telemetry.cstsys.value
    :field transferframe2_mcxpol: masterframe.transferframe2.telemetry.mcxpol
    :field transferframe2_mcypol: masterframe.transferframe2.telemetry.mcypol
    :field transferframe2_mczpol: masterframe.transferframe2.telemetry.mczpol
    :field transferframe2_telemetry_obcbad_raw: masterframe.transferframe2.telemetry.obcbad.raw
    :field transferframe2_telemetry_obcbad_value: masterframe.transferframe2.telemetry.obcbad.value
    :field transferframe2_ceswmc: masterframe.transferframe2.telemetry.ceswmc
    :field transferframe2_beacon: masterframe.transferframe2.telemetry.beacon
    :field transferframe2_telemetry_reserve3_raw: masterframe.transferframe2.telemetry.reserve3.raw
    :field transferframe2_telemetry_reserve3_value: masterframe.transferframe2.telemetry.reserve3.value
    :field transferframe2_telemetry_modcom_raw: masterframe.transferframe2.telemetry.modcom.raw
    :field transferframe2_telemetry_modcom_value: masterframe.transferframe2.telemetry.modcom.value
    :field transferframe2_obcabc: masterframe.transferframe2.telemetry.obcabc
    :field transferframe2_modobc: masterframe.transferframe2.telemetry.modobc
    :field transferframe2_ccecan: masterframe.transferframe2.telemetry.ccecan
    :field transferframe2_obccan: masterframe.transferframe2.telemetry.obccan
    :field transferframe2_telemetry_pcsyst_raw: masterframe.transferframe2.telemetry.pcsyst.raw
    :field transferframe2_telemetry_pcsyst_value: masterframe.transferframe2.telemetry.pcsyst.value
    :field transferframe2_pcbcnt: masterframe.transferframe2.telemetry.pcbcnt
    :field transferframe2_pctxec: masterframe.transferframe2.telemetry.pctxec
    :field transferframe2_pcrxec: masterframe.transferframe2.telemetry.pcrxec
    :field transferframe2_pcoffc: masterframe.transferframe2.telemetry.pcoffc
    :field transferframe2_pcackc: masterframe.transferframe2.telemetry.pcackc
    :field transferframe2_pcch32: masterframe.transferframe2.telemetry.pcch32
    :field transferframe2_pcch33: masterframe.transferframe2.telemetry.pcch33
    :field transferframe2_pcch34: masterframe.transferframe2.telemetry.pcch34
    :field transferframe2_pcch35: masterframe.transferframe2.telemetry.pcch35
    :field transferframe2_pcch36: masterframe.transferframe2.telemetry.pcch36
    :field transferframe2_pcch37: masterframe.transferframe2.telemetry.pcch37
    :field transferframe2_pcch38: masterframe.transferframe2.telemetry.pcch38
    :field transferframe2_pcch39: masterframe.transferframe2.telemetry.pcch39
    :field transferframe2_pcch40: masterframe.transferframe2.telemetry.pcch40
    :field transferframe2_pcch41: masterframe.transferframe2.telemetry.pcch41
    :field transferframe2_telemetry_reserve4_raw: masterframe.transferframe2.telemetry.reserve4.raw
    :field transferframe2_telemetry_reserve4_value: masterframe.transferframe2.telemetry.reserve4.value
    :field transferframe2_telemetry_reserve5_raw: masterframe.transferframe2.telemetry.reserve5.raw
    :field transferframe2_telemetry_reserve5_value: masterframe.transferframe2.telemetry.reserve5.value
    :field transferframe2_telemetry_reserve6_raw: masterframe.transferframe2.telemetry.reserve6.raw
    :field transferframe2_telemetry_reserve6_value: masterframe.transferframe2.telemetry.reserve6.value
    :field transferframe2_telemetry_reserve7_raw: masterframe.transferframe2.telemetry.reserve7.raw
    :field transferframe2_telemetry_reserve7_value: masterframe.transferframe2.telemetry.reserve7.value
    :field transferframe2_telemetry_acswhx_raw: masterframe.transferframe2.telemetry.acswhx.raw
    :field transferframe2_telemetry_acswhx_value: masterframe.transferframe2.telemetry.acswhx.value
    :field transferframe2_telemetry_acswhy_raw: masterframe.transferframe2.telemetry.acswhy.raw
    :field transferframe2_telemetry_acswhy_value: masterframe.transferframe2.telemetry.acswhy.value
    :field transferframe2_telemetry_acswhz_raw: masterframe.transferframe2.telemetry.acswhz.raw
    :field transferframe2_telemetry_acswhz_value: masterframe.transferframe2.telemetry.acswhz.value
    :field transferframe2_telemetry_acsq00_raw: masterframe.transferframe2.telemetry.acsq00.raw
    :field transferframe2_telemetry_acsq00_value: masterframe.transferframe2.telemetry.acsq00.value
    :field transferframe2_telemetry_acsq01_raw: masterframe.transferframe2.telemetry.acsq01.raw
    :field transferframe2_telemetry_acsq01_value: masterframe.transferframe2.telemetry.acsq01.value
    :field transferframe2_telemetry_acsq02_raw: masterframe.transferframe2.telemetry.acsq02.raw
    :field transferframe2_telemetry_acsq02_value: masterframe.transferframe2.telemetry.acsq02.value
    :field transferframe2_telemetry_acsq03_raw: masterframe.transferframe2.telemetry.acsq03.raw
    :field transferframe2_telemetry_acsq03_value: masterframe.transferframe2.telemetry.acsq03.value
    :field transferframe2_telemetry_acssux_raw: masterframe.transferframe2.telemetry.acssux.raw
    :field transferframe2_telemetry_acssux_value: masterframe.transferframe2.telemetry.acssux.value
    :field transferframe2_telemetry_acssuy_raw: masterframe.transferframe2.telemetry.acssuy.raw
    :field transferframe2_telemetry_acssuy_value: masterframe.transferframe2.telemetry.acssuy.value
    :field transferframe2_telemetry_acssuz_raw: masterframe.transferframe2.telemetry.acssuz.raw
    :field transferframe2_telemetry_acssuz_value: masterframe.transferframe2.telemetry.acssuz.value
    :field transferframe2_telemetry_acsmox_raw: masterframe.transferframe2.telemetry.acsmox.raw
    :field transferframe2_telemetry_acsmox_value: masterframe.transferframe2.telemetry.acsmox.value
    :field transferframe2_telemetry_acsmoy_raw: masterframe.transferframe2.telemetry.acsmoy.raw
    :field transferframe2_telemetry_acsmoy_value: masterframe.transferframe2.telemetry.acsmoy.value
    :field transferframe2_telemetry_acsmoz_raw: masterframe.transferframe2.telemetry.acsmoz.raw
    :field transferframe2_telemetry_acsmoz_value: masterframe.transferframe2.telemetry.acsmoz.value
    :field transferframe2_telemetry_acsm1x_raw: masterframe.transferframe2.telemetry.acsm1x.raw
    :field transferframe2_telemetry_acsm1x_value: masterframe.transferframe2.telemetry.acsm1x.value
    :field transferframe2_telemetry_acsm1y_raw: masterframe.transferframe2.telemetry.acsm1y.raw
    :field transferframe2_telemetry_acsm1y_value: masterframe.transferframe2.telemetry.acsm1y.value
    :field transferframe2_telemetry_acsm1z_raw: masterframe.transferframe2.telemetry.acsm1z.raw
    :field transferframe2_telemetry_acsm1z_value: masterframe.transferframe2.telemetry.acsm1z.value
    :field transferframe2_telemetry_modacs_raw: masterframe.transferframe2.telemetry.modacs.raw
    :field transferframe2_telemetry_modacs_value: masterframe.transferframe2.telemetry.modacs.value
    :field transferframe2_acsgsc: masterframe.transferframe2.telemetry.acsgsc
    :field transferframe2_acsshd: masterframe.transferframe2.telemetry.acsshd
    :field transferframe2_telemetry_reserve8_raw: masterframe.transferframe2.telemetry.reserve8.raw
    :field transferframe2_telemetry_reserve8_value: masterframe.transferframe2.telemetry.reserve8.value
    :field transferframe2_acserr: masterframe.transferframe2.telemetry.acserr
    :field transferframe2_telemetry_acsg1y_raw: masterframe.transferframe2.telemetry.acsg1y.raw
    :field transferframe2_telemetry_acsg1y_value: masterframe.transferframe2.telemetry.acsg1y.value
    :field transferframe2_telemetry_acsg1z_raw: masterframe.transferframe2.telemetry.acsg1z.raw
    :field transferframe2_telemetry_acsg1z_value: masterframe.transferframe2.telemetry.acsg1z.value
    :field transferframe2_telemetry_acsg1x_raw: masterframe.transferframe2.telemetry.acsg1x.raw
    :field transferframe2_telemetry_acsg1x_value: masterframe.transferframe2.telemetry.acsg1x.value
    :field transferframe2_telemetry_reserve9_raw: masterframe.transferframe2.telemetry.reserve9.raw
    :field transferframe2_telemetry_reserve9_value: masterframe.transferframe2.telemetry.reserve9.value
    :field transferframe2_telemetry_reserve10_raw: masterframe.transferframe2.telemetry.reserve10.raw
    :field transferframe2_telemetry_reserve10_value: masterframe.transferframe2.telemetry.reserve10.value
    :field transferframe2_crc000: masterframe.transferframe2.telemetry.crc000
    :field transferframe2_crc001: masterframe.transferframe2.telemetry.crc001
    :field transferframe2_crc002: masterframe.transferframe2.telemetry.crc002
    :field transferframe2_crc003: masterframe.transferframe2.telemetry.crc003
    :field transferframe2_crc004: masterframe.transferframe2.telemetry.crc004
    :field transferframe2_crc005: masterframe.transferframe2.telemetry.crc005
    :field transferframe2_crc006: masterframe.transferframe2.telemetry.crc006
    :field transferframe2_crc007: masterframe.transferframe2.telemetry.crc007
    :field transferframe2_crc008: masterframe.transferframe2.telemetry.crc008
    :field transferframe2_crc009: masterframe.transferframe2.telemetry.crc009
    :field transferframe2_crc010: masterframe.transferframe2.telemetry.crc010
    :field transferframe2_crc011: masterframe.transferframe2.telemetry.crc011
    :field transferframe2_crc012: masterframe.transferframe2.telemetry.crc012
    :field transferframe2_crc013: masterframe.transferframe2.telemetry.crc013
    :field transferframe2_crc014: masterframe.transferframe2.telemetry.crc014
    :field transferframe2_crc015: masterframe.transferframe2.telemetry.crc015
    :field transferframe2_crc016: masterframe.transferframe2.telemetry.crc016
    :field transferframe2_crc017: masterframe.transferframe2.telemetry.crc017
    :field transferframe2_crc018: masterframe.transferframe2.telemetry.crc018
    :field transferframe2_crc019: masterframe.transferframe2.telemetry.crc019
    :field transferframe2_crc020: masterframe.transferframe2.telemetry.crc020
    :field transferframe2_crc021: masterframe.transferframe2.telemetry.crc021
    :field transferframe2_crc022: masterframe.transferframe2.telemetry.crc022
    :field transferframe2_crc023: masterframe.transferframe2.telemetry.crc023
    :field transferframe2_crc024: masterframe.transferframe2.telemetry.crc024
    :field transferframe2_crc025: masterframe.transferframe2.telemetry.crc025
    :field transferframe2_crc026: masterframe.transferframe2.telemetry.crc026
    :field transferframe2_crc027: masterframe.transferframe2.telemetry.crc027
    :field transferframe2_crc028: masterframe.transferframe2.telemetry.crc028
    :field transferframe2_crc029: masterframe.transferframe2.telemetry.crc029
    :field transferframe2_crc030: masterframe.transferframe2.telemetry.crc030
    :field transferframe2_dummy: masterframe.transferframe2.telemetry.dummy
    :field transferframe2_imhd00: masterframe.transferframe2.telemetry.imhd00
    :field transferframe2_imhd01: masterframe.transferframe2.telemetry.imhd01
    :field transferframe2_imhd02: masterframe.transferframe2.telemetry.imhd02
    :field transferframe2_imhd03: masterframe.transferframe2.telemetry.imhd03
    :field transferframe2_imhd04: masterframe.transferframe2.telemetry.imhd04
    :field transferframe2_imhd10: masterframe.transferframe2.telemetry.imhd10
    :field transferframe2_imhd11: masterframe.transferframe2.telemetry.imhd11
    :field transferframe2_imhd12: masterframe.transferframe2.telemetry.imhd12
    :field transferframe2_imhd13: masterframe.transferframe2.telemetry.imhd13
    :field transferframe2_imhd14: masterframe.transferframe2.telemetry.imhd14
    :field transferframe2_imhd20: masterframe.transferframe2.telemetry.imhd20
    :field transferframe2_imhd21: masterframe.transferframe2.telemetry.imhd21
    :field transferframe2_imhd22: masterframe.transferframe2.telemetry.imhd22
    :field transferframe2_imhd23: masterframe.transferframe2.telemetry.imhd23
    :field transferframe2_imhd24: masterframe.transferframe2.telemetry.imhd24
    :field transferframe2_imhd30: masterframe.transferframe2.telemetry.imhd30
    :field transferframe2_imhd31: masterframe.transferframe2.telemetry.imhd31
    :field transferframe2_imhd32: masterframe.transferframe2.telemetry.imhd32
    :field transferframe2_imhd33: masterframe.transferframe2.telemetry.imhd33
    :field transferframe2_imhd34: masterframe.transferframe2.telemetry.imhd34
    :field transferframe2_reserver20: masterframe.transferframe2.telemetry.reserver20
    :field transferframe2_image_id: masterframe.transferframe2.telemetry.image_id
    :field transferframe2_pdh_image: masterframe.transferframe2.telemetry.pdh_image
    :field transferframe2_telemetry_cpdhmcu_raw: masterframe.transferframe2.telemetry.cpdhmcu.raw
    :field transferframe2_telemetry_cpdhmcu_value: masterframe.transferframe2.telemetry.cpdhmcu.value
    :field transferframe2_telemetry_cpdhcam_raw: masterframe.transferframe2.telemetry.cpdhcam.raw
    :field transferframe2_telemetry_cpdhcam_value: masterframe.transferframe2.telemetry.cpdhcam.value
    :field transferframe2_tpdhcam: masterframe.transferframe2.telemetry.tpdhcam
    :field transferframe2_pdhceccm: masterframe.transferframe2.telemetry.pdhceccm
    :field transferframe2_pdhcectc: masterframe.transferframe2.telemetry.pdhcectc
    :field transferframe2_pdhcetlii: masterframe.transferframe2.telemetry.pdhcetlii
    :field transferframe2_pdhcetlc: masterframe.transferframe2.telemetry.pdhcetlc
    :field transferframe2_pdhti: masterframe.transferframe2.telemetry.pdhti
    :field transferframe2_pdhth: masterframe.transferframe2.telemetry.pdhth
    :field transferframe2_pdhceisi: masterframe.transferframe2.telemetry.pdhceisi
    :field transferframe2_pdhceici: masterframe.transferframe2.telemetry.pdhceici
    :field transferframe2_pdhceids: masterframe.transferframe2.telemetry.pdhceids
    :field transferframe2_pdhmode: masterframe.transferframe2.telemetry.pdhmode
    :field transferframe2_pdhcii: masterframe.transferframe2.telemetry.pdhcii
    :field transferframe2_pdhcih: masterframe.transferframe2.telemetry.pdhcih
    :field transferframe2_pdhcescm: masterframe.transferframe2.telemetry.pdhcescm
    :field transferframe2_pdhcessm: masterframe.transferframe2.telemetry.pdhcessm
    :field transferframe2_pdhcescb: masterframe.transferframe2.telemetry.pdhcescb
    :field transferframe2_pdhceslb: masterframe.transferframe2.telemetry.pdhceslb
    :field transferframe2_pdhcesss: masterframe.transferframe2.telemetry.pdhcesss
    :field transferframe2_pdhcessb: masterframe.transferframe2.telemetry.pdhcessb
    :field transferframe2_pdhceseb: masterframe.transferframe2.telemetry.pdhceseb
    :field transferframe2_pdhcesci: masterframe.transferframe2.telemetry.pdhcesci
    :field transferframe2_pdhcsi: masterframe.transferframe2.telemetry.pdhcsi
    :field transferframe2_pdhcsh: masterframe.transferframe2.telemetry.pdhcsh
    :field transferframe2_pdhbtimg: masterframe.transferframe2.telemetry.pdhbtimg
    :field transferframe2_pdhswversion: masterframe.transferframe2.telemetry.pdhswversion
    :field transferframe2_pdhcstsys: masterframe.transferframe2.telemetry.pdhcstsys
    :field transferframe2_pdhctstutc: masterframe.transferframe2.telemetry.pdhctstutc
    :field transferframe2_pdh_reserve: masterframe.transferframe2.telemetry.pdh_reserve
    :field transferframe2_pdhcrc000: masterframe.transferframe2.telemetry.pdhcrc000
    :field transferframe2_pdhcrc001: masterframe.transferframe2.telemetry.pdhcrc001
    :field transferframe2_pdhcrc002: masterframe.transferframe2.telemetry.pdhcrc002
    :field transferframe2_pdhcrc003: masterframe.transferframe2.telemetry.pdhcrc003
    :field transferframe2_pdhcrc004: masterframe.transferframe2.telemetry.pdhcrc004
    :field transferframe2_pdhcrc005: masterframe.transferframe2.telemetry.pdhcrc005
    :field transferframe2_pdhcrc006: masterframe.transferframe2.telemetry.pdhcrc006
    :field transferframe2_pdhcrc007: masterframe.transferframe2.telemetry.pdhcrc007
    :field transferframe2_pdhcrc008: masterframe.transferframe2.telemetry.pdhcrc008
    :field transferframe2_pdhcrc009: masterframe.transferframe2.telemetry.pdhcrc009
    :field transferframe2_pdhcrc010: masterframe.transferframe2.telemetry.pdhcrc010
    :field transferframe2_pdhcrc011: masterframe.transferframe2.telemetry.pdhcrc011
    :field transferframe2_pdhcrc012: masterframe.transferframe2.telemetry.pdhcrc012
    :field transferframe2_pdhcrc013: masterframe.transferframe2.telemetry.pdhcrc013
    :field transferframe2_pdhcrc014: masterframe.transferframe2.telemetry.pdhcrc014
    :field transferframe2_pdhcrc015: masterframe.transferframe2.telemetry.pdhcrc015
    :field transferframe2_pdhcrc016: masterframe.transferframe2.telemetry.pdhcrc016
    :field transferframe2_pdhcrc017: masterframe.transferframe2.telemetry.pdhcrc017
    :field transferframe2_pdhcrc018: masterframe.transferframe2.telemetry.pdhcrc018
    :field transferframe2_pdhcrc019: masterframe.transferframe2.telemetry.pdhcrc019
    :field transferframe2_pdhcrc020: masterframe.transferframe2.telemetry.pdhcrc020
    :field transferframe2_pdhcrc021: masterframe.transferframe2.telemetry.pdhcrc021
    :field transferframe2_pdhcrc022: masterframe.transferframe2.telemetry.pdhcrc022
    :field transferframe2_pdhcrc023: masterframe.transferframe2.telemetry.pdhcrc023
    :field transferframe2_pdhcrc024: masterframe.transferframe2.telemetry.pdhcrc024
    :field transferframe2_pdhcrc025: masterframe.transferframe2.telemetry.pdhcrc025
    :field transferframe2_pdhcrc026: masterframe.transferframe2.telemetry.pdhcrc026
    :field transferframe2_pdhcrc027: masterframe.transferframe2.telemetry.pdhcrc027
    :field transferframe2_pdhcrc028: masterframe.transferframe2.telemetry.pdhcrc028
    :field transferframe2_pdhcrc029: masterframe.transferframe2.telemetry.pdhcrc029
    :field transferframe2_pdhcrc030: masterframe.transferframe2.telemetry.pdhcrc030
    :field transferframe2_pdhcrccmask00: masterframe.transferframe2.telemetry.pdhcrccmask00
    :field transferframe2_acswhx: masterframe.transferframe2.telemetry.acswhx
    :field transferframe2_telemetry_acsm0x_raw: masterframe.transferframe2.telemetry.acsm0x.raw
    :field transferframe2_telemetry_acsm0x_value: masterframe.transferframe2.telemetry.acsm0x.value
    :field transferframe2_telemetry_acsm0y_raw: masterframe.transferframe2.telemetry.acsm0y.raw
    :field transferframe2_telemetry_acsm0y_value: masterframe.transferframe2.telemetry.acsm0y.value
    :field transferframe2_telemetry_acsm0z_raw: masterframe.transferframe2.telemetry.acsm0z.raw
    :field transferframe2_telemetry_acsm0z_value: masterframe.transferframe2.telemetry.acsm0z.value
    :field transferframe2_reserveacsgr: masterframe.transferframe2.telemetry.reserveacsgr
    :field transferframe2_acstemex: masterframe.transferframe2.telemetry.acstemex
    :field transferframe2_acstemey: masterframe.transferframe2.telemetry.acstemey
    :field transferframe2_acstemez: masterframe.transferframe2.telemetry.acstemez
    :field transferframe2_telemetry_acstemevelx_raw: masterframe.transferframe2.telemetry.acstemevelx.raw
    :field transferframe2_telemetry_acstemevelx_value: masterframe.transferframe2.telemetry.acstemevelx.value
    :field transferframe2_telemetry_acstemevely_raw: masterframe.transferframe2.telemetry.acstemevely.raw
    :field transferframe2_telemetry_acstemevely_value: masterframe.transferframe2.telemetry.acstemevely.value
    :field transferframe2_telemetry_acstemevelz_raw: masterframe.transferframe2.telemetry.acstemevelz.raw
    :field transferframe2_telemetry_acstemevelz_value: masterframe.transferframe2.telemetry.acstemevelz.value
    :field transferframe2_acsefx: masterframe.transferframe2.telemetry.acsefx
    :field transferframe2_acsefy: masterframe.transferframe2.telemetry.acsefy
    :field transferframe2_acsefz: masterframe.transferframe2.telemetry.acsefz
    :field transferframe2_telemetry_acsmagifx_raw: masterframe.transferframe2.telemetry.acsmagifx.raw
    :field transferframe2_telemetry_acsmagifx_value: masterframe.transferframe2.telemetry.acsmagifx.value
    :field transferframe2_telemetry_acsmagify_raw: masterframe.transferframe2.telemetry.acsmagify.raw
    :field transferframe2_telemetry_acsmagify_value: masterframe.transferframe2.telemetry.acsmagify.value
    :field transferframe2_telemetry_acsmagifz_raw: masterframe.transferframe2.telemetry.acsmagifz.raw
    :field transferframe2_telemetry_acsmagifz_value: masterframe.transferframe2.telemetry.acsmagifz.value
    :field transferframe2_telemetry_acssunifx_raw: masterframe.transferframe2.telemetry.acssunifx.raw
    :field transferframe2_telemetry_acssunifx_value: masterframe.transferframe2.telemetry.acssunifx.value
    :field transferframe2_telemetry_acssunify_raw: masterframe.transferframe2.telemetry.acssunify.raw
    :field transferframe2_telemetry_acssunify_value: masterframe.transferframe2.telemetry.acssunify.value
    :field transferframe2_telemetry_acssunifz_raw: masterframe.transferframe2.telemetry.acssunifz.raw
    :field transferframe2_telemetry_acssunifz_value: masterframe.transferframe2.telemetry.acssunifz.value
    :field transferframe2_telemetry_acsqdes00_raw: masterframe.transferframe2.telemetry.acsqdes00.raw
    :field transferframe2_telemetry_acsqdes00_value: masterframe.transferframe2.telemetry.acsqdes00.value
    :field transferframe2_telemetry_acsqdes01_raw: masterframe.transferframe2.telemetry.acsqdes01.raw
    :field transferframe2_telemetry_acsqdes01_value: masterframe.transferframe2.telemetry.acsqdes01.value
    :field transferframe2_telemetry_acsqdes02_raw: masterframe.transferframe2.telemetry.acsqdes02.raw
    :field transferframe2_telemetry_acsqdes02_value: masterframe.transferframe2.telemetry.acsqdes02.value
    :field transferframe2_telemetry_acsqdes03_raw: masterframe.transferframe2.telemetry.acsqdes03.raw
    :field transferframe2_telemetry_acsqdes03_value: masterframe.transferframe2.telemetry.acsqdes03.value
    :field transferframe2_telemetry_acswcx_raw: masterframe.transferframe2.telemetry.acswcx.raw
    :field transferframe2_telemetry_acswcx_value: masterframe.transferframe2.telemetry.acswcx.value
    :field transferframe2_telemetry_acswcy_raw: masterframe.transferframe2.telemetry.acswcy.raw
    :field transferframe2_telemetry_acswcy_value: masterframe.transferframe2.telemetry.acswcy.value
    :field transferframe2_telemetry_acswcz_raw: masterframe.transferframe2.telemetry.acswcz.raw
    :field transferframe2_telemetry_acswcz_value: masterframe.transferframe2.telemetry.acswcz.value
    :field transferframe2_telemetry_acswu0_raw: masterframe.transferframe2.telemetry.acswu0.raw
    :field transferframe2_telemetry_acswu0_value: masterframe.transferframe2.telemetry.acswu0.value
    :field transferframe2_telemetry_acswu1_raw: masterframe.transferframe2.telemetry.acswu1.raw
    :field transferframe2_telemetry_acswu1_value: masterframe.transferframe2.telemetry.acswu1.value
    :field transferframe2_telemetry_acswu2_raw: masterframe.transferframe2.telemetry.acswu2.raw
    :field transferframe2_telemetry_acswu2_value: masterframe.transferframe2.telemetry.acswu2.value
    :field transferframe2_telemetry_acswq0_raw: masterframe.transferframe2.telemetry.acswq0.raw
    :field transferframe2_telemetry_acswq0_value: masterframe.transferframe2.telemetry.acswq0.value
    :field transferframe2_telemetry_acswq1_raw: masterframe.transferframe2.telemetry.acswq1.raw
    :field transferframe2_telemetry_acswq1_value: masterframe.transferframe2.telemetry.acswq1.value
    :field transferframe2_telemetry_acswq2_raw: masterframe.transferframe2.telemetry.acswq2.raw
    :field transferframe2_telemetry_acswq2_value: masterframe.transferframe2.telemetry.acswq2.value
    :field transferframe2_telemetry_acswq3_raw: masterframe.transferframe2.telemetry.acswq3.raw
    :field transferframe2_telemetry_acswq3_value: masterframe.transferframe2.telemetry.acswq3.value
    :field transferframe2_acswa0: masterframe.transferframe2.telemetry.acswa0
    :field transferframe2_acswa1: masterframe.transferframe2.telemetry.acswa1
    :field transferframe2_acswa2: masterframe.transferframe2.telemetry.acswa2
    :field transferframe2_acs_tm_vecs_res: masterframe.transferframe2.telemetry.acs_tm_vecs_res
    :field transferframe2_psmfs1: masterframe.transferframe2.telemetry.psmfs1
    :field transferframe2_pcch02: masterframe.transferframe2.telemetry.pcch02
    :field transferframe2_tcfrcp: masterframe.transferframe2.telemetry.tcfrcp
    :field transferframe2_tmhkur: masterframe.transferframe2.telemetry.tmhkur
    :field transferframe2_cstutc: masterframe.transferframe2.telemetry.cstutc
    :field transferframe2_cstsys: masterframe.transferframe2.telemetry.cstsys
    :field transferframe2_pcsyst: masterframe.transferframe2.telemetry.pcsyst
    :field transferframe2_acswhy: masterframe.transferframe2.telemetry.acswhy
    :field transferframe2_acswhz: masterframe.transferframe2.telemetry.acswhz
    :field transferframe2_telemetry_acg1ym_raw: masterframe.transferframe2.telemetry.acg1ym.raw
    :field transferframe2_telemetry_acg1ym_value: masterframe.transferframe2.telemetry.acg1ym.value
    :field transferframe2_telemetry_acg1zm_raw: masterframe.transferframe2.telemetry.acg1zm.raw
    :field transferframe2_telemetry_acg1zm_value: masterframe.transferframe2.telemetry.acg1zm.value
    :field transferframe2_telemetry_acg1xm_raw: masterframe.transferframe2.telemetry.acg1xm.raw
    :field transferframe2_telemetry_acg1xm_value: masterframe.transferframe2.telemetry.acg1xm.value
    :field transferframe2_obctmffp: masterframe.transferframe2.telemetry.obctmffp
    :field transferframe2_obcswversion: masterframe.transferframe2.telemetry.obcswversion
    :field transferframe2_telemetry_acscmod_raw: masterframe.transferframe2.telemetry.acscmod.raw
    :field transferframe2_telemetry_acscmod_value: masterframe.transferframe2.telemetry.acscmod.value
    :field transferframe2_cctccp: masterframe.transferframe2.telemetry.cctccp
    :field transferframe2_telemetry_b2_tm_reserve_raw: masterframe.transferframe2.telemetry.b2_tm_reserve.raw
    :field transferframe2_telemetry_b2_tm_reserve_value: masterframe.transferframe2.telemetry.b2_tm_reserve.value
    :field transferframe2_tledoy: masterframe.transferframe2.telemetry.tledoy
    :field transferframe2_telemetry_tlemem_raw: masterframe.transferframe2.telemetry.tlemem.raw
    :field transferframe2_telemetry_tlemem_value: masterframe.transferframe2.telemetry.tlemem.value
    :field transferframe2_tleecc: masterframe.transferframe2.telemetry.tleecc
    :field transferframe2_telemetry_tleinc_raw: masterframe.transferframe2.telemetry.tleinc.raw
    :field transferframe2_telemetry_tleinc_value: masterframe.transferframe2.telemetry.tleinc.value
    :field transferframe2_telemetry_tleaop_raw: masterframe.transferframe2.telemetry.tleaop.raw
    :field transferframe2_telemetry_tleaop_value: masterframe.transferframe2.telemetry.tleaop.value
    :field transferframe2_telemetry_tleraa_raw: masterframe.transferframe2.telemetry.tleraa.raw
    :field transferframe2_telemetry_tleraa_value: masterframe.transferframe2.telemetry.tleraa.value
    :field transferframe2_telemetry_tleman_raw: masterframe.transferframe2.telemetry.tleman.raw
    :field transferframe2_telemetry_tleman_value: masterframe.transferframe2.telemetry.tleman.value
    :field transferframe2_tledrt: masterframe.transferframe2.telemetry.tledrt
    :field transferframe2_tlexpc: masterframe.transferframe2.telemetry.tlexpc
    :field transferframe2_tleypc: masterframe.transferframe2.telemetry.tleypc
    :field transferframe2_tlettd: masterframe.transferframe2.telemetry.tlettd
    :field transferframe2_tleutd: masterframe.transferframe2.telemetry.tleutd
    :field transferframe2_tledep: masterframe.transferframe2.telemetry.tledep
    :field transferframe2_tledps: masterframe.transferframe2.telemetry.tledps
    :field transferframe2_tleyea: masterframe.transferframe2.telemetry.tleyea
    :field transferframe2_tle_placeholder: masterframe.transferframe2.telemetry.tle_placeholder
    :field transferframe2_fecfd: masterframe.transferframe2.fecfd
    :field transferframe3_asm: masterframe.transferframe3.asm
    :field transferframe3_raw: masterframe.transferframe3.tfvn.raw
    :field transferframe3_value: masterframe.transferframe3.tfvn.value
    :field transferframe3_scid_raw: masterframe.transferframe3.scid.raw
    :field transferframe3_scid_value: masterframe.transferframe3.scid.value
    :field transferframe3_vcidb_raw: masterframe.transferframe3.vcidb.raw
    :field transferframe3_vcidb_value: masterframe.transferframe3.vcidb.value
    :field transferframe3_ocff: masterframe.transferframe3.ocff
    :field transferframe3_mcfc: masterframe.transferframe3.mcfc
    :field transferframe3_vcfc: masterframe.transferframe3.vcfc
    :field transferframe3_tf_shf: masterframe.transferframe3.tf_shf
    :field transferframe3_synchflag: masterframe.transferframe3.synchflag
    :field transferframe3_pof: masterframe.transferframe3.pof
    :field transferframe3_slid_raw: masterframe.transferframe3.slid.raw
    :field transferframe3_slid_value: masterframe.transferframe3.slid.value
    :field transferframe3_fhp_raw: masterframe.transferframe3.fhp.raw
    :field transferframe3_fhp_value: masterframe.transferframe3.fhp.value
    :field transferframe3_source_pvn_raw: masterframe.transferframe3.source.pvn.raw
    :field transferframe3_source_pvn_value: masterframe.transferframe3.source.pvn.value
    :field transferframe3_pt: masterframe.transferframe3.source.pt
    :field transferframe3_shf: masterframe.transferframe3.source.shf
    :field transferframe3_source_apid_raw: masterframe.transferframe3.source.apid.raw
    :field transferframe3_source_apid_value: masterframe.transferframe3.source.apid.value
    :field transferframe3_source_seqflag_raw: masterframe.transferframe3.source.seqflag.raw
    :field transferframe3_source_seqflag_value: masterframe.transferframe3.source.seqflag.value
    :field transferframe3_source_psc_raw: masterframe.transferframe3.source.psc.raw
    :field transferframe3_source_psc_value: masterframe.transferframe3.source.psc.value
    :field transferframe3_pdl: masterframe.transferframe3.source.pdl
    :field transferframe3_telemetry_cstutc_raw: masterframe.transferframe3.telemetry.cstutc.raw
    :field transferframe3_telemetry_cstutc_value: masterframe.transferframe3.telemetry.cstutc.value
    :field transferframe3_telemetry_csaxp_raw: masterframe.transferframe3.telemetry.csaxp.raw
    :field transferframe3_telemetry_csaxp_value: masterframe.transferframe3.telemetry.csaxp.value
    :field transferframe3_telemetry_csaxn_raw: masterframe.transferframe3.telemetry.csaxn.raw
    :field transferframe3_telemetry_csaxn_value: masterframe.transferframe3.telemetry.csaxn.value
    :field transferframe3_telemetry_csayp_raw: masterframe.transferframe3.telemetry.csayp.raw
    :field transferframe3_telemetry_csayp_value: masterframe.transferframe3.telemetry.csayp.value
    :field transferframe3_telemetry_csayn_raw: masterframe.transferframe3.telemetry.csayn.raw
    :field transferframe3_telemetry_csayn_value: masterframe.transferframe3.telemetry.csayn.value
    :field transferframe3_telemetry_csazp_raw: masterframe.transferframe3.telemetry.csazp.raw
    :field transferframe3_telemetry_csazp_value: masterframe.transferframe3.telemetry.csazp.value
    :field transferframe3_telemetry_csazn_raw: masterframe.transferframe3.telemetry.csazn.raw
    :field transferframe3_telemetry_csazn_value: masterframe.transferframe3.telemetry.csazn.value
    :field transferframe3_telemetry_vsabus_raw: masterframe.transferframe3.telemetry.vsabus.raw
    :field transferframe3_telemetry_vsabus_value: masterframe.transferframe3.telemetry.vsabus.value
    :field transferframe3_telemetry_cc0in_raw: masterframe.transferframe3.telemetry.cc0in.raw
    :field transferframe3_telemetry_cc0in_value: masterframe.transferframe3.telemetry.cc0in.value
    :field transferframe3_telemetry_cc1in_raw: masterframe.transferframe3.telemetry.cc1in.raw
    :field transferframe3_telemetry_cc1in_value: masterframe.transferframe3.telemetry.cc1in.value
    :field transferframe3_telemetry_vbat0_raw: masterframe.transferframe3.telemetry.vbat0.raw
    :field transferframe3_telemetry_vbat0_value: masterframe.transferframe3.telemetry.vbat0.value
    :field transferframe3_telemetry_vbat1_raw: masterframe.transferframe3.telemetry.vbat1.raw
    :field transferframe3_telemetry_vbat1_value: masterframe.transferframe3.telemetry.vbat1.value
    :field transferframe3_telemetry_cc0out_raw: masterframe.transferframe3.telemetry.cc0out.raw
    :field transferframe3_telemetry_cc0out_value: masterframe.transferframe3.telemetry.cc0out.value
    :field transferframe3_telemetry_cc1out_raw: masterframe.transferframe3.telemetry.cc1out.raw
    :field transferframe3_telemetry_cc1out_value: masterframe.transferframe3.telemetry.cc1out.value
    :field transferframe3_telemetry_v50bus_raw: masterframe.transferframe3.telemetry.v50bus.raw
    :field transferframe3_telemetry_v50bus_value: masterframe.transferframe3.telemetry.v50bus.value
    :field transferframe3_telemetry_v33bus_raw: masterframe.transferframe3.telemetry.v33bus.raw
    :field transferframe3_telemetry_v33bus_value: masterframe.transferframe3.telemetry.v33bus.value
    :field transferframe3_telemetry_cpcu_raw: masterframe.transferframe3.telemetry.cpcu.raw
    :field transferframe3_telemetry_cpcu_value: masterframe.transferframe3.telemetry.cpcu.value
    :field transferframe3_telemetry_cobc0_raw: masterframe.transferframe3.telemetry.cobc0.raw
    :field transferframe3_telemetry_cobc0_value: masterframe.transferframe3.telemetry.cobc0.value
    :field transferframe3_telemetry_cobc1_raw: masterframe.transferframe3.telemetry.cobc1.raw
    :field transferframe3_telemetry_cobc1_value: masterframe.transferframe3.telemetry.cobc1.value
    :field transferframe3_telemetry_ctnc0_raw: masterframe.transferframe3.telemetry.ctnc0.raw
    :field transferframe3_telemetry_ctnc0_value: masterframe.transferframe3.telemetry.ctnc0.value
    :field transferframe3_telemetry_ctnc1_raw: masterframe.transferframe3.telemetry.ctnc1.raw
    :field transferframe3_telemetry_ctnc1_value: masterframe.transferframe3.telemetry.ctnc1.value
    :field transferframe3_telemetry_ctrx0_raw: masterframe.transferframe3.telemetry.ctrx0.raw
    :field transferframe3_telemetry_ctrx0_value: masterframe.transferframe3.telemetry.ctrx0.value
    :field transferframe3_telemetry_ctrx1_raw: masterframe.transferframe3.telemetry.ctrx1.raw
    :field transferframe3_telemetry_ctrx1_value: masterframe.transferframe3.telemetry.ctrx1.value
    :field transferframe3_telemetry_cpdh_raw: masterframe.transferframe3.telemetry.cpdh.raw
    :field transferframe3_telemetry_cpdh_value: masterframe.transferframe3.telemetry.cpdh.value
    :field transferframe3_telemetry_ccam_raw: masterframe.transferframe3.telemetry.ccam.raw
    :field transferframe3_telemetry_ccam_value: masterframe.transferframe3.telemetry.ccam.value
    :field transferframe3_telemetry_csss_raw: masterframe.transferframe3.telemetry.csss.raw
    :field transferframe3_telemetry_csss_value: masterframe.transferframe3.telemetry.csss.value
    :field transferframe3_telemetry_cmfs0_raw: masterframe.transferframe3.telemetry.cmfs0.raw
    :field transferframe3_telemetry_cmfs0_value: masterframe.transferframe3.telemetry.cmfs0.value
    :field transferframe3_telemetry_cmfs1_raw: masterframe.transferframe3.telemetry.cmfs1.raw
    :field transferframe3_telemetry_cmfs1_value: masterframe.transferframe3.telemetry.cmfs1.value
    :field transferframe3_telemetry_cgyr0_raw: masterframe.transferframe3.telemetry.cgyr0.raw
    :field transferframe3_telemetry_cgyr0_value: masterframe.transferframe3.telemetry.cgyr0.value
    :field transferframe3_telemetry_cmcs_raw: masterframe.transferframe3.telemetry.cmcs.raw
    :field transferframe3_telemetry_cmcs_value: masterframe.transferframe3.telemetry.cmcs.value
    :field transferframe3_telemetry_cwhl_raw: masterframe.transferframe3.telemetry.cwhl.raw
    :field transferframe3_telemetry_cwhl_value: masterframe.transferframe3.telemetry.cwhl.value
    :field transferframe3_telemetry_ccan0_raw: masterframe.transferframe3.telemetry.ccan0.raw
    :field transferframe3_telemetry_ccan0_value: masterframe.transferframe3.telemetry.ccan0.value
    :field transferframe3_telemetry_ccan1_raw: masterframe.transferframe3.telemetry.ccan1.raw
    :field transferframe3_telemetry_ccan1_value: masterframe.transferframe3.telemetry.ccan1.value
    :field transferframe3_telemetry_vmfs0_raw: masterframe.transferframe3.telemetry.vmfs0.raw
    :field transferframe3_telemetry_vmfs0_value: masterframe.transferframe3.telemetry.vmfs0.value
    :field transferframe3_telemetry_vmfs1_raw: masterframe.transferframe3.telemetry.vmfs1.raw
    :field transferframe3_telemetry_vmfs1_value: masterframe.transferframe3.telemetry.vmfs1.value
    :field transferframe3_telemetry_cmcsxp_raw: masterframe.transferframe3.telemetry.cmcsxp.raw
    :field transferframe3_telemetry_cmcsxp_value: masterframe.transferframe3.telemetry.cmcsxp.value
    :field transferframe3_telemetry_cmcsxn_raw: masterframe.transferframe3.telemetry.cmcsxn.raw
    :field transferframe3_telemetry_cmcsxn_value: masterframe.transferframe3.telemetry.cmcsxn.value
    :field transferframe3_telemetry_cmcsyp_raw: masterframe.transferframe3.telemetry.cmcsyp.raw
    :field transferframe3_telemetry_cmcsyp_value: masterframe.transferframe3.telemetry.cmcsyp.value
    :field transferframe3_telemetry_cmcsyn_raw: masterframe.transferframe3.telemetry.cmcsyn.raw
    :field transferframe3_telemetry_cmcsyn_value: masterframe.transferframe3.telemetry.cmcsyn.value
    :field transferframe3_telemetry_cmcszp_raw: masterframe.transferframe3.telemetry.cmcszp.raw
    :field transferframe3_telemetry_cmcszp_value: masterframe.transferframe3.telemetry.cmcszp.value
    :field transferframe3_telemetry_cmcszn_raw: masterframe.transferframe3.telemetry.cmcszn.raw
    :field transferframe3_telemetry_cmcszn_value: masterframe.transferframe3.telemetry.cmcszn.value
    :field transferframe3_telemetry_cobcmcu_raw: masterframe.transferframe3.telemetry.cobcmcu.raw
    :field transferframe3_telemetry_cobcmcu_value: masterframe.transferframe3.telemetry.cobcmcu.value
    :field transferframe3_telemetry_cobcext_raw: masterframe.transferframe3.telemetry.cobcext.raw
    :field transferframe3_telemetry_cobcext_value: masterframe.transferframe3.telemetry.cobcext.value
    :field transferframe3_telemetry_ttrx1_raw: masterframe.transferframe3.telemetry.ttrx1.raw
    :field transferframe3_telemetry_ttrx1_value: masterframe.transferframe3.telemetry.ttrx1.value
    :field transferframe3_telemetry_cpdh2_raw: masterframe.transferframe3.telemetry.cpdh2.raw
    :field transferframe3_telemetry_cpdh2_value: masterframe.transferframe3.telemetry.cpdh2.value
    :field transferframe3_telemetry_ccam2_raw: masterframe.transferframe3.telemetry.ccam2.raw
    :field transferframe3_telemetry_ccam2_value: masterframe.transferframe3.telemetry.ccam2.value
    :field transferframe3_asstop: masterframe.transferframe3.telemetry.asstop
    :field transferframe3_assintv: masterframe.transferframe3.telemetry.assintv
    :field transferframe3_ascest: masterframe.transferframe3.telemetry.ascest
    :field transferframe3_asactv: masterframe.transferframe3.telemetry.asactv
    :field transferframe3_reserve2: masterframe.transferframe3.telemetry.reserve2
    :field transferframe3_reserve1: masterframe.transferframe3.telemetry.reserve1
    :field transferframe3_telemetry_tsaxp_raw: masterframe.transferframe3.telemetry.tsaxp.raw
    :field transferframe3_telemetry_tsaxp_value: masterframe.transferframe3.telemetry.tsaxp.value
    :field transferframe3_telemetry_tsaxn_raw: masterframe.transferframe3.telemetry.tsaxn.raw
    :field transferframe3_telemetry_tsaxn_value: masterframe.transferframe3.telemetry.tsaxn.value
    :field transferframe3_telemetry_tsayp_raw: masterframe.transferframe3.telemetry.tsayp.raw
    :field transferframe3_telemetry_tsayp_value: masterframe.transferframe3.telemetry.tsayp.value
    :field transferframe3_telemetry_tsayn_raw: masterframe.transferframe3.telemetry.tsayn.raw
    :field transferframe3_telemetry_tsayn_value: masterframe.transferframe3.telemetry.tsayn.value
    :field transferframe3_telemetry_tsazp_raw: masterframe.transferframe3.telemetry.tsazp.raw
    :field transferframe3_telemetry_tsazp_value: masterframe.transferframe3.telemetry.tsazp.value
    :field transferframe3_telemetry_tsazn_raw: masterframe.transferframe3.telemetry.tsazn.raw
    :field transferframe3_telemetry_tsazn_value: masterframe.transferframe3.telemetry.tsazn.value
    :field transferframe3_telemetry_tbat0_raw: masterframe.transferframe3.telemetry.tbat0.raw
    :field transferframe3_telemetry_tbat0_value: masterframe.transferframe3.telemetry.tbat0.value
    :field transferframe3_telemetry_tbat1_raw: masterframe.transferframe3.telemetry.tbat1.raw
    :field transferframe3_telemetry_tbat1_value: masterframe.transferframe3.telemetry.tbat1.value
    :field transferframe3_telemetry_tpcu00_raw: masterframe.transferframe3.telemetry.tpcu00.raw
    :field transferframe3_telemetry_tpcu00_value: masterframe.transferframe3.telemetry.tpcu00.value
    :field transferframe3_telemetry_tpcu01_raw: masterframe.transferframe3.telemetry.tpcu01.raw
    :field transferframe3_telemetry_tpcu01_value: masterframe.transferframe3.telemetry.tpcu01.value
    :field transferframe3_telemetry_tmfs0_raw: masterframe.transferframe3.telemetry.tmfs0.raw
    :field transferframe3_telemetry_tmfs0_value: masterframe.transferframe3.telemetry.tmfs0.value
    :field transferframe3_telemetry_tmfs1_raw: masterframe.transferframe3.telemetry.tmfs1.raw
    :field transferframe3_telemetry_tmfs1_value: masterframe.transferframe3.telemetry.tmfs1.value
    :field transferframe3_telemetry_twhlx_raw: masterframe.transferframe3.telemetry.twhlx.raw
    :field transferframe3_telemetry_twhlx_value: masterframe.transferframe3.telemetry.twhlx.value
    :field transferframe3_telemetry_twhly_raw: masterframe.transferframe3.telemetry.twhly.raw
    :field transferframe3_telemetry_twhly_value: masterframe.transferframe3.telemetry.twhly.value
    :field transferframe3_telemetry_twhlz_raw: masterframe.transferframe3.telemetry.twhlz.raw
    :field transferframe3_telemetry_twhlz_value: masterframe.transferframe3.telemetry.twhlz.value
    :field transferframe3_telemetry_tgyrox_raw: masterframe.transferframe3.telemetry.tgyrox.raw
    :field transferframe3_telemetry_tgyrox_value: masterframe.transferframe3.telemetry.tgyrox.value
    :field transferframe3_telemetry_tgyroy_raw: masterframe.transferframe3.telemetry.tgyroy.raw
    :field transferframe3_telemetry_tgyroy_value: masterframe.transferframe3.telemetry.tgyroy.value
    :field transferframe3_telemetry_tgyroz_raw: masterframe.transferframe3.telemetry.tgyroz.raw
    :field transferframe3_telemetry_tgyroz_value: masterframe.transferframe3.telemetry.tgyroz.value
    :field transferframe3_telemetry_tobc00_raw: masterframe.transferframe3.telemetry.tobc00.raw
    :field transferframe3_telemetry_tobc00_value: masterframe.transferframe3.telemetry.tobc00.value
    :field transferframe3_telemetry_tobc01_raw: masterframe.transferframe3.telemetry.tobc01.raw
    :field transferframe3_telemetry_tobc01_value: masterframe.transferframe3.telemetry.tobc01.value
    :field transferframe3_telemetry_tobc02_raw: masterframe.transferframe3.telemetry.tobc02.raw
    :field transferframe3_telemetry_tobc02_value: masterframe.transferframe3.telemetry.tobc02.value
    :field transferframe3_telemetry_ttrx0_raw: masterframe.transferframe3.telemetry.ttrx0.raw
    :field transferframe3_telemetry_ttrx0_value: masterframe.transferframe3.telemetry.ttrx0.value
    :field transferframe3_reserve: masterframe.transferframe3.telemetry.reserve
    :field transferframe3_telemetry_acssuxpx0_raw: masterframe.transferframe3.telemetry.acssuxpx0.raw
    :field transferframe3_telemetry_acssuxpx0_value: masterframe.transferframe3.telemetry.acssuxpx0.value
    :field transferframe3_telemetry_acssuxpx1_raw: masterframe.transferframe3.telemetry.acssuxpx1.raw
    :field transferframe3_telemetry_acssuxpx1_value: masterframe.transferframe3.telemetry.acssuxpx1.value
    :field transferframe3_telemetry_acssuxpy0_raw: masterframe.transferframe3.telemetry.acssuxpy0.raw
    :field transferframe3_telemetry_acssuxpy0_value: masterframe.transferframe3.telemetry.acssuxpy0.value
    :field transferframe3_telemetry_acssuxpy1_raw: masterframe.transferframe3.telemetry.acssuxpy1.raw
    :field transferframe3_telemetry_acssuxpy1_value: masterframe.transferframe3.telemetry.acssuxpy1.value
    :field transferframe3_telemetry_acssuxnx0_raw: masterframe.transferframe3.telemetry.acssuxnx0.raw
    :field transferframe3_telemetry_acssuxnx0_value: masterframe.transferframe3.telemetry.acssuxnx0.value
    :field transferframe3_telemetry_acssuxnx1_raw: masterframe.transferframe3.telemetry.acssuxnx1.raw
    :field transferframe3_telemetry_acssuxnx1_value: masterframe.transferframe3.telemetry.acssuxnx1.value
    :field transferframe3_telemetry_acssuxny0_raw: masterframe.transferframe3.telemetry.acssuxny0.raw
    :field transferframe3_telemetry_acssuxny0_value: masterframe.transferframe3.telemetry.acssuxny0.value
    :field transferframe3_telemetry_acssuxny1_raw: masterframe.transferframe3.telemetry.acssuxny1.raw
    :field transferframe3_telemetry_acssuxny1_value: masterframe.transferframe3.telemetry.acssuxny1.value
    :field transferframe3_telemetry_acssuypx0_raw: masterframe.transferframe3.telemetry.acssuypx0.raw
    :field transferframe3_telemetry_acssuypx0_value: masterframe.transferframe3.telemetry.acssuypx0.value
    :field transferframe3_telemetry_acssuypx1_raw: masterframe.transferframe3.telemetry.acssuypx1.raw
    :field transferframe3_telemetry_acssuypx1_value: masterframe.transferframe3.telemetry.acssuypx1.value
    :field transferframe3_telemetry_acssuypy0_raw: masterframe.transferframe3.telemetry.acssuypy0.raw
    :field transferframe3_telemetry_acssuypy0_value: masterframe.transferframe3.telemetry.acssuypy0.value
    :field transferframe3_telemetry_acssuypy1_raw: masterframe.transferframe3.telemetry.acssuypy1.raw
    :field transferframe3_telemetry_acssuypy1_value: masterframe.transferframe3.telemetry.acssuypy1.value
    :field transferframe3_telemetry_acssuynx0_raw: masterframe.transferframe3.telemetry.acssuynx0.raw
    :field transferframe3_telemetry_acssuynx0_value: masterframe.transferframe3.telemetry.acssuynx0.value
    :field transferframe3_telemetry_acssuynx1_raw: masterframe.transferframe3.telemetry.acssuynx1.raw
    :field transferframe3_telemetry_acssuynx1_value: masterframe.transferframe3.telemetry.acssuynx1.value
    :field transferframe3_telemetry_acssuyny0_raw: masterframe.transferframe3.telemetry.acssuyny0.raw
    :field transferframe3_telemetry_acssuyny0_value: masterframe.transferframe3.telemetry.acssuyny0.value
    :field transferframe3_telemetry_acssuyny1_raw: masterframe.transferframe3.telemetry.acssuyny1.raw
    :field transferframe3_telemetry_acssuyny1_value: masterframe.transferframe3.telemetry.acssuyny1.value
    :field transferframe3_telemetry_acssuzpx0_raw: masterframe.transferframe3.telemetry.acssuzpx0.raw
    :field transferframe3_telemetry_acssuzpx0_value: masterframe.transferframe3.telemetry.acssuzpx0.value
    :field transferframe3_telemetry_acssuzpx1_raw: masterframe.transferframe3.telemetry.acssuzpx1.raw
    :field transferframe3_telemetry_acssuzpx1_value: masterframe.transferframe3.telemetry.acssuzpx1.value
    :field transferframe3_telemetry_acssuzpy0_raw: masterframe.transferframe3.telemetry.acssuzpy0.raw
    :field transferframe3_telemetry_acssuzpy0_value: masterframe.transferframe3.telemetry.acssuzpy0.value
    :field transferframe3_telemetry_acssuzpy1_raw: masterframe.transferframe3.telemetry.acssuzpy1.raw
    :field transferframe3_telemetry_acssuzpy1_value: masterframe.transferframe3.telemetry.acssuzpy1.value
    :field transferframe3_telemetry_acssuznx0_raw: masterframe.transferframe3.telemetry.acssuznx0.raw
    :field transferframe3_telemetry_acssuznx0_value: masterframe.transferframe3.telemetry.acssuznx0.value
    :field transferframe3_telemetry_acssuznx1_raw: masterframe.transferframe3.telemetry.acssuznx1.raw
    :field transferframe3_telemetry_acssuznx1_value: masterframe.transferframe3.telemetry.acssuznx1.value
    :field transferframe3_telemetry_acssuzny0_raw: masterframe.transferframe3.telemetry.acssuzny0.raw
    :field transferframe3_telemetry_acssuzny0_value: masterframe.transferframe3.telemetry.acssuzny0.value
    :field transferframe3_telemetry_acssuzny1_raw: masterframe.transferframe3.telemetry.acssuzny1.raw
    :field transferframe3_telemetry_acssuzny1_value: masterframe.transferframe3.telemetry.acssuzny1.value
    :field transferframe3_telemetry_cmfs0x_raw: masterframe.transferframe3.telemetry.cmfs0x.raw
    :field transferframe3_telemetry_cmfs0x_value: masterframe.transferframe3.telemetry.cmfs0x.value
    :field transferframe3_telemetry_cmfs0y_raw: masterframe.transferframe3.telemetry.cmfs0y.raw
    :field transferframe3_telemetry_cmfs0y_value: masterframe.transferframe3.telemetry.cmfs0y.value
    :field transferframe3_telemetry_cmfs0z_raw: masterframe.transferframe3.telemetry.cmfs0z.raw
    :field transferframe3_telemetry_cmfs0z_value: masterframe.transferframe3.telemetry.cmfs0z.value
    :field transferframe3_telemetry_cmfs1x_raw: masterframe.transferframe3.telemetry.cmfs1x.raw
    :field transferframe3_telemetry_cmfs1x_value: masterframe.transferframe3.telemetry.cmfs1x.value
    :field transferframe3_telemetry_cmfs1y_raw: masterframe.transferframe3.telemetry.cmfs1y.raw
    :field transferframe3_telemetry_cmfs1y_value: masterframe.transferframe3.telemetry.cmfs1y.value
    :field transferframe3_telemetry_cmfs1z_raw: masterframe.transferframe3.telemetry.cmfs1z.raw
    :field transferframe3_telemetry_cmfs1z_value: masterframe.transferframe3.telemetry.cmfs1z.value
    :field transferframe3_telemetry_acsgy0x_raw: masterframe.transferframe3.telemetry.acsgy0x.raw
    :field transferframe3_telemetry_acsgy0x_value: masterframe.transferframe3.telemetry.acsgy0x.value
    :field transferframe3_telemetry_acsgy0y_raw: masterframe.transferframe3.telemetry.acsgy0y.raw
    :field transferframe3_telemetry_acsgy0y_value: masterframe.transferframe3.telemetry.acsgy0y.value
    :field transferframe3_telemetry_acsgy0z_raw: masterframe.transferframe3.telemetry.acsgy0z.raw
    :field transferframe3_telemetry_acsgy0z_value: masterframe.transferframe3.telemetry.acsgy0z.value
    :field transferframe3_telemetry_reserve1_raw: masterframe.transferframe3.telemetry.reserve1.raw
    :field transferframe3_telemetry_reserve1_value: masterframe.transferframe3.telemetry.reserve1.value
    :field transferframe3_psant0: masterframe.transferframe3.telemetry.psant0
    :field transferframe3_psant1: masterframe.transferframe3.telemetry.psant1
    :field transferframe3_psgyr1: masterframe.transferframe3.telemetry.psgyr1
    :field transferframe3_pscom1: masterframe.transferframe3.telemetry.pscom1
    :field transferframe3_psuhf0: masterframe.transferframe3.telemetry.psuhf0
    :field transferframe3_psuhf1: masterframe.transferframe3.telemetry.psuhf1
    :field transferframe3_pstnc0: masterframe.transferframe3.telemetry.pstnc0
    :field transferframe3_pstnc1: masterframe.transferframe3.telemetry.pstnc1
    :field transferframe3_psgyr0: masterframe.transferframe3.telemetry.psgyr0
    :field transferframe3_psmcsx: masterframe.transferframe3.telemetry.psmcsx
    :field transferframe3_psmcsy: masterframe.transferframe3.telemetry.psmcsy
    :field transferframe3_psmcsz: masterframe.transferframe3.telemetry.psmcsz
    :field transferframe3_pswhls: masterframe.transferframe3.telemetry.pswhls
    :field transferframe3_psobc0: masterframe.transferframe3.telemetry.psobc0
    :field transferframe3_psobc1: masterframe.transferframe3.telemetry.psobc1
    :field transferframe3_pspdh0: masterframe.transferframe3.telemetry.pspdh0
    :field transferframe3_pscam0: masterframe.transferframe3.telemetry.pscam0
    :field transferframe3_pssuns: masterframe.transferframe3.telemetry.pssuns
    :field transferframe3_psmfs0: masterframe.transferframe3.telemetry.psmfs0
    :field transferframe3_psms1: masterframe.transferframe3.telemetry.psms1
    :field transferframe3_pstemp: masterframe.transferframe3.telemetry.pstemp
    :field transferframe3_pscan0: masterframe.transferframe3.telemetry.pscan0
    :field transferframe3_pscan1: masterframe.transferframe3.telemetry.pscan1
    :field transferframe3_psccw0: masterframe.transferframe3.telemetry.psccw0
    :field transferframe3_psccw1: masterframe.transferframe3.telemetry.psccw1
    :field transferframe3_ps5vcn: masterframe.transferframe3.telemetry.ps5vcn
    :field transferframe3_pcuaid: masterframe.transferframe3.telemetry.pcuaid
    :field transferframe3_pcbobc: masterframe.transferframe3.telemetry.pcbobc
    :field transferframe3_pcbext: masterframe.transferframe3.telemetry.pcbext
    :field transferframe3_pcch00: masterframe.transferframe3.telemetry.pcch00
    :field transferframe3_pcch01: masterframe.transferframe3.telemetry.pcch01
    :field transferframe3_pccho2: masterframe.transferframe3.telemetry.pccho2
    :field transferframe3_pcch03: masterframe.transferframe3.telemetry.pcch03
    :field transferframe3_pcch04: masterframe.transferframe3.telemetry.pcch04
    :field transferframe3_pcch05: masterframe.transferframe3.telemetry.pcch05
    :field transferframe3_pcch06: masterframe.transferframe3.telemetry.pcch06
    :field transferframe3_telemetry_rxsig0_raw: masterframe.transferframe3.telemetry.rxsig0.raw
    :field transferframe3_telemetry_rxsig0_value: masterframe.transferframe3.telemetry.rxsig0.value
    :field transferframe3_pcch07: masterframe.transferframe3.telemetry.pcch07
    :field transferframe3_pcch08: masterframe.transferframe3.telemetry.pcch08
    :field transferframe3_pcch09: masterframe.transferframe3.telemetry.pcch09
    :field transferframe3_pcch10: masterframe.transferframe3.telemetry.pcch10
    :field transferframe3_telemetry_rxsig1_raw: masterframe.transferframe3.telemetry.rxsig1.raw
    :field transferframe3_telemetry_rxsig1_value: masterframe.transferframe3.telemetry.rxsig1.value
    :field transferframe3_pcch11: masterframe.transferframe3.telemetry.pcch11
    :field transferframe3_pcch12: masterframe.transferframe3.telemetry.pcch12
    :field transferframe3_pcch13: masterframe.transferframe3.telemetry.pcch13
    :field transferframe3_pcch14: masterframe.transferframe3.telemetry.pcch14
    :field transferframe3_pcch15: masterframe.transferframe3.telemetry.pcch15
    :field transferframe3_pcch16: masterframe.transferframe3.telemetry.pcch16
    :field transferframe3_pcch17: masterframe.transferframe3.telemetry.pcch17
    :field transferframe3_pcch18: masterframe.transferframe3.telemetry.pcch18
    :field transferframe3_pcch19: masterframe.transferframe3.telemetry.pcch19
    :field transferframe3_pcch20: masterframe.transferframe3.telemetry.pcch20
    :field transferframe3_pcch21: masterframe.transferframe3.telemetry.pcch21
    :field transferframe3_pcch22: masterframe.transferframe3.telemetry.pcch22
    :field transferframe3_pcch23: masterframe.transferframe3.telemetry.pcch23
    :field transferframe3_pcch24: masterframe.transferframe3.telemetry.pcch24
    :field transferframe3_pcch25: masterframe.transferframe3.telemetry.pcch25
    :field transferframe3_pcch26: masterframe.transferframe3.telemetry.pcch26
    :field transferframe3_tcrxid: masterframe.transferframe3.telemetry.tcrxid
    :field transferframe3_obcaid: masterframe.transferframe3.telemetry.obcaid
    :field transferframe3_tmtxrt: masterframe.transferframe3.telemetry.tmtxrt
    :field transferframe3_pcch27: masterframe.transferframe3.telemetry.pcch27
    :field transferframe3_pcch28: masterframe.transferframe3.telemetry.pcch28
    :field transferframe3_pcch29: masterframe.transferframe3.telemetry.pcch29
    :field transferframe3_pcch30: masterframe.transferframe3.telemetry.pcch30
    :field transferframe3_pcch31: masterframe.transferframe3.telemetry.pcch31
    :field transferframe3_cctcic: masterframe.transferframe3.telemetry.cctcic
    :field transferframe3_cctctt: masterframe.transferframe3.telemetry.cctctt
    :field transferframe3_ccetcs: masterframe.transferframe3.telemetry.ccetcs
    :field transferframe3_cceimc: masterframe.transferframe3.telemetry.cceimc
    :field transferframe3_ccettc: masterframe.transferframe3.telemetry.ccettc
    :field transferframe3_ccettg: masterframe.transferframe3.telemetry.ccettg
    :field transferframe3_ccetcc: masterframe.transferframe3.telemetry.ccetcc
    :field transferframe3_telemetry_tcrxqu_raw: masterframe.transferframe3.telemetry.tcrxqu.raw
    :field transferframe3_telemetry_tcrxqu_value: masterframe.transferframe3.telemetry.tcrxqu.value
    :field transferframe3_telemetry_tcfrcp_raw: masterframe.transferframe3.telemetry.tcfrcp.raw
    :field transferframe3_telemetry_tcfrcp_value: masterframe.transferframe3.telemetry.tcfrcp.value
    :field transferframe3_telemetry_tmhkur_raw: masterframe.transferframe3.telemetry.tmhkur.raw
    :field transferframe3_telemetry_tmhkur_value: masterframe.transferframe3.telemetry.tmhkur.value
    :field transferframe3_telemetry_cstsys_raw: masterframe.transferframe3.telemetry.cstsys.raw
    :field transferframe3_telemetry_cstsys_value: masterframe.transferframe3.telemetry.cstsys.value
    :field transferframe3_mcxpol: masterframe.transferframe3.telemetry.mcxpol
    :field transferframe3_mcypol: masterframe.transferframe3.telemetry.mcypol
    :field transferframe3_mczpol: masterframe.transferframe3.telemetry.mczpol
    :field transferframe3_telemetry_obcbad_raw: masterframe.transferframe3.telemetry.obcbad.raw
    :field transferframe3_telemetry_obcbad_value: masterframe.transferframe3.telemetry.obcbad.value
    :field transferframe3_ceswmc: masterframe.transferframe3.telemetry.ceswmc
    :field transferframe3_beacon: masterframe.transferframe3.telemetry.beacon
    :field transferframe3_telemetry_reserve3_raw: masterframe.transferframe3.telemetry.reserve3.raw
    :field transferframe3_telemetry_reserve3_value: masterframe.transferframe3.telemetry.reserve3.value
    :field transferframe3_telemetry_modcom_raw: masterframe.transferframe3.telemetry.modcom.raw
    :field transferframe3_telemetry_modcom_value: masterframe.transferframe3.telemetry.modcom.value
    :field transferframe3_obcabc: masterframe.transferframe3.telemetry.obcabc
    :field transferframe3_modobc: masterframe.transferframe3.telemetry.modobc
    :field transferframe3_ccecan: masterframe.transferframe3.telemetry.ccecan
    :field transferframe3_obccan: masterframe.transferframe3.telemetry.obccan
    :field transferframe3_telemetry_pcsyst_raw: masterframe.transferframe3.telemetry.pcsyst.raw
    :field transferframe3_telemetry_pcsyst_value: masterframe.transferframe3.telemetry.pcsyst.value
    :field transferframe3_pcbcnt: masterframe.transferframe3.telemetry.pcbcnt
    :field transferframe3_pctxec: masterframe.transferframe3.telemetry.pctxec
    :field transferframe3_pcrxec: masterframe.transferframe3.telemetry.pcrxec
    :field transferframe3_pcoffc: masterframe.transferframe3.telemetry.pcoffc
    :field transferframe3_pcackc: masterframe.transferframe3.telemetry.pcackc
    :field transferframe3_pcch32: masterframe.transferframe3.telemetry.pcch32
    :field transferframe3_pcch33: masterframe.transferframe3.telemetry.pcch33
    :field transferframe3_pcch34: masterframe.transferframe3.telemetry.pcch34
    :field transferframe3_pcch35: masterframe.transferframe3.telemetry.pcch35
    :field transferframe3_pcch36: masterframe.transferframe3.telemetry.pcch36
    :field transferframe3_pcch37: masterframe.transferframe3.telemetry.pcch37
    :field transferframe3_pcch38: masterframe.transferframe3.telemetry.pcch38
    :field transferframe3_pcch39: masterframe.transferframe3.telemetry.pcch39
    :field transferframe3_pcch40: masterframe.transferframe3.telemetry.pcch40
    :field transferframe3_pcch41: masterframe.transferframe3.telemetry.pcch41
    :field transferframe3_telemetry_reserve4_raw: masterframe.transferframe3.telemetry.reserve4.raw
    :field transferframe3_telemetry_reserve4_value: masterframe.transferframe3.telemetry.reserve4.value
    :field transferframe3_telemetry_reserve5_raw: masterframe.transferframe3.telemetry.reserve5.raw
    :field transferframe3_telemetry_reserve5_value: masterframe.transferframe3.telemetry.reserve5.value
    :field transferframe3_telemetry_reserve6_raw: masterframe.transferframe3.telemetry.reserve6.raw
    :field transferframe3_telemetry_reserve6_value: masterframe.transferframe3.telemetry.reserve6.value
    :field transferframe3_telemetry_reserve7_raw: masterframe.transferframe3.telemetry.reserve7.raw
    :field transferframe3_telemetry_reserve7_value: masterframe.transferframe3.telemetry.reserve7.value
    :field transferframe3_telemetry_acswhx_raw: masterframe.transferframe3.telemetry.acswhx.raw
    :field transferframe3_telemetry_acswhx_value: masterframe.transferframe3.telemetry.acswhx.value
    :field transferframe3_telemetry_acswhy_raw: masterframe.transferframe3.telemetry.acswhy.raw
    :field transferframe3_telemetry_acswhy_value: masterframe.transferframe3.telemetry.acswhy.value
    :field transferframe3_telemetry_acswhz_raw: masterframe.transferframe3.telemetry.acswhz.raw
    :field transferframe3_telemetry_acswhz_value: masterframe.transferframe3.telemetry.acswhz.value
    :field transferframe3_telemetry_acsq00_raw: masterframe.transferframe3.telemetry.acsq00.raw
    :field transferframe3_telemetry_acsq00_value: masterframe.transferframe3.telemetry.acsq00.value
    :field transferframe3_telemetry_acsq01_raw: masterframe.transferframe3.telemetry.acsq01.raw
    :field transferframe3_telemetry_acsq01_value: masterframe.transferframe3.telemetry.acsq01.value
    :field transferframe3_telemetry_acsq02_raw: masterframe.transferframe3.telemetry.acsq02.raw
    :field transferframe3_telemetry_acsq02_value: masterframe.transferframe3.telemetry.acsq02.value
    :field transferframe3_telemetry_acsq03_raw: masterframe.transferframe3.telemetry.acsq03.raw
    :field transferframe3_telemetry_acsq03_value: masterframe.transferframe3.telemetry.acsq03.value
    :field transferframe3_telemetry_acssux_raw: masterframe.transferframe3.telemetry.acssux.raw
    :field transferframe3_telemetry_acssux_value: masterframe.transferframe3.telemetry.acssux.value
    :field transferframe3_telemetry_acssuy_raw: masterframe.transferframe3.telemetry.acssuy.raw
    :field transferframe3_telemetry_acssuy_value: masterframe.transferframe3.telemetry.acssuy.value
    :field transferframe3_telemetry_acssuz_raw: masterframe.transferframe3.telemetry.acssuz.raw
    :field transferframe3_telemetry_acssuz_value: masterframe.transferframe3.telemetry.acssuz.value
    :field transferframe3_telemetry_acsmox_raw: masterframe.transferframe3.telemetry.acsmox.raw
    :field transferframe3_telemetry_acsmox_value: masterframe.transferframe3.telemetry.acsmox.value
    :field transferframe3_telemetry_acsmoy_raw: masterframe.transferframe3.telemetry.acsmoy.raw
    :field transferframe3_telemetry_acsmoy_value: masterframe.transferframe3.telemetry.acsmoy.value
    :field transferframe3_telemetry_acsmoz_raw: masterframe.transferframe3.telemetry.acsmoz.raw
    :field transferframe3_telemetry_acsmoz_value: masterframe.transferframe3.telemetry.acsmoz.value
    :field transferframe3_telemetry_acsm1x_raw: masterframe.transferframe3.telemetry.acsm1x.raw
    :field transferframe3_telemetry_acsm1x_value: masterframe.transferframe3.telemetry.acsm1x.value
    :field transferframe3_telemetry_acsm1y_raw: masterframe.transferframe3.telemetry.acsm1y.raw
    :field transferframe3_telemetry_acsm1y_value: masterframe.transferframe3.telemetry.acsm1y.value
    :field transferframe3_telemetry_acsm1z_raw: masterframe.transferframe3.telemetry.acsm1z.raw
    :field transferframe3_telemetry_acsm1z_value: masterframe.transferframe3.telemetry.acsm1z.value
    :field transferframe3_telemetry_modacs_raw: masterframe.transferframe3.telemetry.modacs.raw
    :field transferframe3_telemetry_modacs_value: masterframe.transferframe3.telemetry.modacs.value
    :field transferframe3_acsgsc: masterframe.transferframe3.telemetry.acsgsc
    :field transferframe3_acsshd: masterframe.transferframe3.telemetry.acsshd
    :field transferframe3_telemetry_reserve8_raw: masterframe.transferframe3.telemetry.reserve8.raw
    :field transferframe3_telemetry_reserve8_value: masterframe.transferframe3.telemetry.reserve8.value
    :field transferframe3_acserr: masterframe.transferframe3.telemetry.acserr
    :field transferframe3_telemetry_acsg1y_raw: masterframe.transferframe3.telemetry.acsg1y.raw
    :field transferframe3_telemetry_acsg1y_value: masterframe.transferframe3.telemetry.acsg1y.value
    :field transferframe3_telemetry_acsg1z_raw: masterframe.transferframe3.telemetry.acsg1z.raw
    :field transferframe3_telemetry_acsg1z_value: masterframe.transferframe3.telemetry.acsg1z.value
    :field transferframe3_telemetry_acsg1x_raw: masterframe.transferframe3.telemetry.acsg1x.raw
    :field transferframe3_telemetry_acsg1x_value: masterframe.transferframe3.telemetry.acsg1x.value
    :field transferframe3_telemetry_reserve9_raw: masterframe.transferframe3.telemetry.reserve9.raw
    :field transferframe3_telemetry_reserve9_value: masterframe.transferframe3.telemetry.reserve9.value
    :field transferframe3_telemetry_reserve10_raw: masterframe.transferframe3.telemetry.reserve10.raw
    :field transferframe3_telemetry_reserve10_value: masterframe.transferframe3.telemetry.reserve10.value
    :field transferframe3_crc000: masterframe.transferframe3.telemetry.crc000
    :field transferframe3_crc001: masterframe.transferframe3.telemetry.crc001
    :field transferframe3_crc002: masterframe.transferframe3.telemetry.crc002
    :field transferframe3_crc003: masterframe.transferframe3.telemetry.crc003
    :field transferframe3_crc004: masterframe.transferframe3.telemetry.crc004
    :field transferframe3_crc005: masterframe.transferframe3.telemetry.crc005
    :field transferframe3_crc006: masterframe.transferframe3.telemetry.crc006
    :field transferframe3_crc007: masterframe.transferframe3.telemetry.crc007
    :field transferframe3_crc008: masterframe.transferframe3.telemetry.crc008
    :field transferframe3_crc009: masterframe.transferframe3.telemetry.crc009
    :field transferframe3_crc010: masterframe.transferframe3.telemetry.crc010
    :field transferframe3_crc011: masterframe.transferframe3.telemetry.crc011
    :field transferframe3_crc012: masterframe.transferframe3.telemetry.crc012
    :field transferframe3_crc013: masterframe.transferframe3.telemetry.crc013
    :field transferframe3_crc014: masterframe.transferframe3.telemetry.crc014
    :field transferframe3_crc015: masterframe.transferframe3.telemetry.crc015
    :field transferframe3_crc016: masterframe.transferframe3.telemetry.crc016
    :field transferframe3_crc017: masterframe.transferframe3.telemetry.crc017
    :field transferframe3_crc018: masterframe.transferframe3.telemetry.crc018
    :field transferframe3_crc019: masterframe.transferframe3.telemetry.crc019
    :field transferframe3_crc020: masterframe.transferframe3.telemetry.crc020
    :field transferframe3_crc021: masterframe.transferframe3.telemetry.crc021
    :field transferframe3_crc022: masterframe.transferframe3.telemetry.crc022
    :field transferframe3_crc023: masterframe.transferframe3.telemetry.crc023
    :field transferframe3_crc024: masterframe.transferframe3.telemetry.crc024
    :field transferframe3_crc025: masterframe.transferframe3.telemetry.crc025
    :field transferframe3_crc026: masterframe.transferframe3.telemetry.crc026
    :field transferframe3_crc027: masterframe.transferframe3.telemetry.crc027
    :field transferframe3_crc028: masterframe.transferframe3.telemetry.crc028
    :field transferframe3_crc029: masterframe.transferframe3.telemetry.crc029
    :field transferframe3_crc030: masterframe.transferframe3.telemetry.crc030
    :field transferframe3_dummy: masterframe.transferframe3.telemetry.dummy
    :field transferframe3_imhd00: masterframe.transferframe3.telemetry.imhd00
    :field transferframe3_imhd01: masterframe.transferframe3.telemetry.imhd01
    :field transferframe3_imhd02: masterframe.transferframe3.telemetry.imhd02
    :field transferframe3_imhd03: masterframe.transferframe3.telemetry.imhd03
    :field transferframe3_imhd04: masterframe.transferframe3.telemetry.imhd04
    :field transferframe3_imhd10: masterframe.transferframe3.telemetry.imhd10
    :field transferframe3_imhd11: masterframe.transferframe3.telemetry.imhd11
    :field transferframe3_imhd12: masterframe.transferframe3.telemetry.imhd12
    :field transferframe3_imhd13: masterframe.transferframe3.telemetry.imhd13
    :field transferframe3_imhd14: masterframe.transferframe3.telemetry.imhd14
    :field transferframe3_imhd20: masterframe.transferframe3.telemetry.imhd20
    :field transferframe3_imhd21: masterframe.transferframe3.telemetry.imhd21
    :field transferframe3_imhd22: masterframe.transferframe3.telemetry.imhd22
    :field transferframe3_imhd23: masterframe.transferframe3.telemetry.imhd23
    :field transferframe3_imhd24: masterframe.transferframe3.telemetry.imhd24
    :field transferframe3_imhd30: masterframe.transferframe3.telemetry.imhd30
    :field transferframe3_imhd31: masterframe.transferframe3.telemetry.imhd31
    :field transferframe3_imhd32: masterframe.transferframe3.telemetry.imhd32
    :field transferframe3_imhd33: masterframe.transferframe3.telemetry.imhd33
    :field transferframe3_imhd34: masterframe.transferframe3.telemetry.imhd34
    :field transferframe3_reserver20: masterframe.transferframe3.telemetry.reserver20
    :field transferframe3_image_id: masterframe.transferframe3.telemetry.image_id
    :field transferframe3_pdh_image: masterframe.transferframe3.telemetry.pdh_image
    :field transferframe3_telemetry_cpdhmcu_raw: masterframe.transferframe3.telemetry.cpdhmcu.raw
    :field transferframe3_telemetry_cpdhmcu_value: masterframe.transferframe3.telemetry.cpdhmcu.value
    :field transferframe3_telemetry_cpdhcam_raw: masterframe.transferframe3.telemetry.cpdhcam.raw
    :field transferframe3_telemetry_cpdhcam_value: masterframe.transferframe3.telemetry.cpdhcam.value
    :field transferframe3_tpdhcam: masterframe.transferframe3.telemetry.tpdhcam
    :field transferframe3_pdhceccm: masterframe.transferframe3.telemetry.pdhceccm
    :field transferframe3_pdhcectc: masterframe.transferframe3.telemetry.pdhcectc
    :field transferframe3_pdhcetlii: masterframe.transferframe3.telemetry.pdhcetlii
    :field transferframe3_pdhcetlc: masterframe.transferframe3.telemetry.pdhcetlc
    :field transferframe3_pdhti: masterframe.transferframe3.telemetry.pdhti
    :field transferframe3_pdhth: masterframe.transferframe3.telemetry.pdhth
    :field transferframe3_pdhceisi: masterframe.transferframe3.telemetry.pdhceisi
    :field transferframe3_pdhceici: masterframe.transferframe3.telemetry.pdhceici
    :field transferframe3_pdhceids: masterframe.transferframe3.telemetry.pdhceids
    :field transferframe3_pdhmode: masterframe.transferframe3.telemetry.pdhmode
    :field transferframe3_pdhcii: masterframe.transferframe3.telemetry.pdhcii
    :field transferframe3_pdhcih: masterframe.transferframe3.telemetry.pdhcih
    :field transferframe3_pdhcescm: masterframe.transferframe3.telemetry.pdhcescm
    :field transferframe3_pdhcessm: masterframe.transferframe3.telemetry.pdhcessm
    :field transferframe3_pdhcescb: masterframe.transferframe3.telemetry.pdhcescb
    :field transferframe3_pdhceslb: masterframe.transferframe3.telemetry.pdhceslb
    :field transferframe3_pdhcesss: masterframe.transferframe3.telemetry.pdhcesss
    :field transferframe3_pdhcessb: masterframe.transferframe3.telemetry.pdhcessb
    :field transferframe3_pdhceseb: masterframe.transferframe3.telemetry.pdhceseb
    :field transferframe3_pdhcesci: masterframe.transferframe3.telemetry.pdhcesci
    :field transferframe3_pdhcsi: masterframe.transferframe3.telemetry.pdhcsi
    :field transferframe3_pdhcsh: masterframe.transferframe3.telemetry.pdhcsh
    :field transferframe3_pdhbtimg: masterframe.transferframe3.telemetry.pdhbtimg
    :field transferframe3_pdhswversion: masterframe.transferframe3.telemetry.pdhswversion
    :field transferframe3_pdhcstsys: masterframe.transferframe3.telemetry.pdhcstsys
    :field transferframe3_pdhctstutc: masterframe.transferframe3.telemetry.pdhctstutc
    :field transferframe3_pdh_reserve: masterframe.transferframe3.telemetry.pdh_reserve
    :field transferframe3_pdhcrc000: masterframe.transferframe3.telemetry.pdhcrc000
    :field transferframe3_pdhcrc001: masterframe.transferframe3.telemetry.pdhcrc001
    :field transferframe3_pdhcrc002: masterframe.transferframe3.telemetry.pdhcrc002
    :field transferframe3_pdhcrc003: masterframe.transferframe3.telemetry.pdhcrc003
    :field transferframe3_pdhcrc004: masterframe.transferframe3.telemetry.pdhcrc004
    :field transferframe3_pdhcrc005: masterframe.transferframe3.telemetry.pdhcrc005
    :field transferframe3_pdhcrc006: masterframe.transferframe3.telemetry.pdhcrc006
    :field transferframe3_pdhcrc007: masterframe.transferframe3.telemetry.pdhcrc007
    :field transferframe3_pdhcrc008: masterframe.transferframe3.telemetry.pdhcrc008
    :field transferframe3_pdhcrc009: masterframe.transferframe3.telemetry.pdhcrc009
    :field transferframe3_pdhcrc010: masterframe.transferframe3.telemetry.pdhcrc010
    :field transferframe3_pdhcrc011: masterframe.transferframe3.telemetry.pdhcrc011
    :field transferframe3_pdhcrc012: masterframe.transferframe3.telemetry.pdhcrc012
    :field transferframe3_pdhcrc013: masterframe.transferframe3.telemetry.pdhcrc013
    :field transferframe3_pdhcrc014: masterframe.transferframe3.telemetry.pdhcrc014
    :field transferframe3_pdhcrc015: masterframe.transferframe3.telemetry.pdhcrc015
    :field transferframe3_pdhcrc016: masterframe.transferframe3.telemetry.pdhcrc016
    :field transferframe3_pdhcrc017: masterframe.transferframe3.telemetry.pdhcrc017
    :field transferframe3_pdhcrc018: masterframe.transferframe3.telemetry.pdhcrc018
    :field transferframe3_pdhcrc019: masterframe.transferframe3.telemetry.pdhcrc019
    :field transferframe3_pdhcrc020: masterframe.transferframe3.telemetry.pdhcrc020
    :field transferframe3_pdhcrc021: masterframe.transferframe3.telemetry.pdhcrc021
    :field transferframe3_pdhcrc022: masterframe.transferframe3.telemetry.pdhcrc022
    :field transferframe3_pdhcrc023: masterframe.transferframe3.telemetry.pdhcrc023
    :field transferframe3_pdhcrc024: masterframe.transferframe3.telemetry.pdhcrc024
    :field transferframe3_pdhcrc025: masterframe.transferframe3.telemetry.pdhcrc025
    :field transferframe3_pdhcrc026: masterframe.transferframe3.telemetry.pdhcrc026
    :field transferframe3_pdhcrc027: masterframe.transferframe3.telemetry.pdhcrc027
    :field transferframe3_pdhcrc028: masterframe.transferframe3.telemetry.pdhcrc028
    :field transferframe3_pdhcrc029: masterframe.transferframe3.telemetry.pdhcrc029
    :field transferframe3_pdhcrc030: masterframe.transferframe3.telemetry.pdhcrc030
    :field transferframe3_pdhcrccmask00: masterframe.transferframe3.telemetry.pdhcrccmask00
    :field transferframe3_acswhx: masterframe.transferframe3.telemetry.acswhx
    :field transferframe3_telemetry_acsm0x_raw: masterframe.transferframe3.telemetry.acsm0x.raw
    :field transferframe3_telemetry_acsm0x_value: masterframe.transferframe3.telemetry.acsm0x.value
    :field transferframe3_telemetry_acsm0y_raw: masterframe.transferframe3.telemetry.acsm0y.raw
    :field transferframe3_telemetry_acsm0y_value: masterframe.transferframe3.telemetry.acsm0y.value
    :field transferframe3_telemetry_acsm0z_raw: masterframe.transferframe3.telemetry.acsm0z.raw
    :field transferframe3_telemetry_acsm0z_value: masterframe.transferframe3.telemetry.acsm0z.value
    :field transferframe3_reserveacsgr: masterframe.transferframe3.telemetry.reserveacsgr
    :field transferframe3_acstemex: masterframe.transferframe3.telemetry.acstemex
    :field transferframe3_acstemey: masterframe.transferframe3.telemetry.acstemey
    :field transferframe3_acstemez: masterframe.transferframe3.telemetry.acstemez
    :field transferframe3_telemetry_acstemevelx_raw: masterframe.transferframe3.telemetry.acstemevelx.raw
    :field transferframe3_telemetry_acstemevelx_value: masterframe.transferframe3.telemetry.acstemevelx.value
    :field transferframe3_telemetry_acstemevely_raw: masterframe.transferframe3.telemetry.acstemevely.raw
    :field transferframe3_telemetry_acstemevely_value: masterframe.transferframe3.telemetry.acstemevely.value
    :field transferframe3_telemetry_acstemevelz_raw: masterframe.transferframe3.telemetry.acstemevelz.raw
    :field transferframe3_telemetry_acstemevelz_value: masterframe.transferframe3.telemetry.acstemevelz.value
    :field transferframe3_acsefx: masterframe.transferframe3.telemetry.acsefx
    :field transferframe3_acsefy: masterframe.transferframe3.telemetry.acsefy
    :field transferframe3_acsefz: masterframe.transferframe3.telemetry.acsefz
    :field transferframe3_telemetry_acsmagifx_raw: masterframe.transferframe3.telemetry.acsmagifx.raw
    :field transferframe3_telemetry_acsmagifx_value: masterframe.transferframe3.telemetry.acsmagifx.value
    :field transferframe3_telemetry_acsmagify_raw: masterframe.transferframe3.telemetry.acsmagify.raw
    :field transferframe3_telemetry_acsmagify_value: masterframe.transferframe3.telemetry.acsmagify.value
    :field transferframe3_telemetry_acsmagifz_raw: masterframe.transferframe3.telemetry.acsmagifz.raw
    :field transferframe3_telemetry_acsmagifz_value: masterframe.transferframe3.telemetry.acsmagifz.value
    :field transferframe3_telemetry_acssunifx_raw: masterframe.transferframe3.telemetry.acssunifx.raw
    :field transferframe3_telemetry_acssunifx_value: masterframe.transferframe3.telemetry.acssunifx.value
    :field transferframe3_telemetry_acssunify_raw: masterframe.transferframe3.telemetry.acssunify.raw
    :field transferframe3_telemetry_acssunify_value: masterframe.transferframe3.telemetry.acssunify.value
    :field transferframe3_telemetry_acssunifz_raw: masterframe.transferframe3.telemetry.acssunifz.raw
    :field transferframe3_telemetry_acssunifz_value: masterframe.transferframe3.telemetry.acssunifz.value
    :field transferframe3_telemetry_acsqdes00_raw: masterframe.transferframe3.telemetry.acsqdes00.raw
    :field transferframe3_telemetry_acsqdes00_value: masterframe.transferframe3.telemetry.acsqdes00.value
    :field transferframe3_telemetry_acsqdes01_raw: masterframe.transferframe3.telemetry.acsqdes01.raw
    :field transferframe3_telemetry_acsqdes01_value: masterframe.transferframe3.telemetry.acsqdes01.value
    :field transferframe3_telemetry_acsqdes02_raw: masterframe.transferframe3.telemetry.acsqdes02.raw
    :field transferframe3_telemetry_acsqdes02_value: masterframe.transferframe3.telemetry.acsqdes02.value
    :field transferframe3_telemetry_acsqdes03_raw: masterframe.transferframe3.telemetry.acsqdes03.raw
    :field transferframe3_telemetry_acsqdes03_value: masterframe.transferframe3.telemetry.acsqdes03.value
    :field transferframe3_telemetry_acswcx_raw: masterframe.transferframe3.telemetry.acswcx.raw
    :field transferframe3_telemetry_acswcx_value: masterframe.transferframe3.telemetry.acswcx.value
    :field transferframe3_telemetry_acswcy_raw: masterframe.transferframe3.telemetry.acswcy.raw
    :field transferframe3_telemetry_acswcy_value: masterframe.transferframe3.telemetry.acswcy.value
    :field transferframe3_telemetry_acswcz_raw: masterframe.transferframe3.telemetry.acswcz.raw
    :field transferframe3_telemetry_acswcz_value: masterframe.transferframe3.telemetry.acswcz.value
    :field transferframe3_telemetry_acswu0_raw: masterframe.transferframe3.telemetry.acswu0.raw
    :field transferframe3_telemetry_acswu0_value: masterframe.transferframe3.telemetry.acswu0.value
    :field transferframe3_telemetry_acswu1_raw: masterframe.transferframe3.telemetry.acswu1.raw
    :field transferframe3_telemetry_acswu1_value: masterframe.transferframe3.telemetry.acswu1.value
    :field transferframe3_telemetry_acswu2_raw: masterframe.transferframe3.telemetry.acswu2.raw
    :field transferframe3_telemetry_acswu2_value: masterframe.transferframe3.telemetry.acswu2.value
    :field transferframe3_telemetry_acswq0_raw: masterframe.transferframe3.telemetry.acswq0.raw
    :field transferframe3_telemetry_acswq0_value: masterframe.transferframe3.telemetry.acswq0.value
    :field transferframe3_telemetry_acswq1_raw: masterframe.transferframe3.telemetry.acswq1.raw
    :field transferframe3_telemetry_acswq1_value: masterframe.transferframe3.telemetry.acswq1.value
    :field transferframe3_telemetry_acswq2_raw: masterframe.transferframe3.telemetry.acswq2.raw
    :field transferframe3_telemetry_acswq2_value: masterframe.transferframe3.telemetry.acswq2.value
    :field transferframe3_telemetry_acswq3_raw: masterframe.transferframe3.telemetry.acswq3.raw
    :field transferframe3_telemetry_acswq3_value: masterframe.transferframe3.telemetry.acswq3.value
    :field transferframe3_acswa0: masterframe.transferframe3.telemetry.acswa0
    :field transferframe3_acswa1: masterframe.transferframe3.telemetry.acswa1
    :field transferframe3_acswa2: masterframe.transferframe3.telemetry.acswa2
    :field transferframe3_acs_tm_vecs_res: masterframe.transferframe3.telemetry.acs_tm_vecs_res
    :field transferframe3_psmfs1: masterframe.transferframe3.telemetry.psmfs1
    :field transferframe3_pcch02: masterframe.transferframe3.telemetry.pcch02
    :field transferframe3_tcfrcp: masterframe.transferframe3.telemetry.tcfrcp
    :field transferframe3_tmhkur: masterframe.transferframe3.telemetry.tmhkur
    :field transferframe3_cstutc: masterframe.transferframe3.telemetry.cstutc
    :field transferframe3_cstsys: masterframe.transferframe3.telemetry.cstsys
    :field transferframe3_pcsyst: masterframe.transferframe3.telemetry.pcsyst
    :field transferframe3_acswhy: masterframe.transferframe3.telemetry.acswhy
    :field transferframe3_acswhz: masterframe.transferframe3.telemetry.acswhz
    :field transferframe3_telemetry_acg1ym_raw: masterframe.transferframe3.telemetry.acg1ym.raw
    :field transferframe3_telemetry_acg1ym_value: masterframe.transferframe3.telemetry.acg1ym.value
    :field transferframe3_telemetry_acg1zm_raw: masterframe.transferframe3.telemetry.acg1zm.raw
    :field transferframe3_telemetry_acg1zm_value: masterframe.transferframe3.telemetry.acg1zm.value
    :field transferframe3_telemetry_acg1xm_raw: masterframe.transferframe3.telemetry.acg1xm.raw
    :field transferframe3_telemetry_acg1xm_value: masterframe.transferframe3.telemetry.acg1xm.value
    :field transferframe3_obctmffp: masterframe.transferframe3.telemetry.obctmffp
    :field transferframe3_obcswversion: masterframe.transferframe3.telemetry.obcswversion
    :field transferframe3_telemetry_acscmod_raw: masterframe.transferframe3.telemetry.acscmod.raw
    :field transferframe3_telemetry_acscmod_value: masterframe.transferframe3.telemetry.acscmod.value
    :field transferframe3_cctccp: masterframe.transferframe3.telemetry.cctccp
    :field transferframe3_telemetry_b2_tm_reserve_raw: masterframe.transferframe3.telemetry.b2_tm_reserve.raw
    :field transferframe3_telemetry_b2_tm_reserve_value: masterframe.transferframe3.telemetry.b2_tm_reserve.value
    :field transferframe3_tledoy: masterframe.transferframe3.telemetry.tledoy
    :field transferframe3_telemetry_tlemem_raw: masterframe.transferframe3.telemetry.tlemem.raw
    :field transferframe3_telemetry_tlemem_value: masterframe.transferframe3.telemetry.tlemem.value
    :field transferframe3_tleecc: masterframe.transferframe3.telemetry.tleecc
    :field transferframe3_telemetry_tleinc_raw: masterframe.transferframe3.telemetry.tleinc.raw
    :field transferframe3_telemetry_tleinc_value: masterframe.transferframe3.telemetry.tleinc.value
    :field transferframe3_telemetry_tleaop_raw: masterframe.transferframe3.telemetry.tleaop.raw
    :field transferframe3_telemetry_tleaop_value: masterframe.transferframe3.telemetry.tleaop.value
    :field transferframe3_telemetry_tleraa_raw: masterframe.transferframe3.telemetry.tleraa.raw
    :field transferframe3_telemetry_tleraa_value: masterframe.transferframe3.telemetry.tleraa.value
    :field transferframe3_telemetry_tleman_raw: masterframe.transferframe3.telemetry.tleman.raw
    :field transferframe3_telemetry_tleman_value: masterframe.transferframe3.telemetry.tleman.value
    :field transferframe3_tledrt: masterframe.transferframe3.telemetry.tledrt
    :field transferframe3_tlexpc: masterframe.transferframe3.telemetry.tlexpc
    :field transferframe3_tleypc: masterframe.transferframe3.telemetry.tleypc
    :field transferframe3_tlettd: masterframe.transferframe3.telemetry.tlettd
    :field transferframe3_tleutd: masterframe.transferframe3.telemetry.tleutd
    :field transferframe3_tledep: masterframe.transferframe3.telemetry.tledep
    :field transferframe3_tledps: masterframe.transferframe3.telemetry.tledps
    :field transferframe3_tleyea: masterframe.transferframe3.telemetry.tleyea
    :field transferframe3_tle_placeholder: masterframe.transferframe3.telemetry.tle_placeholder
    :field transferframe3_fecfd: masterframe.transferframe3.fecfd
    :field rxqual: masterframe.rxqual
    :field errmar: masterframe.errmar
    :field tmptnc: masterframe.tmptnc
    """
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.masterframe = Beesat2.Masterframe(self._io, self, self._root)

    class Uvmfs012(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.raw = self._io.read_bits_int_be(12)

        @property
        def value(self):
            if hasattr(self, '_m_value'):
                return self._m_value

            self._m_value = (self.raw * 0.000886615953947)
            return getattr(self, '_m_value', None)


    class F8Dec8(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.raw = self._io.read_f8be()

        @property
        def value(self):
            if hasattr(self, '_m_value'):
                return self._m_value

            self._m_value = (self.raw * 229.183118052)
            return getattr(self, '_m_value', None)


    class Telemetrypacket2(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.cstutc = Beesat2.Binary32(self._io, self, self._root)
            self.csaxp = Beesat2.Ucmcs12(self._io, self, self._root)
            self.csaxn = Beesat2.Ucmcs12(self._io, self, self._root)
            self.csayp = Beesat2.Ucmcs12(self._io, self, self._root)
            self.csayn = Beesat2.Ucmcs12(self._io, self, self._root)
            self.csazp = Beesat2.Ucmcs12(self._io, self, self._root)
            self.csazn = Beesat2.Ucmcs12(self._io, self, self._root)
            self.vsabus = Beesat2.Uv50bus12(self._io, self, self._root)
            self.cc0in = Beesat2.Ucwhl12(self._io, self, self._root)
            self.cc1in = Beesat2.Ucwhl12(self._io, self, self._root)
            self.vbat0 = Beesat2.Uvbat12(self._io, self, self._root)
            self.vbat1 = Beesat2.Uvbat12(self._io, self, self._root)
            self.cc0out = Beesat2.Uccout12(self._io, self, self._root)
            self.cc1out = Beesat2.Uccout12(self._io, self, self._root)
            self.tsaxp = Beesat2.Utsa10(self._io, self, self._root)
            self.tsaxn = Beesat2.Utsa10(self._io, self, self._root)
            self.tsayp = Beesat2.Utsa10(self._io, self, self._root)
            self.tsayn = Beesat2.Utsa10(self._io, self, self._root)
            self.tsazp = Beesat2.Utsa10(self._io, self, self._root)
            self.tsazn = Beesat2.Utsa10(self._io, self, self._root)
            self.tbat0 = Beesat2.Utbat12(self._io, self, self._root)
            self.tbat1 = Beesat2.Utbat12(self._io, self, self._root)
            self.tpcu00 = Beesat2.Utpcu12(self._io, self, self._root)
            self.tpcu01 = Beesat2.Utpcu12(self._io, self, self._root)
            self.tmfs0 = Beesat2.Utmfs012(self._io, self, self._root)
            self.tmfs1 = Beesat2.Utmfs012(self._io, self, self._root)
            self.twhlx = Beesat2.Utmfs012(self._io, self, self._root)
            self.twhly = Beesat2.Utmfs012(self._io, self, self._root)
            self.twhlz = Beesat2.Utmfs012(self._io, self, self._root)
            self.tgyrox = Beesat2.Utmfs012(self._io, self, self._root)
            self.tgyroy = Beesat2.Utmfs012(self._io, self, self._root)
            self.tgyroz = Beesat2.Utmfs012(self._io, self, self._root)
            self.tobc00 = Beesat2.Utpcu12(self._io, self, self._root)
            self.tobc01 = Beesat2.Utpcu12(self._io, self, self._root)
            self.tobc02 = Beesat2.Utpcu12(self._io, self, self._root)
            self.ttrx0 = Beesat2.Ucttrx12(self._io, self, self._root)
            self.ttrx1 = Beesat2.Ucttrx12(self._io, self, self._root)
            self.reserve = (KaitaiStream.bytes_terminate(self._io.read_bytes(70), 0, False)).decode(u"latin1")


    class Utsa10(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.raw = self._io.read_bits_int_be(10)

        @property
        def value(self):
            if hasattr(self, '_m_value'):
                return self._m_value

            self._m_value = ((self.raw * 0.244140625) - 50.0)
            return getattr(self, '_m_value', None)


    class Binary32(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.raw = self._io.read_bits_int_be(32)

        @property
        def value(self):
            if hasattr(self, '_m_value'):
                return self._m_value

            self._m_value = self.raw
            return getattr(self, '_m_value', None)


    class Telemetrypacket1429(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.image_id = self._io.read_u1()
            self.pdh_image = (KaitaiStream.bytes_terminate(self._io.read_bytes(125), 0, False)).decode(u"latin1")


    class Utpcu12(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.raw = self._io.read_bits_int_be(12)

        @property
        def value(self):
            if hasattr(self, '_m_value'):
                return self._m_value

            self._m_value = (self.raw * 0.125)
            return getattr(self, '_m_value', None)


    class Utcrxqu8(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.raw = self._io.read_bits_int_be(8)

        @property
        def value(self):
            if hasattr(self, '_m_value'):
                return self._m_value

            self._m_value = ((self.raw * 0.0548780487) + 1.573172)
            return getattr(self, '_m_value', None)


    class S2P10(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.raw = self._io.read_s2be()

        @property
        def value(self):
            if hasattr(self, '_m_value'):
                return self._m_value

            self._m_value = (self.raw * 10)
            return getattr(self, '_m_value', None)


    class S2Dec3(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.raw = self._io.read_s2be()

        @property
        def value(self):
            if hasattr(self, '_m_value'):
                return self._m_value

            self._m_value = (self.raw * 0.001)
            return getattr(self, '_m_value', None)


    class Ucttrx12(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.raw = self._io.read_bits_int_be(10)

        @property
        def value(self):
            if hasattr(self, '_m_value'):
                return self._m_value

            self._m_value = ((self.raw * 0.9765625) - 50)
            return getattr(self, '_m_value', None)


    class Telemetrypacket612(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.crc000 = (KaitaiStream.bytes_terminate(self._io.read_bytes(4), 0, False)).decode(u"ascii")
            self.crc001 = (KaitaiStream.bytes_terminate(self._io.read_bytes(4), 0, False)).decode(u"ascii")
            self.crc002 = (KaitaiStream.bytes_terminate(self._io.read_bytes(4), 0, False)).decode(u"ascii")
            self.crc003 = (KaitaiStream.bytes_terminate(self._io.read_bytes(4), 0, False)).decode(u"ascii")
            self.crc004 = (KaitaiStream.bytes_terminate(self._io.read_bytes(4), 0, False)).decode(u"ascii")
            self.crc005 = (KaitaiStream.bytes_terminate(self._io.read_bytes(4), 0, False)).decode(u"ascii")
            self.crc006 = (KaitaiStream.bytes_terminate(self._io.read_bytes(4), 0, False)).decode(u"ascii")
            self.crc007 = (KaitaiStream.bytes_terminate(self._io.read_bytes(4), 0, False)).decode(u"ascii")
            self.crc008 = (KaitaiStream.bytes_terminate(self._io.read_bytes(4), 0, False)).decode(u"ascii")
            self.crc009 = (KaitaiStream.bytes_terminate(self._io.read_bytes(4), 0, False)).decode(u"ascii")
            self.crc010 = (KaitaiStream.bytes_terminate(self._io.read_bytes(4), 0, False)).decode(u"ascii")
            self.crc011 = (KaitaiStream.bytes_terminate(self._io.read_bytes(4), 0, False)).decode(u"ascii")
            self.crc012 = (KaitaiStream.bytes_terminate(self._io.read_bytes(4), 0, False)).decode(u"ascii")
            self.crc013 = (KaitaiStream.bytes_terminate(self._io.read_bytes(4), 0, False)).decode(u"ascii")
            self.crc014 = (KaitaiStream.bytes_terminate(self._io.read_bytes(4), 0, False)).decode(u"ascii")
            self.crc015 = (KaitaiStream.bytes_terminate(self._io.read_bytes(4), 0, False)).decode(u"ascii")
            self.crc016 = (KaitaiStream.bytes_terminate(self._io.read_bytes(4), 0, False)).decode(u"ascii")
            self.crc017 = (KaitaiStream.bytes_terminate(self._io.read_bytes(4), 0, False)).decode(u"ascii")
            self.crc018 = (KaitaiStream.bytes_terminate(self._io.read_bytes(4), 0, False)).decode(u"ascii")
            self.crc019 = (KaitaiStream.bytes_terminate(self._io.read_bytes(4), 0, False)).decode(u"ascii")
            self.crc020 = (KaitaiStream.bytes_terminate(self._io.read_bytes(4), 0, False)).decode(u"ascii")
            self.crc021 = (KaitaiStream.bytes_terminate(self._io.read_bytes(4), 0, False)).decode(u"ascii")
            self.crc022 = (KaitaiStream.bytes_terminate(self._io.read_bytes(4), 0, False)).decode(u"ascii")
            self.crc023 = (KaitaiStream.bytes_terminate(self._io.read_bytes(4), 0, False)).decode(u"ascii")
            self.crc024 = (KaitaiStream.bytes_terminate(self._io.read_bytes(4), 0, False)).decode(u"ascii")
            self.crc025 = (KaitaiStream.bytes_terminate(self._io.read_bytes(4), 0, False)).decode(u"ascii")
            self.crc026 = (KaitaiStream.bytes_terminate(self._io.read_bytes(4), 0, False)).decode(u"ascii")
            self.crc027 = (KaitaiStream.bytes_terminate(self._io.read_bytes(4), 0, False)).decode(u"ascii")
            self.crc028 = (KaitaiStream.bytes_terminate(self._io.read_bytes(4), 0, False)).decode(u"ascii")
            self.crc029 = (KaitaiStream.bytes_terminate(self._io.read_bytes(4), 0, False)).decode(u"ascii")
            self.crc030 = (KaitaiStream.bytes_terminate(self._io.read_bytes(4), 0, False)).decode(u"ascii")
            self.dummy = self._io.read_u2be()


    class F8Dec4(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.raw = self._io.read_f8be()

        @property
        def value(self):
            if hasattr(self, '_m_value'):
                return self._m_value

            self._m_value = (self.raw * 57.2957795130823)
            return getattr(self, '_m_value', None)


    class Telemetrypacket40(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.cstutc = Beesat2.Binary32(self._io, self, self._root)
            self.acswhx = self._io.read_s2be()
            self.acswhy = Beesat2.S2Dec4(self._io, self, self._root)
            self.acswhz = Beesat2.S2Dec4(self._io, self, self._root)
            self.acsq00 = Beesat2.S2Dec4(self._io, self, self._root)
            self.acsq01 = Beesat2.S2Dec4(self._io, self, self._root)
            self.acsq02 = Beesat2.S2Dec4(self._io, self, self._root)
            self.acsq03 = Beesat2.S2Dec4(self._io, self, self._root)
            self.acssux = Beesat2.S2Dec4(self._io, self, self._root)
            self.acssuy = Beesat2.S2Dec4(self._io, self, self._root)
            self.acssuz = Beesat2.S2Dec4(self._io, self, self._root)
            self.acsm0x = Beesat2.S2P10(self._io, self, self._root)
            self.acsm0y = Beesat2.S2P10(self._io, self, self._root)
            self.acsm0z = Beesat2.S2P10(self._io, self, self._root)
            self.acsm1x = Beesat2.S2P10(self._io, self, self._root)
            self.acsm1y = Beesat2.S2P10(self._io, self, self._root)
            self.acsm1z = Beesat2.S2P10(self._io, self, self._root)
            self.reserveacsgr = self._io.read_bits_int_be(48)
            self._io.align_to_byte()
            self.acstemex = self._io.read_s2be()
            self.acstemey = self._io.read_s2be()
            self.acstemez = self._io.read_s2be()
            self.acstemevelx = Beesat2.S2Dec3(self._io, self, self._root)
            self.acstemevely = Beesat2.S2Dec3(self._io, self, self._root)
            self.acstemevelz = Beesat2.S2Dec3(self._io, self, self._root)
            self.acsefx = self._io.read_s2be()
            self.acsefy = self._io.read_s2be()
            self.acsefz = self._io.read_s2be()
            self.acsmagifx = Beesat2.S2P10(self._io, self, self._root)
            self.acsmagify = Beesat2.S2P10(self._io, self, self._root)
            self.acsmagifz = Beesat2.S2P10(self._io, self, self._root)
            self.acssunifx = Beesat2.S2Dec4(self._io, self, self._root)
            self.acssunify = Beesat2.S2Dec4(self._io, self, self._root)
            self.acssunifz = Beesat2.S2Dec4(self._io, self, self._root)
            self.acsqdes00 = Beesat2.S2Dec4(self._io, self, self._root)
            self.acsqdes01 = Beesat2.S2Dec4(self._io, self, self._root)
            self.acsqdes02 = Beesat2.S2Dec4(self._io, self, self._root)
            self.acsqdes03 = Beesat2.S2Dec4(self._io, self, self._root)
            self.acswcx = Beesat2.S2N0d5(self._io, self, self._root)
            self.acswcy = Beesat2.S2N0d5(self._io, self, self._root)
            self.acswcz = Beesat2.S2P0d5(self._io, self, self._root)
            self.acswu0 = Beesat2.S2Dec7(self._io, self, self._root)
            self.acswu1 = Beesat2.S2Dec7(self._io, self, self._root)
            self.acswu2 = Beesat2.S2Dec7(self._io, self, self._root)
            self.acswq0 = Beesat2.S2Dec4(self._io, self, self._root)
            self.acswq1 = Beesat2.S2Dec4(self._io, self, self._root)
            self.acswq2 = Beesat2.S2Dec4(self._io, self, self._root)
            self.acswq3 = Beesat2.S2Dec4(self._io, self, self._root)
            self.acswa0 = self._io.read_s2be()
            self.acswa1 = self._io.read_s2be()
            self.acswa2 = self._io.read_s2be()
            self.acs_tm_vecs_res = (KaitaiStream.bytes_terminate(self._io.read_bytes(20), 0, False)).decode(u"latin1")


    class Uccout12(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.raw = self._io.read_bits_int_be(12)

        @property
        def value(self):
            if hasattr(self, '_m_value'):
                return self._m_value

            self._m_value = (self.raw * 0.6103515625)
            return getattr(self, '_m_value', None)


    class Utmfs012(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.raw = self._io.read_bits_int_be(12)

        @property
        def value(self):
            if hasattr(self, '_m_value'):
                return self._m_value

            self._m_value = ((self.raw * 0.06103515625) - 50.0)
            return getattr(self, '_m_value', None)


    class S2P0d5(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.raw = self._io.read_s2be()

        @property
        def value(self):
            if hasattr(self, '_m_value'):
                return self._m_value

            self._m_value = (self.raw * 0.5)
            return getattr(self, '_m_value', None)


    class Telemetrypacket5(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.vsabus = Beesat2.Uv50bus12(self._io, self, self._root)
            self.psant0 = self._io.read_bits_int_be(1) != 0
            self.psant1 = self._io.read_bits_int_be(1) != 0
            self.psgyr1 = self._io.read_bits_int_be(1) != 0
            self.pscom1 = self._io.read_bits_int_be(1) != 0
            self._io.align_to_byte()
            self.vbat0 = Beesat2.Uvbat12(self._io, self, self._root)
            self.psuhf0 = self._io.read_bits_int_be(1) != 0
            self.psuhf1 = self._io.read_bits_int_be(1) != 0
            self.pstnc0 = self._io.read_bits_int_be(1) != 0
            self.pstnc1 = self._io.read_bits_int_be(1) != 0
            self._io.align_to_byte()
            self.vbat1 = Beesat2.Uvbat12(self._io, self, self._root)
            self.psgyr0 = self._io.read_bits_int_be(1) != 0
            self.psmcsx = self._io.read_bits_int_be(1) != 0
            self.psmcsy = self._io.read_bits_int_be(1) != 0
            self.psmcsz = self._io.read_bits_int_be(1) != 0
            self._io.align_to_byte()
            self.v50bus = Beesat2.Uv50bus12(self._io, self, self._root)
            self.pswhls = self._io.read_bits_int_be(1) != 0
            self.psobc0 = self._io.read_bits_int_be(1) != 0
            self.psobc1 = self._io.read_bits_int_be(1) != 0
            self.pspdh0 = self._io.read_bits_int_be(1) != 0
            self._io.align_to_byte()
            self.v33bus = Beesat2.Uv33bus12(self._io, self, self._root)
            self.pscam0 = self._io.read_bits_int_be(1) != 0
            self.pssuns = self._io.read_bits_int_be(1) != 0
            self.psmfs0 = self._io.read_bits_int_be(1) != 0
            self.psms1 = self._io.read_bits_int_be(1) != 0
            self._io.align_to_byte()
            self.cc0out = Beesat2.Uccout12(self._io, self, self._root)
            self.pstemp = self._io.read_bits_int_be(1) != 0
            self.pscan0 = self._io.read_bits_int_be(1) != 0
            self.pscan1 = self._io.read_bits_int_be(1) != 0
            self.psccw0 = self._io.read_bits_int_be(1) != 0
            self._io.align_to_byte()
            self.cc1out = Beesat2.Uccout12(self._io, self, self._root)
            self.psccw1 = self._io.read_bits_int_be(1) != 0
            self.ps5vcn = self._io.read_bits_int_be(1) != 0
            self.pcuaid = self._io.read_bits_int_be(1) != 0
            self.pcbobc = self._io.read_bits_int_be(1) != 0
            self._io.align_to_byte()
            self.tbat0 = Beesat2.Utbat12(self._io, self, self._root)
            self.pcbext = self._io.read_bits_int_be(1) != 0
            self.pcch00 = self._io.read_bits_int_be(1) != 0
            self.pcch01 = self._io.read_bits_int_be(1) != 0
            self.pccho2 = self._io.read_bits_int_be(1) != 0
            self._io.align_to_byte()
            self.tbat1 = Beesat2.Utbat12(self._io, self, self._root)
            self.pcch03 = self._io.read_bits_int_be(1) != 0
            self.pcch04 = self._io.read_bits_int_be(1) != 0
            self.pcch05 = self._io.read_bits_int_be(1) != 0
            self.pcch06 = self._io.read_bits_int_be(1) != 0
            self._io.align_to_byte()
            self.rxsig0 = Beesat2.Binary12(self._io, self, self._root)
            self.pcch07 = self._io.read_bits_int_be(1) != 0
            self.pcch08 = self._io.read_bits_int_be(1) != 0
            self.pcch09 = self._io.read_bits_int_be(1) != 0
            self.pcch10 = self._io.read_bits_int_be(1) != 0
            self._io.align_to_byte()
            self.rxsig1 = Beesat2.Binary12(self._io, self, self._root)
            self.pcch11 = self._io.read_bits_int_be(1) != 0
            self.pcch12 = self._io.read_bits_int_be(1) != 0
            self.pcch13 = self._io.read_bits_int_be(1) != 0
            self.pcch14 = self._io.read_bits_int_be(1) != 0
            self._io.align_to_byte()
            self.cwhl = Beesat2.Ucwhl12(self._io, self, self._root)
            self.pcch15 = self._io.read_bits_int_be(1) != 0
            self.pcch16 = self._io.read_bits_int_be(1) != 0
            self.pcch17 = self._io.read_bits_int_be(1) != 0
            self.pcch18 = self._io.read_bits_int_be(1) != 0
            self._io.align_to_byte()
            self.twhlx = Beesat2.Utmfs012(self._io, self, self._root)
            self.pcch19 = self._io.read_bits_int_be(1) != 0
            self.pcch20 = self._io.read_bits_int_be(1) != 0
            self.pcch21 = self._io.read_bits_int_be(1) != 0
            self.pcch22 = self._io.read_bits_int_be(1) != 0
            self._io.align_to_byte()
            self.twhly = Beesat2.Utmfs012(self._io, self, self._root)
            self.pcch23 = self._io.read_bits_int_be(1) != 0
            self.pcch24 = self._io.read_bits_int_be(1) != 0
            self.pcch25 = self._io.read_bits_int_be(1) != 0
            self.pcch26 = self._io.read_bits_int_be(1) != 0
            self._io.align_to_byte()
            self.twhlz = Beesat2.Utmfs012(self._io, self, self._root)
            self.tcrxid = self._io.read_bits_int_be(1) != 0
            self.obcaid = self._io.read_bits_int_be(1) != 0
            self.tmtxrt = self._io.read_bits_int_be(1) != 0
            self.pcch27 = self._io.read_bits_int_be(1) != 0
            self._io.align_to_byte()
            self.cc0in = Beesat2.Ucwhl12(self._io, self, self._root)
            self.pcch28 = self._io.read_bits_int_be(1) != 0
            self.pcch29 = self._io.read_bits_int_be(1) != 0
            self.pcch30 = self._io.read_bits_int_be(1) != 0
            self.pcch31 = self._io.read_bits_int_be(1) != 0
            self._io.align_to_byte()
            self.cctcic = self._io.read_u1()
            self.cctctt = self._io.read_u1()
            self.ccetcs = self._io.read_u1()
            self.cceimc = self._io.read_u1()
            self.ccettc = self._io.read_u1()
            self.ccettg = self._io.read_u1()
            self.ccetcc = self._io.read_u1()
            self.tcrxqu = Beesat2.Utcrxqu8(self._io, self, self._root)
            self.tcfrcp = Beesat2.Binary16(self._io, self, self._root)
            self.tmhkur = Beesat2.Binary16(self._io, self, self._root)
            self.cstutc = Beesat2.Binary32(self._io, self, self._root)
            self.cstsys = Beesat2.Binary32(self._io, self, self._root)
            self.mcxpol = self._io.read_bits_int_be(1) != 0
            self.mcypol = self._io.read_bits_int_be(1) != 0
            self.mczpol = self._io.read_bits_int_be(1) != 0
            self.reserve1 = self._io.read_bits_int_be(1) != 0
            self._io.align_to_byte()
            self.obcbad = Beesat2.Binary4(self._io, self, self._root)
            self.ceswmc = self._io.read_u1()
            self.reserve2 = self._io.read_u1()
            self.beacon = self._io.read_bits_int_be(1) != 0
            self._io.align_to_byte()
            self.reserve3 = Beesat2.Binary3(self._io, self, self._root)
            self.modcom = Beesat2.Binary4(self._io, self, self._root)
            self.obcabc = self._io.read_u1()
            self.modobc = self._io.read_u1()
            self.ccecan = self._io.read_u1()
            self.obccan = self._io.read_u1()
            self.pcsyst = Beesat2.Binary16(self._io, self, self._root)
            self.pcbcnt = self._io.read_u1()
            self.pctxec = self._io.read_u1()
            self.pcrxec = self._io.read_u1()
            self.pcoffc = self._io.read_u1()
            self.pcackc = self._io.read_u1()
            self.pcch32 = self._io.read_bits_int_be(1) != 0
            self.pcch33 = self._io.read_bits_int_be(1) != 0
            self.pcch34 = self._io.read_bits_int_be(1) != 0
            self.pcch35 = self._io.read_bits_int_be(1) != 0
            self.pcch36 = self._io.read_bits_int_be(1) != 0
            self.pcch37 = self._io.read_bits_int_be(1) != 0
            self.pcch38 = self._io.read_bits_int_be(1) != 0
            self.pcch39 = self._io.read_bits_int_be(1) != 0
            self.pcch40 = self._io.read_bits_int_be(1) != 0
            self.pcch41 = self._io.read_bits_int_be(1) != 0
            self._io.align_to_byte()
            self.csaxn = Beesat2.Ucmcs12(self._io, self, self._root)
            self.reserve4 = Beesat2.Binary2(self._io, self, self._root)
            self.cc1in = Beesat2.Ucwhl12(self._io, self, self._root)
            self.reserve5 = Beesat2.Binary4(self._io, self, self._root)
            self.tpcu00 = Beesat2.Utpcu12(self._io, self, self._root)
            self.reserve6 = Beesat2.Binary4(self._io, self, self._root)
            self.tmfs0 = Beesat2.Utmfs012(self._io, self, self._root)
            self.reserve7 = Beesat2.Binary4(self._io, self, self._root)
            self.acswhx = Beesat2.Binary16(self._io, self, self._root)
            self.acswhy = Beesat2.Binary16(self._io, self, self._root)
            self.acswhz = Beesat2.Binary16(self._io, self, self._root)
            self.acsq00 = Beesat2.Binary16(self._io, self, self._root)
            self.acsq01 = Beesat2.Binary16(self._io, self, self._root)
            self.acsq02 = Beesat2.Binary16(self._io, self, self._root)
            self.acsq03 = Beesat2.Binary16(self._io, self, self._root)
            self.acssux = Beesat2.Binary16(self._io, self, self._root)
            self.acssuy = Beesat2.Binary16(self._io, self, self._root)
            self.acssuz = Beesat2.Binary16(self._io, self, self._root)
            self.acsmox = Beesat2.Binary16(self._io, self, self._root)
            self.acsmoy = Beesat2.Binary16(self._io, self, self._root)
            self.acsmoz = Beesat2.Binary16(self._io, self, self._root)
            self.acsm1x = Beesat2.Binary16(self._io, self, self._root)
            self.acsm1y = Beesat2.Binary16(self._io, self, self._root)
            self.acsm1z = Beesat2.Binary16(self._io, self, self._root)
            self.modacs = Beesat2.Binary4(self._io, self, self._root)
            self.acsgsc = self._io.read_bits_int_be(1) != 0
            self.acsshd = self._io.read_bits_int_be(1) != 0
            self._io.align_to_byte()
            self.reserve8 = Beesat2.Binary2(self._io, self, self._root)
            self.acserr = self._io.read_u1()
            self.acsg1y = Beesat2.Binary16(self._io, self, self._root)
            self.acsg1z = Beesat2.Binary16(self._io, self, self._root)
            self.acsg1x = Beesat2.Binary16(self._io, self, self._root)
            self.tobc00 = Beesat2.Utpcu12(self._io, self, self._root)
            self.reserve9 = Beesat2.Binary4(self._io, self, self._root)
            self.csaxp = Beesat2.Ucmcs12(self._io, self, self._root)
            self.csayp = Beesat2.Ucmcs12(self._io, self, self._root)
            self.csazp = Beesat2.Ucmcs12(self._io, self, self._root)
            self.csayn = Beesat2.Ucmcs12(self._io, self, self._root)
            self.csazn = Beesat2.Ucmcs12(self._io, self, self._root)
            self.reserve10 = Beesat2.Binary4(self._io, self, self._root)


    class Uacsgy0y12(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.raw = self._io.read_bits_int_be(12)

        @property
        def value(self):
            if hasattr(self, '_m_value'):
                return self._m_value

            self._m_value = ((self.raw * -0.097680097) + 200)
            return getattr(self, '_m_value', None)


    class Ucpdhcam16(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.raw = self._io.read_bits_int_be(16)

        @property
        def value(self):
            if hasattr(self, '_m_value'):
                return self._m_value

            self._m_value = (self.raw * 0.080586)
            return getattr(self, '_m_value', None)


    class Utbat12(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.raw = self._io.read_bits_int_be(12)

        @property
        def value(self):
            if hasattr(self, '_m_value'):
                return self._m_value

            self._m_value = ((self.raw * 0.244140625) - 50.0)
            return getattr(self, '_m_value', None)


    class Ucmcs12(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.raw = self._io.read_bits_int_be(12)

        @property
        def value(self):
            if hasattr(self, '_m_value'):
                return self._m_value

            self._m_value = (self.raw * 0.152587891)
            return getattr(self, '_m_value', None)


    class Uv33bus12(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.raw = self._io.read_bits_int_be(12)

        @property
        def value(self):
            if hasattr(self, '_m_value'):
                return self._m_value

            self._m_value = (self.raw * 0.001220703125)
            return getattr(self, '_m_value', None)


    class Binary4(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.raw = self._io.read_bits_int_be(4)

        @property
        def value(self):
            if hasattr(self, '_m_value'):
                return self._m_value

            self._m_value = self.raw
            return getattr(self, '_m_value', None)


    class Sacg1ym(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.raw = self._io.read_s2be()

        @property
        def value(self):
            if hasattr(self, '_m_value'):
                return self._m_value

            self._m_value = (self.raw * 0.00875)
            return getattr(self, '_m_value', None)


    class Ucmfs0x12(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.raw = self._io.read_bits_int_be(12)

        @property
        def value(self):
            if hasattr(self, '_m_value'):
                return self._m_value

            self._m_value = ((self.raw * 0.003037316470) - 6.218905472637)
            return getattr(self, '_m_value', None)


    class Utgyrox12(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.raw = self._io.read_bits_int_be(12)

        @property
        def value(self):
            if hasattr(self, '_m_value'):
                return self._m_value

            self._m_value = ((self.raw * 0.534341562589) - 270.619047619)
            return getattr(self, '_m_value', None)


    class Telemetrypacket4(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.cstutc = Beesat2.Binary32(self._io, self, self._root)
            self.v50bus = Beesat2.Uv50bus12(self._io, self, self._root)
            self.v33bus = Beesat2.Uv33bus12(self._io, self, self._root)
            self.csss = Beesat2.Ucsss12(self._io, self, self._root)
            self.cmfs0 = Beesat2.Ucsss12(self._io, self, self._root)
            self.cmfs1 = Beesat2.Ucsss12(self._io, self, self._root)
            self.cgyr0 = Beesat2.Ucsss12(self._io, self, self._root)
            self.cmcs = Beesat2.Ucmcs12(self._io, self, self._root)
            self.cwhl = Beesat2.Ucwhl12(self._io, self, self._root)
            self.acssuxpx0 = Beesat2.Binary12(self._io, self, self._root)
            self.acssuxpx1 = Beesat2.Binary12(self._io, self, self._root)
            self.acssuxpy0 = Beesat2.Binary12(self._io, self, self._root)
            self.acssuxpy1 = Beesat2.Binary12(self._io, self, self._root)
            self.acssuxnx0 = Beesat2.Binary12(self._io, self, self._root)
            self.acssuxnx1 = Beesat2.Binary12(self._io, self, self._root)
            self.acssuxny0 = Beesat2.Binary12(self._io, self, self._root)
            self.acssuxny1 = Beesat2.Binary12(self._io, self, self._root)
            self.acssuypx0 = Beesat2.Binary12(self._io, self, self._root)
            self.acssuypx1 = Beesat2.Binary12(self._io, self, self._root)
            self.acssuypy0 = Beesat2.Binary12(self._io, self, self._root)
            self.acssuypy1 = Beesat2.Binary12(self._io, self, self._root)
            self.acssuynx0 = Beesat2.Binary12(self._io, self, self._root)
            self.acssuynx1 = Beesat2.Binary12(self._io, self, self._root)
            self.acssuyny0 = Beesat2.Binary12(self._io, self, self._root)
            self.acssuyny1 = Beesat2.Binary12(self._io, self, self._root)
            self.acssuzpx0 = Beesat2.Binary12(self._io, self, self._root)
            self.acssuzpx1 = Beesat2.Binary12(self._io, self, self._root)
            self.acssuzpy0 = Beesat2.Binary12(self._io, self, self._root)
            self.acssuzpy1 = Beesat2.Binary12(self._io, self, self._root)
            self.acssuznx0 = Beesat2.Binary12(self._io, self, self._root)
            self.acssuznx1 = Beesat2.Binary12(self._io, self, self._root)
            self.acssuzny0 = Beesat2.Binary12(self._io, self, self._root)
            self.acssuzny1 = Beesat2.Binary12(self._io, self, self._root)
            self.cmfs0x = Beesat2.Ucmfs0x12(self._io, self, self._root)
            self.cmfs0y = Beesat2.Ucmfs0x12(self._io, self, self._root)
            self.cmfs0z = Beesat2.Ucmfs0x12(self._io, self, self._root)
            self.vmfs0 = Beesat2.Uvmfs012(self._io, self, self._root)
            self.tmfs0 = Beesat2.Utmfs012(self._io, self, self._root)
            self.cmfs1x = Beesat2.Ucmfs0x12(self._io, self, self._root)
            self.cmfs1y = Beesat2.Ucmfs0x12(self._io, self, self._root)
            self.cmfs1z = Beesat2.Ucmfs0x12(self._io, self, self._root)
            self.vmfs1 = Beesat2.Uvmfs012(self._io, self, self._root)
            self.tmfs1 = Beesat2.Utmfs012(self._io, self, self._root)
            self.acsgy0x = Beesat2.Uacsgy0x12(self._io, self, self._root)
            self.acsgy0y = Beesat2.Uacsgy0y12(self._io, self, self._root)
            self.acsgy0z = Beesat2.Uacsgy0y12(self._io, self, self._root)
            self.cmcsxp = Beesat2.Ucsss12(self._io, self, self._root)
            self.cmcsxn = Beesat2.Ucsss12(self._io, self, self._root)
            self.cmcsyp = Beesat2.Ucsss12(self._io, self, self._root)
            self.cmcsyn = Beesat2.Ucsss12(self._io, self, self._root)
            self.cmcszp = Beesat2.Ucsss12(self._io, self, self._root)
            self.cmcszn = Beesat2.Ucsss12(self._io, self, self._root)
            self.twhlx = Beesat2.Utmfs012(self._io, self, self._root)
            self.twhly = Beesat2.Utmfs012(self._io, self, self._root)
            self.twhlz = Beesat2.Utmfs012(self._io, self, self._root)
            self.tgyrox = Beesat2.Utgyrox12(self._io, self, self._root)
            self.tgyroy = Beesat2.Utgyrox12(self._io, self, self._root)
            self.tgyroz = Beesat2.Utgyrox12(self._io, self, self._root)
            self.reserve1 = Beesat2.Binary4(self._io, self, self._root)
            self.reserve2 = (KaitaiStream.bytes_terminate(self._io.read_bytes(36), 0, False)).decode(u"latin1")


    class Binary14(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.raw = self._io.read_bits_int_be(14)

        @property
        def value(self):
            if hasattr(self, '_m_value'):
                return self._m_value

            self._m_value = self.raw
            return getattr(self, '_m_value', None)


    class S2N0d5(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.raw = self._io.read_s2be()

        @property
        def value(self):
            if hasattr(self, '_m_value'):
                return self._m_value

            self._m_value = (self.raw * -0.5)
            return getattr(self, '_m_value', None)


    class Binary15(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.raw = self._io.read_bits_int_be(15)

        @property
        def value(self):
            if hasattr(self, '_m_value'):
                return self._m_value

            self._m_value = self.raw
            return getattr(self, '_m_value', None)


    class Uvbat12(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.raw = self._io.read_bits_int_be(12)

        @property
        def value(self):
            if hasattr(self, '_m_value'):
                return self._m_value

            self._m_value = (self.raw * 0.00337252651687956)
            return getattr(self, '_m_value', None)


    class Binary10(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.raw = self._io.read_bits_int_be(10)

        @property
        def value(self):
            if hasattr(self, '_m_value'):
                return self._m_value

            self._m_value = self.raw
            return getattr(self, '_m_value', None)


    class Binary2(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.raw = self._io.read_bits_int_be(2)

        @property
        def value(self):
            if hasattr(self, '_m_value'):
                return self._m_value

            self._m_value = self.raw
            return getattr(self, '_m_value', None)


    class Sourcepacket(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.pvn = Beesat2.Binary3(self._io, self, self._root)
            self.pt = self._io.read_bits_int_be(1) != 0
            self.shf = self._io.read_bits_int_be(1) != 0
            self._io.align_to_byte()
            self.apid = Beesat2.Binary11(self._io, self, self._root)
            self.seqflag = Beesat2.Binary2(self._io, self, self._root)
            self.psc = Beesat2.Binary14(self._io, self, self._root)
            self.pdl = self._io.read_u2be()


    class Ucwhl12(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.raw = self._io.read_bits_int_be(12)

        @property
        def value(self):
            if hasattr(self, '_m_value'):
                return self._m_value

            self._m_value = (self.raw * 0.30517578125)
            return getattr(self, '_m_value', None)


    class Uv50bus12(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.raw = self._io.read_bits_int_be(12)

        @property
        def value(self):
            if hasattr(self, '_m_value'):
                return self._m_value

            self._m_value = (self.raw * 0.001619779146)
            return getattr(self, '_m_value', None)


    class Telemetrypacket30(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.cpdhmcu = Beesat2.Ucpdhmcu16(self._io, self, self._root)
            self.cpdhcam = Beesat2.Ucpdhcam16(self._io, self, self._root)
            self.tpdhcam = self._io.read_u2be()
            self.pdhceccm = self._io.read_u1()
            self.pdhcectc = self._io.read_u1()
            self.pdhcetlii = self._io.read_u1()
            self.pdhcetlc = self._io.read_u1()
            self.pdhti = self._io.read_u1()
            self.pdhth = self._io.read_u1()
            self.pdhceisi = self._io.read_u1()
            self.pdhceici = self._io.read_u1()
            self.pdhceids = self._io.read_u1()
            self.pdhmode = self._io.read_u1()
            self.pdhcii = self._io.read_u1()
            self.pdhcih = self._io.read_u1()
            self.pdhcescm = self._io.read_u1()
            self.pdhcessm = self._io.read_u1()
            self.pdhcescb = self._io.read_u1()
            self.pdhceslb = self._io.read_u1()
            self.pdhcesss = self._io.read_u1()
            self.pdhcessb = self._io.read_u1()
            self.pdhceseb = self._io.read_u1()
            self.pdhcesci = self._io.read_u1()
            self.pdhcsi = self._io.read_u1()
            self.pdhcsh = self._io.read_u1()
            self.pdhbtimg = self._io.read_u1()
            self.pdhswversion = self._io.read_u2be()
            self.pdhcstsys = self._io.read_u4be()
            self.pdhctstutc = self._io.read_u4be()
            self.pdh_reserve = (KaitaiStream.bytes_terminate(self._io.read_bytes(87), 0, False)).decode(u"latin1")


    class Telemetrypacket1(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.cstutc = Beesat2.Binary32(self._io, self, self._root)
            self.csaxp = Beesat2.Ucmcs12(self._io, self, self._root)
            self.csaxn = Beesat2.Ucmcs12(self._io, self, self._root)
            self.csayp = Beesat2.Ucmcs12(self._io, self, self._root)
            self.csayn = Beesat2.Ucmcs12(self._io, self, self._root)
            self.csazp = Beesat2.Ucmcs12(self._io, self, self._root)
            self.csazn = Beesat2.Ucmcs12(self._io, self, self._root)
            self.vsabus = Beesat2.Uv50bus12(self._io, self, self._root)
            self.cc0in = Beesat2.Ucwhl12(self._io, self, self._root)
            self.cc1in = Beesat2.Ucwhl12(self._io, self, self._root)
            self.vbat0 = Beesat2.Uvbat12(self._io, self, self._root)
            self.vbat1 = Beesat2.Uvbat12(self._io, self, self._root)
            self.cc0out = Beesat2.Uccout12(self._io, self, self._root)
            self.cc1out = Beesat2.Uccout12(self._io, self, self._root)
            self.v50bus = Beesat2.Uv50bus12(self._io, self, self._root)
            self.v33bus = Beesat2.Uv33bus12(self._io, self, self._root)
            self.cpcu = Beesat2.Ucsss12(self._io, self, self._root)
            self.cobc0 = Beesat2.Ucmcs12(self._io, self, self._root)
            self.cobc1 = Beesat2.Ucmcs12(self._io, self, self._root)
            self.ctnc0 = Beesat2.Ucsss12(self._io, self, self._root)
            self.ctnc1 = Beesat2.Ucsss12(self._io, self, self._root)
            self.ctrx0 = Beesat2.Ucmcs12(self._io, self, self._root)
            self.ctrx1 = Beesat2.Ucmcs12(self._io, self, self._root)
            self.cpdh = Beesat2.Ucmcs12(self._io, self, self._root)
            self.ccam = Beesat2.Ucsss12(self._io, self, self._root)
            self.csss = Beesat2.Ucsss12(self._io, self, self._root)
            self.cmfs0 = Beesat2.Ucsss12(self._io, self, self._root)
            self.cmfs1 = Beesat2.Ucsss12(self._io, self, self._root)
            self.cgyr0 = Beesat2.Ucsss12(self._io, self, self._root)
            self.cmcs = Beesat2.Ucmcs12(self._io, self, self._root)
            self.cwhl = Beesat2.Ucwhl12(self._io, self, self._root)
            self.ccan0 = Beesat2.Ucsss12(self._io, self, self._root)
            self.ccan1 = Beesat2.Ucsss12(self._io, self, self._root)
            self.vmfs0 = Beesat2.Uvmfs012(self._io, self, self._root)
            self.vmfs1 = Beesat2.Uvmfs012(self._io, self, self._root)
            self.cmcsxp = Beesat2.Ucmcs12(self._io, self, self._root)
            self.cmcsxn = Beesat2.Ucmcs12(self._io, self, self._root)
            self.cmcsyp = Beesat2.Ucmcs12(self._io, self, self._root)
            self.cmcsyn = Beesat2.Ucmcs12(self._io, self, self._root)
            self.cmcszp = Beesat2.Ucmcs12(self._io, self, self._root)
            self.cmcszn = Beesat2.Ucmcs12(self._io, self, self._root)
            self.cobcmcu = Beesat2.Ucmcs12(self._io, self, self._root)
            self.cobcext = Beesat2.Ucmcs12(self._io, self, self._root)
            self.ttrx1 = Beesat2.Ucttrx12(self._io, self, self._root)
            self.cpdh2 = Beesat2.Ucmcs12(self._io, self, self._root)
            self.ccam2 = Beesat2.Ucsss12(self._io, self, self._root)
            self.asstop = self._io.read_u4be()
            self.assintv = self._io.read_u2be()
            self.ascest = self._io.read_u1()
            self.asactv = self._io.read_bits_int_be(1) != 0
            self.reserve2 = self._io.read_bits_int_be(5)
            self._io.align_to_byte()
            self.reserve1 = (KaitaiStream.bytes_terminate(self._io.read_bytes(47), 0, False)).decode(u"latin1")


    class Uacsgy0x12(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.raw = self._io.read_bits_int_be(12)

        @property
        def value(self):
            if hasattr(self, '_m_value'):
                return self._m_value

            self._m_value = ((self.raw * 0.097680097) - 200)
            return getattr(self, '_m_value', None)


    class S2Dec7(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.raw = self._io.read_s2be()

        @property
        def value(self):
            if hasattr(self, '_m_value'):
                return self._m_value

            self._m_value = (self.raw * 1E-8)
            return getattr(self, '_m_value', None)


    class Telemetrypacket41(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.vsabus = Beesat2.Uv50bus12(self._io, self, self._root)
            self.psant0 = self._io.read_bits_int_be(1) != 0
            self.psant1 = self._io.read_bits_int_be(1) != 0
            self.psgyr1 = self._io.read_bits_int_be(1) != 0
            self.pscom1 = self._io.read_bits_int_be(1) != 0
            self._io.align_to_byte()
            self.vbat0 = Beesat2.Uvbat12(self._io, self, self._root)
            self.psuhf0 = self._io.read_bits_int_be(1) != 0
            self.psuhf1 = self._io.read_bits_int_be(1) != 0
            self.pstnc0 = self._io.read_bits_int_be(1) != 0
            self.pstnc1 = self._io.read_bits_int_be(1) != 0
            self._io.align_to_byte()
            self.vbat1 = Beesat2.Uvbat12(self._io, self, self._root)
            self.psgyr0 = self._io.read_bits_int_be(1) != 0
            self.psmcsx = self._io.read_bits_int_be(1) != 0
            self.psmcsy = self._io.read_bits_int_be(1) != 0
            self.psmcsz = self._io.read_bits_int_be(1) != 0
            self._io.align_to_byte()
            self.v50bus = Beesat2.Uv50bus12(self._io, self, self._root)
            self.pswhls = self._io.read_bits_int_be(1) != 0
            self.psobc0 = self._io.read_bits_int_be(1) != 0
            self.psobc1 = self._io.read_bits_int_be(1) != 0
            self.pspdh0 = self._io.read_bits_int_be(1) != 0
            self._io.align_to_byte()
            self.v33bus = Beesat2.Uv33bus12(self._io, self, self._root)
            self.pscam0 = self._io.read_bits_int_be(1) != 0
            self.pssuns = self._io.read_bits_int_be(1) != 0
            self.psmfs0 = self._io.read_bits_int_be(1) != 0
            self.psmfs1 = self._io.read_bits_int_be(1) != 0
            self._io.align_to_byte()
            self.cc0out = Beesat2.Uccout12(self._io, self, self._root)
            self.psccw1 = self._io.read_bits_int_be(1) != 0
            self.ps5vcn = self._io.read_bits_int_be(1) != 0
            self.pcuaid = self._io.read_bits_int_be(1) != 0
            self.pcbobc = self._io.read_bits_int_be(1) != 0
            self._io.align_to_byte()
            self.tbat0 = Beesat2.Utbat12(self._io, self, self._root)
            self.pcbext = self._io.read_bits_int_be(1) != 0
            self.pcch00 = self._io.read_bits_int_be(1) != 0
            self.pcch01 = self._io.read_bits_int_be(1) != 0
            self.pcch02 = self._io.read_bits_int_be(1) != 0
            self._io.align_to_byte()
            self.tbat1 = Beesat2.Utbat12(self._io, self, self._root)
            self.pcch03 = self._io.read_bits_int_be(1) != 0
            self.pcch04 = self._io.read_bits_int_be(1) != 0
            self.pcch05 = self._io.read_bits_int_be(1) != 0
            self.pcch06 = self._io.read_bits_int_be(1) != 0
            self._io.align_to_byte()
            self.rxsig0 = Beesat2.Binary12(self._io, self, self._root)
            self.pcch07 = self._io.read_bits_int_be(1) != 0
            self.pcch08 = self._io.read_bits_int_be(1) != 0
            self.pcch09 = self._io.read_bits_int_be(1) != 0
            self.pcch10 = self._io.read_bits_int_be(1) != 0
            self._io.align_to_byte()
            self.rxsig1 = Beesat2.Binary12(self._io, self, self._root)
            self.pcch11 = self._io.read_bits_int_be(1) != 0
            self.pcch12 = self._io.read_bits_int_be(1) != 0
            self.pcch13 = self._io.read_bits_int_be(1) != 0
            self.pcch14 = self._io.read_bits_int_be(1) != 0
            self._io.align_to_byte()
            self.cwhl = Beesat2.Ucwhl12(self._io, self, self._root)
            self.pcch15 = self._io.read_bits_int_be(1) != 0
            self.pcch16 = self._io.read_bits_int_be(1) != 0
            self.pcch17 = self._io.read_bits_int_be(1) != 0
            self.pcch18 = self._io.read_bits_int_be(1) != 0
            self._io.align_to_byte()
            self.twhlx = Beesat2.Utmfs012(self._io, self, self._root)
            self.pcch19 = self._io.read_bits_int_be(1) != 0
            self.pcch20 = self._io.read_bits_int_be(1) != 0
            self.pcch21 = self._io.read_bits_int_be(1) != 0
            self.pcch22 = self._io.read_bits_int_be(1) != 0
            self._io.align_to_byte()
            self.twhly = Beesat2.Utmfs012(self._io, self, self._root)
            self.pcch23 = self._io.read_bits_int_be(1) != 0
            self.pcch24 = self._io.read_bits_int_be(1) != 0
            self.pcch25 = self._io.read_bits_int_be(1) != 0
            self.pcch26 = self._io.read_bits_int_be(1) != 0
            self._io.align_to_byte()
            self.twhlz = Beesat2.Utmfs012(self._io, self, self._root)
            self.tcrxid = self._io.read_bits_int_be(1) != 0
            self.obcaid = self._io.read_bits_int_be(1) != 0
            self.tmtxrt = self._io.read_bits_int_be(1) != 0
            self.pcch27 = self._io.read_bits_int_be(1) != 0
            self._io.align_to_byte()
            self.cc0in = Beesat2.Ucwhl12(self._io, self, self._root)
            self.pcch28 = self._io.read_bits_int_be(1) != 0
            self.pcch29 = self._io.read_bits_int_be(1) != 0
            self.pcch30 = self._io.read_bits_int_be(1) != 0
            self.pcch31 = self._io.read_bits_int_be(1) != 0
            self._io.align_to_byte()
            self.cctcic = self._io.read_u1()
            self.cctctt = self._io.read_bits_int_be(1) != 0
            self.ccetcs = self._io.read_bits_int_be(1) != 0
            self.cceimc = self._io.read_bits_int_be(1) != 0
            self.ccettc = self._io.read_bits_int_be(1) != 0
            self.ccettg = self._io.read_bits_int_be(1) != 0
            self.ccetcc = self._io.read_bits_int_be(1) != 0
            self._io.align_to_byte()
            self.tcrxqu = Beesat2.Utcrxqu8(self._io, self, self._root)
            self.tcfrcp = self._io.read_u2be()
            self.tmhkur = self._io.read_u2be()
            self.cstutc = self._io.read_u4be()
            self.cstsys = self._io.read_u4be()
            self.mcxpol = self._io.read_bits_int_be(1) != 0
            self.mcypol = self._io.read_bits_int_be(1) != 0
            self.mczpol = self._io.read_bits_int_be(1) != 0
            self.reserve1 = self._io.read_bits_int_be(1) != 0
            self._io.align_to_byte()
            self.obcbad = Beesat2.Binary4(self._io, self, self._root)
            self.ceswmc = self._io.read_u1()
            self.reserve2 = self._io.read_u1()
            self.beacon = self._io.read_bits_int_be(1) != 0
            self._io.align_to_byte()
            self.reserve3 = Beesat2.Binary3(self._io, self, self._root)
            self.modcom = Beesat2.Binary4(self._io, self, self._root)
            self.obcabc = self._io.read_u1()
            self.modobc = self._io.read_u1()
            self.ccecan = self._io.read_u1()
            self.obccan = self._io.read_u1()
            self.pcsyst = self._io.read_u2be()
            self.pcbcnt = self._io.read_u1()
            self.pctxec = self._io.read_u1()
            self.pcrxec = self._io.read_u1()
            self.pcoffc = self._io.read_u1()
            self.pcackc = self._io.read_u1()
            self.pcch32 = self._io.read_bits_int_be(1) != 0
            self.pcch33 = self._io.read_bits_int_be(1) != 0
            self.pcch34 = self._io.read_bits_int_be(1) != 0
            self.pcch35 = self._io.read_bits_int_be(1) != 0
            self.pcch36 = self._io.read_bits_int_be(1) != 0
            self.pcch37 = self._io.read_bits_int_be(1) != 0
            self.pcch38 = self._io.read_bits_int_be(1) != 0
            self.pcch39 = self._io.read_bits_int_be(1) != 0
            self.pcch40 = self._io.read_bits_int_be(1) != 0
            self.pcch41 = self._io.read_bits_int_be(1) != 0
            self._io.align_to_byte()
            self.csaxn = Beesat2.Ucmcs12(self._io, self, self._root)
            self.reserve4 = Beesat2.Binary2(self._io, self, self._root)
            self.cc1in = Beesat2.Ucwhl12(self._io, self, self._root)
            self.reserve5 = Beesat2.Binary4(self._io, self, self._root)
            self.tpcu00 = Beesat2.Utpcu12(self._io, self, self._root)
            self.reserve6 = Beesat2.Binary4(self._io, self, self._root)
            self.tmfs0 = Beesat2.Utmfs012(self._io, self, self._root)
            self.reserve7 = Beesat2.Binary4(self._io, self, self._root)
            self.acswhx = self._io.read_s2be()
            self.acswhy = self._io.read_s2be()
            self.acswhz = self._io.read_s2be()
            self.acsq00 = Beesat2.S2Dec4(self._io, self, self._root)
            self.acsq01 = Beesat2.S2Dec4(self._io, self, self._root)
            self.acsq02 = Beesat2.S2Dec4(self._io, self, self._root)
            self.acsq03 = Beesat2.S2Dec4(self._io, self, self._root)
            self.acssux = Beesat2.S2Dec4(self._io, self, self._root)
            self.acssuy = Beesat2.S2Dec4(self._io, self, self._root)
            self.acssuz = Beesat2.S2Dec4(self._io, self, self._root)
            self.acsm0x = Beesat2.S2P10(self._io, self, self._root)
            self.acsm0y = Beesat2.S2P10(self._io, self, self._root)
            self.acsm0z = Beesat2.S2P10(self._io, self, self._root)
            self.acsm1x = Beesat2.S2P10(self._io, self, self._root)
            self.acsm1y = Beesat2.S2P10(self._io, self, self._root)
            self.acsm1z = Beesat2.S2P10(self._io, self, self._root)
            self.modacs = Beesat2.Binary4(self._io, self, self._root)
            self.acsgsc = self._io.read_bits_int_be(1) != 0
            self.acsshd = self._io.read_bits_int_be(1) != 0
            self._io.align_to_byte()
            self.reserve8 = Beesat2.Binary2(self._io, self, self._root)
            self.acserr = self._io.read_u1()
            self.acg1ym = Beesat2.Sacg1ym(self._io, self, self._root)
            self.acg1zm = Beesat2.Sacg1xzm(self._io, self, self._root)
            self.acg1xm = Beesat2.Sacg1xzm(self._io, self, self._root)
            self.tobc00 = Beesat2.Utpcu12(self._io, self, self._root)
            self.reserve9 = Beesat2.Binary4(self._io, self, self._root)
            self.obctmffp = self._io.read_u2be()
            self.obcswversion = (KaitaiStream.bytes_terminate(self._io.read_bytes(32), 0, False)).decode(u"ascii")
            self.acscmod = Beesat2.Binary4(self._io, self, self._root)
            self.cctccp = self._io.read_u1()
            self.b2_tm_reserve = Beesat2.Binary4(self._io, self, self._root)


    class Binary11(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.raw = self._io.read_bits_int_be(11)

        @property
        def value(self):
            if hasattr(self, '_m_value'):
                return self._m_value

            self._m_value = self.raw
            return getattr(self, '_m_value', None)


    class Binary16(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.raw = self._io.read_bits_int_be(16)

        @property
        def value(self):
            if hasattr(self, '_m_value'):
                return self._m_value

            self._m_value = self.raw
            return getattr(self, '_m_value', None)


    class Binary3(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.raw = self._io.read_bits_int_be(3)

        @property
        def value(self):
            if hasattr(self, '_m_value'):
                return self._m_value

            self._m_value = self.raw
            return getattr(self, '_m_value', None)


    class Masterframe(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.contrl = (KaitaiStream.bytes_terminate(self._io.read_bytes(2), 0, False)).decode(u"ascii")
            self.calsgn = (KaitaiStream.bytes_terminate(self._io.read_bytes(6), 0, False)).decode(u"latin1")
            self.crcsgn = self._io.read_u2be()
            self.transferframe0 = Beesat2.Transferframe(self._io, self, self._root)
            self.transferframe1 = Beesat2.Transferframe(self._io, self, self._root)
            self.transferframe2 = Beesat2.Transferframe(self._io, self, self._root)
            self.transferframe3 = Beesat2.Transferframe(self._io, self, self._root)
            self.rxqual = self._io.read_u1()
            self.errmar = self._io.read_u4be()
            self.tmptnc = self._io.read_u1()


    class Ucpdhmcu16(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.raw = self._io.read_bits_int_be(16)

        @property
        def value(self):
            if hasattr(self, '_m_value'):
                return self._m_value

            self._m_value = (self.raw * 0.016117)
            return getattr(self, '_m_value', None)


    class Transferframe(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.asm = self._io.read_u4be()
            self.tfvn = Beesat2.Binary2(self._io, self, self._root)
            self.scid = Beesat2.Binary10(self._io, self, self._root)
            self.vcidb = Beesat2.Binary3(self._io, self, self._root)
            self.ocff = self._io.read_bits_int_be(1) != 0
            self._io.align_to_byte()
            self.mcfc = self._io.read_u1()
            self.vcfc = self._io.read_u1()
            self.tf_shf = self._io.read_bits_int_be(1) != 0
            self.synchflag = self._io.read_bits_int_be(1) != 0
            self.pof = self._io.read_bits_int_be(1) != 0
            self._io.align_to_byte()
            self.slid = Beesat2.Binary2(self._io, self, self._root)
            self.fhp = Beesat2.Binary11(self._io, self, self._root)
            self.source = Beesat2.Sourcepacket(self._io, self, self._root)
            _on = self.source.apid.value
            if _on == 14:
                self.telemetry = Beesat2.Telemetrypacket1429(self._io, self, self._root)
            elif _on == 10:
                self.telemetry = Beesat2.Telemetrypacket612(self._io, self, self._root)
            elif _on == 17:
                self.telemetry = Beesat2.Telemetrypacket1429(self._io, self, self._root)
            elif _on == 4:
                self.telemetry = Beesat2.Telemetrypacket4(self._io, self, self._root)
            elif _on == 42:
                self.telemetry = Beesat2.Telemetrypacket42(self._io, self, self._root)
            elif _on == 39:
                self.telemetry = Beesat2.Telemetrypacket3739(self._io, self, self._root)
            elif _on == 24:
                self.telemetry = Beesat2.Telemetrypacket1429(self._io, self, self._root)
            elif _on == 6:
                self.telemetry = Beesat2.Telemetrypacket612(self._io, self, self._root)
            elif _on == 20:
                self.telemetry = Beesat2.Telemetrypacket1429(self._io, self, self._root)
            elif _on == 1:
                self.telemetry = Beesat2.Telemetrypacket1(self._io, self, self._root)
            elif _on == 27:
                self.telemetry = Beesat2.Telemetrypacket1429(self._io, self, self._root)
            elif _on == 13:
                self.telemetry = Beesat2.Telemetrypacket13(self._io, self, self._root)
            elif _on == 11:
                self.telemetry = Beesat2.Telemetrypacket612(self._io, self, self._root)
            elif _on == 12:
                self.telemetry = Beesat2.Telemetrypacket612(self._io, self, self._root)
            elif _on == 5:
                self.telemetry = Beesat2.Telemetrypacket5(self._io, self, self._root)
            elif _on == 19:
                self.telemetry = Beesat2.Telemetrypacket1429(self._io, self, self._root)
            elif _on == 23:
                self.telemetry = Beesat2.Telemetrypacket1429(self._io, self, self._root)
            elif _on == 15:
                self.telemetry = Beesat2.Telemetrypacket1429(self._io, self, self._root)
            elif _on == 8:
                self.telemetry = Beesat2.Telemetrypacket612(self._io, self, self._root)
            elif _on == 38:
                self.telemetry = Beesat2.Telemetrypacket3739(self._io, self, self._root)
            elif _on == 40:
                self.telemetry = Beesat2.Telemetrypacket40(self._io, self, self._root)
            elif _on == 9:
                self.telemetry = Beesat2.Telemetrypacket612(self._io, self, self._root)
            elif _on == 21:
                self.telemetry = Beesat2.Telemetrypacket1429(self._io, self, self._root)
            elif _on == 37:
                self.telemetry = Beesat2.Telemetrypacket3739(self._io, self, self._root)
            elif _on == 41:
                self.telemetry = Beesat2.Telemetrypacket41(self._io, self, self._root)
            elif _on == 28:
                self.telemetry = Beesat2.Telemetrypacket1429(self._io, self, self._root)
            elif _on == 16:
                self.telemetry = Beesat2.Telemetrypacket1429(self._io, self, self._root)
            elif _on == 18:
                self.telemetry = Beesat2.Telemetrypacket1429(self._io, self, self._root)
            elif _on == 26:
                self.telemetry = Beesat2.Telemetrypacket1429(self._io, self, self._root)
            elif _on == 2:
                self.telemetry = Beesat2.Telemetrypacket2(self._io, self, self._root)
            elif _on == 29:
                self.telemetry = Beesat2.Telemetrypacket1429(self._io, self, self._root)
            elif _on == 25:
                self.telemetry = Beesat2.Telemetrypacket1429(self._io, self, self._root)
            elif _on == 22:
                self.telemetry = Beesat2.Telemetrypacket1429(self._io, self, self._root)
            elif _on == 30:
                self.telemetry = Beesat2.Telemetrypacket30(self._io, self, self._root)
            self.fecfd = self._io.read_u2be()


    class S2Dec4(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.raw = self._io.read_s2be()

        @property
        def value(self):
            if hasattr(self, '_m_value'):
                return self._m_value

            self._m_value = (self.raw * 0.0001)
            return getattr(self, '_m_value', None)


    class Telemetrypacket42(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.tledoy = self._io.read_f8be()
            self.tlemem = Beesat2.F8Dec8(self._io, self, self._root)
            self.tleecc = self._io.read_f8be()
            self.tleinc = Beesat2.F8Dec4(self._io, self, self._root)
            self.tleaop = Beesat2.F8Dec4(self._io, self, self._root)
            self.tleraa = Beesat2.F8Dec4(self._io, self, self._root)
            self.tleman = Beesat2.F8Dec4(self._io, self, self._root)
            self.tledrt = self._io.read_f8be()
            self.tlexpc = self._io.read_f8be()
            self.tleypc = self._io.read_f8be()
            self.tlettd = self._io.read_f8be()
            self.tleutd = self._io.read_f8be()
            self.tledep = self._io.read_f8be()
            self.tledps = self._io.read_f8be()
            self.tleyea = self._io.read_u2be()
            self.tle_placeholder = (KaitaiStream.bytes_terminate(self._io.read_bytes(12), 0, False)).decode(u"latin1")


    class Telemetrypacketother(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.data = (KaitaiStream.bytes_terminate(self._io.read_bytes(126), 0, False)).decode(u"latin1")


    class Telemetrypacket13(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.imhd00 = (KaitaiStream.bytes_terminate(self._io.read_bytes(4), 0, False)).decode(u"ascii")
            self.imhd01 = (KaitaiStream.bytes_terminate(self._io.read_bytes(4), 0, False)).decode(u"ascii")
            self.imhd02 = self._io.read_u4be()
            self.imhd03 = (KaitaiStream.bytes_terminate(self._io.read_bytes(4), 0, False)).decode(u"ascii")
            self.imhd04 = (KaitaiStream.bytes_terminate(self._io.read_bytes(4), 0, False)).decode(u"ascii")
            self.imhd10 = (KaitaiStream.bytes_terminate(self._io.read_bytes(4), 0, False)).decode(u"ascii")
            self.imhd11 = (KaitaiStream.bytes_terminate(self._io.read_bytes(4), 0, False)).decode(u"ascii")
            self.imhd12 = self._io.read_u4be()
            self.imhd13 = (KaitaiStream.bytes_terminate(self._io.read_bytes(4), 0, False)).decode(u"ascii")
            self.imhd14 = (KaitaiStream.bytes_terminate(self._io.read_bytes(4), 0, False)).decode(u"ascii")
            self.imhd20 = (KaitaiStream.bytes_terminate(self._io.read_bytes(4), 0, False)).decode(u"ascii")
            self.imhd21 = (KaitaiStream.bytes_terminate(self._io.read_bytes(4), 0, False)).decode(u"ascii")
            self.imhd22 = self._io.read_u4be()
            self.imhd23 = (KaitaiStream.bytes_terminate(self._io.read_bytes(4), 0, False)).decode(u"ascii")
            self.imhd24 = (KaitaiStream.bytes_terminate(self._io.read_bytes(4), 0, False)).decode(u"ascii")
            self.imhd30 = (KaitaiStream.bytes_terminate(self._io.read_bytes(4), 0, False)).decode(u"ascii")
            self.imhd31 = (KaitaiStream.bytes_terminate(self._io.read_bytes(4), 0, False)).decode(u"ascii")
            self.imhd32 = self._io.read_u4be()
            self.imhd33 = (KaitaiStream.bytes_terminate(self._io.read_bytes(4), 0, False)).decode(u"ascii")
            self.imhd34 = (KaitaiStream.bytes_terminate(self._io.read_bytes(4), 0, False)).decode(u"ascii")
            self.reserver20 = (KaitaiStream.bytes_terminate(self._io.read_bytes(46), 0, False)).decode(u"latin1")


    class Telemetrypacket3739(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.pdhcrc000 = (KaitaiStream.bytes_terminate(self._io.read_bytes(32), 0, False)).decode(u"ascii")
            self.pdhcrc001 = (KaitaiStream.bytes_terminate(self._io.read_bytes(32), 0, False)).decode(u"ascii")
            self.pdhcrc002 = (KaitaiStream.bytes_terminate(self._io.read_bytes(32), 0, False)).decode(u"ascii")
            self.pdhcrc003 = (KaitaiStream.bytes_terminate(self._io.read_bytes(32), 0, False)).decode(u"ascii")
            self.pdhcrc004 = (KaitaiStream.bytes_terminate(self._io.read_bytes(32), 0, False)).decode(u"ascii")
            self.pdhcrc005 = (KaitaiStream.bytes_terminate(self._io.read_bytes(32), 0, False)).decode(u"ascii")
            self.pdhcrc006 = (KaitaiStream.bytes_terminate(self._io.read_bytes(32), 0, False)).decode(u"ascii")
            self.pdhcrc007 = (KaitaiStream.bytes_terminate(self._io.read_bytes(32), 0, False)).decode(u"ascii")
            self.pdhcrc008 = (KaitaiStream.bytes_terminate(self._io.read_bytes(32), 0, False)).decode(u"ascii")
            self.pdhcrc009 = (KaitaiStream.bytes_terminate(self._io.read_bytes(32), 0, False)).decode(u"ascii")
            self.pdhcrc010 = (KaitaiStream.bytes_terminate(self._io.read_bytes(32), 0, False)).decode(u"ascii")
            self.pdhcrc011 = (KaitaiStream.bytes_terminate(self._io.read_bytes(32), 0, False)).decode(u"ascii")
            self.pdhcrc012 = (KaitaiStream.bytes_terminate(self._io.read_bytes(32), 0, False)).decode(u"ascii")
            self.pdhcrc013 = (KaitaiStream.bytes_terminate(self._io.read_bytes(32), 0, False)).decode(u"ascii")
            self.pdhcrc014 = (KaitaiStream.bytes_terminate(self._io.read_bytes(32), 0, False)).decode(u"ascii")
            self.pdhcrc015 = (KaitaiStream.bytes_terminate(self._io.read_bytes(32), 0, False)).decode(u"ascii")
            self.pdhcrc016 = (KaitaiStream.bytes_terminate(self._io.read_bytes(32), 0, False)).decode(u"ascii")
            self.pdhcrc017 = (KaitaiStream.bytes_terminate(self._io.read_bytes(32), 0, False)).decode(u"ascii")
            self.pdhcrc018 = (KaitaiStream.bytes_terminate(self._io.read_bytes(32), 0, False)).decode(u"ascii")
            self.pdhcrc019 = (KaitaiStream.bytes_terminate(self._io.read_bytes(32), 0, False)).decode(u"ascii")
            self.pdhcrc020 = (KaitaiStream.bytes_terminate(self._io.read_bytes(32), 0, False)).decode(u"ascii")
            self.pdhcrc021 = (KaitaiStream.bytes_terminate(self._io.read_bytes(32), 0, False)).decode(u"ascii")
            self.pdhcrc022 = (KaitaiStream.bytes_terminate(self._io.read_bytes(32), 0, False)).decode(u"ascii")
            self.pdhcrc023 = (KaitaiStream.bytes_terminate(self._io.read_bytes(32), 0, False)).decode(u"ascii")
            self.pdhcrc024 = (KaitaiStream.bytes_terminate(self._io.read_bytes(32), 0, False)).decode(u"ascii")
            self.pdhcrc025 = (KaitaiStream.bytes_terminate(self._io.read_bytes(32), 0, False)).decode(u"ascii")
            self.pdhcrc026 = (KaitaiStream.bytes_terminate(self._io.read_bytes(32), 0, False)).decode(u"ascii")
            self.pdhcrc027 = (KaitaiStream.bytes_terminate(self._io.read_bytes(32), 0, False)).decode(u"ascii")
            self.pdhcrc028 = (KaitaiStream.bytes_terminate(self._io.read_bytes(32), 0, False)).decode(u"ascii")
            self.pdhcrc029 = (KaitaiStream.bytes_terminate(self._io.read_bytes(32), 0, False)).decode(u"ascii")
            self.pdhcrc030 = (KaitaiStream.bytes_terminate(self._io.read_bytes(32), 0, False)).decode(u"ascii")
            self.pdhcrccmask00 = (KaitaiStream.bytes_terminate(self._io.read_bytes(16), 0, False)).decode(u"ascii")


    class Binary12(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.raw = self._io.read_bits_int_be(12)

        @property
        def value(self):
            if hasattr(self, '_m_value'):
                return self._m_value

            self._m_value = self.raw
            return getattr(self, '_m_value', None)


    class Ucsss12(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.raw = self._io.read_bits_int_be(12)

        @property
        def value(self):
            if hasattr(self, '_m_value'):
                return self._m_value

            self._m_value = (self.raw * 0.030517578125)
            return getattr(self, '_m_value', None)


    class Sacg1xzm(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.raw = self._io.read_s2be()

        @property
        def value(self):
            if hasattr(self, '_m_value'):
                return self._m_value

            self._m_value = (self.raw * -0.00875)
            return getattr(self, '_m_value', None)



