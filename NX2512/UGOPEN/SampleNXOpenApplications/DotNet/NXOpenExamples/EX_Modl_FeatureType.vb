' ==================================================================================================
'
'            Copyright (c) 2004 UGS PLM Solutions.
'                   Unpublished - All rights reserved
'
'====================================================================================================
'File description: Example for Wrapped UFUNC (NXOpen.NET)
' 
'====================================================================================================
Option Strict Off
Imports System
Imports System.IO
Imports System.Runtime.InteropServices
Imports NXOpen
Imports NXOpen.Features
Imports NXOpen.Preferences
Imports NXOpen.UF

Module EX_Modl_FeatureType

    Dim theSession As Session
    Dim theUfSession As UFSession

    Public Const UF_feature_type As Integer = 205

    Public Sub Main()
        theSession = Session.GetSession()
        theUfSession = UFSession.GetUFSession()

        Dim fs As New FileStream("EX_Modl_FeatureType.log", FileMode.Create, FileAccess.Write)
        Dim stream As New StreamWriter(fs) ' create a stream writer 
        stream.WriteLine("--Log entry goes here--")
        stream.Flush() ' update underlying file

        If File.Exists("EX_Modl_FeatureType.prt") Then
            stream.WriteLine("Remove EX_Modl_FeatureType.prt file from <Project Folder>\\bin\\Debug !!")
            stream.WriteLine("EX_Modl_FeatureType.prt already exists. !!")
            stream.Close()
            Return
        End If

        Dim nError As Integer = Execute(stream, theUfSession)
        stream.WriteLine("End of Log File")
        stream.Close()

    End Sub

    Function Execute(ByVal stream As StreamWriter, ByVal theUfSession As NXOpen.UF.UFSession) As Integer
        Try
            Dim UFPart As NXOpen.Tag
            Dim part_name As String = "EX_Modl_FeatureType"
            Dim units As Integer = 2
            Dim name As String
            'Dim Information As String

            theUfSession.Part.[New](part_name, units, UFPart)
            stream.WriteLine("New part : {0} ", part_name, " Created")

            Dim index As Integer
            Dim num_parents, num_children As Integer
            Dim enttype As Integer
            Dim feat1, master_feature As NXOpen.Tag
            Dim parent_array(), children_array() As NXOpen.Tag
            Dim part_tag As NXOpen.Tag
            Dim feat_type As String
            feat1 = 0
            master_feature = 0
            index = 0
            enttype = UF_feature_type
            Dim block_orig() As Double = {0.0, 0.0, 0.0}
            Dim block_len() As String = {"1", "2", "3"}
            Dim blk_obj As NXOpen.Tag
            theUfSession.Modl.CreateBlock1(FeatureSigns.Nullsign, block_orig, block_len, blk_obj)
            stream.WriteLine("Successful:Modl.CreateBlock1")

            'Get the tag of the work UFPart 
            part_tag = theUfSession.Assem.AskWorkPart()
            stream.WriteLine("Successful:Assem.AskWorkPart")

            'Cycle through all the features in the UFPart 
            Do
                theUfSession.Obj.CycleObjsInPart(part_tag, enttype, feat1)
                stream.WriteLine("Successful:Obj.CycleObjsInPart")

                If (feat1 = NXOpen.Tag.Null) Then
                    Exit Do
                End If
                'Get the feature type 
                theUfSession.Modl.AskFeatType(feat1, feat_type)
                stream.WriteLine("Successful:Modl.AskFeatType")

                'Information = " Feature "+ index + "  = " + feat1 + " is of type " + feat_type + "\n";
                stream.WriteLine("Feature {0} = {1} is of type {2}", index, feat1, feat_type)
                index = index + 1

                ' If the feature is an INSTANCE, then get the master feature and its type */
                If (String.Compare(feat_type, "INSTANCE") = 0) Then
                    theUfSession.Modl.AskMaster(feat1, master_feature)
                    stream.WriteLine("Successful:Modl.AskMaster")

                    theUfSession.Modl.AskFeatType(master_feature, feat_type)
                    stream.WriteLine("Successful:Modl.AskFeatType")
                    stream.WriteLine(" master feature {0} is of type = {1} ", master_feature, feat_type)

                End If
                theUfSession.Modl.AskFeatRelatives(feat1, num_parents, parent_array, num_children, children_array)
                stream.WriteLine("Successful:Modl.AskFeatRelatives")
                stream.WriteLine("Parent array for {0} contains {1} members", feat1, num_parents)

                If (num_parents > 0) Then
                    For inx As Integer = 0 To num_parents - 1
                        theUfSession.Modl.AskFeatType(parent_array(inx), feat_type)
                        stream.WriteLine("Successful:Modl.AskFeatType")
                        stream.WriteLine("  parent id {0} = {1} is of feature type {2}", inx, parent_array(inx), feat_type)
                    Next
                End If

                stream.WriteLine("  children array for feature {0} conatins {1} members", feat1, num_children)

                If (num_children > 0) Then
                    For iny As Integer = 0 To num_children - 1
                        theUfSession.Modl.AskFeatType(children_array(iny), feat_type)
                        stream.WriteLine("Successful:Modl.AskFeatType")
                        stream.WriteLine("    child id {0} = {1} is of feature type = {2}", iny, children_array(iny), feat_type)
                    Next
                End If
            Loop While (feat1 <> 0)

            'Save the Part
            theUfSession.Part.Save()
        Catch ex As Exception
            stream.WriteLine("EXCEPTION: ", ex.Message)
            Return 1
        End Try
        Return 0

    End Function

End Module


