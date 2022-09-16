: HCN2 channel
: original .Mod file Channelpedia https://channelpedia.epfl.ch/wiki/ionchannels/62 ; Model HCN2 (ID=10) 
: Reference :Cellular expression and functional characterization of four hyperpolarization-activated pacemaker channels in cardiac and neuronal tissues. Eur. J. Biochem., 2001, 268, 1646-52

NEURON	{
	SUFFIX hcn2
	NONSPECIFIC_CURRENT ihcn
	RANGE gMax, gHCN2, ihcn, mTauMult
}

UNITS	{
	(S) = (siemens)
	(pS) = (picosiemens)
	(um) = (micron)
	(mA) = (milliamp)
	(mV) = (millivolt)
}

PARAMETER	{
	gMax = 0 (pS/um2) <0,1e9> :set in NEURON only for active model
	ehcn = -23.4 (mV)	:HCN reversal potential [ref. Byczkowicz 2009, PMID: 31496517]
	mVHalf = -99 (mV) :half-max of activation
	mVWidth = 6.2 (mV) :slope of activation

	mTauBaseline = 184 (ms)
	mTauMult = 1


}

ASSIGNED	{
	v		(mV)
	ihcn	(mA/cm2)
	gHCN2	(S/cm2)
	mInf
	mTau	(ms)
}

STATE	{
	m
}

BREAKPOINT	{
	SOLVE states METHOD cnexp
	gHCN2 = gMax*(1e-4) * m :to convert gMax from pS/um2 to S/cm2 multiply by 1e-4
	ihcn = gHCN2*(v-ehcn)
}

DERIVATIVE states	{
	rates()
	m' = (mInf-m)/mTau
}

INITIAL{
	rates()
	m = mInf
}

PROCEDURE rates(){
		mInf = 1/(1+exp((mVHalf-v)/mVWidth))
		mTau = mTauBaseline * mTauMult
}
