
###########################################################
# BioAntiFatigue Coral experiment 05.2025                     
# Multi scan automation - Drs. Vitienes, I., Zaslansky, P. 
###########################################################


## Change the following variables per sample

scan_no = 190
samp = "pt014"
tip_z = 72.36  # motor position when tip of sample is at the lower edge of computer window


######################################

# make sure shutter is open!
%shopen
%fastshutteropen
%startLive

# set common parameters
mt.nref = 20  # number of flat field images
mt.ndark = 20. # number of dark images
mt.nproj = 4720  #number of projections
mt.scanrange = 360.0  # angular range of projections


#### launch scans

# tip scan
mt.scanname = str(scan_no) + "_" + samp + "_tip_10x_HA_0p65_200ms_100mm_45keV_gap5p5mm_Cu0p45_4720prj"
%amove tomo1tz tip_z
mt.setFlyScanParameters()
%doTomo

# sub-tip scan 1
mt.scanname = str(scan_no+1) + "_" + samp + "_1p2subtip_10x_HA_0p65_200ms_100mm_45keV_gap5p5mm_Cu0p45_4720prj"
%dmove tomo1tz 1.2
mt.setFlyScanParameters()
%doTomo

# sub-tip scan 2
mt.scanname = str(scan_no+2) + "_" + samp + "_2p4subtip_10x_HA_0p65_200ms_100mm_45keV_gap5p5mm_Cu0p45_4720prj"
%dmove tomo1tz 1.2
mt.setFlyScanParameters()
%doTomo


%shclose
