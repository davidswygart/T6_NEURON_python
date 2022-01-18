TITLE HCN2 with one time constant
: Konstantin Stadler 2009

UNITS {
	(pS) = (picosiemens)
	(um) = (micron)
	(mA) = (milliamp)
	(mV) = (millivolt)
}

PARAMETER {
	gMax = 1.5	(pS/um2) <0,1e9>
	v 		(mV)
	Vrev  = -40	(mV)


	vhakt = -93.6		(mV)
	k     = -11.9		(mV)

	vhtau = -84.6		(mV)
	a0t   = 0.00372		(/ms)
	zetat = 1.5		(/mV)
	gmt   = .561	(1)

	celsius		(degC)
	temp  = 23	(degC)
	q10   = 4.5		(1)
	qtl   = 1		(1)
}


NEURON {
	SUFFIX hcn2
	NONSPECIFIC_CURRENT i
    	RANGE gMax, vhakt, a0t
}

STATE {
        l
}

ASSIGNED {
	i (mA/cm2)
    	linf (1)
    	taul (ms)
    	ghd (pS/um2)
}

INITIAL {
	rate(v)
	l=linf
}


BREAKPOINT {
	SOLVE states METHOD cnexp
	ghd = gMax*l
	i = ghd*(v-Vrev) * (1e-12) * (1e+08) :conversion factors for femtosiemens -> S and um -> cm

}


FUNCTION alpt(v(mV)) (1) {
  alpt = exp(0.0378*zetat*(v-vhtau))
}

FUNCTION bett(v(mV)) (1) {
  bett = exp(0.0378*zetat*gmt*(v-vhtau))
}

DERIVATIVE states {
        rate(v)
        l' =  (linf - l)/taul
}

PROCEDURE rate(v (mV)) {
        LOCAL a,b,qt

        qt=q10^((celsius-temp)/10(degC))
        a = alpt(v)			:a und b fuer tau
        b = bett(v)
        linf = 1/(1 + exp(-(v-vhakt)/k))
        taul = b/(qtl*qt*a0t*(1+a))
}
