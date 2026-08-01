/*
 ==============================================================================

      Copyright (c) 2018  Siemens Product Lifecycle Management Software Inc.
                         All rights reserved

 ==============================================================================
 ******************************************************************************
  Description
    Class that provides the tool objects

 */
using System.Collections.Generic;

namespace External_to_ini
{
    public class ToolObject
    {
        public int m_ToolNumber { get; set; }
        public string m_ToolName { get; set; }
        public int m_TrackingPoints { get; set; }
        public int m_ToolAdjustRegister { get; set; }
        public int m_ToolStatus { get; set; }
        public int m_ToolType { get; set; }
        public string m_ToolChannel { get; set; }
        public double m_ToolFluteLength { get; set; }
        public double m_ToolLength { get; set; }
        public double m_ToolCorrectionX { get; set; }
        public double m_ToolCorrectionY { get; set; }
        public double m_ToolCorrectionZ { get; set; }
        public double m_ToolRadius { get; set; }
        public double m_ToolCutterRadius { get; set; }

        /// <summary>
        /// Contains all tracking points which are defined in the tool.
        /// </summary>
        public List<ToolTrackingPoint> m_ListTrackingPoints { get; set; } = new List<ToolTrackingPoint>();
        public ToolObject()
        {

        }
    }

    public class ToolTrackingPoint
    {
        public int m_TpToolAdjustRegister { get; set; }
        public int m_TpToolType { get; set; }
        public double m_TpToolFluteLength { get; set; }
        public double m_TpToolCorrectionX { get; set; }
        public double m_TpToolCorrectionY { get; set; }
        public double m_TpToolCorrectionZ { get; set; }
        public double m_TpToolRadius { get; set; }
        public double m_TpToolCutterRadius { get; set; }

        public ToolTrackingPoint()
        {
        }
    }

    public class AssemblyToolInfo
    {
        public string m_FullPathName { get; set; }
        public string m_Filename { get; set; }
        public string m_Toolname { get; set; }

        public AssemblyToolInfo()
        {

        }
    }
}
