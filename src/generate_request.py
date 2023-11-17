import os
from typing import List


start = """<?xml version="1.0" encoding="UTF-8"?>
<AcitivityPlanOptimizationRequest>
  <Activity_Plan>
    <Fixed_Header>
      <File_Name>Activity</File_Name>
      <Validity_Period/>
      <File_Version/>
    </Fixed_Header>
    <Metadata>
      <Start_Time>UTC=2021-01-01T00:00:00</Start_Time>
    </Metadata>
    <Data_Block>
      <List_Of_RVR_Activities count="9">
"""
end = """      </List_Of_RVR_Activities>
    </Data_Block>
  </Activity_Plan>
  <initialState>
    <subsysState>
      <subsysName>RTB</subsysName>
      <stateComponents>
        <stateComponentVal name="RTB_STATUS">RTB_OFF</stateComponentVal>
      </stateComponents>
    </subsysState>
    <subsysState>
      <subsysName>Environment</subsysName>
      <stateComponents>
        <stateComponentVal name="ENV_SAMPLE_STATUS">ENV_SAMPLE_SUBSURFACE</stateComponentVal>
        <stateComponentVal name="ENV_TERRAIN_IMAGE">NO_IMAGE</stateComponentVal>
        <stateComponentVal name="ENV_DRILL_IMAGE">NO_IMAGE</stateComponentVal>
        <stateComponentVal name="ENV_ROVER_POS">INITIAL_POS</stateComponentVal>
      </stateComponents>
    </subsysState>
    <subsysState>
      <subsysName>Ade</subsysName>
      <stateComponents>
        <stateComponentVal name="ADE_LEFT_STATUS">ADE_LEFT_OFF</stateComponentVal>
        <stateComponentVal name="ADE_RIGHT_STATUS">ADE_RIGHT_OFF</stateComponentVal>
      </stateComponents>
    </subsysState>
    <subsysState>
      <subsysName>System</subsysName>
      <stateComponents>
        <stateComponentVal name="SYS_STATUS">SYS_READY</stateComponentVal>
        <stateComponentVal name="SYS_AVAILABLE_MEMORY">300</stateComponentVal>
        <stateComponentVal name="SYS_AVAILABLE_POWER">80.0</stateComponentVal>
        <stateComponentVal name="SYS_AVAILABLE_ENERGY">1000.0</stateComponentVal>
        <stateComponentVal name="SYS_AVAILABLE_DURATION">72000.0</stateComponentVal>
        <stateComponentVal name="SYS_ROVER_LONGITUDE">-24.55</stateComponentVal>
        <stateComponentVal name="SYS_ROVER_LATITUDE">+25</stateComponentVal>
        <stateComponentVal name="SYS_SIMSTART_UTC">2021-01-01T09:00:00</stateComponentVal>
        <stateComponentVal name="SYS_ROVER_RET">0/0.0</stateComponentVal>
      </stateComponents>
    </subsysState>
    <subsysState>
      <subsysName>Dhs</subsysName>
      <stateComponents>
        <stateComponentVal name="DHS_STATUS">DHS_LOWPOWER</stateComponentVal>
      </stateComponents>
    </subsysState>
    <subsysState>
      <subsysName>Mmega</subsysName>
      <stateComponents>
        <stateComponentVal name="MMEGA_STATUS">MMEGA_OFF</stateComponentVal>
        <stateComponentVal name="MMEGA_Initialize_successful">0</stateComponentVal>
        <stateComponentVal name="MMEGA_Cooldown_successful">0</stateComponentVal>
        <stateComponentVal name="MMEGA_SetConfig_successful">0</stateComponentVal>
        <stateComponentVal name="NB_SPOTS_RLS">20</stateComponentVal>
        <stateComponentVal name="NB_SPOTS_MOMA">3</stateComponentVal>
        <stateComponentVal name="RLS_SPDS_POSITIONS">238.40 239.0 240.0 241.0 242.0 243.0 244.0 245.0 246.0 247.0 248.0 249.0 250.0 251.0 252.0 253.0 254.0 255.0 256.0 257.0 258.0 259.0 260.0 261.0 262.0 263.0 264.0 265.0 266.0 267.0 268.0 269.0 270.0 271.0 272.0 273.0 274.0 275.0 276.0</stateComponentVal>
        <stateComponentVal name="MOMA_SPDS_POSITIONS">130.60 131.0 132.0 133.0 134.0 135.0 136.0 137.0 138.0 139.0 140.0 141.0 142.0 143.0 144.0 145.0 146.0 147.0 148.0 149.0</stateComponentVal>
      </stateComponents>
    </subsysState>
    <subsysState>
      <subsysName>Isem</subsysName>
      <stateComponents>
        <stateComponentVal name="ISEM_STATUS">ISEM_OFF</stateComponentVal>
      </stateComponents>
    </subsysState>
    <subsysState>
      <subsysName>Rover</subsysName>
      <stateComponents>
        <stateComponentVal name="RV_STATUS">RV_READY</stateComponentVal>
      </stateComponents>
    </subsysState>
    <subsysState>
      <subsysName>Wisdom</subsysName>
      <stateComponents>
        <stateComponentVal name="WSD_STATUS">WSD_OFF</stateComponentVal>
        <stateComponentVal name="WSD_GeneratedData">0.0</stateComponentVal>
        <stateComponentVal name="WSD_GeneratedDataCompressed">0.0</stateComponentVal>
      </stateComponents>
    </subsysState>
    <subsysState>
      <subsysName>RLS</subsysName>
      <stateComponents>
        <stateComponentVal name="RLS_STATUS">RLS_OFF</stateComponentVal>
        <stateComponentVal name="RLS_LaserStatus">0</stateComponentVal>
        <stateComponentVal name="RLS_SpotID">0</stateComponentVal>
        <stateComponentVal name="RLS_NrOfDarkSpots">0</stateComponentVal>
        <stateComponentVal name="RLS_TimeAtPowerOn">0</stateComponentVal>
        <stateComponentVal name="RLS_SPOTS_INTERESTING">0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0</stateComponentVal>
      </stateComponents>
    </subsysState>
    <subsysState>
      <subsysName>PanCam</subsysName>
      <stateComponents>
        <stateComponentVal name="PANCAM_STATUS">PANCAM_OFF</stateComponentVal>
        <stateComponentVal name="PANCAM_L_FPOS">1</stateComponentVal>
        <stateComponentVal name="PANCAM_R_FPOS">1</stateComponentVal>
      </stateComponents>
    </subsysState>
    <subsysState>
      <subsysName>Comms</subsysName>
      <stateComponents>
        <stateComponentVal name="COMMS_MAIN_STATUS">COMMS_MAIN_OFF</stateComponentVal>
        <stateComponentVal name="COMMS_RED_STATUS">COMMS_RED_OFF</stateComponentVal>
        <stateComponentVal name="RV_HP_integral">0</stateComponentVal>
        <stateComponentVal name="MMS_FIFO_HP_integral">0</stateComponentVal>
        <stateComponentVal name="MMS_FIFO_LP_integral">0</stateComponentVal>
        <stateComponentVal name="COMMS_PERIODS">{2021-09-13T3:55:00, 2021-09-13T4:15:05, 85.0, Sol_0_Comms_1}, {2021-09-13T20:24:25, 2021-09-13T20:44:30, 85.0, Sol_0_Comms_2}, {2021-09-14T4:40:00, 2021-09-14T4:58:00, 85.0, Sol_1_Comms_1}, {2021-09-14T21:10:00, 2021-09-14T21:30:00, 85.0, Sol_1_Comms_2}</stateComponentVal>
      </stateComponents>
    </subsysState>
    <subsysState>
      <subsysName>Clupi</subsysName>
      <stateComponents>
        <stateComponentVal name="CLUPI_STATUS">CLUPI_OFF</stateComponentVal>
        <stateComponentVal name="CLUPI_ImageDataType">1</stateComponentVal>
        <stateComponentVal name="CLUPI_Quantization">0</stateComponentVal>
        <stateComponentVal name="CLUPI_Binning">0</stateComponentVal>
        <stateComponentVal name="CLUPI_Mem_Check">0</stateComponentVal>
        <stateComponentVal name="CLUPI_Time_Synch">0</stateComponentVal>
      </stateComponents>
    </subsysState>
    <subsysState>
      <subsysName>Adron</subsysName>
      <stateComponents>
        <stateComponentVal name="ADRON_STATUS">ADRON_OFF</stateComponentVal>
        <stateComponentVal name="ADRON_POLLING_RATE">20</stateComponentVal>
      </stateComponents>
    </subsysState>
    <subsysState>
      <subsysName>Mast</subsysName>
      <stateComponents>
        <stateComponentVal name="MAST_DEP_STATUS">MAST_DEP_OFF</stateComponentVal>
        <stateComponentVal name="MAST_PAN_STATUS">MAST_PAN_OFF</stateComponentVal>
        <stateComponentVal name="MAST_TILT_STATUS">MAST_TILT_OFF</stateComponentVal>
        <stateComponentVal name="MAST_Q1">-90.0</stateComponentVal>
        <stateComponentVal name="MAST_Q2">0.0</stateComponentVal>
        <stateComponentVal name="MAST_Q3">-90.0</stateComponentVal>
      </stateComponents>
    </subsysState>
    <subsysState>
      <subsysName>SolarArray</subsysName>
      <stateComponents>
        <stateComponentVal name="SA_LEFT_PRIM_STATUS">SA_LEFT_PRIM_OFF</stateComponentVal>
        <stateComponentVal name="SA_LEFT_SEC_STATUS">SA_LEFT_SEC_OFF</stateComponentVal>
        <stateComponentVal name="SA_RIGHT_PRIM_STATUS">SA_RIGHT_PRIM_OFF</stateComponentVal>
        <stateComponentVal name="SA_RIGHT_SEC_STATUS">SA_RIGHT_SEC_OFF</stateComponentVal>
        <stateComponentVal name="SA_Q1">-180</stateComponentVal>
        <stateComponentVal name="SA_Q2">-180</stateComponentVal>
        <stateComponentVal name="SA_Q3">-180</stateComponentVal>
        <stateComponentVal name="SA_Q4">-180</stateComponentVal>
      </stateComponents>
    </subsysState>
    <subsysState>
      <subsysName>Moma</subsysName>
      <stateComponents>
        <stateComponentVal name="MOMA_STATUS">MOMA_OFF</stateComponentVal>
      </stateComponents>
    </subsysState>
    <subsysState>
      <subsysName>DrillMamissSpds</subsysName>
      <stateComponents>
        <stateComponentVal name="DRILL_STATUS">DRILL_SPDS_OFF</stateComponentVal>
        <stateComponentVal name="DRILL_DB_Q1">0.0</stateComponentVal>
        <stateComponentVal name="DRILL_DB_Q2">0.0</stateComponentVal>
        <stateComponentVal name="DRILL_ROD_Q">0.0</stateComponentVal>
        <stateComponentVal name="DRILL_POSITIONER_PHASE">0</stateComponentVal>
        <stateComponentVal name="DRILL_ROD_SAMPLE_PHASE">0</stateComponentVal>
        <stateComponentVal name="DRILL_SENSOR_CALIB_STATUS">0</stateComponentVal>
        <stateComponentVal name="SPDS_CSTM_POSE_ID">0</stateComponentVal>
        <stateComponentVal name="SPDS_BSD_POSE">0.0</stateComponentVal>
        <stateComponentVal name="SPDS_CSTM_POSE">0.0</stateComponentVal>
        <stateComponentVal name="SPDS_CS_POSE">0.0</stateComponentVal>
        <stateComponentVal name="SPDS_CS_DEJAM_POSE">0.0</stateComponentVal>
        <stateComponentVal name="SPDS_CS_VSM_POSE">0.0</stateComponentVal>
        <stateComponentVal name="SPDS_DS_1_POSE">0.0</stateComponentVal>
        <stateComponentVal name="SPDS_DS_2_POSE">0.0</stateComponentVal>
        <stateComponentVal name="SPDS_PSDDS_POSE">0.0</stateComponentVal>
        <stateComponentVal name="SPDS_PSHS_POSE">0.0</stateComponentVal>
      </stateComponents>
    </subsysState>
    <subsysState>
      <subsysName>GNC</subsysName>
      <stateComponents>
        <stateComponentVal name="IMU_STATUS">IMU_OFF</stateComponentVal>
        <stateComponentVal name="LOCCAM_STATUS">LOCCAM_OFF</stateComponentVal>
        <stateComponentVal name="NAVCAM_STATUS">NAVCAM_OFF</stateComponentVal>
        <stateComponentVal name="BEMA_STATUS">BEMA_OFF</stateComponentVal>
        <stateComponentVal name="COMPRESSION_STATUS">COMPRESSION_OFF</stateComponentVal>
        <stateComponentVal name="HEADING_UPDATED">0</stateComponentVal>
        <stateComponentVal name="POSITION_UPDATED">0</stateComponentVal>
        <stateComponentVal name="LocX">0.0</stateComponentVal>
        <stateComponentVal name="LocY">0.0</stateComponentVal>
        <stateComponentVal name="LocZ">0.0</stateComponentVal>
        <stateComponentVal name="RotX">0.0</stateComponentVal>
        <stateComponentVal name="RotY">0.0</stateComponentVal>
        <stateComponentVal name="RotZ">0.0</stateComponentVal>
      </stateComponents>
    </subsysState>
    <subsysState>
      <subsysName>Power</subsysName>
      <stateComponents>
        <stateComponentVal name="POWER_STATUS">POWER_OPERATIONAL_NIGHT</stateComponentVal>
      </stateComponents>
    </subsysState>
    <subsysState>
      <subsysName>Thermal</subsysName>
      <stateComponents>
        <stateComponentVal name="THERMAL_STATUS">THERMAL_NIGHTTIME</stateComponentVal>
      </stateComponents>
    </subsysState>
  </initialState>
  <dtDefinitionName>exomars</dtDefinitionName>
  <simulationTemplateName>rehearsal_simulator</simulationTemplateName>
</AcitivityPlanOptimizationRequest>
"""

all_activities = {
    "RV_WakeUp" : """        <RVR_Activity>
          <ID>RV_WakeUp</ID>
          <Activity_No />
          <Activity_Name>RV_WakeUp</Activity_Name>
          <Activity_Type>EXEC</Activity_Type>
          <List_of_Parameters count="0" />
        </RVR_Activity>
""",
    "GNC_FPATH_Straight" : """        <RVR_Activity>
          <ID>GNC_FPATH_Straight</ID>
          <Activity_No />
          <Activity_Name>GNC_FPATH_Straight</Activity_Name>
          <Activity_Type>EXEC</Activity_Type>
          <List_of_Parameters count="16">
            <Parameter>
              <Name>opMode</Name>
              <Value>2</Value>
            </Parameter>
            <Parameter>
              <Name>posX_start</Name>
              <Value>0.0</Value>
            </Parameter>
            <Parameter>
              <Name>posY_start</Name>
              <Value>0.0</Value>
            </Parameter>
            <Parameter>
              <Name>posX_end</Name>
              <Value>3.0</Value>
            </Parameter>
            <Parameter>
              <Name>posY_end</Name>
              <Value>0.0</Value>
            </Parameter>
            <Parameter>
              <Name>wsdType</Name>
              <Value>0</Value>
            </Parameter>
            <Parameter>
              <Name>wsdDistance</Name>
              <Value>0.5</Value>
            </Parameter>
            <Parameter>
              <Name>wsdUserCodeNbr</Name>
              <Value>1</Value>
            </Parameter>
            <Parameter>
              <Name>wsdHkSampleNbr</Name>
              <Value>30</Value>
            </Parameter>
            <Parameter>
              <Name>wsdWarmupTime</Name>
              <Value>100</Value>
            </Parameter>
            <Parameter>
              <Name>wsdParamTable1</Name>
              <Value>5</Value>
            </Parameter>
            <Parameter>
              <Name>wsdParamTable2</Name>
              <Value>10</Value>
            </Parameter>
            <Parameter>
              <Name>wsdParamTable3</Name>
              <Value>15</Value>
            </Parameter>
            <Parameter>
              <Name>wsdParamTable4</Name>
              <Value>20</Value>
            </Parameter>
            <Parameter>
              <Name>distance</Name>
              <Value>3.0</Value>
            </Parameter>
            <Parameter>
              <Name>speed</Name>
              <Value>32.0</Value>
            </Parameter>
          </List_of_Parameters>
        </RVR_Activity>
""",
    "RV_ConfigureReset" : """        <RVR_Activity>
          <ID>RV_ConfigureReset</ID>
          <Activity_No />
          <Activity_Name>RV_ConfigureReset</Activity_Name>
          <Activity_Type>EXEC</Activity_Type>
          <List_of_Parameters count="0" />
        </RVR_Activity>
""",
    "CLUPI_AcquireZScience_DrillArea" : """        <RVR_Activity>
          <ID>CLUPI_AcquireZScience_DrillArea</ID>
          <Activity_No />
          <Activity_Name>CLUPI_AcquireZScience_DrillArea</Activity_Name>
          <Activity_Type>EXEC</Activity_Type>
          <List_of_Parameters count="60">
            <Parameter>
              <Name>Quantization</Name>
              <Value>0</Value>
            </Parameter>
            <Parameter>
              <Name>Binning</Name>
              <Value>0</Value>
            </Parameter>
            <Parameter>
              <Name>AutoExposureOnOff</Name>
              <Value>1</Value>
            </Parameter>
            <Parameter>
              <Name>AutoFocusOnOff</Name>
              <Value>1</Value>
            </Parameter>
            <Parameter>
              <Name>GrayscaleOnOff</Name>
              <Value>0</Value>
            </Parameter>
            <Parameter>
              <Name>Criticality</Name>
              <Value>1</Value>
            </Parameter>
            <Parameter>
              <Name>ImageFOVType</Name>
              <Value>3</Value>
            </Parameter>
            <Parameter>
              <Name>IntegrationTime</Name>
              <Value>0</Value>
            </Parameter>
            <Parameter>
              <Name>NrOfImages</Name>
              <Value>2</Value>
            </Parameter>
            <Parameter>
              <Name>WindowingWindowX1</Name>
              <Value>1</Value>
            </Parameter>
            <Parameter>
              <Name>WindowingWindowY1</Name>
              <Value>1</Value>
            </Parameter>
            <Parameter>
              <Name>WindowingWindowX2</Name>
              <Value>2652</Value>
            </Parameter>
            <Parameter>
              <Name>WindowingWindowY2</Name>
              <Value>641</Value>
            </Parameter>
            <Parameter>
              <Name>AutoExposureWindowX1</Name>
              <Value>1</Value>
            </Parameter>
            <Parameter>
              <Name>AutoExposureWindowY1</Name>
              <Value>1</Value>
            </Parameter>
            <Parameter>
              <Name>AutoExposureWindowX2</Name>
              <Value>2652</Value>
            </Parameter>
            <Parameter>
              <Name>AutoExposureWindowY2</Name>
              <Value>641</Value>
            </Parameter>
            <Parameter>
              <Name>AutoFocusWindowX1</Name>
              <Value>1</Value>
            </Parameter>
            <Parameter>
              <Name>AutoFocusWindowY1</Name>
              <Value>1</Value>
            </Parameter>
            <Parameter>
              <Name>AutoFocusWindowX2</Name>
              <Value>1</Value>
            </Parameter>
            <Parameter>
              <Name>AutoFocusWindowY2</Name>
              <Value>1</Value>
            </Parameter>
            <Parameter>
              <Name>FocusPosition1</Name>
              <Value>0</Value>
            </Parameter>
            <Parameter>
              <Name>FocusPosition2</Name>
              <Value>0</Value>
            </Parameter>
            <Parameter>
              <Name>FocusPosition3</Name>
              <Value>0</Value>
            </Parameter>
            <Parameter>
              <Name>FocusPosition4</Name>
              <Value>0</Value>
            </Parameter>
            <Parameter>
              <Name>FocusPosition5</Name>
              <Value>0</Value>
            </Parameter>
            <Parameter>
              <Name>FocusPosition6</Name>
              <Value>0</Value>
            </Parameter>
            <Parameter>
              <Name>FocusPosition7</Name>
              <Value>0</Value>
            </Parameter>
            <Parameter>
              <Name>FocusPosition8</Name>
              <Value>0</Value>
            </Parameter>
            <Parameter>
              <Name>FocusPosition9</Name>
              <Value>0</Value>
            </Parameter>
            <Parameter>
              <Name>FocusPosition10</Name>
              <Value>0</Value>
            </Parameter>
            <Parameter>
              <Name>FocusPosition11</Name>
              <Value>0</Value>
            </Parameter>
            <Parameter>
              <Name>FocusPosition12</Name>
              <Value>0</Value>
            </Parameter>
            <Parameter>
              <Name>FocusPosition13</Name>
              <Value>0</Value>
            </Parameter>
            <Parameter>
              <Name>FocusPosition14</Name>
              <Value>0</Value>
            </Parameter>
            <Parameter>
              <Name>FocusPosition15</Name>
              <Value>0</Value>
            </Parameter>
            <Parameter>
              <Name>FocusPosition16</Name>
              <Value>0</Value>
            </Parameter>
            <Parameter>
              <Name>RefNrAcquiredImage1</Name>
              <Value>1</Value>
            </Parameter>
            <Parameter>
              <Name>RefNrAcquiredImage2</Name>
              <Value>2</Value>
            </Parameter>
            <Parameter>
              <Name>RefNrAcquiredImage3</Name>
              <Value>3</Value>
            </Parameter>
            <Parameter>
              <Name>RefNrAcquiredImage4</Name>
              <Value>4</Value>
            </Parameter>
            <Parameter>
              <Name>RefNrAcquiredImage5</Name>
              <Value>5</Value>
            </Parameter>
            <Parameter>
              <Name>RefNrAcquiredImage6</Name>
              <Value>6</Value>
            </Parameter>
            <Parameter>
              <Name>RefNrAcquiredImage7</Name>
              <Value>7</Value>
            </Parameter>
            <Parameter>
              <Name>RefNrAcquiredImage8</Name>
              <Value>8</Value>
            </Parameter>
            <Parameter>
              <Name>RefNrAcquiredImage9</Name>
              <Value>9</Value>
            </Parameter>
            <Parameter>
              <Name>RefNrAcquiredImage10</Name>
              <Value>10</Value>
            </Parameter>
            <Parameter>
              <Name>RefNrAcquiredImage11</Name>
              <Value>11</Value>
            </Parameter>
            <Parameter>
              <Name>RefNrAcquiredImage12</Name>
              <Value>12</Value>
            </Parameter>
            <Parameter>
              <Name>RefNrAcquiredImage13</Name>
              <Value>13</Value>
            </Parameter>
            <Parameter>
              <Name>RefNrAcquiredImage14</Name>
              <Value>14</Value>
            </Parameter>
            <Parameter>
              <Name>RefNrAcquiredImage15</Name>
              <Value>15</Value>
            </Parameter>
            <Parameter>
              <Name>RefNrAcquiredImage16</Name>
              <Value>16</Value>
            </Parameter>
            <Parameter>
              <Name>NrOfImagesZS</Name>
              <Value>2</Value>
            </Parameter>
            <Parameter>
              <Name>ZSCriticality</Name>
              <Value>1</Value>
            </Parameter>
            <Parameter>
              <Name>RefNrZStackedImage</Name>
              <Value>17</Value>
            </Parameter>
            <Parameter>
              <Name>RefNrImageToTransfer</Name>
              <Value>17</Value>
            </Parameter>
            <Parameter>
              <Name>DTCriticality</Name>
              <Value>0</Value>
            </Parameter>
            <Parameter>
              <Name>ZSTACK</Name>
              <Value>1</Value>
            </Parameter>
            <Parameter>
              <Name>DATAT</Name>
              <Value>1</Value>
            </Parameter>
          </List_of_Parameters>
        </RVR_Activity>
""",
    "Collect_Sample" : """        <RVR_Activity>
          <ID>Collect_Sample</ID>
          <Activity_No />
          <Activity_Name>Collect_Sample</Activity_Name>
          <Activity_Type>EXEC</Activity_Type>
          <List_of_Parameters count="1">
            <Parameter>
              <Name>soil_type</Name>
              <Value>4</Value>
            </Parameter>
          </List_of_Parameters>
        </RVR_Activity>
""",
    "CLUPI_AcquireZScience_DrillFines" : """        <RVR_Activity>
          <ID>CLUPI_AcquireZScience_DrillFines</ID>
          <Activity_No />
          <Activity_Name>CLUPI_AcquireZScience_DrillFines</Activity_Name>
          <Activity_Type>EXEC</Activity_Type>
          <List_of_Parameters count="60">
            <Parameter>
              <Name>Quantization</Name>
              <Value>0</Value>
            </Parameter>
            <Parameter>
              <Name>Binning</Name>
              <Value>0</Value>
            </Parameter>
            <Parameter>
              <Name>AutoExposureOnOff</Name>
              <Value>1</Value>
            </Parameter>
            <Parameter>
              <Name>AutoFocusOnOff</Name>
              <Value>1</Value>
            </Parameter>
            <Parameter>
              <Name>GrayscaleOnOff</Name>
              <Value>0</Value>
            </Parameter>
            <Parameter>
              <Name>Criticality</Name>
              <Value>1</Value>
            </Parameter>
            <Parameter>
              <Name>ImageFOVType</Name>
              <Value>3</Value>
            </Parameter>
            <Parameter>
              <Name>IntegrationTime</Name>
              <Value>0</Value>
            </Parameter>
            <Parameter>
              <Name>NrOfImages</Name>
              <Value>2</Value>
            </Parameter>
            <Parameter>
              <Name>WindowingWindowX1</Name>
              <Value>1</Value>
            </Parameter>
            <Parameter>
              <Name>WindowingWindowY1</Name>
              <Value>1</Value>
            </Parameter>
            <Parameter>
              <Name>WindowingWindowX2</Name>
              <Value>2652</Value>
            </Parameter>
            <Parameter>
              <Name>WindowingWindowY2</Name>
              <Value>641</Value>
            </Parameter>
            <Parameter>
              <Name>AutoExposureWindowX1</Name>
              <Value>1</Value>
            </Parameter>
            <Parameter>
              <Name>AutoExposureWindowY1</Name>
              <Value>1</Value>
            </Parameter>
            <Parameter>
              <Name>AutoExposureWindowX2</Name>
              <Value>2652</Value>
            </Parameter>
            <Parameter>
              <Name>AutoExposureWindowY2</Name>
              <Value>641</Value>
            </Parameter>
            <Parameter>
              <Name>AutoFocusWindowX1</Name>
              <Value>1</Value>
            </Parameter>
            <Parameter>
              <Name>AutoFocusWindowY1</Name>
              <Value>1</Value>
            </Parameter>
            <Parameter>
              <Name>AutoFocusWindowX2</Name>
              <Value>1</Value>
            </Parameter>
            <Parameter>
              <Name>AutoFocusWindowY2</Name>
              <Value>1</Value>
            </Parameter>
            <Parameter>
              <Name>FocusPosition1</Name>
              <Value>0</Value>
            </Parameter>
            <Parameter>
              <Name>FocusPosition2</Name>
              <Value>0</Value>
            </Parameter>
            <Parameter>
              <Name>FocusPosition3</Name>
              <Value>0</Value>
            </Parameter>
            <Parameter>
              <Name>FocusPosition4</Name>
              <Value>0</Value>
            </Parameter>
            <Parameter>
              <Name>FocusPosition5</Name>
              <Value>0</Value>
            </Parameter>
            <Parameter>
              <Name>FocusPosition6</Name>
              <Value>0</Value>
            </Parameter>
            <Parameter>
              <Name>FocusPosition7</Name>
              <Value>0</Value>
            </Parameter>
            <Parameter>
              <Name>FocusPosition8</Name>
              <Value>0</Value>
            </Parameter>
            <Parameter>
              <Name>FocusPosition9</Name>
              <Value>0</Value>
            </Parameter>
            <Parameter>
              <Name>FocusPosition10</Name>
              <Value>0</Value>
            </Parameter>
            <Parameter>
              <Name>FocusPosition11</Name>
              <Value>0</Value>
            </Parameter>
            <Parameter>
              <Name>FocusPosition12</Name>
              <Value>0</Value>
            </Parameter>
            <Parameter>
              <Name>FocusPosition13</Name>
              <Value>0</Value>
            </Parameter>
            <Parameter>
              <Name>FocusPosition14</Name>
              <Value>0</Value>
            </Parameter>
            <Parameter>
              <Name>FocusPosition15</Name>
              <Value>0</Value>
            </Parameter>
            <Parameter>
              <Name>FocusPosition16</Name>
              <Value>0</Value>
            </Parameter>
            <Parameter>
              <Name>RefNrAcquiredImage1</Name>
              <Value>1</Value>
            </Parameter>
            <Parameter>
              <Name>RefNrAcquiredImage2</Name>
              <Value>2</Value>
            </Parameter>
            <Parameter>
              <Name>RefNrAcquiredImage3</Name>
              <Value>3</Value>
            </Parameter>
            <Parameter>
              <Name>RefNrAcquiredImage4</Name>
              <Value>4</Value>
            </Parameter>
            <Parameter>
              <Name>RefNrAcquiredImage5</Name>
              <Value>5</Value>
            </Parameter>
            <Parameter>
              <Name>RefNrAcquiredImage6</Name>
              <Value>6</Value>
            </Parameter>
            <Parameter>
              <Name>RefNrAcquiredImage7</Name>
              <Value>7</Value>
            </Parameter>
            <Parameter>
              <Name>RefNrAcquiredImage8</Name>
              <Value>8</Value>
            </Parameter>
            <Parameter>
              <Name>RefNrAcquiredImage9</Name>
              <Value>9</Value>
            </Parameter>
            <Parameter>
              <Name>RefNrAcquiredImage10</Name>
              <Value>10</Value>
            </Parameter>
            <Parameter>
              <Name>RefNrAcquiredImage11</Name>
              <Value>11</Value>
            </Parameter>
            <Parameter>
              <Name>RefNrAcquiredImage12</Name>
              <Value>12</Value>
            </Parameter>
            <Parameter>
              <Name>RefNrAcquiredImage13</Name>
              <Value>13</Value>
            </Parameter>
            <Parameter>
              <Name>RefNrAcquiredImage14</Name>
              <Value>14</Value>
            </Parameter>
            <Parameter>
              <Name>RefNrAcquiredImage15</Name>
              <Value>15</Value>
            </Parameter>
            <Parameter>
              <Name>RefNrAcquiredImage16</Name>
              <Value>16</Value>
            </Parameter>
            <Parameter>
              <Name>NrOfImagesZS</Name>
              <Value>2</Value>
            </Parameter>
            <Parameter>
              <Name>ZSCriticality</Name>
              <Value>1</Value>
            </Parameter>
            <Parameter>
              <Name>RefNrZStackedImage</Name>
              <Value>17</Value>
            </Parameter>
            <Parameter>
              <Name>RefNrImageToTransfer</Name>
              <Value>17</Value>
            </Parameter>
            <Parameter>
              <Name>DTCriticality</Name>
              <Value>0</Value>
            </Parameter>
            <Parameter>
              <Name>ZSTACK</Name>
              <Value>1</Value>
            </Parameter>
            <Parameter>
              <Name>DATAT</Name>
              <Value>1</Value>
            </Parameter>
          </List_of_Parameters>
        </RVR_Activity>
""",
    "Deliver_Sample" : """        <RVR_Activity>
          <ID>Deliver_Sample</ID>
          <Activity_No />
          <Activity_Name>Deliver_Sample</Activity_Name>
          <Activity_Type>EXEC</Activity_Type>
          <List_of_Parameters count="0" />
        </RVR_Activity>
""",
}


def generate_request_str(activities: List[str]) -> str:
    this_start = start.replace('count="9"', f'count="{len(activities)}"')
    this_activities = map(all_activities.get, activities)

    request = "".join((this_start, *this_activities, end))
    return request

# final_str_list = [start, *activities.values(), end]


# curr_dir = os.path.dirname(os.path.abspath(__file__))
# models_dir = os.path.join(curr_dir, 'models')

# "".join(final_str_list)
# request_filename = os.path.join(models_dir, 'request2.xml')
# with open(request_filename, "w") as f:
#     f.write("".join(final_str_list))
