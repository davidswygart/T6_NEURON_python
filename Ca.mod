: Bipolar cell Calcium  channel
: original .Mod file from Kourenny and  Liu 2002   ABME 30 : 1196-1203
: modified to fit data from Berntson A, Taylor WR, Morgans CW. (2003) PMID: 12478624.

NEURON
{
	SUFFIX Ca

	USEION Ca WRITE iCa VALENCE 2
	RANGE gMax,VhalfCam,SCam
	RANGE VhalfCah,SCah
	RANGE eCa,aomCa,bomCa
	RANGE gammaohCa,deltaohCa
	RANGE mTauMult , hTauMult
	RANGE gCa
}

UNITS
{
	(pS) = (picosiemens)
	(um) = (micron)
	(mA) = (milliamp)
	(mV) = (millivolt)
}

PARAMETER
{
 	gMax = 0  (pS/um2) <0,1e9>	:set in NEURON only for active model [Berntson, 2003]
	eCa =  18 (mV)				:reversal potential for calcium [Berntson, 2003]

	mTauMult = 1
	hTauMult = 1

:Activation
	VhalfCam = -32 (mV)		:half-max of activation: modified to match IV from Berntson, 2003
	SCam =  10 (mV)			:slope of activation: modified to match IV from Berntson, 2003
	aomCa = 0.05 (/ms)			:opening rate multiplier
	bomCa = 0.05 (/ms)			:closing rate multiplier

:Deactivation
	VhalfCah = -10 (mV)		:half-max of inactivation: modified to match IV from Berntson, 2003
	SCah = 12 (mV)			:slope of inactivation: modified to match IV from Berntson, 2003
	gammaohCa = 0.001 (/ms)		:opening rate multiplier
	deltaohCa = 0.001 (/ms)		:closing rate multiplier
}

STATE
{
	mCa
	hCa
}

ASSIGNED
{
	gCa (pS/um2)
	v (mV)
	iCa (mA/cm2)
	infmCa
	taumCa  (ms)
	infhCa
	tauhCa (ms)
}

INITIAL
{
	rate(v)
	mCa = infmCa
	hCa = infhCa
}

BREAKPOINT
{
	SOLVE states METHOD cnexp
	gCa = gMax*mCa*hCa
	iCa = gCa*(v - eCa) * (1e-12) * (1e+08) :conversion factors for femtosiemens -> S and um -> cm
}

DERIVATIVE states
{
	rate(v)
	mCa' = (infmCa-mCa)/taumCa
	hCa'= (infhCa-hCa)/tauhCa
}

FUNCTION alphamCa(v(mV))(/ms)
{
	alphamCa = aomCa*exp((v - VhalfCam)/(2*SCam))
}

FUNCTION betamCa(v(mV))(/ms)
{
	betamCa = bomCa*exp( - (v-VhalfCam)/(2*SCam))
}
FUNCTION gammahCa(v(mV))(/ms)
{
	gammahCa = gammaohCa*exp( (v-VhalfCah)/(2*SCah))
}

FUNCTION deltahCa(v(mV))(/ms)
{
	deltahCa = deltaohCa*exp( - (v-VhalfCah)/(2*SCah))
}

PROCEDURE rate(v (mV))
{
    LOCAL a, b,c, d

	a = alphamCa(v)
	b = betamCa(v)
	taumCa = mTauMult* 1/(a + b)
	infmCa = a/(a + b)

	c = gammahCa(v)
	d = deltahCa(v)
	tauhCa = hTauMult* 1/(c + d)
	infhCa = d/(c + d)
	
}
