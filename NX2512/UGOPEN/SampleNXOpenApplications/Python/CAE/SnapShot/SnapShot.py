#==================================================================================================

#                Copyright (c) 2022 Siemens Product Lifecycle Management Software Inc.
#                                     All Rights Reserved.

#==================================================================================================
#File description:

#    Example capturing image for all the snapshots present in sim file 

#==================================================================================================
#

import os
import os.path
import sys
import NXOpen

DEBUG = False

def parseInput():

    if len(sys.argv) < 2:
        print(" *** ERROR *** Too few arguments...")
        print("    1st argument = Input part filename (sim)")
        print("    2nd argument = Output folder for Image files")
        return (None, None)

    partFile = sys.argv[1]
    imgFileDir = sys.argv[2]

    if not os.path.isfile(partFile):
        print(" *** ERROR *** Specified input file does not exist: {0}".format(partFile))

    if not os.path.exists(imgFileDir):
        print(" *** ERROR *** Specified output directory does not exist: {0}".format(imgFileDir))

    return(partFile, imgFileDir)


def main() :

    (partFile, imgFileDir) = parseInput()

    if partFile is None:
        return
    if imgFileDir is None:
        return

    theSession  = NXOpen.Session.GetSession()

    basePart1, partLoadStatus1 = theSession.Parts.OpenActiveDisplay(partFile, NXOpen.DisplayPartOption.AllowAdditional)

    workPart = theSession.Parts.BaseWork
    partLoadStatus1.Dispose()
    theSession.ApplicationSwitchImmediate("UG_APP_SFEM")

    layoutStateApplicator = workPart.LayoutStates.CreateLayoutStateApplicator()
    imageExportBuilder = workPart.Views.CreateImageExportBuilder()
    imageExportBuilder.RegionMode = False

    imageExportBuilder.FileFormat = NXOpen.Gateway.ImageExportBuilder.FileFormats.Png
    imageExportBuilder.BackgroundOption = NXOpen.Gateway.ImageExportBuilder.BackgroundOptions.Original
    imageExportBuilder.EnhanceEdges = False

    archivedLayouts = workPart.LayoutStates

    for layout in archivedLayouts:
        layoutStateApplicator.SetLayoutState(layout)

        layoutStateApplicator.SetUpdateLayoutState(True)

        layoutStateApplicator.Commit()

        # path to image being exported
        imageExportBuilder.FileName = os.path.join(imgFileDir, layout.Name + ".png")
        print("Generating " + imageExportBuilder.FileName)

        imageExportBuilder.Commit()

    imageExportBuilder.Destroy()

    layoutStateApplicator.Destroy()

    theSession.Parts.CloseAll(NXOpen.BasePart.CloseModified.CloseModified, None)

if __name__ == '__main__':
    main()
