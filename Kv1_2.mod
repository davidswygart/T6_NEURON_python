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
	(S) = (siemens)
}

PARAMETER	{
	gMax = 0 (pS/um2) <0,1e9>

	:Activation

	mVHalf = -9 (mV) :half-max of activation
	mVWidth = 14 (mV) :slope of activation

	mTauVHalf = -67.56 (mV) :half-max of activation tau
	mTauVWidth = 34.1479 (mV) :slope of activation tau
	mTauMult = 150 (ms)


	:Inactivation
	hVHalf = 8 (mV) :half-max of inactivation
	hVWidth = -9 (mV) :slope of inactivation

	hTauVHalf = -46.56 (mV) :half-max of inactivation tau
	hTauVWidth = -44.1479 (mV) :slope of inactivation tau
	hTauMult = 1500 (ms)
}

ASSIGNED	{
	v	(mV)
	ek	(mV)
	ik	(mA/cm2)
	gKv1_2	(S/cm2)
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
	gKv1_2 = gMax*m*h * (1e-4)
	ik = gKv1_2*(v-ek)
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
	mTau = mTauMult/(1+ exp((v-mTauVHalf) / mTauVWidth))

	hInf = 1 / (1 + exp((hVHalf-v) / hVWidth))
	hTau = hTauMult/(1+ exp((v - hTauVHalf)/hTauVWidth))
}
