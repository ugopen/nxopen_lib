package nxopen.examples.assemblies;
/*
 * Created on Feb 24, 2005
 * 
 * Copyright 2005 UGS Corp. All Rights Reserved.
 * 
 */
/**
 * @author pesumner
 * Interface used by AssemblyListing.walk to specify the operation to be
 * performed on the component
 */
public interface IComponentFunctor {

    public void execute (nxopen.assemblies.Component c);

}
