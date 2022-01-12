: Rod  Photoreceptor Ca and Calcium  channel
: Ref. Kourenny and  Liu 2002   ABME 30 : 1196-1203
: Modification 2004-02-07
NEURON
{
	SUFFIX Ca

	USEION Ca WRITE iCa VALENCE 2
        RANGE gCabar,VhalfCam,SCam
        RANGE VhalfCah,SCah
        RANGE eCa,aomCa,bomCa
        RANGE gammaohCa,deltaohCa
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
       : Calcium channel
			 gCabar = 4  (pS/um2) <0,1e9>
       eCa =  40 (mV)

			 : Activation
       VhalfCam = -32 (mV) : modified to match IV from; Berntson A, Taylor WR, Morgans CW. (2003) PMID: 12478624.
			 SCam =  10    (mV) : modified to match IV from; Berntson A, Taylor WR, Morgans CW. (2003) PMID: 12478624.
			 aomCa = 50   (/s)  :opening rate multiplier
			 bomCa = 50   (/s)  :closing rate multiplier

			 : Deactivation
			 VhalfCah = 10 (mV)
			 SCah = 9     (mV)
			 gammaohCa = 1 (/s) :opening rate multiplier
			 deltaohCa = 1 (/s) :closing rate multiplier
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
	gCa = gCabar*mCa*hCa
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
	alphamCa = (0.001)*aomCa*exp( (v - VhalfCam)/(2*SCam)   )
}

FUNCTION betamCa(v(mV))(/ms)
{
	betamCa = (0.001)*bomCa*exp( - ( v-VhalfCam)/(2*SCam) )
}
FUNCTION gammahCa(v(mV))(/ms)
{
	gammahCa = (0.001)*gammaohCa*exp( (v - VhalfCah)/(2*SCah))
}

FUNCTION deltahCa(v(mV))(/ms)
{
	deltahCa = (0.001)*deltaohCa*exp( - ( v-VhalfCah)/(2*SCah) )
}


PROCEDURE rate(v (mV))
{
        LOCAL a, b,c, d


	a = alphamCa(v)
	b = betamCa(v)
	taumCa = 1/(a + b)
	infmCa = a/(a + b)

	c = gammahCa(v)
	d = deltahCa(v)
	tauhCa = 1/(c + d)
	infhCa = d/(c + d)

}
