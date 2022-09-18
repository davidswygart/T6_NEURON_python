:[$URL: https://bbpteam.epfl.ch/svn/analysis/trunk/IonChannel/xmlTomod/CreateMOD.c $]
:[$Revision: 1499 $]
:[$Date: 2012-01-28 10:45:44 +0100 (Sat, 28 Jan 2012) $]
:[$Author: rajnish $]
:Comment :
:Reference :Effects of charybdotoxin on K+ channel (KV1.2) deactivation and inactivation kinetics. Eur. J. Pharmacol., 1996, 314, 357-64

NEURON	{
	SUFFIX Kv1_2
	USEION k READ ek WRITE ik
	RANGE gMax, gKv1_2, ik, mTauMult, hTauMult, mVHalf, mVWidth, hVHalf, hVWidth
}

UNITS	{
	(pS) = (picosiemens)
	(um) = (micron)
	(mV) = (millivolt)
	(mA) = (milliamp)
}

PARAMETER	{
	gMax = 0 (pS/um2) <0,1e9>

	:Activation

	mVHalf = -21 (mV) :half-max of activation
	mVWidth = 11 (mV) :slope of activation
	mTauMult = 1


	:Inactivation
	hVHalf = -22 (mV) :half-max of inactivation
	hVWidth = -11 (mV) :slope of inactivation
	hTauMult = 1
}

ASSIGNED	{
	v	(mV)
	ek	(mV)
	ik	(mA/cm2)
	gKv1_2	(pS/um2)
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
	gKv1_2 = gMax*m*h
	ik = gKv1_2*(v-ek) * (1e-12) * (1e+08) :conversion factors for femtosiemens -> S and um -> cm
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
	mInf = 1 / (1+ exp((mVHalf-v) / mVWidth))
	mTau = mTauMult*(150.0000/(1+ exp((v - -67.5600)/34.1479)))

	hInf = 1 / (1 + exp((hVHalf-v) / hVWidth))
	hTau = hTauMult*(15000.0000/(1+ exp((v - -46.5600)/-44.1479)))
}
