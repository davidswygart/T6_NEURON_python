:[$URL: https://bbpteam.epfl.ch/svn/analysis/trunk/IonChannel/xmlTomod/CreateMOD.c $]
:[$Revision: 1499 $]
:[$Date: 2012-01-28 10:45:44 +0100 (Sat, 28 Jan 2012) $]
:[$Author: rajnish $]
:Comment :
:Reference :Subunit-specific modulation of T-type calcium channels by zinc. J. Physiol. (Lond.), 2007, 578, 159-71

NEURON	{
	SUFFIX Cav3_1
	USEION ca READ eca WRITE ica
	RANGE gCav3_1bar, gCav3_1, ica, m_vHalf, h_vHalf
}

UNITS	{
	(S) = (siemens)
	(mV) = (millivolt)
	(mA) = (milliamp)
}

PARAMETER	{
	gCav3_1bar = 0.00001 (S/cm2)
	m_vHalf = -42.921064
	h_vHalf = -72.907420
}

ASSIGNED	{
	v	(mV)
	eca	(mV)
	ica	(mA/cm2)
	gCav3_1	(S/cm2)
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
	gCav3_1 = gCav3_1bar*m*h
	ica = gCav3_1*(v-eca)
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
		mInf = 1 /(1+exp((v-(m_vHalf))/-5.163208))
		if(v < -10){
			mTau = -0.855809 + (1.493527 * exp(-v/27.414182))
		}
		if(v >= -10){
			mTau = 1.0
		}
		hInf = 1 /(1+exp((v-(h_vHalf))/4.575763))
		hTau = 9.987873 + (0.002883 * exp(-v/5.598574))
	UNITSON
}
