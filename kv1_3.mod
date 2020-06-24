:[$URL: https://bbpteam.epfl.ch/svn/analysis/trunk/IonChannel/xmlTomod/CreateMOD.c $]
:[$Revision: 1499 $]
:[$Date: 2012-01-28 10:45:44 +0100 (Sat, 28 Jan 2012) $]
:[$Author: rajnish $]
:Comment :
:Reference :Characterization and functional expression of a rat genomic DNA clone encoding a lymphocyte potassium channel. J. Immunol., 1990, 144, 4841-50

NEURON	{
	SUFFIX Kv1_3
	USEION k READ ek WRITE ik
	RANGE gKv1_3bar, gKv1_3, ik
}

UNITS	{
	(S) = (siemens)
	(mV) = (millivolt)
	(mA) = (milliamp)
}

PARAMETER	{
	gKv1_3bar = 0.00001 (S/cm2)
}

ASSIGNED	{
	v	(mV)
	ek	(mV)
	ik	(mA/cm2)
	gKv1_3	(S/cm2)
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
	gKv1_3 = gKv1_3bar*m*h
	ik = gKv1_3*(v-ek)
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
		mInf = 1.0000/(1+ exp((v - -14.1000)/-10.3000))
		if(v < 50){
			mTau = (-0.2840 * v) + 19.1600
		}
		if(v >= 50){
			mTau = 5
		}
		hInf = 1.0000/(1+ exp((v - -33.0000)/3.7000))
		if(v < 80){
			hTau = (-13.7600 * v) + 1162.4000
		}
		if(v >= 80){
			hTau = 60
		}
	UNITSON
}
