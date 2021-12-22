TITLE passive membrane channel

UNITS {
	(mV) = (millivolt)
	(mA) = (milliamp)
	(S) = (siemens)
}

NEURON {
	SUFFIX gapJ
	NONSPECIFIC_CURRENT i
	RANGE g, e
}

PARAMETER {
	g = 0	(S/cm2)	<0,1e9>
	e = -35	(mV)
}

ASSIGNED {v (mV)  i (mA/cm2)}

BREAKPOINT {
	i = g*(v - e)
}
