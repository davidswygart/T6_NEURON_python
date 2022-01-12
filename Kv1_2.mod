:[$URL: https://bbpteam.epfl.ch/svn/analysis/trunk/IonChannel/xmlTomod/CreateMOD.c $]
:[$Revision: 1499 $]
:[$Date: 2012-01-28 10:45:44 +0100 (Sat, 28 Jan 2012) $]
:[$Author: rajnish $]
:Comment :
:Reference :Effects of charybdotoxin on K+ channel (KV1.2) deactivation and inactivation kinetics. Eur. J. Pharmacol., 1996, 314, 357-64

NEURON	{
	SUFFIX Kv1_2
	USEION k READ ek WRITE ik
	RANGE gKv1_2bar, gKv1_2, ik
}

UNITS	{
	(pS) = (picosiemens)
	(um) = (micron)
	(mV) = (millivolt)
	(mA) = (milliamp)
}

PARAMETER	{
	gKv1_2bar = 0.1 (pS/um2) <0,1e9>

	:Activation
	a = 1 (/ms) :opening rate of activation (doesn't use voltage to calculate)
	bMult = 1 (/ms)
	mVHalf = -21 (mV) :voltage center for calculating activation %
	mVWidth = -11.3943 (mV) :voltage width for calculating activation %
	mTauVHalf = -67.56 (mV) :voltage center for calculating activation tau
	mTauVWidth =  34.1479 (mV) :voltage width for calculating activation tau


	:Inactivation
	c = 1 (/ms) :opening rate of inactivation (doesn't use voltage to calculate)
	dMult = 1 (/ms)
	hVHalf = -22 (mV)
	hVWidth = 11.3943 (mV)
	hTauVHalf = -46.5600 (mV)
	hTauVWidth = -44.1479 (mV)
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
	gKv1_2 = gKv1_2bar*m*h
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
	mInf = a / (a + bMult * exp((v - mVHalf) / mVWidth))
	mTau = 150 / (a + bMult * exp((v - mTauVHalf) / mTauVWidth))

	hInf = c / (c + dMult * exp((v - hVHalf) / hVWidth))
	hTau = 15000 / (c + dMult * exp((v - hTauVHalf) / hTauVWidth))
}
