from qiskit_metal import designs
from qiskit_metal import MetalGUI
from qiskit_metal.qlibrary.qubits.transmon_cross import TransmonCross


design = designs.DesignPlanar()


gui = MetalGUI(design)


qubit = TransmonCross(
    design,
    'Q1',
    options=dict(
        pos_x='0mm',
        pos_y='0mm',
        cross_width='20um',
        cross_length='200um',
        cross_gap='20um',
        connection_pads=dict(
            readout=dict(
                connector_location='0',
                connector_gap='10um',
                connector_width='10um'
            )
        )
    )
)


gui.rebuild()
gui.autoscale()
gui.show()
gui.qApp.exec_()