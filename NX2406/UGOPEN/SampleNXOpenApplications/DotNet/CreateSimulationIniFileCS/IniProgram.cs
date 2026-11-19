/*
 ==============================================================================

      Copyright (c) 2018  Siemens Product Lifecycle Management Software Inc.
                         All rights reserved

 ==============================================================================
 ******************************************************************************
  Description
    Class that provides sample implementation to create a to_ini file

 */
using System;
using NXOpen;
using NXOpen.UF;
using System.Collections;
using System.Linq;
using System.Collections.Generic;
using System.IO;
using System.Globalization;

public class IniProgram
{
    // class members
    private static Session theSession;
    private static UI theUI;
    private static UFSession theUfSession;
    public static IniProgram theProgram;
    public static bool isDisposeCalled;
    private static List<External_to_ini.GeometryObject> myMcsObjects = new List<External_to_ini.GeometryObject>();
    private static List<External_to_ini.ToolObject> myToolObjects = new List<External_to_ini.ToolObject>();
    private static ArrayList MissedTools = new ArrayList();
    private static ArrayList usedToolNumbers = new ArrayList();
    private static List<External_to_ini.AssemblyToolInfo> AssemblyToolObjects = new List<External_to_ini.AssemblyToolInfo>();
    //------------------------------------------------------------------------------
    // Constructor
    //------------------------------------------------------------------------------
    public IniProgram()
    {
        try
        {
            theSession = Session.GetSession();
            theUI = UI.GetUI();
            theUfSession = UFSession.GetUFSession();
            isDisposeCalled = false;
        }
        catch (NXOpen.NXException ex)
        {
            // ---- Enter your exception handling code here -----
            UI.GetUI().NXMessageBox.Show("Message", NXMessageBox.DialogType.Error, ex.InnerException.ToString());
        }
    }

    //------------------------------------------------------------------------------
    //  Explicit Activation
    //      This entry point is used to activate the application explicitly
    //------------------------------------------------------------------------------
    public static int Main(string[] args)
    {
        int retValue = 0;
        try
        {
            theProgram = new IniProgram();
            
            theUfSession.Ui.SetPrompt("Initializing Tools");
            theUfSession.Ui.SetStatus("Processing Tools");

            theUfSession.Disp.SetDisplay(NXOpen.UF.UFConstants.UF_DISP_SUPPRESS_DISPLAY);
            //GetAllMCS
            GetMCSObjects();

            //
            GetAssemblyToolsFromDir();

            //GetAllTools
            GetToolObjects();

            //Write File
            WriteIniFile();

            theUfSession.Disp.SetDisplay(NXOpen.UF.UFConstants.UF_DISP_UNSUPPRESS_DISPLAY);
            theUfSession.Disp.RegenerateDisplay();

            //Warning if something missing
            string message = string.Empty;
            if (MissedTools.Count > 0)
            {

                foreach (string item in MissedTools)
                {
                    message = message + item.ToString() + Environment.NewLine;
                }
                theUI.NXMessageBox.Show("No definition", NXMessageBox.DialogType.Warning, "Following tooldata were not generated in to_ini-file: " + Environment.NewLine + message);
            }
            theUfSession.Ui.SetStatus("Processing Tools Completed");

            theProgram.Dispose();
        }
        catch (NXOpen.NXException ex)
        {
            // ---- Enter your exception handling code here -----
            theUI.NXMessageBox.Show("testc", NXMessageBox.DialogType.Information, ex.InnerException.ToString());
        }
        return retValue;
    }

    //------------------------------------------------------------------------------
    // Following method disposes all the class members
    //------------------------------------------------------------------------------
    public void Dispose()
    {
        try
        {
            if (isDisposeCalled == false)
            {
                //TODO: Add your application code here 
            }
            isDisposeCalled = true;
        }
        catch (NXOpen.NXException ex)
        {
            // ---- Enter your exception handling code here -----

        }
    }

    public static int GetUnloadOption(string arg)
    {
        //Unloads the image explicitly, via an unload dialog
        //return System.Convert.ToInt32(Session.LibraryUnloadOption.Explicitly);

        //Unloads the image immediately after execution within NX
        return System.Convert.ToInt32(Session.LibraryUnloadOption.Immediately);

        //Unloads the image when the NX session terminates
        // return System.Convert.ToInt32(Session.LibraryUnloadOption.AtTermination);
    }

    public static void GetMCSObjects()
    {
        NXOpen.Tag workPart_Tag = NXOpen.Tag.Null;
        NXOpen.Tag obj_tag = NXOpen.Tag.Null;
        NXOpen.CAM.OrientGeometry orientGeometry2;
        int cycle_target_geomgrp = NXOpen.UF.UFConstants.UF_machining_geometry_grp_type;
        int _type = NXOpen.UF.UFConstants.UF_machining_geometry_grp_type;
        int _subtype = NXOpen.UF.UFConstants.UF_machining_geom_type;
        string name;
        int i = cycle_target_geomgrp;

        workPart_Tag = theSession.Parts.Work.Tag;
        NXOpen.Part workPart = theSession.Parts.Work;
        theUfSession.Obj.CycleObjsInPart(workPart_Tag, cycle_target_geomgrp, ref obj_tag);



        while (obj_tag != NXOpen.Tag.Null)
        {
            theUfSession.Obj.CycleObjsInPart(workPart_Tag, i, ref obj_tag);
            if (obj_tag != NXOpen.Tag.Null)
            {
                theUfSession.Obj.AskTypeAndSubtype(obj_tag, out _type, out _subtype);
                if (_subtype == 60 | _subtype == 30 | _subtype == 120)   //...UGOPEN\uf_object_types.h"
                {
                    theUfSession.Obj.AskName(obj_tag, out name);
                    try
                    {
                        orientGeometry2 = (NXOpen.CAM.OrientGeometry)workPart.CAMSetup.CAMGroupCollection.FindObject(name);
                    }
                    catch
                    {
                        continue;
                    }
                    NXOpen.CAM.MillOrientGeomBuilder millOrientGeomBuilder2;
                    millOrientGeomBuilder2 = workPart.CAMSetup.CAMGroupCollection.CreateMillOrientGeomBuilder(orientGeometry2);

                    External_to_ini.GeometryObject McsObject = new External_to_ini.GeometryObject();
                    McsObject.m_FixtureOffset = millOrientGeomBuilder2.FixtureOffsetBuilder.Value;
                    McsObject.m_PurposeMode = millOrientGeomBuilder2.GetCsysPurposeMode().ToString();
                    McsObject.m_SpecialOutputMode = millOrientGeomBuilder2.GetSpecialOutputMode().ToString();
                    McsObject.m_X = millOrientGeomBuilder2.Mcs.Origin.X;
                    McsObject.m_Y = millOrientGeomBuilder2.Mcs.Origin.Y;
                    McsObject.m_Z = millOrientGeomBuilder2.Mcs.Origin.Z;
                    myMcsObjects.Add(McsObject);
                }
            }
        }

    }

    public static void GetAssemblyToolsFromDir()
    {
        External_to_ini.AssemblyToolInfo AssemblyToolObj;
        string ToolLibraryGraphicsPath = theSession.GetEnvironmentVariableValue("UGII_CAM_LIBRARY_TOOL_GRAPHICS_PATH");

        string[] FilesRoot = Directory.GetFiles(ToolLibraryGraphicsPath);
        string[] DirectoryFiles = Directory.GetDirectories(ToolLibraryGraphicsPath);

        foreach (var File in FilesRoot)
        {
            FileInfo AddFile = new FileInfo(File);
            AssemblyToolObj = new External_to_ini.AssemblyToolInfo();
            AssemblyToolObj.m_FullPathName = AddFile.FullName;
            AssemblyToolObj.m_Filename = AddFile.Name;
            AssemblyToolObj.m_Toolname = AddFile.Name.Replace(".prt", "");
            AssemblyToolObjects.Add(AssemblyToolObj);
        }
        foreach (var DirName in DirectoryFiles)
        {
            DirectoryInfo AddFile = new DirectoryInfo(DirName);

            string AddFileToList = DirName + @"\" + AddFile.Name + ".prt";
            if (File.Exists(AddFileToList))
            {
                FileInfo AddFileFolder = new FileInfo(AddFileToList);
                AssemblyToolObj = new External_to_ini.AssemblyToolInfo();
                AssemblyToolObj.m_FullPathName = AddFileFolder.FullName;
                AssemblyToolObj.m_Filename = AddFileFolder.Name;
                AssemblyToolObj.m_Toolname = AddFileFolder.Name.Replace(".prt", "");
                AssemblyToolObjects.Add(AssemblyToolObj);
            }
        }
    }

    public static void GetToolObjects()
    {


        NXOpen.Tag workPart_Tag = NXOpen.Tag.Null;
        NXOpen.Tag obj_tag = NXOpen.Tag.Null;

        //test cycle objects
        int cycle_target_tools = NXOpen.UF.UFConstants.UF_machining_tool_type;
        int _type = NXOpen.UF.UFConstants.UF_machining_tool_type;
        int _subtype = NXOpen.UF.UFConstants.UF_machining_geom_type;
        int i = cycle_target_tools;
        string name;
        NXOpen.CAM.Tool ToolInformation;
        workPart_Tag = theSession.Parts.Work.Tag;
        NXOpen.Part workPart = theSession.Parts.Work;
        theUfSession.Obj.CycleObjsInPart(workPart_Tag, cycle_target_tools, ref obj_tag);



        while (obj_tag != NXOpen.Tag.Null)
        {
            theUfSession.Obj.AskTypeAndSubtype(obj_tag, out _type, out _subtype);
            if (_subtype == 0 || _subtype == 1 || _subtype == 2)   //for overview "...NX_DIR\UGOPEN\uf_object_types.h" 0=Mill/Turn/Probing/WEDM 1=Unused 2=Tool assembly
            {
                try
                {
                    theUfSession.Obj.AskName(obj_tag, out name);
                    ToolInformation = (NXOpen.CAM.Tool)workPart.CAMSetup.CAMGroupCollection.FindObject(name);
                }
                catch
                {
                    theUfSession.Obj.CycleObjsInPart(workPart_Tag, i, ref obj_tag);
                    continue;
                }

                theUfSession.Ui.SetStatus("Get data from: " + ToolInformation);
                External_to_ini.ToolObject ToolObject;
                bool AssemblyTool = false;
                External_to_ini.AssemblyToolInfo matchedTool = AssemblyToolObjects.FirstOrDefault(item => item.m_Toolname.ToUpper() == ToolInformation.Name);
                if (matchedTool != null)
                {
                    AssemblyTool = true;
                }
                GetToolInfo(ToolInformation, AssemblyTool, matchedTool, out ToolObject);
                myToolObjects.Add(ToolObject);
            }

            theUfSession.Obj.CycleObjsInPart(workPart_Tag, i, ref obj_tag);
        }
    }

    private static void GetToolInfo(NXOpen.CAM.Tool mytool, bool AssemblyTool, External_to_ini.AssemblyToolInfo matchedTool, out External_to_ini.ToolObject Toolobject)
    {
        int ToolType;
        int ToolSubtype;

        theUfSession.Cutter.AskTypeAndSubtype(mytool.Tag, out ToolType, out ToolSubtype);
        NXOpen.Part workPart = theSession.Parts.Work;

        Toolobject = new External_to_ini.ToolObject();

        switch (ToolType)
        {
            #region UF_CUTTER_TYPE_MILL
            case 1:
                //UF_CUTTER_TYPE_MILL
                GetMillToolData(mytool, workPart, AssemblyTool, matchedTool, out Toolobject);
                break;
            #endregion

            case 2:
                //UF_CUTTER_TYPE_DRILL
                GetDrillToolData(mytool, workPart, AssemblyTool, out Toolobject);
                break;

            case 3:
                //UF_CUTTER_TYPE_TURN
                GetTurningToolData(mytool, workPart, AssemblyTool, matchedTool, out Toolobject);
                break;
            case 4:
                //UF_CUTTER_TYPE_GROOVE
                GetGrooveTurningToolData(mytool, workPart, AssemblyTool, matchedTool, out Toolobject);
                break;
            case 5:
                //UF_CUTTER_TYPE_THREAD Turning
                GetThreadTurningToolData(mytool, workPart, AssemblyTool, matchedTool, out Toolobject);
                break;
            case 7:
                //UF_CUTTER_TYPE_BARREL
                MissedTools.Add(mytool.Name + " Type:7");
                break;
            case 8:
                ////UF_CUTTER_TYPE_T
                GetDrillToolData(mytool, workPart, AssemblyTool, out Toolobject);
                break;
            case 9:
                //UF_CUTTER_TYPE_FORM
                MissedTools.Add(mytool.Name + " Type:9");
                break;
            case 11:
                //UF_CUTTER_TYPE_SOLID
                MissedTools.Add(mytool.Name + " Type:11");
                break;
            case 12:
                //UF_CUTTER_TYPE_LASER
                MissedTools.Add(mytool.Name + " Type:12");
                break;
            default:
                MissedTools.Add(mytool.Name + ": Missing Tooltype " + ToolType + " in general.");

                break;

        }
    }


    private static void MapTrackingPoint(int InternalId,out int MappedTpValue)
    {
        switch (InternalId)
        {
            case 0:
                MappedTpValue = 0;
                return; 
            case 1:
                MappedTpValue = 4;
                return;
            case 2:
                MappedTpValue = 3;
                return;
            case 3:
                MappedTpValue = 2;
                return;
            case 4:
                MappedTpValue = 1;
                return;
            case 5:
                MappedTpValue = 5;
                return;
            case 6:
                MappedTpValue = 8;
                return;
            case 7:
                MappedTpValue = 7;
                return;
            case 8:
                MappedTpValue = 6;
                return;
            case 9:
                MappedTpValue = 9;
                return;
            default:
                MappedTpValue = 0;
                return;

        }



    }
    private static void WriteIniFile()
    {
        //Debugger.Launch();
        NXOpen.Part workPart = theSession.Parts.Work;
        string FullPath = workPart.FullPath;
        string IniFileDir = FullPath.Replace(workPart.Name + ".prt", "") + @"cse_files\subprog\";
        ArrayList usedMCS = new ArrayList();


        if (!Directory.Exists(IniFileDir))
        {
            Directory.CreateDirectory(IniFileDir);
        }

        NumberFormatInfo NbFormat = new NumberFormatInfo();
        NbFormat.NumberDecimalSeparator = ".";
        NbFormat.NumberDecimalDigits = 3;
        //Set
        StreamWriter WriteIni = new StreamWriter(IniFileDir + "to_ini.ini", false);

        //Get Main MCS
        External_to_ini.GeometryObject MainMCS = new External_to_ini.GeometryObject();
        foreach (External_to_ini.GeometryObject GeomMCS in myMcsObjects)
        {
            if (GeomMCS.m_PurposeMode == "Main")
            {
                WriteIni.WriteLine("$P_UIFR[0]=CTRANS(X,0.0,Y,0.0,Z,0.0)");
                MainMCS = GeomMCS;
            }
        }

        //Write Zero Offsets
        foreach (External_to_ini.GeometryObject GeomMCS in myMcsObjects)
        {
            if (GeomMCS.m_PurposeMode != "Main")
            {
                double X_value = GeomMCS.m_X - MainMCS.m_X;
                double Y_value = GeomMCS.m_Y - MainMCS.m_Y;
                double Z_value = GeomMCS.m_Z - MainMCS.m_Z;

                if (!usedMCS.Contains(GeomMCS.m_FixtureOffset))
                {
                    WriteIni.WriteLine("$P_UIFR[" + GeomMCS.m_FixtureOffset + "]=CTRANS(X," + X_value.ToString("N6", NbFormat) + ",Y," + Y_value.ToString("N6", NbFormat) + ",Z," + Z_value.ToString("N6", NbFormat) + ")");
                    usedMCS.Add(GeomMCS.m_FixtureOffset);
                }
            }
        }

        WriteIni.WriteLine();
        //Write Tooldata
        int iCounter = 1;
        foreach (External_to_ini.ToolObject ToolToIni in myToolObjects)
        {
            //check for duplicate Toolnumbers
            bool matchedTool = usedToolNumbers.Contains(ToolToIni.m_ToolNumber);
            if (matchedTool == true)
            {
                MissedTools.Add(ToolToIni.m_ToolName + ": Toolnumber " + ToolToIni.m_ToolNumber + "is already used. Tooldata will not be output to to_ini file.");
                continue;
            }
            WriteIni.WriteLine("$TC_TP1[" + iCounter + "]=" + ToolToIni.m_ToolNumber);
            WriteIni.WriteLine("$TC_TP2[" + iCounter + "]=\"" + ToolToIni.m_ToolName + "\"");
            WriteIni.WriteLine("$TC_TP7[" + iCounter + "]=1");
            WriteIni.WriteLine("$TC_TP8[" + iCounter + "]=" + ToolToIni.m_ToolStatus);

            foreach (External_to_ini.ToolTrackingPoint iTrackpoint in ToolToIni.m_ListTrackingPoints)
            {
                WriteIni.WriteLine("$TC_DP1[" + iCounter + "," + iTrackpoint.m_TpToolAdjustRegister + "]=" + iTrackpoint.m_TpToolType);
                if (ToolToIni.m_ToolType >= 500 && ToolToIni.m_ToolType <= 599)
                {
                    WriteIni.WriteLine("$TC_DP2[" + iCounter + "," + iTrackpoint.m_TpToolAdjustRegister + "]=" + iTrackpoint.m_TpToolFluteLength.ToString("N0", NbFormat));
                }
                else
                {
                    WriteIni.WriteLine("$TC_DP2[" + iCounter + "," + iTrackpoint.m_TpToolAdjustRegister + "]=" + iTrackpoint.m_TpToolFluteLength.ToString("N6", NbFormat));
                }
                WriteIni.WriteLine("$TC_DP3[" + iCounter + "," + iTrackpoint.m_TpToolAdjustRegister + "]=" + iTrackpoint.m_TpToolCorrectionX.ToString("N6", NbFormat));
                WriteIni.WriteLine("$TC_DP4[" + iCounter + "," + iTrackpoint.m_TpToolAdjustRegister + "]=" + iTrackpoint.m_TpToolCorrectionY.ToString("N6", NbFormat));
                WriteIni.WriteLine("$TC_DP5[" + iCounter + "," + iTrackpoint.m_TpToolAdjustRegister + "]=" + iTrackpoint.m_TpToolCorrectionZ.ToString("N6", NbFormat));
                WriteIni.WriteLine("$TC_DP6[" + iCounter + "," + iTrackpoint.m_TpToolAdjustRegister + "]=" + iTrackpoint.m_TpToolRadius.ToString("N6", NbFormat));
                WriteIni.WriteLine("$TC_DP7[" + iCounter + "," + iTrackpoint.m_TpToolAdjustRegister + "]=" + iTrackpoint.m_TpToolCutterRadius.ToString("N6", NbFormat));
            }
            WriteIni.WriteLine("$TC_MPP6[" + iCounter + "," + ToolToIni.m_ToolNumber + "]=" + iCounter);
            WriteIni.WriteLine(Environment.NewLine);
            iCounter++;

            //Add Toolnumber to list
            usedToolNumbers.Add(ToolToIni.m_ToolNumber);
        }
        WriteIni.WriteLine("M17");
        WriteIni.WriteLine(Environment.NewLine);
        WriteIni.Close();
    }

    private static void GetMillToolData(NXOpen.CAM.Tool mytool, NXOpen.Part workPart, bool AssemblyTool, External_to_ini.AssemblyToolInfo matchedTool, out External_to_ini.ToolObject Toolobject)
    {
        double AssemblyToolLengthX = 0;
        double AssemblyToolLengthY = 0;

        Toolobject = new External_to_ini.ToolObject();
        External_to_ini.ToolTrackingPoint AddTrackingPoint;

        NXOpen.CAM.MillToolBuilder millToolBuilder1;
        millToolBuilder1 = workPart.CAMSetup.CAMGroupCollection.CreateMillToolBuilder(mytool);

        #region GetDataFromAssemblyTool
        if (AssemblyTool == true)
        {
            try
            {
                bool ToolTipFound = false;
                bool ToolMountFound = false;
                NXOpen.Point3d ToolTipPoint = new Point3d();
                NXOpen.Point3d ToolMountPoint = new Point3d();

                //GetJunction if a static holder is used
                NXOpen.SIM.KinematicConfigurator kinematicConfiguratorAssemblyTools;
                kinematicConfiguratorAssemblyTools = workPart.KinematicConfigurator;


                NXOpen.SIM.KinematicComponent kinematicComponentTool;
                kinematicComponentTool = kinematicConfiguratorAssemblyTools.ComponentCollection.FindObject(mytool.Name);

                NXOpen.SIM.KinematicJunction[] ComponentJct;
                kinematicComponentTool.GetJunctions(out ComponentJct);

                foreach (NXOpen.SIM.KinematicJunction jct in ComponentJct)
                {
                    NXOpen.SIM.KinematicJunctionBuilder jctbuilder;
                    jctbuilder = kinematicConfiguratorAssemblyTools.CreateJunctionBuilder(kinematicComponentTool, jct);


                    if (jctbuilder.IsToolTip())
                    {
                        NXOpen.CartesianCoordinateSystem cartesianCoordinateSystemToolTip;
                        cartesianCoordinateSystemToolTip = jctbuilder.Csys;
                        ToolTipPoint = cartesianCoordinateSystemToolTip.Origin;
                        ToolTipFound = true;
                    }
                    if (jctbuilder.IsToolMount())
                    {
                        NXOpen.CartesianCoordinateSystem cartesianCoordinateSystemToolMount;
                        cartesianCoordinateSystemToolMount = jctbuilder.Csys;
                        ToolMountPoint = cartesianCoordinateSystemToolMount.Origin;
                        ToolMountFound = true;
                    }
                    jctbuilder.Destroy();
                }

                if (ToolTipFound == true && ToolMountFound == true)
                {
                    AssemblyToolLengthX = ToolMountPoint.X - ToolTipPoint.X;
                    AssemblyToolLengthY = ToolMountPoint.Y - ToolTipPoint.Y;
                }
            }
            catch (Exception ex)
            {
                //Tool is not placed in a static_Holder, try to get kinematics from part file
                if (matchedTool != null)
                {
                    NXOpen.Tag KinToolTag = NXOpen.Tag.Null;
                    NXOpen.Tag origin_workpart_tag = workPart.Tag;
                    try
                    {
                        UFPart.LoadStatus errorStatus;


                        theUfSession.Part.OpenQuiet(matchedTool.m_FullPathName, out KinToolTag, out errorStatus);

                        theUfSession.Part.SetDisplayPart(KinToolTag);

                        // theSession.Parts.OpenDisplay(matchedTool.m_FullPathName, out loadstatus);
                        NXOpen.Part KinToolPart = (NXOpen.Part)theSession.Parts.FindObject(matchedTool.m_Filename);

                        //NXOpen.BasePart myBase = KinToolPart;
                        //theSession.Parts.SetActiveDisplay(myBase, DisplayPartOption.AllowAdditional, PartDisplayPartWorkPartOption.SameAsDisplay, out loadstatus);
                        //NXOpen.Part KinToolPart = (NXOpen.Part)NXOpen.Utilities.NXObjectManager.Get(KinToolTag);
                        //NXOpen.Part KinToolPart = theSession.Parts.Open(matchedTool.m_FullPathName, out loadstatus);



                        //theSession.Parts.SetWork(KinToolPart);

                        NXOpen.SIM.KinematicConfigurator kinematicConfiguratorAssemblyTools;
                        kinematicConfiguratorAssemblyTools = KinToolPart.KinematicConfigurator;
                        NXOpen.SIM.KinematicJunction[] KimJunctions;
                        kinematicConfiguratorAssemblyTools.GetJunctions(out KimJunctions);


                        NXOpen.SIM.KinematicComponentCollection CollectedComponents = kinematicConfiguratorAssemblyTools.ComponentCollection;
                        bool ToolTipFound = false;
                        bool ToolMountFound = false;
                        NXOpen.Point3d ToolTipPoint = new Point3d();
                        NXOpen.Point3d ToolMountPoint = new Point3d();

                        foreach (NXOpen.SIM.KinematicComponent component in CollectedComponents)
                        {
                            NXOpen.SIM.KinematicJunction[] ComponentJct;
                            component.GetJunctions(out ComponentJct);

                            foreach (NXOpen.SIM.KinematicJunction jct in ComponentJct)
                            {
                                NXOpen.SIM.KinematicJunctionBuilder jctbuilder;
                                jctbuilder = kinematicConfiguratorAssemblyTools.CreateJunctionBuilder(component, jct);


                                if (jctbuilder.IsToolTip())
                                {
                                    NXOpen.CartesianCoordinateSystem cartesianCoordinateSystemToolTip;
                                    cartesianCoordinateSystemToolTip = jctbuilder.Csys;
                                    ToolTipPoint = cartesianCoordinateSystemToolTip.Origin;
                                    ToolTipFound = true;
                                }
                                if (jctbuilder.IsToolMount())
                                {
                                    NXOpen.CartesianCoordinateSystem cartesianCoordinateSystemToolMount;
                                    cartesianCoordinateSystemToolMount = jctbuilder.Csys;
                                    ToolMountPoint = cartesianCoordinateSystemToolMount.Origin;
                                    ToolMountFound = true;
                                }
                                jctbuilder.Destroy();
                            }

                            if (ToolTipFound == true && ToolMountFound == true)
                            {
                                AssemblyToolLengthX = ToolMountPoint.X - ToolTipPoint.X;
                                AssemblyToolLengthY = ToolMountPoint.Y - ToolTipPoint.Y;
                                break;
                            }

                        }

                    }
                    catch (Exception ex2)
                    {

                    }
                    finally
                    {
                        theUfSession.Part.SetDisplayPart(origin_workpart_tag);
                        theUfSession.Part.Close(KinToolTag, 0, 1);
                    }
                }

            }
        }
        #endregion

        Toolobject.m_ToolNumber = millToolBuilder1.TlNumberBuilder.Value;
        Toolobject.m_ToolName = mytool.Name;
        Toolobject.m_ToolStatus = 10;
        Toolobject.m_TrackingPoints = millToolBuilder1.MillingTrackpointBuilder.NumberOfTrackPoints;
        Toolobject.m_ToolLength = millToolBuilder1.TlHeightBuilder.Value;

        if (millToolBuilder1.TlLowCorRadBuilder.Value > 0)
        {
            Toolobject.m_ToolType = 121;
            Toolobject.m_ToolCutterRadius = millToolBuilder1.TlLowCorRadBuilder.Value;
        }
        else
        {
            Toolobject.m_ToolType = 120;
            Toolobject.m_ToolCutterRadius = 0;
        }



        int sections = millToolBuilder1.HolderSectionBuilder.NumberOfSections;
        double HolderLength = 0;
        if (sections > 0)
        {

            for (int i = 0; i < sections; i++)
            {
                double Diameter, Length, TaperAngle, CornerRadius;
                NXObject HolderSection = millToolBuilder1.HolderSectionBuilder.GetSection(i);
                millToolBuilder1.HolderSectionBuilder.Get(HolderSection, out Diameter, out Length, out TaperAngle, out CornerRadius);
                HolderLength = HolderLength + Length;
            }
        }


        if (Toolobject.m_TrackingPoints == 0)
        {
            AddTrackingPoint = new External_to_ini.ToolTrackingPoint();
            AddTrackingPoint.m_TpToolAdjustRegister = millToolBuilder1.TlAdjRegBuilder.Value;
            AddTrackingPoint.m_TpToolType = Toolobject.m_ToolType;
            AddTrackingPoint.m_TpToolFluteLength = millToolBuilder1.TlFluteLnBuilder.Value;
            if (AssemblyTool == true && AssemblyToolLengthX != 0)
            {
                AddTrackingPoint.m_TpToolCorrectionX = AssemblyToolLengthX;
            }
            else
            {
                AddTrackingPoint.m_TpToolCorrectionX = millToolBuilder1.TlHeightBuilder.Value + HolderLength;
            }
            AddTrackingPoint.m_TpToolCorrectionY = 0;
            AddTrackingPoint.m_TpToolCorrectionZ = 0;
            AddTrackingPoint.m_TpToolRadius = millToolBuilder1.TlDiameterBuilder.Value / 2;
            AddTrackingPoint.m_TpToolCutterRadius = Toolobject.m_ToolCutterRadius;
            Toolobject.m_ListTrackingPoints.Add(AddTrackingPoint);
        }
        else
        {
            for (int iTrackingpoint = 0; iTrackingpoint < Toolobject.m_TrackingPoints; iTrackingpoint++)
            {
                NXObject SingleTrackpoint = millToolBuilder1.MillingTrackpointBuilder.GetTrackPoint(iTrackingpoint);
                string TpName;
                double TpDiameter, TpDistance, TpZOffset;
                int TpZOffsetIsUsed, TpAdjustReg, TpAdjustIsUsed, TpCustcom, TpCutcomIsUsed;

                millToolBuilder1.MillingTrackpointBuilder.Get(SingleTrackpoint, out TpName, out TpDiameter, out TpDistance, out TpZOffset, out TpZOffsetIsUsed, out TpAdjustReg, out TpAdjustIsUsed, out TpCustcom, out TpCutcomIsUsed);
                AddTrackingPoint = new External_to_ini.ToolTrackingPoint();
                if (TpAdjustIsUsed == 1)
                {
                    AddTrackingPoint.m_TpToolAdjustRegister = TpAdjustReg;
                }
                else
                {
                    AddTrackingPoint.m_TpToolAdjustRegister = millToolBuilder1.TlAdjRegBuilder.Value;
                }
                AddTrackingPoint.m_TpToolType = Toolobject.m_ToolType;
                AddTrackingPoint.m_TpToolFluteLength = millToolBuilder1.TlFluteLnBuilder.Value;


                if (TpAdjustIsUsed == 1)
                {
                    AddTrackingPoint.m_TpToolCorrectionX = millToolBuilder1.TlHeightBuilder.Value + HolderLength - TpDistance;
                }
                else
                {
                    AddTrackingPoint.m_TpToolCorrectionX = millToolBuilder1.TlHeightBuilder.Value + HolderLength;
                }
                AddTrackingPoint.m_TpToolCorrectionY = 0;
                AddTrackingPoint.m_TpToolCorrectionZ = 0;
                AddTrackingPoint.m_TpToolRadius = millToolBuilder1.TlDiameterBuilder.Value / 2;
                AddTrackingPoint.m_TpToolCutterRadius = Toolobject.m_ToolCutterRadius;
                Toolobject.m_ListTrackingPoints.Add(AddTrackingPoint);
            }
        }
        millToolBuilder1.Destroy();
    }
    private static void GetDrillToolData(NXOpen.CAM.Tool mytool, NXOpen.Part workPart, bool AssemblyTool, out External_to_ini.ToolObject Toolobject)
    {
        double AssemblyToolLength = 0;

        Toolobject = new External_to_ini.ToolObject();
        External_to_ini.ToolTrackingPoint AddTrackingPoint;

        NXOpen.CAM.DrillToolBuilder drillToolBuilder;
        drillToolBuilder = workPart.CAMSetup.CAMGroupCollection.CreateDrillStdToolBuilder(mytool);
        Toolobject.m_ToolNumber = drillToolBuilder.TlNumberBuilder.Value;
        Toolobject.m_ToolName = mytool.Name;
        Toolobject.m_ToolStatus = 10;
        Toolobject.m_TrackingPoints = drillToolBuilder.MillingTrackpointBuilder.NumberOfTrackPoints;
        Toolobject.m_ToolType = 200;
        int sections = drillToolBuilder.HolderSectionBuilder.NumberOfSections;
        double HolderLength = 0;
        if (sections > 0)
        {

            for (int i = 0; i < sections; i++)
            {
                double Diameter, Length, TaperAngle, CornerRadius;
                NXObject HolderSection = drillToolBuilder.HolderSectionBuilder.GetSection(i);
                drillToolBuilder.HolderSectionBuilder.Get(HolderSection, out Diameter, out Length, out TaperAngle, out CornerRadius);
                HolderLength = HolderLength + Length;
            }
        }
        //Store one ore multiple Trackingpoints


        if (Toolobject.m_TrackingPoints == 0)
        {
            AddTrackingPoint = new External_to_ini.ToolTrackingPoint();
            AddTrackingPoint.m_TpToolAdjustRegister = drillToolBuilder.TlAdjRegBuilder.Value;
            AddTrackingPoint.m_TpToolType = Toolobject.m_ToolType;
            AddTrackingPoint.m_TpToolFluteLength = drillToolBuilder.TlFluteLnBuilder.Value;
            if (AssemblyTool == true && AssemblyToolLength != 0)
            {
                AddTrackingPoint.m_TpToolCorrectionX = AssemblyToolLength;
            }
            else
            {
                AddTrackingPoint.m_TpToolCorrectionX = drillToolBuilder.TlHeightBuilder.Value + HolderLength;
            }
            AddTrackingPoint.m_TpToolCorrectionY = 0;
            AddTrackingPoint.m_TpToolCorrectionZ = 0;
            AddTrackingPoint.m_TpToolRadius = drillToolBuilder.TlDiameterBuilder.Value / 2;
            AddTrackingPoint.m_TpToolCutterRadius = Toolobject.m_ToolCutterRadius;
            Toolobject.m_ListTrackingPoints.Add(AddTrackingPoint);
        }
        else
        {
            for (int iTrackingpoint = 0; iTrackingpoint < Toolobject.m_TrackingPoints; iTrackingpoint++)
            {
                NXObject SingleTrackpoint = drillToolBuilder.MillingTrackpointBuilder.GetTrackPoint(iTrackingpoint);
                string TpName;
                double TpDiameter, TpDistance, TpZOffset;
                int TpZOffsetIsUsed, TpAdjustReg, TpAdjustIsUsed, TpCustcom, TpCutcomIsUsed;

                drillToolBuilder.MillingTrackpointBuilder.Get(SingleTrackpoint, out TpName, out TpDiameter, out TpDistance, out TpZOffset, out TpZOffsetIsUsed, out TpAdjustReg, out TpAdjustIsUsed, out TpCustcom, out TpCutcomIsUsed);
                AddTrackingPoint = new External_to_ini.ToolTrackingPoint();
                if (TpAdjustIsUsed == 1)
                {
                    AddTrackingPoint.m_TpToolAdjustRegister = TpAdjustReg;
                }
                else
                {
                    AddTrackingPoint.m_TpToolAdjustRegister = drillToolBuilder.TlAdjRegBuilder.Value;
                }
                AddTrackingPoint.m_TpToolType = Toolobject.m_ToolType;
                AddTrackingPoint.m_TpToolFluteLength = drillToolBuilder.TlFluteLnBuilder.Value;


                if (TpAdjustIsUsed == 1)
                {
                    AddTrackingPoint.m_TpToolCorrectionX = drillToolBuilder.TlHeightBuilder.Value + HolderLength - TpDistance;
                }
                else
                {
                    AddTrackingPoint.m_TpToolCorrectionX = drillToolBuilder.TlHeightBuilder.Value + HolderLength;
                }
                AddTrackingPoint.m_TpToolCorrectionY = 0;
                AddTrackingPoint.m_TpToolCorrectionZ = 0;
                AddTrackingPoint.m_TpToolRadius = drillToolBuilder.TlDiameterBuilder.Value / 2;
                AddTrackingPoint.m_TpToolCutterRadius = Toolobject.m_ToolCutterRadius;
                Toolobject.m_ListTrackingPoints.Add(AddTrackingPoint);
            }
        }


        drillToolBuilder.Destroy();
    }

    private static void GetTToolData(NXOpen.CAM.Tool mytool, NXOpen.Part workPart, bool AssemblyTool, out External_to_ini.ToolObject Toolobject)
    {
        double AssemblyToolLength = 0;

        Toolobject = new External_to_ini.ToolObject();
        External_to_ini.ToolTrackingPoint AddTrackingPoint;
        NXOpen.CAM.TToolBuilder tToolBuilder1;
        tToolBuilder1 = workPart.CAMSetup.CAMGroupCollection.CreateTToolBuilder(mytool);
        Toolobject.m_ToolNumber = tToolBuilder1.TlNumberBuilder.Value;
        Toolobject.m_ToolName = mytool.Name;
        Toolobject.m_ToolStatus = 10;
        Toolobject.m_TrackingPoints = tToolBuilder1.MillingTrackpointBuilder.NumberOfTrackPoints;
        Toolobject.m_ToolType = 200;
        int sections = tToolBuilder1.HolderSectionBuilder.NumberOfSections;
        double HolderLength = 0;
        if (sections > 0)
        {

            for (int i = 0; i < sections; i++)
            {
                double Diameter, Length, TaperAngle, CornerRadius;
                NXObject HolderSection = tToolBuilder1.HolderSectionBuilder.GetSection(i);
                tToolBuilder1.HolderSectionBuilder.Get(HolderSection, out Diameter, out Length, out TaperAngle, out CornerRadius);
                HolderLength = HolderLength + Length;
            }
        }
        //Store one ore multiple Trackingpoints


        if (Toolobject.m_TrackingPoints == 0)
        {
            AddTrackingPoint = new External_to_ini.ToolTrackingPoint();
            AddTrackingPoint.m_TpToolAdjustRegister = tToolBuilder1.TlAdjRegBuilder.Value;
            AddTrackingPoint.m_TpToolType = Toolobject.m_ToolType;
            AddTrackingPoint.m_TpToolFluteLength = tToolBuilder1.TlFluteLnBuilder.Value;
            if (AssemblyTool == true && AssemblyToolLength != 0)
            {
                AddTrackingPoint.m_TpToolCorrectionX = AssemblyToolLength;
            }
            else
            {
                AddTrackingPoint.m_TpToolCorrectionX = tToolBuilder1.TlHeightBuilder.Value + HolderLength;
            }
            AddTrackingPoint.m_TpToolCorrectionY = 0;
            AddTrackingPoint.m_TpToolCorrectionZ = 0;
            AddTrackingPoint.m_TpToolRadius = tToolBuilder1.TlDiameterBuilder.Value / 2;
            AddTrackingPoint.m_TpToolCutterRadius = Toolobject.m_ToolCutterRadius;
            Toolobject.m_ListTrackingPoints.Add(AddTrackingPoint);
        }
        else
        {
            for (int iTrackingpoint = 0; iTrackingpoint < Toolobject.m_TrackingPoints; iTrackingpoint++)
            {
                NXObject SingleTrackpoint = tToolBuilder1.MillingTrackpointBuilder.GetTrackPoint(iTrackingpoint);
                string TpName;
                double TpDiameter, TpDistance, TpZOffset;
                int TpZOffsetIsUsed, TpAdjustReg, TpAdjustIsUsed, TpCustcom, TpCutcomIsUsed;

                tToolBuilder1.MillingTrackpointBuilder.Get(SingleTrackpoint, out TpName, out TpDiameter, out TpDistance, out TpZOffset, out TpZOffsetIsUsed, out TpAdjustReg, out TpAdjustIsUsed, out TpCustcom, out TpCutcomIsUsed);
                AddTrackingPoint = new External_to_ini.ToolTrackingPoint();
                if (TpAdjustIsUsed == 1)
                {
                    AddTrackingPoint.m_TpToolAdjustRegister = TpAdjustReg;
                }
                else
                {
                    AddTrackingPoint.m_TpToolAdjustRegister = tToolBuilder1.TlAdjRegBuilder.Value;
                }
                AddTrackingPoint.m_TpToolType = Toolobject.m_ToolType;
                AddTrackingPoint.m_TpToolFluteLength = tToolBuilder1.TlFluteLnBuilder.Value;


                if (TpAdjustIsUsed == 1)
                {
                    AddTrackingPoint.m_TpToolCorrectionX = tToolBuilder1.TlHeightBuilder.Value + HolderLength - TpDistance;
                }
                else
                {
                    AddTrackingPoint.m_TpToolCorrectionX = tToolBuilder1.TlHeightBuilder.Value + HolderLength;
                }
                AddTrackingPoint.m_TpToolCorrectionY = 0;
                AddTrackingPoint.m_TpToolCorrectionZ = 0;
                AddTrackingPoint.m_TpToolRadius = tToolBuilder1.TlDiameterBuilder.Value / 2;
                AddTrackingPoint.m_TpToolCutterRadius = Toolobject.m_ToolCutterRadius;
                Toolobject.m_ListTrackingPoints.Add(AddTrackingPoint);
            }
        }
        tToolBuilder1.Destroy();
    }

    private static void GetTurningToolData(NXOpen.CAM.Tool mytool, NXOpen.Part workPart, bool AssemblyTool, External_to_ini.AssemblyToolInfo matchedTool, out External_to_ini.ToolObject Toolobject)
    {
        double AssemblyToolLengthX = 0;
        double AssemblyToolLengthY = 0;

        Toolobject = new External_to_ini.ToolObject();
        External_to_ini.ToolTrackingPoint AddTrackingPoint;

        NXOpen.CAM.TurningToolBuilder turningToolBuilder;
        turningToolBuilder = workPart.CAMSetup.CAMGroupCollection.CreateTurnToolBuilder(mytool);
        //Debugger.Launch();
        #region GetDataFromAssemblyTool
        if (AssemblyTool == true)
        {
            try
            {
                bool ToolTipFound = false;
                bool ToolMountFound = false;
                NXOpen.Point3d ToolTipPoint = new Point3d();
                NXOpen.Point3d ToolMountPoint = new Point3d();

                //GetJunction if a static holder is used
                NXOpen.SIM.KinematicConfigurator kinematicConfiguratorAssemblyTools;
                kinematicConfiguratorAssemblyTools = workPart.KinematicConfigurator;


                NXOpen.SIM.KinematicComponent kinematicComponentTool;
                kinematicComponentTool = kinematicConfiguratorAssemblyTools.ComponentCollection.FindObject(mytool.Name);

                NXOpen.SIM.KinematicJunction[] ComponentJct;
                kinematicComponentTool.GetJunctions(out ComponentJct);

                foreach (NXOpen.SIM.KinematicJunction jct in ComponentJct)
                {
                    NXOpen.SIM.KinematicJunctionBuilder jctbuilder;
                    jctbuilder = kinematicConfiguratorAssemblyTools.CreateJunctionBuilder(kinematicComponentTool, jct);


                    if (jctbuilder.IsToolTip())
                    {
                        NXOpen.CartesianCoordinateSystem cartesianCoordinateSystemToolTip;
                        cartesianCoordinateSystemToolTip = jctbuilder.Csys;
                        ToolTipPoint = cartesianCoordinateSystemToolTip.Origin;
                        ToolTipFound = true;
                    }
                    if (jctbuilder.IsToolMount())
                    {
                        NXOpen.CartesianCoordinateSystem cartesianCoordinateSystemToolMount;
                        cartesianCoordinateSystemToolMount = jctbuilder.Csys;
                        ToolMountPoint = cartesianCoordinateSystemToolMount.Origin;
                        ToolMountFound = true;
                    }
                    jctbuilder.Destroy();
                }

                if (ToolTipFound == true && ToolMountFound == true)
                {
                    AssemblyToolLengthX = ToolMountPoint.X - ToolTipPoint.X;
                    AssemblyToolLengthY = ToolMountPoint.Y - ToolTipPoint.Y;
                }
            }
            catch (Exception ex)
            {
                //Tool is not placed in a static_Holder, try to get kinematics from part file
                if (matchedTool != null)
                {
                    NXOpen.Tag KinToolTag = NXOpen.Tag.Null;
                    NXOpen.Tag origin_workpart_tag = workPart.Tag;
                    try
                    {
                        UFPart.LoadStatus errorStatus;


                        theUfSession.Part.OpenQuiet(matchedTool.m_FullPathName, out KinToolTag, out errorStatus);
                        
                        theUfSession.Part.SetDisplayPart(KinToolTag);

                        // theSession.Parts.OpenDisplay(matchedTool.m_FullPathName, out loadstatus);
                        NXOpen.Part KinToolPart = (NXOpen.Part)theSession.Parts.FindObject(matchedTool.m_Filename);

                        //NXOpen.BasePart myBase = KinToolPart;
                        //theSession.Parts.SetActiveDisplay(myBase, DisplayPartOption.AllowAdditional, PartDisplayPartWorkPartOption.SameAsDisplay, out loadstatus);
                        //NXOpen.Part KinToolPart = (NXOpen.Part)NXOpen.Utilities.NXObjectManager.Get(KinToolTag);
                        //NXOpen.Part KinToolPart = theSession.Parts.Open(matchedTool.m_FullPathName, out loadstatus);



                        //theSession.Parts.SetWork(KinToolPart);

                        NXOpen.SIM.KinematicConfigurator kinematicConfiguratorAssemblyTools;
                        kinematicConfiguratorAssemblyTools = KinToolPart.KinematicConfigurator;
                        NXOpen.SIM.KinematicJunction[] KimJunctions;
                        kinematicConfiguratorAssemblyTools.GetJunctions(out KimJunctions);


                        NXOpen.SIM.KinematicComponentCollection CollectedComponents = kinematicConfiguratorAssemblyTools.ComponentCollection;
                        bool ToolTipFound = false;
                        bool ToolMountFound = false;
                        NXOpen.Point3d ToolTipPoint = new Point3d();
                        NXOpen.Point3d ToolMountPoint = new Point3d();

                        foreach (NXOpen.SIM.KinematicComponent component in CollectedComponents)
                        {
                            NXOpen.SIM.KinematicJunction[] ComponentJct;
                            component.GetJunctions(out ComponentJct);

                            foreach (NXOpen.SIM.KinematicJunction jct in ComponentJct)
                            {
                                NXOpen.SIM.KinematicJunctionBuilder jctbuilder;
                                jctbuilder = kinematicConfiguratorAssemblyTools.CreateJunctionBuilder(component, jct);


                                if (jctbuilder.IsToolTip())
                                {
                                    NXOpen.CartesianCoordinateSystem cartesianCoordinateSystemToolTip;
                                    cartesianCoordinateSystemToolTip = jctbuilder.Csys;
                                    ToolTipPoint = cartesianCoordinateSystemToolTip.Origin;
                                    ToolTipFound = true;
                                }
                                if (jctbuilder.IsToolMount())
                                {
                                    NXOpen.CartesianCoordinateSystem cartesianCoordinateSystemToolMount;
                                    cartesianCoordinateSystemToolMount = jctbuilder.Csys;
                                    ToolMountPoint = cartesianCoordinateSystemToolMount.Origin;
                                    ToolMountFound = true;
                                }
                                jctbuilder.Destroy();
                            }

                            if (ToolTipFound == true && ToolMountFound == true)
                            {
                                AssemblyToolLengthX = ToolMountPoint.X - ToolTipPoint.X;
                                AssemblyToolLengthY = ToolMountPoint.Y - ToolTipPoint.Y;
                                break;
                            }

                        }

                    }
                    catch (Exception ex2)
                    {

                    }
                    finally
                    {
                        theUfSession.Part.SetDisplayPart(origin_workpart_tag);
                        theUfSession.Part.Close(KinToolTag, 0, 1);
                    }
                }

            }
        }
        #endregion

        NXObject toolTipJunction;
        int Trackingpoint, RadiusId;

        turningToolBuilder.ManageToolPartBuilder.AskToolTipJunction(out toolTipJunction, out Trackingpoint, out RadiusId);

        Toolobject.m_ToolNumber = turningToolBuilder.TlNumberBuilder.Value;
        Toolobject.m_ToolName = mytool.Name;
        Toolobject.m_ToolStatus = 10;
        Toolobject.m_ToolType = 500;
        Toolobject.m_TrackingPoints = turningToolBuilder.TrackingBuilder.NumberOfTrackPoints;

        for (int iTrackingpoint = 0; iTrackingpoint < Toolobject.m_TrackingPoints; iTrackingpoint++)
        {
            NXObject SingleTrackpoint = turningToolBuilder.TrackingBuilder.GetTrackPoint(iTrackingpoint);
            string TpName;
            double TpAngle, TpDistance, TpXOffset, TpYOffset, TpRadius;
            int TpRadiusId, TpAdjustReg, TpAdjustIsUsed, TpCustcom, TpNumber;

            turningToolBuilder.TrackingBuilder.Get(SingleTrackpoint, out TpName, out TpRadiusId, out TpNumber, out TpAngle, out TpRadius, out TpXOffset, out TpYOffset, out TpAdjustReg, out TpCustcom);
            AddTrackingPoint = new External_to_ini.ToolTrackingPoint();
            AddTrackingPoint.m_TpToolAdjustRegister = TpAdjustReg;
            AddTrackingPoint.m_TpToolType = Toolobject.m_ToolType;
            AddTrackingPoint.m_TpToolFluteLength = TpNumber;

            if (AssemblyTool == true && AssemblyToolLengthX != 0)
            {
                AddTrackingPoint.m_TpToolCorrectionX = AssemblyToolLengthX;
                AddTrackingPoint.m_TpToolCorrectionY = AssemblyToolLengthY;
            }
            AddTrackingPoint.m_TpToolCorrectionZ = 0;
            AddTrackingPoint.m_TpToolRadius = turningToolBuilder.NoseRadiusBuilder.Value;
            AddTrackingPoint.m_TpToolCutterRadius = 0;
            Toolobject.m_ListTrackingPoints.Add(AddTrackingPoint);
        }
        //}
        turningToolBuilder.Destroy();
    }

    private static void GetThreadTurningToolData(NXOpen.CAM.Tool mytool, NXOpen.Part workPart, bool AssemblyTool, External_to_ini.AssemblyToolInfo matchedTool, out External_to_ini.ToolObject Toolobject)
    {
        double AssemblyToolLengthX = 0;
        double AssemblyToolLengthY = 0;

        Toolobject = new External_to_ini.ToolObject();
        External_to_ini.ToolTrackingPoint AddTrackingPoint;

        NXOpen.CAM.TurningToolBuilder turningToolBuilder;
        turningToolBuilder = workPart.CAMSetup.CAMGroupCollection.CreateTurnToolBuilder(mytool);

        #region GetDataFromAssemblyTool
        if (AssemblyTool == true)
        {
            try
            {
                bool ToolTipFound = false;
                bool ToolMountFound = false;
                NXOpen.Point3d ToolTipPoint = new Point3d();
                NXOpen.Point3d ToolMountPoint = new Point3d();

                //GetJunction if a static holder is used
                NXOpen.SIM.KinematicConfigurator kinematicConfiguratorAssemblyTools;
                kinematicConfiguratorAssemblyTools = workPart.KinematicConfigurator;


                NXOpen.SIM.KinematicComponent kinematicComponentTool;
                kinematicComponentTool = kinematicConfiguratorAssemblyTools.ComponentCollection.FindObject(mytool.Name);

                NXOpen.SIM.KinematicJunction[] ComponentJct;
                kinematicComponentTool.GetJunctions(out ComponentJct);

                foreach (NXOpen.SIM.KinematicJunction jct in ComponentJct)
                {
                    NXOpen.SIM.KinematicJunctionBuilder jctbuilder;
                    jctbuilder = kinematicConfiguratorAssemblyTools.CreateJunctionBuilder(kinematicComponentTool, jct);


                    if (jctbuilder.IsToolTip())
                    {
                        NXOpen.CartesianCoordinateSystem cartesianCoordinateSystemToolTip;
                        cartesianCoordinateSystemToolTip = jctbuilder.Csys;
                        ToolTipPoint = cartesianCoordinateSystemToolTip.Origin;
                        ToolTipFound = true;
                    }
                    if (jctbuilder.IsToolMount())
                    {
                        NXOpen.CartesianCoordinateSystem cartesianCoordinateSystemToolMount;
                        cartesianCoordinateSystemToolMount = jctbuilder.Csys;
                        ToolMountPoint = cartesianCoordinateSystemToolMount.Origin;
                        ToolMountFound = true;
                    }
                    jctbuilder.Destroy();
                }

                if (ToolTipFound == true && ToolMountFound == true)
                {
                    AssemblyToolLengthX = ToolMountPoint.X - ToolTipPoint.X;
                    AssemblyToolLengthY = ToolMountPoint.Y - ToolTipPoint.Y;
                }
            }
            catch (Exception ex)
            {
                //Tool is not placed in a static_Holder, try to get kinematics from part file
                if (matchedTool != null)
                {
                    NXOpen.Tag KinToolTag = NXOpen.Tag.Null;
                    NXOpen.Tag origin_workpart_tag = workPart.Tag;
                    try
                    {
                        UFPart.LoadStatus errorStatus;


                        theUfSession.Part.OpenQuiet(matchedTool.m_FullPathName, out KinToolTag, out errorStatus);

                        theUfSession.Part.SetDisplayPart(KinToolTag);

                        // theSession.Parts.OpenDisplay(matchedTool.m_FullPathName, out loadstatus);
                        NXOpen.Part KinToolPart = (NXOpen.Part)theSession.Parts.FindObject(matchedTool.m_Filename);

                        //NXOpen.BasePart myBase = KinToolPart;
                        //theSession.Parts.SetActiveDisplay(myBase, DisplayPartOption.AllowAdditional, PartDisplayPartWorkPartOption.SameAsDisplay, out loadstatus);
                        //NXOpen.Part KinToolPart = (NXOpen.Part)NXOpen.Utilities.NXObjectManager.Get(KinToolTag);
                        //NXOpen.Part KinToolPart = theSession.Parts.Open(matchedTool.m_FullPathName, out loadstatus);



                        //theSession.Parts.SetWork(KinToolPart);

                        NXOpen.SIM.KinematicConfigurator kinematicConfiguratorAssemblyTools;
                        kinematicConfiguratorAssemblyTools = KinToolPart.KinematicConfigurator;
                        NXOpen.SIM.KinematicJunction[] KimJunctions;
                        kinematicConfiguratorAssemblyTools.GetJunctions(out KimJunctions);


                        NXOpen.SIM.KinematicComponentCollection CollectedComponents = kinematicConfiguratorAssemblyTools.ComponentCollection;
                        bool ToolTipFound = false;
                        bool ToolMountFound = false;
                        NXOpen.Point3d ToolTipPoint = new Point3d();
                        NXOpen.Point3d ToolMountPoint = new Point3d();

                        foreach (NXOpen.SIM.KinematicComponent component in CollectedComponents)
                        {
                            NXOpen.SIM.KinematicJunction[] ComponentJct;
                            component.GetJunctions(out ComponentJct);

                            foreach (NXOpen.SIM.KinematicJunction jct in ComponentJct)
                            {
                                NXOpen.SIM.KinematicJunctionBuilder jctbuilder;
                                jctbuilder = kinematicConfiguratorAssemblyTools.CreateJunctionBuilder(component, jct);


                                if (jctbuilder.IsToolTip())
                                {
                                    NXOpen.CartesianCoordinateSystem cartesianCoordinateSystemToolTip;
                                    cartesianCoordinateSystemToolTip = jctbuilder.Csys;
                                    ToolTipPoint = cartesianCoordinateSystemToolTip.Origin;
                                    ToolTipFound = true;
                                }
                                if (jctbuilder.IsToolMount())
                                {
                                    NXOpen.CartesianCoordinateSystem cartesianCoordinateSystemToolMount;
                                    cartesianCoordinateSystemToolMount = jctbuilder.Csys;
                                    ToolMountPoint = cartesianCoordinateSystemToolMount.Origin;
                                    ToolMountFound = true;
                                }
                                jctbuilder.Destroy();
                            }

                            if (ToolTipFound == true && ToolMountFound == true)
                            {
                                AssemblyToolLengthX = ToolMountPoint.X - ToolTipPoint.X;
                                AssemblyToolLengthY = ToolMountPoint.Y - ToolTipPoint.Y;
                                break;
                            }

                        }

                    }
                    catch (Exception ex2)
                    {

                    }
                    finally
                    {
                        theUfSession.Part.SetDisplayPart(origin_workpart_tag);
                        theUfSession.Part.Close(KinToolTag, 0, 1);
                    }
                }

            }
        }
        #endregion

        NXObject toolTipJunction;
        int Trackingpoint, RadiusId;

        turningToolBuilder.ManageToolPartBuilder.AskToolTipJunction(out toolTipJunction, out Trackingpoint, out RadiusId);

        Toolobject.m_ToolNumber = turningToolBuilder.TlNumberBuilder.Value;
        Toolobject.m_ToolName = mytool.Name;
        Toolobject.m_ToolStatus = 10;
        Toolobject.m_ToolType = 540;
        Toolobject.m_TrackingPoints = turningToolBuilder.TrackingBuilder.NumberOfTrackPoints;

        for (int iTrackingpoint = 0; iTrackingpoint < Toolobject.m_TrackingPoints; iTrackingpoint++)
        {
            NXObject SingleTrackpoint = turningToolBuilder.TrackingBuilder.GetTrackPoint(iTrackingpoint);
            string TpName;
            double TpAngle, TpDistance, TpXOffset, TpYOffset, TpRadius;
            int TpRadiusId, TpAdjustReg, TpAdjustIsUsed, TpCustcom, TpNumber;

            turningToolBuilder.TrackingBuilder.Get(SingleTrackpoint, out TpName, out TpRadiusId, out TpNumber, out TpAngle, out TpRadius, out TpXOffset, out TpYOffset, out TpAdjustReg, out TpCustcom);
            AddTrackingPoint = new External_to_ini.ToolTrackingPoint();
            AddTrackingPoint.m_TpToolAdjustRegister = TpAdjustReg;
            AddTrackingPoint.m_TpToolType = Toolobject.m_ToolType;
            AddTrackingPoint.m_TpToolFluteLength = TpNumber;

            if (AssemblyTool == true && AssemblyToolLengthX != 0)
            {
                AddTrackingPoint.m_TpToolCorrectionX = AssemblyToolLengthX;
                AddTrackingPoint.m_TpToolCorrectionY = AssemblyToolLengthY;
            }
            AddTrackingPoint.m_TpToolCorrectionZ = 0;
            AddTrackingPoint.m_TpToolRadius = turningToolBuilder.NoseRadiusBuilder.Value;
            AddTrackingPoint.m_TpToolCutterRadius = 0;
            Toolobject.m_ListTrackingPoints.Add(AddTrackingPoint);
        }
        //}
        turningToolBuilder.Destroy();
    }

    private static void GetGrooveTurningToolData(NXOpen.CAM.Tool mytool, NXOpen.Part workPart, bool AssemblyTool, External_to_ini.AssemblyToolInfo matchedTool, out External_to_ini.ToolObject Toolobject)
    {
        double AssemblyToolLengthX = 0;
        double AssemblyToolLengthY = 0;

        Toolobject = new External_to_ini.ToolObject();
        External_to_ini.ToolTrackingPoint AddTrackingPoint;

        //NXOpen.CAM.TurningToolBuilder turningToolBuilder;
        NXOpen.CAM.TurnToolBuilder turningToolBuilder;
        turningToolBuilder = workPart.CAMSetup.CAMGroupCollection.CreateTurnToolBuilder(mytool);

        #region GetDataFromAssemblyTool
        if (AssemblyTool == true)
        {
            try
            {
                bool ToolTipFound = false;
                bool ToolMountFound = false;
                NXOpen.Point3d ToolTipPoint = new Point3d();
                NXOpen.Point3d ToolMountPoint = new Point3d();

                //GetJunction if a static holder is used
                NXOpen.SIM.KinematicConfigurator kinematicConfiguratorAssemblyTools;
                kinematicConfiguratorAssemblyTools = workPart.KinematicConfigurator;


                NXOpen.SIM.KinematicComponent kinematicComponentTool;
                kinematicComponentTool = kinematicConfiguratorAssemblyTools.ComponentCollection.FindObject(mytool.Name);

                NXOpen.SIM.KinematicJunction[] ComponentJct;
                kinematicComponentTool.GetJunctions(out ComponentJct);

                foreach (NXOpen.SIM.KinematicJunction jct in ComponentJct)
                {
                    NXOpen.SIM.KinematicJunctionBuilder jctbuilder;
                    jctbuilder = kinematicConfiguratorAssemblyTools.CreateJunctionBuilder(kinematicComponentTool, jct);


                    if (jctbuilder.IsToolTip())
                    {
                        NXOpen.CartesianCoordinateSystem cartesianCoordinateSystemToolTip;
                        cartesianCoordinateSystemToolTip = jctbuilder.Csys;
                        ToolTipPoint = cartesianCoordinateSystemToolTip.Origin;
                        ToolTipFound = true;
                    }
                    if (jctbuilder.IsToolMount())
                    {
                        NXOpen.CartesianCoordinateSystem cartesianCoordinateSystemToolMount;
                        cartesianCoordinateSystemToolMount = jctbuilder.Csys;
                        ToolMountPoint = cartesianCoordinateSystemToolMount.Origin;
                        ToolMountFound = true;
                    }
                    jctbuilder.Destroy();
                }

                if (ToolTipFound == true && ToolMountFound == true)
                {
                    AssemblyToolLengthX = ToolMountPoint.X - ToolTipPoint.X;
                    AssemblyToolLengthY = ToolMountPoint.Y - ToolTipPoint.Y;
                }
            }
            catch (Exception ex)
            {
                //Tool is not placed in a static_Holder, try to get kinematics from part file
                if (matchedTool != null)
                {
                    NXOpen.Tag KinToolTag = NXOpen.Tag.Null;
                    NXOpen.Tag origin_workpart_tag = workPart.Tag;
                    try
                    {
                        UFPart.LoadStatus errorStatus;


                        theUfSession.Part.OpenQuiet(matchedTool.m_FullPathName, out KinToolTag, out errorStatus);

                        theUfSession.Part.SetDisplayPart(KinToolTag);

                        // theSession.Parts.OpenDisplay(matchedTool.m_FullPathName, out loadstatus);
                        NXOpen.Part KinToolPart = (NXOpen.Part)theSession.Parts.FindObject(matchedTool.m_Filename);

                        //NXOpen.BasePart myBase = KinToolPart;
                        //theSession.Parts.SetActiveDisplay(myBase, DisplayPartOption.AllowAdditional, PartDisplayPartWorkPartOption.SameAsDisplay, out loadstatus);
                        //NXOpen.Part KinToolPart = (NXOpen.Part)NXOpen.Utilities.NXObjectManager.Get(KinToolTag);
                        //NXOpen.Part KinToolPart = theSession.Parts.Open(matchedTool.m_FullPathName, out loadstatus);



                        //theSession.Parts.SetWork(KinToolPart);

                        NXOpen.SIM.KinematicConfigurator kinematicConfiguratorAssemblyTools;
                        kinematicConfiguratorAssemblyTools = KinToolPart.KinematicConfigurator;
                        NXOpen.SIM.KinematicJunction[] KimJunctions;
                        kinematicConfiguratorAssemblyTools.GetJunctions(out KimJunctions);


                        NXOpen.SIM.KinematicComponentCollection CollectedComponents = kinematicConfiguratorAssemblyTools.ComponentCollection;
                        bool ToolTipFound = false;
                        bool ToolMountFound = false;
                        NXOpen.Point3d ToolTipPoint = new Point3d();
                        NXOpen.Point3d ToolMountPoint = new Point3d();

                        foreach (NXOpen.SIM.KinematicComponent component in CollectedComponents)
                        {
                            NXOpen.SIM.KinematicJunction[] ComponentJct;
                            component.GetJunctions(out ComponentJct);

                            foreach (NXOpen.SIM.KinematicJunction jct in ComponentJct)
                            {
                                NXOpen.SIM.KinematicJunctionBuilder jctbuilder;
                                jctbuilder = kinematicConfiguratorAssemblyTools.CreateJunctionBuilder(component, jct);


                                if (jctbuilder.IsToolTip())
                                {
                                    NXOpen.CartesianCoordinateSystem cartesianCoordinateSystemToolTip;
                                    cartesianCoordinateSystemToolTip = jctbuilder.Csys;
                                    ToolTipPoint = cartesianCoordinateSystemToolTip.Origin;
                                    ToolTipFound = true;
                                }
                                if (jctbuilder.IsToolMount())
                                {
                                    NXOpen.CartesianCoordinateSystem cartesianCoordinateSystemToolMount;
                                    cartesianCoordinateSystemToolMount = jctbuilder.Csys;
                                    ToolMountPoint = cartesianCoordinateSystemToolMount.Origin;
                                    ToolMountFound = true;
                                }
                                jctbuilder.Destroy();
                            }

                            if (ToolTipFound == true && ToolMountFound == true)
                            {
                                AssemblyToolLengthX = ToolMountPoint.X - ToolTipPoint.X;
                                AssemblyToolLengthY = ToolMountPoint.Y - ToolTipPoint.Y;
                                break;
                            }

                        }

                    }
                    catch (Exception ex2)
                    {

                    }
                    finally
                    {
                        theUfSession.Part.SetDisplayPart(origin_workpart_tag);
                        theUfSession.Part.Close(KinToolTag, 0, 1);
                    }
                }

            }
        }
        #endregion

        //Debugger.Launch();

        NXObject toolTipJunction;
        int Trackingpoint, RadiusId;

        turningToolBuilder.ManageToolPartBuilder.AskToolTipJunction(out toolTipJunction, out Trackingpoint, out RadiusId);

        Toolobject.m_ToolNumber = turningToolBuilder.TlNumberBuilder.Value;
        Toolobject.m_ToolName = mytool.Name;
        Toolobject.m_ToolStatus = 10;
        Toolobject.m_ToolType = 520;
        Toolobject.m_TrackingPoints = turningToolBuilder.TrackingBuilder.NumberOfTrackPoints;

       

        for (int iTrackingpoint = 0; iTrackingpoint < Toolobject.m_TrackingPoints; iTrackingpoint++)
        {
            NXObject SingleTrackpoint = turningToolBuilder.TrackingBuilder.GetTrackPoint(iTrackingpoint);
            string TpName;
            double TpAngle, TpDistance, TpXOffset, TpYOffset, TpRadius;
            int TpRadiusId, TpAdjustReg, TpAdjustIsUsed, TpCustcom, TpNumber;

            turningToolBuilder.TrackingBuilder.Get(SingleTrackpoint, out TpName, out TpRadiusId, out TpNumber, out TpAngle, out TpRadius, out TpXOffset, out TpYOffset, out TpAdjustReg, out TpCustcom);
            AddTrackingPoint = new External_to_ini.ToolTrackingPoint();
            AddTrackingPoint.m_TpToolAdjustRegister = TpAdjustReg;
            AddTrackingPoint.m_TpToolType = Toolobject.m_ToolType;

            int MappedTpNumber;
            MapTrackingPoint(TpNumber, out MappedTpNumber);
            AddTrackingPoint.m_TpToolFluteLength = MappedTpNumber;

            if (AssemblyTool == true && AssemblyToolLengthX != 0)
            {
                AddTrackingPoint.m_TpToolCorrectionX = AssemblyToolLengthX;
                AddTrackingPoint.m_TpToolCorrectionY = AssemblyToolLengthY;
            }
            AddTrackingPoint.m_TpToolCorrectionZ = 0;
            AddTrackingPoint.m_TpToolRadius = turningToolBuilder.NoseRadiusBuilder.Value;
            AddTrackingPoint.m_TpToolCutterRadius = 0;
            Toolobject.m_ListTrackingPoints.Add(AddTrackingPoint);
        }
        //}
        turningToolBuilder.Destroy();
    }

}

