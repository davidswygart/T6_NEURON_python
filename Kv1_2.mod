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
	(S) = (siemens)
	(mV) = (millivolt)
	(mA) = (milliamp)
}

PARAMETER	{
	gKv1_2bar = 0.00001 (S/cm2)
}

ASSIGNED	{
	v	(mV)
	ek	(mV)
	ik	(mA/cm2)
	gKv1_2	(S/cm2)
	mInf
	mTau
	hInf
	hTau
}

STATE	{
	m
	h
}

BREAKPOINT	{
	SOLVE states METHOD cnexp
	gKv1_2 = gKv1_2bar*m*h
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
	UNITSOFF
		mInf = 1.0000/(1+ exp((v - -21.0000)/-11.3943))
		mTau = 150.0000/(1+ exp((v - -67.5600)/34.1479))
		hInf = 1.0000/(1+ exp((v - -22.0000)/11.3943))
		hTau = 15000.0000/(1+ exp((v - -46.5600)/-44.1479))
	UNITSON
}
