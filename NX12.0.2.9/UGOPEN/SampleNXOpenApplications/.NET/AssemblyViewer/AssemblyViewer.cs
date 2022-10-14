/*=============================================================================

                    Copyright (c) 2004 UGS PLM Solutions
                    Unpublished - All rights reserved

===============================================================================
File description: Sample NX/Open Application
===============================================================================
 
=============================================================================
*/
using System;
using System.Drawing;
using System.Collections;
using System.Windows.Forms;
using System.Data;
using System.Diagnostics;

using NXOpen;
using NXOpen.Assemblies;
using NXOpen.UF;

// This class demonstrates a simple viewer that displays the tree structure of an
// assembly. The color of the selected component can be changed by pressing the "Set
// Color" button.

public class AssemblyViewer : System.Windows.Forms.Form
{
    // Cached NXOpen session
    private static NXOpen.Session theSession;
    private static NXOpen.UF.UFSession theUFSession;

    // The active AssemblyViewer 
    private static AssemblyViewer theViewer;


    // Hashtable containing basic color names and their corresponding color IDs. 
    // For simplicity, we are just supporting the basic primaries. See UFDisp
    // for a full set of color handling methods.
    private static Hashtable colorTable;

    static AssemblyViewer() {
        colorTable = new Hashtable();
        colorTable["Blue"] = UFDisp.ColorName.BlueName;
        colorTable["Green"] = UFDisp.ColorName.GreenName;
        colorTable["Cyan"] = UFDisp.ColorName.CyanName;
        colorTable["Red"] = UFDisp.ColorName.RedName;
        colorTable["Magenta"] = UFDisp.ColorName.MagentaName;
        colorTable["Yellow"] = UFDisp.ColorName.YellowName;
        colorTable["White"] = UFDisp.ColorName.WhiteName;
        colorTable["Black"] = UFDisp.ColorName.BlackName;

    }

    // WinForm components
    private System.Windows.Forms.TreeView assemblyTree;
    private System.Windows.Forms.ComboBox colorBox;
    private System.Windows.Forms.GroupBox groupBox1;
    private System.Windows.Forms.Button setColorButton;
    private System.Windows.Forms.RadioButton allComponentsButton;
    private System.Windows.Forms.RadioButton singleComponentButton;
    private System.Windows.Forms.Button closeButton;


    // Lookup table which maps the selected tree node onto a component
    Hashtable componentTable = new Hashtable();

    // Currently selected component
    Component selectedComponent = null;

    // Controls whether to draw just the selected component, or the selected
    // component and all similar components.
    private static bool drawAll = false;

    // Identifier for the part callbacks
    private IntPtr onChangeWorkPartID;
    private IntPtr onClosePartID;

    // Delegates for the part callbacks. Note that these need to be declared
    // as members rather than local variables to ensure that they are not
    // garbage collected
    UF.CallbackFnT WorkPartCallbackFunction;
    UF.CallbackFnT ClosePartCallbackFunction;


    public AssemblyViewer()
    {
        //
        // Required for Windows Form Designer support
        //
        InitializeComponent();

        FillColorBox();

        // Fill in the assembly tree
        UpdateTree();
        
        // Make the displayed window a child of the main NX window
        NXOpenUI.FormUtilities.SetApplicationIcon(this);
        NXOpenUI.FormUtilities.ReparentForm(this);


        // Register methods to be invoked when the work part changes, or a part is closed.

        WorkPartCallbackFunction  = new UF.CallbackFnT( OnChangeWorkPart );

        theUFSession.UF.AddCallbackFunction(CallbackReason.ChangeWorkPartReason, 
                                            WorkPartCallbackFunction ,
                                            IntPtr.Zero, out onChangeWorkPartID);


        ClosePartCallbackFunction  = new UF.CallbackFnT( OnClosePart );

        theUFSession.UF.AddCallbackFunction(CallbackReason.ClosePartReason,
                                            ClosePartCallbackFunction ,
                                            IntPtr.Zero, out onClosePartID);
    }

    // Fills in the entries in the color combo box
    private void FillColorBox()
    {
        ICollection colorNames = colorTable.Keys;

        foreach (string key in colorTable.Keys)
            this.colorBox.Items.Add(key);
        this.colorBox.SelectedIndex = 0;
    }


    // Removes the registered callbacks
    private void UnregisterCallbacks()
    {
        theUFSession.UF.RemoveCallbackFunction(onChangeWorkPartID);
        theUFSession.UF.RemoveCallbackFunction(onClosePartID);
    }

    // Registered method which is invoked when the work part changes.
     void OnChangeWorkPart( CallbackReason reason,
                           IntPtr application_data,
                           IntPtr user_data)
    {
        // We should catch any exceptions in our callback, so that we don't
        // return an exception to NX.
        try 
        {
            HighlightComponent(selectedComponent, false);
            UpdateTree();
        }
        catch (Exception ex) 
        {
            theSession.LogFile.WriteLine("Got exception in callback");
            theSession.LogFile.WriteLine(ex.ToString());
        }
    }
    
    // Registered method which is invoked when a part closes
    void OnClosePart( CallbackReason reason,
                           IntPtr application_data,
                           IntPtr user_data)
    {
        // We should catch any exceptions in our callback, so that we don't
        // return an exception to NX.
        try 
        {
            // If the display part has been closed, call UpdateTree(),
            // which will clear all elements from the tree.
            if (theSession.Parts.Display == null)
                UpdateTree();
        }
        catch (Exception ex) 
        {
            theSession.LogFile.WriteLine("Got exception in callback");
            theSession.LogFile.WriteLine(ex.ToString());
        }
    }

    // Updates the assemblyTree that contains the assembly structrue. Called at startup,
    // and whenever the work part changes.
    private void UpdateTree()
    {
        assemblyTree.Nodes.Clear();
        componentTable.Clear();
        selectedComponent = null;

        if (theSession.Parts.Display != null)
        {
            // For a piece part, the RootComponent will be null, so we don't display
            // an assembly tree.
            Component rootComponent = theSession.Parts.Display.ComponentAssembly.RootComponent;
            if (rootComponent != null)
            {
                TreeNode rootNode = new TreeNode("ROOT");
                assemblyTree.Nodes.Add(rootNode);
                componentTable[rootNode] = rootComponent;
                AddChildren(rootNode, rootComponent);
                rootNode.Expand();
            }
        }
    }

    // Recursive method that adds the children of "component" to the tree node "node"
    private void AddChildren(TreeNode node, Component component) 
    {
        Component[] childComponents = component.GetChildren();
        for (int i = 0; i < childComponents.Length; i++) 
        {
            TreeNode childNode = new TreeNode(childComponents[i].Name);
            componentTable[childNode] = childComponents[i];
            node.Nodes.Add(childNode);
            AddChildren(childNode, childComponents[i]);
        }

    }


    // Invoked when the viewer is closed. Unhighlight any components
    // that we have selected, and unregister the work part callback. 
    private void OnClose(object sender, System.ComponentModel.CancelEventArgs e)
    {
        HighlightComponent(selectedComponent, false);
        selectedComponent = null;
        UnregisterCallbacks();
    }


    // Invoked when the SetColor button is clicked
    private void SetColorClicked(object sender, System.EventArgs e)
    {
        if (selectedComponent != null)
        {
            // Get the color ID from the colorTable, using the currently selected name
            // as the key. The find the corresponding color index in the displayed part

            UFDisp.ColorName colorID = (UFDisp.ColorName) colorTable[colorBox.SelectedItem];
            int colorIndex;
            theUFSession.Disp.AskClosestColorInDisplayedPart(colorID, out colorIndex);
            // Set an undo mark before modifying the color;

            theSession.SetUndoMark(Session.MarkVisibility.Visible, "Set color "  + colorBox.SelectedItem);

            // Create a DisplayModification object to set the color

            DisplayModification displayMod = theSession.DisplayManager.NewDisplayModification();
            displayMod.ApplyToAllFaces = false;
            displayMod.NewColor = colorIndex;
            DisplayableObject[] objArray = new DisplayableObject[1];
            objArray[0] = selectedComponent;
            displayMod.Apply(objArray);
		}
    }


    // Invoked when the Close button is clicked
    private void CloseClicked(object sender, System.EventArgs e)
    {
		Close();
    }


    // Called when a node in the tree is selected. Unhighlights the old component,
    // and highlights the new.
    private void NodeSelected(object sender, System.Windows.Forms.TreeViewEventArgs e)
    {
        HighlightComponent(selectedComponent, false);
        selectedComponent = (Component) componentTable[e.Node];
        if (selectedComponent == theSession.Parts.Display.ComponentAssembly.RootComponent)
            selectedComponent = null;
        HighlightComponent(selectedComponent, true);
    }


    // Highlights or Unhighlights a component. Depending on the the state of the drawAll
    // flag, this will either draw just the individual component, or the component plus
    // all of the equivalent components in other subassemblies.
    //
    // To see this in action, load the ToyCar assembly, and select the LEFT_WHEEL
    // component from the front axle. If drawAll is set to true, then the LEFT_WHEEL
    // component on the rear axle will be highlit as well.
    

    private void HighlightComponent(Component component, bool highlight)
    {
        if (component != null)
        {
            if (highlight)
                component.Highlight();
            else
                component.Unhighlight();


            if (drawAll)
            {
                // To find the equivalent, map "component" onto the equivalent component
                // in its owning part. Then map this equivalent component onto the array
                // of equivalents in the displayed part.

                ComponentAssembly owner = component.DirectOwner;
                Component mapped =  owner.MapComponentFromParent(component);
                ComponentAssembly topOwner = theSession.Parts.Display.ComponentAssembly;
                Component[] mappedBack  = topOwner.MapComponentsFromSubassembly(mapped);
                for (int i = 0; i < mappedBack.Length; i++) 
                {
                    if(highlight)
                        mappedBack[i].Highlight();
                    else
                        mappedBack[i].Unhighlight();

                }
            }
        }

    }


    // Radio button callbacks to set the state of the drawAll flag.
    private void singleComponentClicked(object sender, System.EventArgs e)
    {
        HighlightComponent(selectedComponent, false);
        drawAll = false;
        HighlightComponent(selectedComponent, true);
    }

    private void allComponentsClicked(object sender, System.EventArgs e)
    {
        HighlightComponent(selectedComponent, false);
        drawAll = true;
        HighlightComponent(selectedComponent, true);
    }




#region Windows Form Designer generated code
    /// <summary>
    /// Required method for Designer support - do not modify
    /// the contents of this method with the code editor.
    /// </summary>
    private void InitializeComponent()
    {
        this.assemblyTree = new System.Windows.Forms.TreeView();
        this.closeButton = new System.Windows.Forms.Button();
        this.setColorButton = new System.Windows.Forms.Button();
        this.colorBox = new System.Windows.Forms.ComboBox();
        this.groupBox1 = new System.Windows.Forms.GroupBox();
        this.singleComponentButton = new System.Windows.Forms.RadioButton();
        this.allComponentsButton = new System.Windows.Forms.RadioButton();
        this.groupBox1.SuspendLayout();

        // 
        // assemblyTree
        // 
        this.assemblyTree.ImageIndex = -1;
        this.assemblyTree.Location = new System.Drawing.Point(32, 8);
        this.assemblyTree.Name = "assemblyTree";
        this.assemblyTree.SelectedImageIndex = -1;
        this.assemblyTree.Size = new System.Drawing.Size(352, 240);
        this.assemblyTree.TabIndex = 0;
        this.assemblyTree.AfterSelect += new System.Windows.Forms.TreeViewEventHandler(this.NodeSelected);

        // 
        // setColorButton
        // 
        this.setColorButton.Location = new System.Drawing.Point(232, 288);
        this.setColorButton.Name = "setColorButton";
        this.setColorButton.TabIndex = 2;
        this.setColorButton.Text = "Set Color";
        this.setColorButton.Click += new System.EventHandler(this.SetColorClicked);
        // 
        // colorBox
        // 
        this.colorBox.Location = new System.Drawing.Point(232, 320);
        this.colorBox.Name = "colorBox";
        this.colorBox.Size = new System.Drawing.Size(121, 21);
        this.colorBox.TabIndex = 3;
        this.colorBox.Text = "colorBox";
        this.colorBox.DropDownStyle = ComboBoxStyle.DropDownList;
        
        // groupBox1
        // 
        this.groupBox1.Controls.Add(this.allComponentsButton);
        this.groupBox1.Controls.Add(this.singleComponentButton);
        this.groupBox1.Location = new System.Drawing.Point(32, 280);
        this.groupBox1.Name = "groupBox1";
        this.groupBox1.Size = new System.Drawing.Size(168, 72);
        this.groupBox1.TabIndex = 4;
        this.groupBox1.TabStop = false;
        this.groupBox1.Text = "Component Display Options";
        // 
        // allComponentsButton
        // 
        this.allComponentsButton.Location = new System.Drawing.Point(8, 40);
        this.allComponentsButton.Name = "allComponentsButton";
        this.allComponentsButton.TabIndex = 1;
        this.allComponentsButton.Text = "All Components";
        this.allComponentsButton.Text = "All Components";
        this.allComponentsButton.Click += new System.EventHandler(this.allComponentsClicked);
        // 
        // singleComponentButton
        // 
        this.singleComponentButton.Cursor = System.Windows.Forms.Cursors.Default;
        this.singleComponentButton.Location = new System.Drawing.Point(8, 16);
        this.singleComponentButton.Name = "singleComponentButton";
        this.singleComponentButton.Size = new System.Drawing.Size(120, 24);
        this.singleComponentButton.TabIndex = 0;
        this.singleComponentButton.Text = "Single Component";
        this.singleComponentButton.Checked = true;
        this.singleComponentButton.Click += new System.EventHandler(this.singleComponentClicked);
        // 
        // closeButton
        // 
        this.closeButton.Location = new System.Drawing.Point(232, 376);
        this.closeButton.Name = "closeButton";
        this.closeButton.TabIndex = 5;
        this.closeButton.Text = "Close";
        this.closeButton.Click += new System.EventHandler(this.CloseClicked);

        // 
        // AssemblyViewer
        // 
        this.AutoScaleBaseSize = new System.Drawing.Size(5, 13);
        this.ClientSize = new System.Drawing.Size(408, 413);
        this.Controls.Add(this.closeButton);
        this.Controls.Add(this.groupBox1);
        this.Controls.Add(this.colorBox);
        this.Controls.Add(this.setColorButton);
        this.Controls.Add(this.assemblyTree);
        this.Name = "AssemblyViewer";
        this.Text = "Assembly Viewer";
        this.Closing += new System.ComponentModel.CancelEventHandler(this.OnClose);
        this.groupBox1.ResumeLayout(false);
        this.ResumeLayout(false);

    }
#endregion


    //--------------------------------------------------------------------------
    // The main interface by which NX will start and stop the application
    //--------------------------------------------------------------------------


    // The main entry point. Called when this library is loaded

	public static void Main() 
    {
        theSession = Session.GetSession();
        theUFSession = UFSession.GetUFSession();
        theViewer = new AssemblyViewer();
        theViewer.Show();
    }
    

    // Called to determine whether this library can be unloaded

    public static int GetUnloadOption(string arg)
    {
        // Return code to indicate this library can be unloaded
        // by the user.
        return (int) Session.LibraryUnloadOption.Explicitly;
    }


    // Called by NX when the library is unloaded.

    public static int UnloadLibrary(string arg)
    {
        if (theViewer != null)
        {
            // Ensure that the callbacks are unregistered. It is important to do this
            // before the library is unloaded, otherwise an error will occur the next time
            // NX tries to invoke the callback.
            theViewer.UnregisterCallbacks();
            theViewer.Close();
            theViewer.Dispose();
            theViewer = null;
        }
        return 0;
    }



} 
