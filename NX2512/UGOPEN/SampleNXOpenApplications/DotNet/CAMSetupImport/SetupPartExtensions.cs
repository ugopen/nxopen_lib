/*
==============================================================================
 
        Copyright (c) 2017 Siemens Product Lifecycle Management Software Inc.
                         Unpublished - All rights reserved

==============================================================================

 Description
    This class contains extension methods for the NXOpen.Part class
    used to configure the setup.

==============================================================================*/

using NXOpen;
using NXOpen.Assemblies;
using NXOpen.CAM;
using System;

namespace CAMSetupImport
{
    public static class SetupPartExtensions
    {
        public static void LoadMachine(this NXOpen.Part setupPart, string libRef)
        {
            NCGroup nCGroup = (NCGroup)setupPart.CAMSetup.CAMGroupCollection.FindObject("GENERIC_MACHINE");
            MachineGroupBuilder machineGroupBuilder = setupPart.CAMSetup.CAMGroupCollection.CreateMachineGroupBuilder(nCGroup);
            machineGroupBuilder.RemoveMachine();

            NcmctPartMountingBuilder ncmctPartMountingBuilder = setupPart.CAMSetup.CreateNcmctPartMountingBuilder(libRef);
            if (ncmctPartMountingBuilder == null)
                throw new NotSupportedException("Machine not available in library");
            ncmctPartMountingBuilder.Positioning = NcmctPartMountingBuilder.PositioningTypes.UsePartMountJunction;
            ncmctPartMountingBuilder.LayerOptions = NcmctPartMountingBuilder.LayerTypes.OriginalMakeVisible;


            Point3d origin1 = new Point3d(0, 0, 0);
            Vector3d xDirection1 = new Vector3d(1.0, 0.0, 0.0);
            Vector3d yDirection1 = new Vector3d(0.0, 1.0, 0.0);
            Xform xform1 = setupPart.Xforms.CreateXform(origin1, xDirection1, yDirection1, SmartObject.UpdateOption.AfterModeling, 1.0);

            CartesianCoordinateSystem cartesianCoordinateSystem1;
            cartesianCoordinateSystem1 = setupPart.CoordinateSystems.CreateCoordinateSystem(xform1, SmartObject.UpdateOption.AfterModeling);
            ncmctPartMountingBuilder.PartMountJunction = cartesianCoordinateSystem1;
            NXObject nXObject = ncmctPartMountingBuilder.Commit();
            machineGroupBuilder.UpdateCamSetup(MachineGroupBuilder.RetrieveToolPocketInformation.Yes, ncmctPartMountingBuilder);
            ncmctPartMountingBuilder.Destroy();
            machineGroupBuilder.Destroy();
        }

        public static void AddBlank(this NXOpen.Part setupPart, Component comp)
        {
            setupPart.AddKimSetupComponent(comp, "BLANK");
        }

        public static void AddPart(this NXOpen.Part setupPart, Component comp)
        {
            setupPart.AddKimSetupComponent(comp, "PART");
        }

        public static void AddClamp(this NXOpen.Part setupPart, Component comp)
        {
            setupPart.AddKimSetupComponent(comp, "FIXTURE");
        }

        private static void AddKimSetupComponent(this NXOpen.Part setupPart, Component comp, String type)
        {
            NXOpen.SIM.KinematicConfigurator kinematicConfigurator3;
            kinematicConfigurator3 = setupPart.KinematicConfigurator;

            NXOpen.SIM.KinematicComponent kinematicComponent1;
            kinematicComponent1 = kinematicConfigurator3.ComponentCollection.FindObject("SETUP");
            NXOpen.SIM.KinematicComponent kinematicComponent2;
            kinematicComponent2 = kinematicConfigurator3.ComponentCollection.FindObject(type);

            NXOpen.SIM.KinematicComponentBuilder kinematicComponentBuilder1;
            kinematicComponentBuilder1 = kinematicConfigurator3.ComponentCollection.CreateComponentBuilder(kinematicComponent1, kinematicComponent2);

            kinematicComponentBuilder1.AddGeometry(comp);
            kinematicComponentBuilder1.Commit();
            kinematicComponentBuilder1.Destroy();
        }

        public static void MoveComp(this NXOpen.Part setupPart, Component comp, Position position, NXOpen.SIM.KinematicJunction junction)
        {
            if (position == null)
                return;

            /******************************************************/
            /*                 Revert move                        */
            /******************************************************/
            Point3d compPosition;
            Matrix3x3 compOrientation;
            comp.GetPosition(out compPosition, out compOrientation);

            Vector3d translation = new Vector3d(
                -compPosition.X,
                -compPosition.Y,
                -compPosition.Z);
            Matrix3x3 rotation = new Matrix3x3();
            rotation.Xx = compOrientation.Xx;
            rotation.Xy = compOrientation.Yx;
            rotation.Xz = compOrientation.Zx;
            rotation.Yx = compOrientation.Xy;
            rotation.Yy = compOrientation.Yy;
            rotation.Yz = compOrientation.Zy;
            rotation.Zx = compOrientation.Xz;
            rotation.Zy = compOrientation.Yz;
            rotation.Zz = compOrientation.Zz;

            setupPart.ComponentAssembly.MoveComponent(comp, translation, rotation);


            /******************************************************/
            /*                 Move to position                   */
            /******************************************************/
            Matrix3x3 junctionMatrix = junction.Matrix;
            Vector3d junctionOrigin = junction.Origin;

            double alpha = Convert.ToDouble(position.Alpha);
            double beta = Convert.ToDouble(position.Beta);
            double gamma = Convert.ToDouble(position.Gamma);
            rotation = MatrixHelper.ConvertToMatrix(alpha, beta, gamma);
            double x = Convert.ToDouble(position.X);
            double y = Convert.ToDouble(position.Y);
            double z = Convert.ToDouble(position.Z);
            translation = new Vector3d(x, y, z);

            translation = junctionMatrix.Multiply(translation);
            translation.X += junctionOrigin.X;
            translation.Y += junctionOrigin.Y;
            translation.Z += junctionOrigin.Z;
            rotation = junctionMatrix.Multiply(rotation);

            setupPart.ComponentAssembly.MoveComponent(comp, translation, rotation);
        }

        public static void FillCarrier(this NXOpen.Part setupPart, ResourcesToolListCarrier carrier)
        {
            foreach (var slot in carrier.Slot)
            {
                NXOpen.CAM.NCGroup nCGroup1 = (NXOpen.CAM.NCGroup)setupPart.CAMSetup.CAMGroupCollection.FindObject(slot.Name);
                NXOpen.CAM.CAMObject cAMObject1;
                NXOpen.CAM.Tool tool1;
                try
                {
                    bool success1;
                    tool1 = setupPart.CAMSetup.RetrieveTool(slot.Tool, nCGroup1, out cAMObject1, out success1);
                }
                catch (NXOpen.NXException ex)
                {
                    MessageUtils.ShowError("Could not add tool: " + slot.Tool + "\n" + ex.Message);
                }
            }
        }
    }
}
