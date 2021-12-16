#include <stdio.h>
#include "hocdec.h"
#define IMPORT extern __declspec(dllimport)
IMPORT int nrnmpi_myid, nrn_nobanner_;

extern void _Ca_reg();
extern void _Cad_reg();
extern void _HCN2r_reg();
extern void _Kv1_2_reg();
extern void _kv1_3_reg();

void modl_reg(){
	//nrn_mswindll_stdio(stdin, stdout, stderr);
    if (!nrn_nobanner_) if (nrnmpi_myid < 1) {
	fprintf(stderr, "Additional mechanisms from files\n");

fprintf(stderr," Ca.mod");
fprintf(stderr," Cad.mod");
fprintf(stderr," HCN2r.mod");
fprintf(stderr," Kv1_2.mod");
fprintf(stderr," kv1_3.mod");
fprintf(stderr, "\n");
    }
_Ca_reg();
_Cad_reg();
_HCN2r_reg();
_Kv1_2_reg();
_kv1_3_reg();
}
