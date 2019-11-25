/* Created by Language version: 7.5.0 */
/* VECTORIZED */
#define NRN_VECTORIZED 1
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "scoplib_ansi.h"
#undef PI
#define nil 0
#include "md1redef.h"
#include "section.h"
#include "nrniv_mf.h"
#include "md2redef.h"
 
#if METHOD3
extern int _method3;
#endif

#if !NRNGPU
#undef exp
#define exp hoc_Exp
extern double hoc_Exp(double);
#endif
 
#define nrn_init _nrn_init__BKCAm
#define _nrn_initial _nrn_initial__BKCAm
#define nrn_cur _nrn_cur__BKCAm
#define _nrn_current _nrn_current__BKCAm
#define nrn_jacob _nrn_jacob__BKCAm
#define nrn_state _nrn_state__BKCAm
#define _net_receive _net_receive__BKCAm 
#define kin kin__BKCAm 
#define prates prates__BKCAm 
#define rates rates__BKCAm 
 
#define _threadargscomma_ _p, _ppvar, _thread, _nt,
#define _threadargsprotocomma_ double* _p, Datum* _ppvar, Datum* _thread, _NrnThread* _nt,
#define _threadargs_ _p, _ppvar, _thread, _nt
#define _threadargsproto_ double* _p, Datum* _ppvar, Datum* _thread, _NrnThread* _nt
 	/*SUPPRESS 761*/
	/*SUPPRESS 762*/
	/*SUPPRESS 763*/
	/*SUPPRESS 765*/
	 extern double *getarg();
 /* Thread safe. No static _p or _ppvar. */
 
#define t _nt->_t
#define dt _nt->_dt
#define gkbar _p[0]
#define kon _p[1]
#define kcoff _p[2]
#define kooff _p[3]
#define c0o0c _p[4]
#define c0c1c _p[5]
#define o0c0c _p[6]
#define o0o1c _p[7]
#define o4c4c _p[8]
#define c4o4c _p[9]
#define hva _p[10]
#define hvi _p[11]
#define sla _p[12]
#define sli _p[13]
#define ik _p[14]
#define a _p[15]
#define b _p[16]
#define o _p[17]
#define c0 _p[18]
#define c1 _p[19]
#define c2 _p[20]
#define c3 _p[21]
#define c4 _p[22]
#define o0 _p[23]
#define o1 _p[24]
#define o2 _p[25]
#define o3 _p[26]
#define o4 _p[27]
#define cai _p[28]
#define ek _p[29]
#define c0c1 _p[30]
#define c1c0 _p[31]
#define c1c2 _p[32]
#define c2c1 _p[33]
#define c2c3 _p[34]
#define c3c2 _p[35]
#define c3c4 _p[36]
#define c4c3 _p[37]
#define o0o1 _p[38]
#define o1o0 _p[39]
#define o1o2 _p[40]
#define o2o1 _p[41]
#define o2o3 _p[42]
#define o3o2 _p[43]
#define o3o4 _p[44]
#define o4o3 _p[45]
#define c0o0 _p[46]
#define o0c0 _p[47]
#define c1o1 _p[48]
#define o1c1 _p[49]
#define c2o2 _p[50]
#define o2c2 _p[51]
#define c3o3 _p[52]
#define o3c3 _p[53]
#define c4o4 _p[54]
#define o4c4 _p[55]
#define Dc0 _p[56]
#define Dc1 _p[57]
#define Dc2 _p[58]
#define Dc3 _p[59]
#define Dc4 _p[60]
#define Do0 _p[61]
#define Do1 _p[62]
#define Do2 _p[63]
#define Do3 _p[64]
#define Do4 _p[65]
#define v _p[66]
#define _g _p[67]
#define _ion_ek	*_ppvar[0]._pval
#define _ion_ik	*_ppvar[1]._pval
#define _ion_dikdv	*_ppvar[2]._pval
#define _ion_cai	*_ppvar[3]._pval
 
#if MAC
#if !defined(v)
#define v _mlhv
#endif
#if !defined(h)
#define h _mlhh
#endif
#endif
 
#if defined(__cplusplus)
extern "C" {
#endif
 static int hoc_nrnpointerindex =  -1;
 static Datum* _extcall_thread;
 static Prop* _extcall_prop;
 /* external NEURON variables */
 /* declaration of user functions */
 static void _hoc_prates(void);
 static void _hoc_rates(void);
 static int _mechtype;
extern void _nrn_cacheloop_reg(int, int);
extern void hoc_register_prop_size(int, int, int);
extern void hoc_register_limits(int, HocParmLimits*);
extern void hoc_register_units(int, HocParmUnits*);
extern void nrn_promote(Prop*, int, int);
extern Memb_func* memb_func;
 extern void _nrn_setdata_reg(int, void(*)(Prop*));
 static void _setdata(Prop* _prop) {
 _extcall_prop = _prop;
 }
 static void _hoc_setdata() {
 Prop *_prop, *hoc_getdata_range(int);
 _prop = hoc_getdata_range(_mechtype);
   _setdata(_prop);
 hoc_retpushx(1.);
}
 /* connect user functions to hoc names */
 static VoidFunc hoc_intfunc[] = {
 "setdata_BKCAm", _hoc_setdata,
 "prates_BKCAm", _hoc_prates,
 "rates_BKCAm", _hoc_rates,
 0, 0
};
 /* declare global and static user variables */
 /* some parameters have upper and lower limits */
 static HocParmLimits _hoc_parm_limits[] = {
 0,0,0
};
 static HocParmUnits _hoc_parm_units[] = {
 "gkbar_BKCAm", "S/cm2",
 "ik_BKCAm", "mA/cm2",
 0,0
};
 static double c40 = 0;
 static double c30 = 0;
 static double c20 = 0;
 static double c10 = 0;
 static double c00 = 0;
 static double delta_t = 0.01;
 static double o40 = 0;
 static double o30 = 0;
 static double o20 = 0;
 static double o10 = 0;
 static double o00 = 0;
 /* connect global user variables to hoc */
 static DoubScal hoc_scdoub[] = {
 0,0
};
 static DoubVec hoc_vdoub[] = {
 0,0,0
};
 static double _sav_indep;
 static void nrn_alloc(Prop*);
static void  nrn_init(_NrnThread*, _Memb_list*, int);
static void nrn_state(_NrnThread*, _Memb_list*, int);
 static void nrn_cur(_NrnThread*, _Memb_list*, int);
static void  nrn_jacob(_NrnThread*, _Memb_list*, int);
 
static int _ode_count(int);
static void _ode_map(int, double**, double**, double*, Datum*, double*, int);
static void _ode_spec(_NrnThread*, _Memb_list*, int);
static void _ode_matsol(_NrnThread*, _Memb_list*, int);
 
#define _cvode_ieq _ppvar[4]._i
 static void _ode_matsol_instance1(_threadargsproto_);
 /* connect range variables in _p that hoc is supposed to know about */
 static const char *_mechanism[] = {
 "7.5.0",
"BKCAm",
 "gkbar_BKCAm",
 "kon_BKCAm",
 "kcoff_BKCAm",
 "kooff_BKCAm",
 "c0o0c_BKCAm",
 "c0c1c_BKCAm",
 "o0c0c_BKCAm",
 "o0o1c_BKCAm",
 "o4c4c_BKCAm",
 "c4o4c_BKCAm",
 "hva_BKCAm",
 "hvi_BKCAm",
 "sla_BKCAm",
 "sli_BKCAm",
 0,
 "ik_BKCAm",
 "a_BKCAm",
 "b_BKCAm",
 "o_BKCAm",
 0,
 "c0_BKCAm",
 "c1_BKCAm",
 "c2_BKCAm",
 "c3_BKCAm",
 "c4_BKCAm",
 "o0_BKCAm",
 "o1_BKCAm",
 "o2_BKCAm",
 "o3_BKCAm",
 "o4_BKCAm",
 0,
 0};
 static Symbol* _k_sym;
 static Symbol* _ca_sym;
 
extern Prop* need_memb(Symbol*);

static void nrn_alloc(Prop* _prop) {
	Prop *prop_ion;
	double *_p; Datum *_ppvar;
 	_p = nrn_prop_data_alloc(_mechtype, 68, _prop);
 	/*initialize range parameters*/
 	gkbar = 0.024;
 	kon = 40633;
 	kcoff = 11;
 	kooff = 1.1;
 	c0o0c = 0.02162;
 	c0c1c = 4;
 	o0c0c = 318.108;
 	o0o1c = 4;
 	o4c4c = 0.35;
 	c4o4c = 0.002;
 	hva = 35;
 	hvi = 15.776;
 	sla = 380;
 	sli = 330;
 	_prop->param = _p;
 	_prop->param_size = 68;
 	_ppvar = nrn_prop_datum_alloc(_mechtype, 5, _prop);
 	_prop->dparam = _ppvar;
 	/*connect ionic variables to this model*/
 prop_ion = need_memb(_k_sym);
 nrn_promote(prop_ion, 0, 1);
 	_ppvar[0]._pval = &prop_ion->param[0]; /* ek */
 	_ppvar[1]._pval = &prop_ion->param[3]; /* ik */
 	_ppvar[2]._pval = &prop_ion->param[4]; /* _ion_dikdv */
 prop_ion = need_memb(_ca_sym);
 nrn_promote(prop_ion, 1, 0);
 	_ppvar[3]._pval = &prop_ion->param[1]; /* cai */
 
}
 static void _initlists();
  /* some states have an absolute tolerance */
 static Symbol** _atollist;
 static HocStateTolerance _hoc_state_tol[] = {
 0,0
};
 static void _thread_cleanup(Datum*);
 static void _update_ion_pointer(Datum*);
 extern Symbol* hoc_lookup(const char*);
extern void _nrn_thread_reg(int, int, void(*)(Datum*));
extern void _nrn_thread_table_reg(int, void(*)(double*, Datum*, Datum*, _NrnThread*, int));
extern void hoc_register_tolerance(int, HocStateTolerance*, Symbol***);
extern void _cvode_abstol( Symbol**, double*, int);

 void _BKCAm_reg() {
	int _vectorized = 1;
  _initlists();
 	ion_reg("k", -10000.);
 	ion_reg("ca", -10000.);
 	_k_sym = hoc_lookup("k_ion");
 	_ca_sym = hoc_lookup("ca_ion");
 	register_mech(_mechanism, nrn_alloc,nrn_cur, nrn_jacob, nrn_state, nrn_init, hoc_nrnpointerindex, 3);
  _extcall_thread = (Datum*)ecalloc(2, sizeof(Datum));
 _mechtype = nrn_get_mechtype(_mechanism[1]);
     _nrn_setdata_reg(_mechtype, _setdata);
     _nrn_thread_reg(_mechtype, 0, _thread_cleanup);
     _nrn_thread_reg(_mechtype, 2, _update_ion_pointer);
  hoc_register_prop_size(_mechtype, 68, 5);
  hoc_register_dparam_semantics(_mechtype, 0, "k_ion");
  hoc_register_dparam_semantics(_mechtype, 1, "k_ion");
  hoc_register_dparam_semantics(_mechtype, 2, "k_ion");
  hoc_register_dparam_semantics(_mechtype, 3, "ca_ion");
  hoc_register_dparam_semantics(_mechtype, 4, "cvodeieq");
 	hoc_register_cvode(_mechtype, _ode_count, _ode_map, _ode_spec, _ode_matsol);
 	hoc_register_tolerance(_mechtype, _hoc_state_tol, &_atollist);
 	hoc_register_var(hoc_scdoub, hoc_vdoub, hoc_intfunc);
 	ivoc_help("help ?1 BKCAm /Users/dis006/Box Sync/T6 BP NEURON SIM/V3/Calcium_NMODL/MahapatraEtAl2018/x86_64/BKCAm.mod\n");
 hoc_register_limits(_mechtype, _hoc_parm_limits);
 hoc_register_units(_mechtype, _hoc_parm_units);
 }
static int _reset;
static char *modelname = "Calcium activated Potassium channel (BK)  ";

static int error;
static int _ninits = 0;
static int _match_recurse=1;
static void _modl_cleanup(){ _match_recurse=1;}
static int prates(_threadargsprotocomma_ double);
static int rates(_threadargsprotocomma_ double);
 extern double *_nrn_thread_getelm();
 
#define _MATELM1(_row,_col) *(_nrn_thread_getelm(_so, _row + 1, _col + 1))
 
#define _RHS1(_arg) _rhs[_arg+1]
  
#define _linmat1  1
 static int _spth1 = 1;
 static int _cvspth1 = 0;
 
static int _ode_spec1(_threadargsproto_);
/*static int _ode_matsol1(_threadargsproto_);*/
 static int _slist1[10], _dlist1[10]; static double *_temp1;
 static int kin();
 
static int kin (void* _so, double* _rhs, double* _p, Datum* _ppvar, Datum* _thread, _NrnThread* _nt)
 {int _reset=0;
 {
   double b_flux, f_flux, _term; int _i;
 {int _i; double _dt1 = 1.0/dt;
for(_i=1;_i<10;_i++){
  	_RHS1(_i) = -_dt1*(_p[_slist1[_i]] - _p[_dlist1[_i]]);
	_MATELM1(_i, _i) = _dt1;
      
} }
 rates ( _threadargscomma_ v ) ;
   /* ~ c0 <-> c1 ( c0c1 , c1c0 )*/
 f_flux =  c0c1 * c0 ;
 b_flux =  c1c0 * c1 ;
 _RHS1( 5) -= (f_flux - b_flux);
 _RHS1( 4) += (f_flux - b_flux);
 
 _term =  c0c1 ;
 _MATELM1( 5 ,5)  += _term;
 _MATELM1( 4 ,5)  -= _term;
 _term =  c1c0 ;
 _MATELM1( 5 ,4)  -= _term;
 _MATELM1( 4 ,4)  += _term;
 /*REACTION*/
  /* ~ c1 <-> c2 ( c1c2 , c2c1 )*/
 f_flux =  c1c2 * c1 ;
 b_flux =  c2c1 * c2 ;
 _RHS1( 4) -= (f_flux - b_flux);
 _RHS1( 3) += (f_flux - b_flux);
 
 _term =  c1c2 ;
 _MATELM1( 4 ,4)  += _term;
 _MATELM1( 3 ,4)  -= _term;
 _term =  c2c1 ;
 _MATELM1( 4 ,3)  -= _term;
 _MATELM1( 3 ,3)  += _term;
 /*REACTION*/
  /* ~ c2 <-> c3 ( c2c3 , c3c2 )*/
 f_flux =  c2c3 * c2 ;
 b_flux =  c3c2 * c3 ;
 _RHS1( 3) -= (f_flux - b_flux);
 _RHS1( 2) += (f_flux - b_flux);
 
 _term =  c2c3 ;
 _MATELM1( 3 ,3)  += _term;
 _MATELM1( 2 ,3)  -= _term;
 _term =  c3c2 ;
 _MATELM1( 3 ,2)  -= _term;
 _MATELM1( 2 ,2)  += _term;
 /*REACTION*/
  /* ~ c3 <-> c4 ( c3c4 , c4c3 )*/
 f_flux =  c3c4 * c3 ;
 b_flux =  c4c3 * c4 ;
 _RHS1( 2) -= (f_flux - b_flux);
 _RHS1( 1) += (f_flux - b_flux);
 
 _term =  c3c4 ;
 _MATELM1( 2 ,2)  += _term;
 _MATELM1( 1 ,2)  -= _term;
 _term =  c4c3 ;
 _MATELM1( 2 ,1)  -= _term;
 _MATELM1( 1 ,1)  += _term;
 /*REACTION*/
  /* ~ o0 <-> o1 ( o0o1 , o1o0 )*/
 f_flux =  o0o1 * o0 ;
 b_flux =  o1o0 * o1 ;
 _RHS1( 9) -= (f_flux - b_flux);
 _RHS1( 8) += (f_flux - b_flux);
 
 _term =  o0o1 ;
 _MATELM1( 9 ,9)  += _term;
 _MATELM1( 8 ,9)  -= _term;
 _term =  o1o0 ;
 _MATELM1( 9 ,8)  -= _term;
 _MATELM1( 8 ,8)  += _term;
 /*REACTION*/
  /* ~ o1 <-> o2 ( o1o2 , o2o1 )*/
 f_flux =  o1o2 * o1 ;
 b_flux =  o2o1 * o2 ;
 _RHS1( 8) -= (f_flux - b_flux);
 _RHS1( 7) += (f_flux - b_flux);
 
 _term =  o1o2 ;
 _MATELM1( 8 ,8)  += _term;
 _MATELM1( 7 ,8)  -= _term;
 _term =  o2o1 ;
 _MATELM1( 8 ,7)  -= _term;
 _MATELM1( 7 ,7)  += _term;
 /*REACTION*/
  /* ~ o2 <-> o3 ( o2o3 , o3o2 )*/
 f_flux =  o2o3 * o2 ;
 b_flux =  o3o2 * o3 ;
 _RHS1( 7) -= (f_flux - b_flux);
 _RHS1( 6) += (f_flux - b_flux);
 
 _term =  o2o3 ;
 _MATELM1( 7 ,7)  += _term;
 _MATELM1( 6 ,7)  -= _term;
 _term =  o3o2 ;
 _MATELM1( 7 ,6)  -= _term;
 _MATELM1( 6 ,6)  += _term;
 /*REACTION*/
  /* ~ o3 <-> o4 ( o3o4 , o4o3 )*/
 f_flux =  o3o4 * o3 ;
 b_flux =  o4o3 * o4 ;
 _RHS1( 6) -= (f_flux - b_flux);
 
 _term =  o3o4 ;
 _MATELM1( 6 ,6)  += _term;
 _term =  o4o3 ;
 _MATELM1( 6 ,0)  -= _term;
 /*REACTION*/
  /* ~ c0 <-> o0 ( c0o0 , o0c0 )*/
 f_flux =  c0o0 * c0 ;
 b_flux =  o0c0 * o0 ;
 _RHS1( 5) -= (f_flux - b_flux);
 _RHS1( 9) += (f_flux - b_flux);
 
 _term =  c0o0 ;
 _MATELM1( 5 ,5)  += _term;
 _MATELM1( 9 ,5)  -= _term;
 _term =  o0c0 ;
 _MATELM1( 5 ,9)  -= _term;
 _MATELM1( 9 ,9)  += _term;
 /*REACTION*/
  /* ~ c1 <-> o1 ( c1o1 , o1c1 )*/
 f_flux =  c1o1 * c1 ;
 b_flux =  o1c1 * o1 ;
 _RHS1( 4) -= (f_flux - b_flux);
 _RHS1( 8) += (f_flux - b_flux);
 
 _term =  c1o1 ;
 _MATELM1( 4 ,4)  += _term;
 _MATELM1( 8 ,4)  -= _term;
 _term =  o1c1 ;
 _MATELM1( 4 ,8)  -= _term;
 _MATELM1( 8 ,8)  += _term;
 /*REACTION*/
  /* ~ c2 <-> o2 ( c2o2 , o2c2 )*/
 f_flux =  c2o2 * c2 ;
 b_flux =  o2c2 * o2 ;
 _RHS1( 3) -= (f_flux - b_flux);
 _RHS1( 7) += (f_flux - b_flux);
 
 _term =  c2o2 ;
 _MATELM1( 3 ,3)  += _term;
 _MATELM1( 7 ,3)  -= _term;
 _term =  o2c2 ;
 _MATELM1( 3 ,7)  -= _term;
 _MATELM1( 7 ,7)  += _term;
 /*REACTION*/
  /* ~ c3 <-> o3 ( c3o3 , o3c3 )*/
 f_flux =  c3o3 * c3 ;
 b_flux =  o3c3 * o3 ;
 _RHS1( 2) -= (f_flux - b_flux);
 _RHS1( 6) += (f_flux - b_flux);
 
 _term =  c3o3 ;
 _MATELM1( 2 ,2)  += _term;
 _MATELM1( 6 ,2)  -= _term;
 _term =  o3c3 ;
 _MATELM1( 2 ,6)  -= _term;
 _MATELM1( 6 ,6)  += _term;
 /*REACTION*/
  /* ~ c4 <-> o4 ( c4o4 , o4c4 )*/
 f_flux =  c4o4 * c4 ;
 b_flux =  o4c4 * o4 ;
 _RHS1( 1) -= (f_flux - b_flux);
 
 _term =  c4o4 ;
 _MATELM1( 1 ,1)  += _term;
 _term =  o4c4 ;
 _MATELM1( 1 ,0)  -= _term;
 /*REACTION*/
   /* c0 + c1 + c2 + c3 + c4 + o0 + o1 + o2 + o3 + o4 = 1.0 */
 _RHS1(0) =  1.0;
 _MATELM1(0, 0) = 1;
 _RHS1(0) -= o4 ;
 _MATELM1(0, 6) = 1;
 _RHS1(0) -= o3 ;
 _MATELM1(0, 7) = 1;
 _RHS1(0) -= o2 ;
 _MATELM1(0, 8) = 1;
 _RHS1(0) -= o1 ;
 _MATELM1(0, 9) = 1;
 _RHS1(0) -= o0 ;
 _MATELM1(0, 1) = 1;
 _RHS1(0) -= c4 ;
 _MATELM1(0, 2) = 1;
 _RHS1(0) -= c3 ;
 _MATELM1(0, 3) = 1;
 _RHS1(0) -= c2 ;
 _MATELM1(0, 4) = 1;
 _RHS1(0) -= c1 ;
 _MATELM1(0, 5) = 1;
 _RHS1(0) -= c0 ;
 /*CONSERVATION*/
   } return _reset;
 }
 
static int  rates ( _threadargsprotocomma_ double _lv ) {
    a = exp ( hva * _lv / sla ) ;
   b = exp ( hvi * _lv / sli ) ;
   c0o0 = c0o0c * a ;
   c1o1 = 0.000869 * a ;
   c2o2 = 0.0000281 * a ;
   c3o3 = 0.000781 * a ;
   c4o4 = c4o4c * a ;
   o0c0 = o0c0c * b ;
   o1c1 = 144.1736 * b ;
   o2c2 = 32.6594 * b ;
   o3c3 = 0.095312 * b ;
   o4c4 = o4c4c * b ;
     return 0; }
 
static void _hoc_rates(void) {
  double _r;
   double* _p; Datum* _ppvar; Datum* _thread; _NrnThread* _nt;
   if (_extcall_prop) {_p = _extcall_prop->param; _ppvar = _extcall_prop->dparam;}else{ _p = (double*)0; _ppvar = (Datum*)0; }
  _thread = _extcall_thread;
  _nt = nrn_threads;
 _r = 1.;
 rates ( _p, _ppvar, _thread, _nt, *getarg(1) );
 hoc_retpushx(_r);
}
 
static int  prates ( _threadargsprotocomma_ double _lcai ) {
    c0c1 = c0c1c * kon * _lcai ;
   c1c2 = 3.0 * kon * _lcai ;
   c2c3 = 2.0 * kon * _lcai ;
   c3c4 = kon * _lcai ;
   c4c3 = 4.0 * kcoff * _lcai ;
   c3c2 = 3.0 * kcoff * _lcai ;
   c2c1 = 2.0 * kcoff * _lcai ;
   c1c0 = kcoff * _lcai ;
   o0o1 = 4.0 * kon * _lcai ;
   o1o2 = 3.0 * kon * _lcai ;
   o2o3 = 2.0 * kon * _lcai ;
   o3o4 = kon * _lcai ;
   o4o3 = 4.0 * kooff * _lcai ;
   o3o2 = 3.0 * kooff * _lcai ;
   o2o1 = 2.0 * kooff * _lcai ;
   o1o0 = kooff * _lcai ;
     return 0; }
 
static void _hoc_prates(void) {
  double _r;
   double* _p; Datum* _ppvar; Datum* _thread; _NrnThread* _nt;
   if (_extcall_prop) {_p = _extcall_prop->param; _ppvar = _extcall_prop->dparam;}else{ _p = (double*)0; _ppvar = (Datum*)0; }
  _thread = _extcall_thread;
  _nt = nrn_threads;
 _r = 1.;
 prates ( _p, _ppvar, _thread, _nt, *getarg(1) );
 hoc_retpushx(_r);
}
 
/*CVODE ode begin*/
 static int _ode_spec1(double* _p, Datum* _ppvar, Datum* _thread, _NrnThread* _nt) {int _reset=0;{
 double b_flux, f_flux, _term; int _i;
 {int _i; for(_i=0;_i<10;_i++) _p[_dlist1[_i]] = 0.0;}
 rates ( _threadargscomma_ v ) ;
 /* ~ c0 <-> c1 ( c0c1 , c1c0 )*/
 f_flux =  c0c1 * c0 ;
 b_flux =  c1c0 * c1 ;
 Dc0 -= (f_flux - b_flux);
 Dc1 += (f_flux - b_flux);
 
 /*REACTION*/
  /* ~ c1 <-> c2 ( c1c2 , c2c1 )*/
 f_flux =  c1c2 * c1 ;
 b_flux =  c2c1 * c2 ;
 Dc1 -= (f_flux - b_flux);
 Dc2 += (f_flux - b_flux);
 
 /*REACTION*/
  /* ~ c2 <-> c3 ( c2c3 , c3c2 )*/
 f_flux =  c2c3 * c2 ;
 b_flux =  c3c2 * c3 ;
 Dc2 -= (f_flux - b_flux);
 Dc3 += (f_flux - b_flux);
 
 /*REACTION*/
  /* ~ c3 <-> c4 ( c3c4 , c4c3 )*/
 f_flux =  c3c4 * c3 ;
 b_flux =  c4c3 * c4 ;
 Dc3 -= (f_flux - b_flux);
 Dc4 += (f_flux - b_flux);
 
 /*REACTION*/
  /* ~ o0 <-> o1 ( o0o1 , o1o0 )*/
 f_flux =  o0o1 * o0 ;
 b_flux =  o1o0 * o1 ;
 Do0 -= (f_flux - b_flux);
 Do1 += (f_flux - b_flux);
 
 /*REACTION*/
  /* ~ o1 <-> o2 ( o1o2 , o2o1 )*/
 f_flux =  o1o2 * o1 ;
 b_flux =  o2o1 * o2 ;
 Do1 -= (f_flux - b_flux);
 Do2 += (f_flux - b_flux);
 
 /*REACTION*/
  /* ~ o2 <-> o3 ( o2o3 , o3o2 )*/
 f_flux =  o2o3 * o2 ;
 b_flux =  o3o2 * o3 ;
 Do2 -= (f_flux - b_flux);
 Do3 += (f_flux - b_flux);
 
 /*REACTION*/
  /* ~ o3 <-> o4 ( o3o4 , o4o3 )*/
 f_flux =  o3o4 * o3 ;
 b_flux =  o4o3 * o4 ;
 Do3 -= (f_flux - b_flux);
 Do4 += (f_flux - b_flux);
 
 /*REACTION*/
  /* ~ c0 <-> o0 ( c0o0 , o0c0 )*/
 f_flux =  c0o0 * c0 ;
 b_flux =  o0c0 * o0 ;
 Dc0 -= (f_flux - b_flux);
 Do0 += (f_flux - b_flux);
 
 /*REACTION*/
  /* ~ c1 <-> o1 ( c1o1 , o1c1 )*/
 f_flux =  c1o1 * c1 ;
 b_flux =  o1c1 * o1 ;
 Dc1 -= (f_flux - b_flux);
 Do1 += (f_flux - b_flux);
 
 /*REACTION*/
  /* ~ c2 <-> o2 ( c2o2 , o2c2 )*/
 f_flux =  c2o2 * c2 ;
 b_flux =  o2c2 * o2 ;
 Dc2 -= (f_flux - b_flux);
 Do2 += (f_flux - b_flux);
 
 /*REACTION*/
  /* ~ c3 <-> o3 ( c3o3 , o3c3 )*/
 f_flux =  c3o3 * c3 ;
 b_flux =  o3c3 * o3 ;
 Dc3 -= (f_flux - b_flux);
 Do3 += (f_flux - b_flux);
 
 /*REACTION*/
  /* ~ c4 <-> o4 ( c4o4 , o4c4 )*/
 f_flux =  c4o4 * c4 ;
 b_flux =  o4c4 * o4 ;
 Dc4 -= (f_flux - b_flux);
 Do4 += (f_flux - b_flux);
 
 /*REACTION*/
   /* c0 + c1 + c2 + c3 + c4 + o0 + o1 + o2 + o3 + o4 = 1.0 */
 /*CONSERVATION*/
   } return _reset;
 }
 
/*CVODE matsol*/
 static int _ode_matsol1(void* _so, double* _rhs, double* _p, Datum* _ppvar, Datum* _thread, _NrnThread* _nt) {int _reset=0;{
 double b_flux, f_flux, _term; int _i;
   b_flux = f_flux = 0.;
 {int _i; double _dt1 = 1.0/dt;
for(_i=0;_i<10;_i++){
  	_RHS1(_i) = _dt1*(_p[_dlist1[_i]]);
	_MATELM1(_i, _i) = _dt1;
      
} }
 rates ( _threadargscomma_ v ) ;
 /* ~ c0 <-> c1 ( c0c1 , c1c0 )*/
 _term =  c0c1 ;
 _MATELM1( 5 ,5)  += _term;
 _MATELM1( 4 ,5)  -= _term;
 _term =  c1c0 ;
 _MATELM1( 5 ,4)  -= _term;
 _MATELM1( 4 ,4)  += _term;
 /*REACTION*/
  /* ~ c1 <-> c2 ( c1c2 , c2c1 )*/
 _term =  c1c2 ;
 _MATELM1( 4 ,4)  += _term;
 _MATELM1( 3 ,4)  -= _term;
 _term =  c2c1 ;
 _MATELM1( 4 ,3)  -= _term;
 _MATELM1( 3 ,3)  += _term;
 /*REACTION*/
  /* ~ c2 <-> c3 ( c2c3 , c3c2 )*/
 _term =  c2c3 ;
 _MATELM1( 3 ,3)  += _term;
 _MATELM1( 2 ,3)  -= _term;
 _term =  c3c2 ;
 _MATELM1( 3 ,2)  -= _term;
 _MATELM1( 2 ,2)  += _term;
 /*REACTION*/
  /* ~ c3 <-> c4 ( c3c4 , c4c3 )*/
 _term =  c3c4 ;
 _MATELM1( 2 ,2)  += _term;
 _MATELM1( 1 ,2)  -= _term;
 _term =  c4c3 ;
 _MATELM1( 2 ,1)  -= _term;
 _MATELM1( 1 ,1)  += _term;
 /*REACTION*/
  /* ~ o0 <-> o1 ( o0o1 , o1o0 )*/
 _term =  o0o1 ;
 _MATELM1( 9 ,9)  += _term;
 _MATELM1( 8 ,9)  -= _term;
 _term =  o1o0 ;
 _MATELM1( 9 ,8)  -= _term;
 _MATELM1( 8 ,8)  += _term;
 /*REACTION*/
  /* ~ o1 <-> o2 ( o1o2 , o2o1 )*/
 _term =  o1o2 ;
 _MATELM1( 8 ,8)  += _term;
 _MATELM1( 7 ,8)  -= _term;
 _term =  o2o1 ;
 _MATELM1( 8 ,7)  -= _term;
 _MATELM1( 7 ,7)  += _term;
 /*REACTION*/
  /* ~ o2 <-> o3 ( o2o3 , o3o2 )*/
 _term =  o2o3 ;
 _MATELM1( 7 ,7)  += _term;
 _MATELM1( 6 ,7)  -= _term;
 _term =  o3o2 ;
 _MATELM1( 7 ,6)  -= _term;
 _MATELM1( 6 ,6)  += _term;
 /*REACTION*/
  /* ~ o3 <-> o4 ( o3o4 , o4o3 )*/
 _term =  o3o4 ;
 _MATELM1( 6 ,6)  += _term;
 _MATELM1( 0 ,6)  -= _term;
 _term =  o4o3 ;
 _MATELM1( 6 ,0)  -= _term;
 _MATELM1( 0 ,0)  += _term;
 /*REACTION*/
  /* ~ c0 <-> o0 ( c0o0 , o0c0 )*/
 _term =  c0o0 ;
 _MATELM1( 5 ,5)  += _term;
 _MATELM1( 9 ,5)  -= _term;
 _term =  o0c0 ;
 _MATELM1( 5 ,9)  -= _term;
 _MATELM1( 9 ,9)  += _term;
 /*REACTION*/
  /* ~ c1 <-> o1 ( c1o1 , o1c1 )*/
 _term =  c1o1 ;
 _MATELM1( 4 ,4)  += _term;
 _MATELM1( 8 ,4)  -= _term;
 _term =  o1c1 ;
 _MATELM1( 4 ,8)  -= _term;
 _MATELM1( 8 ,8)  += _term;
 /*REACTION*/
  /* ~ c2 <-> o2 ( c2o2 , o2c2 )*/
 _term =  c2o2 ;
 _MATELM1( 3 ,3)  += _term;
 _MATELM1( 7 ,3)  -= _term;
 _term =  o2c2 ;
 _MATELM1( 3 ,7)  -= _term;
 _MATELM1( 7 ,7)  += _term;
 /*REACTION*/
  /* ~ c3 <-> o3 ( c3o3 , o3c3 )*/
 _term =  c3o3 ;
 _MATELM1( 2 ,2)  += _term;
 _MATELM1( 6 ,2)  -= _term;
 _term =  o3c3 ;
 _MATELM1( 2 ,6)  -= _term;
 _MATELM1( 6 ,6)  += _term;
 /*REACTION*/
  /* ~ c4 <-> o4 ( c4o4 , o4c4 )*/
 _term =  c4o4 ;
 _MATELM1( 1 ,1)  += _term;
 _MATELM1( 0 ,1)  -= _term;
 _term =  o4c4 ;
 _MATELM1( 1 ,0)  -= _term;
 _MATELM1( 0 ,0)  += _term;
 /*REACTION*/
   /* c0 + c1 + c2 + c3 + c4 + o0 + o1 + o2 + o3 + o4 = 1.0 */
 /*CONSERVATION*/
   } return _reset;
 }
 
/*CVODE end*/
 
static int _ode_count(int _type){ return 10;}
 
static void _ode_spec(_NrnThread* _nt, _Memb_list* _ml, int _type) {
   double* _p; Datum* _ppvar; Datum* _thread;
   Node* _nd; double _v; int _iml, _cntml;
  _cntml = _ml->_nodecount;
  _thread = _ml->_thread;
  for (_iml = 0; _iml < _cntml; ++_iml) {
    _p = _ml->_data[_iml]; _ppvar = _ml->_pdata[_iml];
    _nd = _ml->_nodelist[_iml];
    v = NODEV(_nd);
  ek = _ion_ek;
  cai = _ion_cai;
     _ode_spec1 (_p, _ppvar, _thread, _nt);
  }}
 
static void _ode_map(int _ieq, double** _pv, double** _pvdot, double* _pp, Datum* _ppd, double* _atol, int _type) { 
	double* _p; Datum* _ppvar;
 	int _i; _p = _pp; _ppvar = _ppd;
	_cvode_ieq = _ieq;
	for (_i=0; _i < 10; ++_i) {
		_pv[_i] = _pp + _slist1[_i];  _pvdot[_i] = _pp + _dlist1[_i];
		_cvode_abstol(_atollist, _atol, _i);
	}
 }
 
static void _ode_matsol_instance1(_threadargsproto_) {
 _cvode_sparse_thread(&_thread[_cvspth1]._pvoid, 10, _dlist1, _p, _ode_matsol1, _ppvar, _thread, _nt);
 }
 
static void _ode_matsol(_NrnThread* _nt, _Memb_list* _ml, int _type) {
   double* _p; Datum* _ppvar; Datum* _thread;
   Node* _nd; double _v; int _iml, _cntml;
  _cntml = _ml->_nodecount;
  _thread = _ml->_thread;
  for (_iml = 0; _iml < _cntml; ++_iml) {
    _p = _ml->_data[_iml]; _ppvar = _ml->_pdata[_iml];
    _nd = _ml->_nodelist[_iml];
    v = NODEV(_nd);
  ek = _ion_ek;
  cai = _ion_cai;
 _ode_matsol_instance1(_threadargs_);
 }}
 
static void _thread_cleanup(Datum* _thread) {
   _nrn_destroy_sparseobj_thread(_thread[_cvspth1]._pvoid);
   _nrn_destroy_sparseobj_thread(_thread[_spth1]._pvoid);
 }
 extern void nrn_update_ion_pointer(Symbol*, Datum*, int, int);
 static void _update_ion_pointer(Datum* _ppvar) {
   nrn_update_ion_pointer(_k_sym, _ppvar, 0, 0);
   nrn_update_ion_pointer(_k_sym, _ppvar, 1, 3);
   nrn_update_ion_pointer(_k_sym, _ppvar, 2, 4);
   nrn_update_ion_pointer(_ca_sym, _ppvar, 3, 1);
 }

static void initmodel(double* _p, Datum* _ppvar, Datum* _thread, _NrnThread* _nt) {
  int _i; double _save;{
  c4 = c40;
  c3 = c30;
  c2 = c20;
  c1 = c10;
  c0 = c00;
  o4 = o40;
  o3 = o30;
  o2 = o20;
  o1 = o10;
  o0 = o00;
 {
    _ss_sparse_thread(&_thread[_spth1]._pvoid, 10, _slist1, _dlist1, _p, &t, dt, kin, _linmat1, _ppvar, _thread, _nt);
     if (secondorder) {
    int _i;
    for (_i = 0; _i < 10; ++_i) {
      _p[_slist1[_i]] += dt*_p[_dlist1[_i]];
    }}
 }
 
}
}

static void nrn_init(_NrnThread* _nt, _Memb_list* _ml, int _type){
double* _p; Datum* _ppvar; Datum* _thread;
Node *_nd; double _v; int* _ni; int _iml, _cntml;
#if CACHEVEC
    _ni = _ml->_nodeindices;
#endif
_cntml = _ml->_nodecount;
_thread = _ml->_thread;
for (_iml = 0; _iml < _cntml; ++_iml) {
 _p = _ml->_data[_iml]; _ppvar = _ml->_pdata[_iml];
#if CACHEVEC
  if (use_cachevec) {
    _v = VEC_V(_ni[_iml]);
  }else
#endif
  {
    _nd = _ml->_nodelist[_iml];
    _v = NODEV(_nd);
  }
 v = _v;
  ek = _ion_ek;
  cai = _ion_cai;
 initmodel(_p, _ppvar, _thread, _nt);
 }
}

static double _nrn_current(double* _p, Datum* _ppvar, Datum* _thread, _NrnThread* _nt, double _v){double _current=0.;v=_v;{ {
   o = o0 + o1 + o2 + o3 + o4 ;
   ik = gkbar * o * ( v - ek ) ;
   }
 _current += ik;

} return _current;
}

static void nrn_cur(_NrnThread* _nt, _Memb_list* _ml, int _type) {
double* _p; Datum* _ppvar; Datum* _thread;
Node *_nd; int* _ni; double _rhs, _v; int _iml, _cntml;
#if CACHEVEC
    _ni = _ml->_nodeindices;
#endif
_cntml = _ml->_nodecount;
_thread = _ml->_thread;
for (_iml = 0; _iml < _cntml; ++_iml) {
 _p = _ml->_data[_iml]; _ppvar = _ml->_pdata[_iml];
#if CACHEVEC
  if (use_cachevec) {
    _v = VEC_V(_ni[_iml]);
  }else
#endif
  {
    _nd = _ml->_nodelist[_iml];
    _v = NODEV(_nd);
  }
  ek = _ion_ek;
  cai = _ion_cai;
 _g = _nrn_current(_p, _ppvar, _thread, _nt, _v + .001);
 	{ double _dik;
  _dik = ik;
 _rhs = _nrn_current(_p, _ppvar, _thread, _nt, _v);
  _ion_dikdv += (_dik - ik)/.001 ;
 	}
 _g = (_g - _rhs)/.001;
  _ion_ik += ik ;
#if CACHEVEC
  if (use_cachevec) {
	VEC_RHS(_ni[_iml]) -= _rhs;
  }else
#endif
  {
	NODERHS(_nd) -= _rhs;
  }
 
}
 
}

static void nrn_jacob(_NrnThread* _nt, _Memb_list* _ml, int _type) {
double* _p; Datum* _ppvar; Datum* _thread;
Node *_nd; int* _ni; int _iml, _cntml;
#if CACHEVEC
    _ni = _ml->_nodeindices;
#endif
_cntml = _ml->_nodecount;
_thread = _ml->_thread;
for (_iml = 0; _iml < _cntml; ++_iml) {
 _p = _ml->_data[_iml];
#if CACHEVEC
  if (use_cachevec) {
	VEC_D(_ni[_iml]) += _g;
  }else
#endif
  {
     _nd = _ml->_nodelist[_iml];
	NODED(_nd) += _g;
  }
 
}
 
}

static void nrn_state(_NrnThread* _nt, _Memb_list* _ml, int _type) {
double* _p; Datum* _ppvar; Datum* _thread;
Node *_nd; double _v = 0.0; int* _ni; int _iml, _cntml;
double _dtsav = dt;
if (secondorder) { dt *= 0.5; }
#if CACHEVEC
    _ni = _ml->_nodeindices;
#endif
_cntml = _ml->_nodecount;
_thread = _ml->_thread;
for (_iml = 0; _iml < _cntml; ++_iml) {
 _p = _ml->_data[_iml]; _ppvar = _ml->_pdata[_iml];
 _nd = _ml->_nodelist[_iml];
#if CACHEVEC
  if (use_cachevec) {
    _v = VEC_V(_ni[_iml]);
  }else
#endif
  {
    _nd = _ml->_nodelist[_iml];
    _v = NODEV(_nd);
  }
 v=_v;
{
  ek = _ion_ek;
  cai = _ion_cai;
 {  sparse_thread(&_thread[_spth1]._pvoid, 10, _slist1, _dlist1, _p, &t, dt, kin, _linmat1, _ppvar, _thread, _nt);
     if (secondorder) {
    int _i;
    for (_i = 0; _i < 10; ++_i) {
      _p[_slist1[_i]] += dt*_p[_dlist1[_i]];
    }}
 } }}
 dt = _dtsav;
}

static void terminal(){}

static void _initlists(){
 double _x; double* _p = &_x;
 int _i; static int _first = 1;
  if (!_first) return;
 _slist1[0] = &(o4) - _p;  _dlist1[0] = &(Do4) - _p;
 _slist1[1] = &(c4) - _p;  _dlist1[1] = &(Dc4) - _p;
 _slist1[2] = &(c3) - _p;  _dlist1[2] = &(Dc3) - _p;
 _slist1[3] = &(c2) - _p;  _dlist1[3] = &(Dc2) - _p;
 _slist1[4] = &(c1) - _p;  _dlist1[4] = &(Dc1) - _p;
 _slist1[5] = &(c0) - _p;  _dlist1[5] = &(Dc0) - _p;
 _slist1[6] = &(o3) - _p;  _dlist1[6] = &(Do3) - _p;
 _slist1[7] = &(o2) - _p;  _dlist1[7] = &(Do2) - _p;
 _slist1[8] = &(o1) - _p;  _dlist1[8] = &(Do1) - _p;
 _slist1[9] = &(o0) - _p;  _dlist1[9] = &(Do0) - _p;
_first = 0;
}

#if defined(__cplusplus)
} /* extern "C" */
#endif
