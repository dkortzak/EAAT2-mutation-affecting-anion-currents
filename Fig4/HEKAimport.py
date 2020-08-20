# -*- coding: utf-8 -*-
"""
Created on Mon Aug 04 13:55:38 2014

@author: Stölting
"""
import sys
import struct
import numpy as np
import PULimport
import PGFimport
import DATimport

from PyQt4 import QtGui
from PyQt4.QtCore import SIGNAL, SLOT
from HEKATree import Ui_Dialog as Dlg

import matplotlib
import matplotlib.gridspec as gridspec
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar

import scalebars as sb

"""
class MeinDialog(QtGui.QDialog, Dlg):
    
    def __init__(self):
        QtGui.QDialog.__init__(self)
              
        setupUi(self)



        figure = Figure()

        canvas = FigureCanvas(figure)
        toolbar = NavigationToolbar(canvas, self)
        layout = QtGui.QVBoxLayout()
        layout.addWidget(toolbar)
        layout.addWidget(canvas)
        widget.setLayout(layout)
        
        #quitButton.clicked.connect(onQuit)
        displayButton.clicked.connect(onDisplay)
        openButton.clicked.connect(onOpen)
        treeView.clicked.connect(treeSelection) 
        treeView.doubleClicked.connect(onDisplay)
        
        raise_()
        
        
        activateWindow()
        
        selected_group = 0
        selected_series = 0
        
        matplotlib.rc_file("matplotlibrc")
        

"""
        
def loadPatchmasterFile(self, filename):
        
        if filename is "":
            return      
                
        patchmaster_file = open(filename, 'rb')
        patchmaster_data = patchmaster_file.read()      
        if "DAT2" not in str(struct.unpack("8s", patchmaster_data[0:8])[0]):
            print("Sorry, but this does not appear to be a properly bundled HEKA Patchmaster file.")
            quit()
        number_of_items = struct.unpack('i', patchmaster_data[48:52])[0]
        start_dict = {}
        stop_dict = {}
        for i in np.arange(0, number_of_items):
            data_type = b"".join(struct.unpack("4c", patchmaster_data[72+(i*16):76+(i*16)]))
            start_dict[data_type] = int(struct.unpack("i", patchmaster_data[64+(i*16):68+(i*16)])[0])
            stop_dict[data_type] = int(struct.unpack("i", patchmaster_data[68+(i*16):72+(i*16)])[0])   
        
        pulfile = PULimport.PULfile(patchmaster_data, int(start_dict[b".pul"]))
        pgffile = PGFimport.PGFfile(patchmaster_data, int(start_dict[b".pgf"]))
        model = QtGui.QStandardItemModel()
        model.setHorizontalHeaderLabels([filename])
        #treeView.setUniformRowHeights(True)
        #treeView.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers) # The TreeView should not be editable
        print ("C")
        for group in pulfile.Groups:
            parent_group = QtGui.QStandardItem(group.Label.decode())
            parent_group.setSelectable(False)
            for series in group.Series:
                parent_group.appendRow(QtGui.QStandardItem(series.Label.decode()))
            model.appendRow(parent_group)
        print ("D")
        #treeView.setModel(model)        
        
   # def onQuit(self):
        close()
        exit()
        
    #def onOpen(self):
    #    filename = QtGui.QFileDialog.getOpenFileName(self, "Open File...", "/", "HEKA Patchmaster (*.dat)")    
   #     loadPatchmasterFile(filename)
        
    #def onDisplay(self):
        if selected_group < 0:
            print("Can't display group", selected_group, selected_series)
        else :
            figure.clf()
            gs = gridspec.GridSpec(2,1, height_ratios=[1,3])
            vol_ax = figure.add_subplot(gs[0])
            cm_ax = figure.add_subplot(gs[1])
            cm_ax.hold(False) 
            
            for sweep in pulfile.Groups[selected_group].Series[selected_series].Sweeps:
                tr_plot = 0 # Cm Trace
                ########
                trace_data = DATimport.DATload(patchmaster_data, sweep.Traces[tr_plot].Data, sweep.Traces[tr_plot].DataPoints, sweep.Traces[tr_plot].DataFormat, (sweep.Traces[tr_plot].DataScaler*10**12), False)    
                ### trace_data beinhaltet alle Datenpunkte von einem (!) Sweep
                cm_ax.plot(np.arange(0,sweep.Traces[tr_plot].DataPoints*sweep.Traces[tr_plot].XInterval, sweep.Traces[tr_plot].XInterval), trace_data)
                cm_ax.hold(True)
                vol_start = 0
                print sweep
            
            xscale = 0.1*(sweep.Traces[0].DataPoints*sweep.Traces[0].XInterval)
            xscale_string = str((100*(sweep.Traces[0].DataPoints*sweep.Traces[0].XInterval))) + " ms"
            
            cm_ax.axis('off')  # Don't show regular axis in order to not interfere with the scalebar
            vol_ax.axis('off')  # Don't show voltage axis
            
            if cm_ax.axis()[3] < 100:
                yscale = 100
                yscale_string = "0.1 nA"
            else:
                yscale = 1000
                yscale_string = "1 nA"
                
            sb.add_scalebar(cm_ax, matchx=False, matchy=False, hidex=True, hidey=True, sizex=xscale, sizey=yscale, labelx=xscale_string, labely=yscale_string, loc=3)
            
            canvas.draw()
    
    def treeSelection(self, newSelection):
        selected_group = int(newSelection.parent().row())
        selected_series = int(newSelection.row())
        
        

##### Begin of main routine

# Start with the definition of the combined data
#print "".join(struct.unpack('8c', patchmaster_data[0:8]))
 
app = QtGui.QApplication(sys.argv)
dialog = MeinDialog()
dialog.show()
app.connect(app, SIGNAL("lastWindowClosed()"), app, SLOT("quit()"))
rc = app.exec_()
exit(rc)
