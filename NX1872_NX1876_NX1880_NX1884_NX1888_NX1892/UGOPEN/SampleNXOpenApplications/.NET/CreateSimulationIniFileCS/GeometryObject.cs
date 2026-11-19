/*
 ==============================================================================

      Copyright (c) 2018  Siemens Product Lifecycle Management Software Inc.
                         All rights reserved

 ==============================================================================
 ******************************************************************************
  Description
    Class that provides the geometry objects

 */

namespace External_to_ini
{
    public class GeometryObject
    {
        public string m_Name { get; set; }
        /// <summary>
        /// Return Main or Local
        /// </summary>
        public string m_PurposeMode { get; set; }
        /// <summary>
        /// Return Fixture Offset Value from MCS
        /// </summary>
        public int m_FixtureOffset { get; set; }
        /// <summary>
        /// Return the special output mode
        /// </summary>
        public string m_SpecialOutputMode { get; set; }
        public double m_X { get; set; }

        public double m_Y { get; set; }

        public double m_Z { get; set; }

        public string m_VarName { get; set; }

        public string m_TransCommand { get; set; }

        public string m_Channel { get; set; }
        public GeometryObject()
        {

        }
    }
}
