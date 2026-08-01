/*
 * Created on Mar 2, 2005
 * 
 * Copyright 2005 UGS Corp. All Rights Reserved.
 * 
 */
package nxopen.examples.assemblies;

import nxopen.assemblies.Component;

/**
 * @author pesumner
 * Contains a Component and a count of the number of times the component
 * appears in the assembly.
 */
public class BOMPair {
    
    private Component comp;
    private int count;
    
    public BOMPair(Component c, int num) {
        comp = c;
        count = num;
    }

    /**
     * @return Returns the comp.
     */
    public Component getComponent() {
        return comp;
    }
    /**
     * @return Returns the count.
     */
    public int getCount() {
        return count;
    }
    
    public void incrementCount(){
        ++count;
    }
}
