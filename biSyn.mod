COMMENT
a binary synapse whos conductance immediately jumps to gmax and does not decay
        i = g * (v - e)      i(nanoamps), g(microsiemens);
        where
         g = 0 for t < onset and
         g = gmax for t>= onset
          for t > onset
ENDCOMMENT

NEURON {
	POINT_PROCESS biSyn
	RANGE onset, gmax, e, i
	NONSPECIFIC_CURRENT i
}
UNITS {
	(nA) = (nanoamp)
	(mV) = (millivolt)
	(pS) = (picosiemens)
}

PARAMETER {
	onset=0 (ms)
	gmax=0 	(pS)	<0,1e9>
	e=0	(mV)
}

ASSIGNED {
	v (mV)
	i (nA)  
	g (pS)
	}

BREAKPOINT {
	if (gmax) { at_time(onset) }
	g = gmax * isT((t - onset)/onset)
	i = g*(v - e) * (1e-06)
}

FUNCTION isT(x) {
	if (x < 0) {
		isT = 0
	}else{
		isT = 1
	}
}
