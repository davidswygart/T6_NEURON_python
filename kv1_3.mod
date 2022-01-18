:[$URL: https://bbpteam.epfl.ch/svn/analysis/trunk/IonChannel/xmlTomod/CreateMOD.c $]
:[$Revision: 1499 $]
:[$Date: 2012-01-28 10:45:44 +0100 (Sat, 28 Jan 2012) $]
:[$Author: rajnish $]
:Comment :
:Reference :Characterization and functional expression of a rat genomic DNA clone encoding a lymphocyte potassium channel. J. Immunol., 1990, 144, 4841-50

NEURON	{
	SUFFIX Kv1_3
	USEION k READ ek WRITE ik
	RANGE gMax, gKv1_3, ik
}

UNITS	{
	(pS) = (picosiemens)
	(um) = (micron)
	(mV) = (millivolt)
	(mA) = (milliamp)
}

PARAMETER	{
	gMax = 0.1 (pS/um2) <0,1e9>


	:Activation
	a = 1 (/ms) :opening rate multiplier (doesn't use voltage to calculate)
	bMult = 1 (/ms) :closing rate multiplier
	vHalfB = -14.1 (mV) :voltage center for calculating closing rate of activation
	widthB = -10.3 (mV) :voltage width for calculating closing rate of activation
	mTauMult = 1 (ms/mV) :scale factor for tau of activation (used to get correct units)

	:Inactivation
	c = 1 (/ms) :opening rate multiplier
	dMult = 1 (/ms) :closing rate multiplier
	vHalfD = -33 (mV)
	widthD = 3.7 (mV)
	hTauMult = 1 (ms/mV) :scale factor for tau of inactivation (used to get correct units)
}

ASSIGNED	{
	v	(mV)
	ek	(mV)
	ik	(mA/cm2)
	gKv1_3	(pS/um2)
	mInf
	mTau (ms)
	hInf
	hTau (ms)
}

STATE	{
	m
	h
}

BREAKPOINT	{
	SOLVE states METHOD cnexp
	gKv1_3 = gMax*m*h
	ik = gKv1_3*(v-ek) * (1e-12) * (1e+08) :conversion factors for femtosiemens -> S and um -> cm
}

DERIVATIVE states	{
	rates()
	m' = (mInf-m)/mTau
	h' = (hInf-h)/hTau
}

INITIAL{
	rates()
	m = mInf
	h = hInf
}

PROCEDURE rates(){
	LOCAL b, d

	b = bMult * exp((v - vHalfB)/ widthB)

	mInf = a / (a + b)

	if(v < 50){
		mTau = mTauMult * ((-0.284 * v) + 19.16)
	}
	if(v >= 50){
		mTau = mTauMult * ((0 * v) + 5)
	}

	d = dMult * exp((v - vHalfD)/widthD)
	hInf = c/(c + d)
	if(v < 80){
		hTau = hTauMult * ((-13.76 * v) + 1162.4)
	}
	if(v >= 80){
		hTau = hTauMult * ((0 * v) + 60)
	}
}
