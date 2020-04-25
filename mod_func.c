#include <stdio.h>
#include "hocdec.h"
#define IMPORT extern __declspec(dllimport)
IMPORT int nrnmpi_myid, nrn_nobanner_;

extern void _CAD_reg();
extern void _CaL_reg();
extern void _HCN2r_reg();
extern void _kv_reg();

void modl_reg(){
	//nrn_mswindll_stdio(stdin, stdout, stderr);
    if (!nrn_nobanner_) if (nrnmpi_myid < 1) {
	fprintf(stderr, "Additional mechanisms from files\n");

fprintf(stderr," CAD.mod");
fprintf(stderr," CaL.mod");
fprintf(stderr," HCN2r.mod");
fprintf(stderr," kv.mod");
fprintf(stderr, "\n");
    }
_CAD_reg();
_CaL_reg();
_HCN2r_reg();
_kv_reg();
}
