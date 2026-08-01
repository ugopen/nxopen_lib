/*
==============================================================================
 
        Copyright (c) 2017 Siemens Product Lifecycle Management Software Inc.
                         Unpublished - All rights reserved

==============================================================================

 Description
    This class contains extension methods for the ImportRealNcSimulation.Resources class.

==============================================================================*/

using NXOpen.Assemblies;
using System;
using System.Collections.Generic;
using System.IO;

namespace CAMSetupImport
{
    public static class ResourcesExtensions
    {
        public static void ResolveRelativePaths(this Resources data, string directory)
        {
            if (data.ProgramList != null)
            {
                foreach (var program in data.ProgramList)
                {
                    program.FileName = ResolveRelativePath(directory, program.FileName);
                }
            }

            if (data.Parts != null)
            {
                foreach (var part in data.Parts)
                {
                    part.Path = ResolveRelativePath(directory, part.Path);
                }
            }

            if (data.Clamps != null)
            {
                foreach (var clamp in data.Clamps)
                {
                    clamp.Path = ResolveRelativePath(directory, clamp.Path);
                }
            }
        }

        private static string ResolveRelativePath(string directory, string path)
        {
            if (String.IsNullOrEmpty(path))
                return null;

            if (!Path.IsPathRooted(path))
            {
                return Path.GetFullPath(Path.Combine(directory, path));
            }
            return path;
        }

        public static void LoadMachine(this Resources data)
        {
            if (data.Machine == null || data.Machine.Name == null)
                throw new InvalidOperationException("No machine name given. Cannot proceed.");

            NXOpen.Part workPart = NXOpen.Session.GetSession().Parts.Work;
            workPart.LoadMachine(data.Machine.Name);
        }

        public static void LoadPrograms(this Resources data)
        {
            if (data.ProgramList == null)
                return;

            NXOpen.Part workPart = NXOpen.Session.GetSession().Parts.Work;

            var ncProgramManagerBuilder = workPart.KinematicConfigurator.CreateNcProgramManagerBuilder();
            var externalSource = ncProgramManagerBuilder.GetExternalFileSource();
            var setupSource = ncProgramManagerBuilder.GetSetupSource();
            foreach (Program program in data.ProgramList)
            {
                if (program.PrgID.IndexOf("main", StringComparison.OrdinalIgnoreCase) >= 0)
                {
                    if (externalSource.AddMainProgram(program.Channel, program.FileName) == null)
                        MessageUtils.ShowError(program.FileName + " was not added");
                }
                else
                {
                    if (setupSource.AddSubprogram(program.FileName) == null)
                        MessageUtils.ShowError(program.FileName + " was not added");
                }
            }
        }

        public static void LoadPartsAndClamps(this Resources data)
        {
            NXOpen.Part workPart = NXOpen.Session.GetSession().Parts.Work;

            var parts = new Dictionary<string, Component>();
            if (data.Parts != null)
            {
                foreach (ResourcesPart part in data.Parts)
                {
                    if (!new FileInfo(part.Path).Exists)
                    {
                        MessageUtils.ShowError("File " + part.Path + " cannot be found.");
                        parts.Add(part.Name, null);
                        continue;
                    }

                    Component comp = Utils.AddComponent(part.Path);
                    parts.Add(part.Name, comp);
                    if (comp == null)
                        continue;

                    if (part.IsFinishedPart)
                        workPart.AddPart(comp);
                    else
                        workPart.AddBlank(comp);
                }
            }

            var clamps = new Dictionary<string, Component>();
            if (data.Clamps != null)
            {
                foreach (ResourcesClamp clamp in data.Clamps)
                {
                    if (!new FileInfo(clamp.Path).Exists)
                    {
                        MessageUtils.ShowError("File " + clamp.Path + " cannot be found.");
                        clamps.Add(clamp.Name, null);
                        continue;
                    }

                    Component comp = Utils.AddComponent(clamp.Path);
                    clamps.Add(clamp.Name, comp);
                    if (comp == null)
                        continue;
                    workPart.AddClamp(comp);
                }
            }

            var partMountJunction = workPart.KinematicConfigurator.FindJunction("PART_MOUNT_JCT");

            if (data.Instances != null)
            {
                if (data.Instances.Parts != null)
                {
                    foreach (Instance partInstance in data.Instances.Parts)
                    {
                        if (!parts.ContainsKey(partInstance.Name))
                        {
                            MessageUtils.ShowError("Part with name " + partInstance.Name + " was not found in XML.");
                            continue;
                        }

                        var comp = parts[partInstance.Name];
                        if (comp != null)
                        {
                            workPart.MoveComp(comp, partInstance.Position, partMountJunction);
                        }
                    }
                }

                if (data.Instances.Clamps != null)
                {
                    foreach (Instance clampInstance in data.Instances.Clamps)
                    {
                        if (!clamps.ContainsKey(clampInstance.Name))
                        {
                            MessageUtils.ShowError("Clamp with name " + clampInstance.Name + " was not found in XML.");
                            continue;
                        }

                        var comp = clamps[clampInstance.Name];
                        if (comp != null)
                        {
                            workPart.MoveComp(comp, clampInstance.Position, partMountJunction);
                        }
                    }
                }
            }
        }

        public static void LoadTools(this Resources data)
        {
            NXOpen.Part workPart = NXOpen.Session.GetSession().Parts.Work;

            if (data.ToolList == null || data.ToolList.CarrierPlacements == null)
                return;

            foreach (ResourcesToolListCarrier carrier in data.ToolList.CarrierPlacements)
            {
                workPart.FillCarrier(carrier);
            }
        }

    }
}
