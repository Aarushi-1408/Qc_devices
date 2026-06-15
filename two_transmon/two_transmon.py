from qiskit_metal import designs
from qiskit_metal import MetalGUI
from qiskit_metal.qlibrary.qubits.transmon_cross import TransmonCross


design = designs.DesignPlanar()


gui = MetalGUI(design)


q1 = TransmonCross(
    design,
    'Q1',
    options=dict(
        pos_x='-0.5mm',
        pos_y='0mm',
        cross_width='20um',
        cross_length='200um',
        cross_gap='20um'
    )
)


q2 = TransmonCross(
    design,
    'Q2',
    options=dict(
        pos_x='0.5mm',
        pos_y='0mm',
        cross_width='20um',
        cross_length='200um',
        cross_gap='20um'
    )
)

gui.rebuild()
gui.autoscale()
gui.show()
gui.qApp.exec_()