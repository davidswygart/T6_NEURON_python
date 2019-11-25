#include <stdio.h>
#include "hocdec.h"
extern int nrnmpi_myid;
extern int nrn_nobanner_;

extern void _BKCAm_reg(void);
extern void _CAD_reg(void);
extern void _CaL_reg(void);
extern void _CaT_reg(void);
extern void _Exp2Syn_reg(void);
extern void _IH_reg(void);
extern void _IKCA_reg(void);
extern void _KATP_reg(void);
extern void _KCNQ_reg(void);
extern void _KV2_reg(void);
extern void _SKCA_reg(void);

void modl_reg(){
  if (!nrn_nobanner_) if (nrnmpi_myid < 1) {
    fprintf(stderr, "Additional mechanisms from files\n");

    fprintf(stderr," BKCAm.mod");
    fprintf(stderr," CAD.mod");
    fprintf(stderr," CaL.mod");
    fprintf(stderr," CaT.mod");
    fprintf(stderr," Exp2Syn.mod");
    fprintf(stderr," IH.mod");
    fprintf(stderr," IKCA.mod");
    fprintf(stderr," KATP.mod");
    fprintf(stderr," KCNQ.mod");
    fprintf(stderr," KV2.mod");
    fprintf(stderr," SKCA.mod");
    fprintf(stderr, "\n");
  }
  _BKCAm_reg();
  _CAD_reg();
  _CaL_reg();
  _CaT_reg();
  _Exp2Syn_reg();
  _IH_reg();
  _IKCA_reg();
  _KATP_reg();
  _KCNQ_reg();
  _KV2_reg();
  _SKCA_reg();
}
