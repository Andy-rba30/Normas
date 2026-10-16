#!/bin/bash
set -e
cd /tmp/claude-0/-home-user-Normas/1d8bfce3-3294-5b1e-ace9-ad5fa4f1a13c/scratchpad/aln
OUT=/home/user/Normas/civil3d/eje
rm -rf out_final && mkdir -p out_final
TOL=${TOL:-1.5}
python3 -I tangent_pass.py model.pkl model_t.pkl $TOL
python3 -I tangent_pass.py model_sp.pkl model_sp_t.pkl $TOL
python3 -I write_outputs.py model_t.pkl out_final circular "EJE DG2018 V40 CIRCULAR"
python3 -I write_outputs.py model_sp_t.pkl out_final clotoides "EJE DG2018 V40 CLOTOIDES"
for t in circular clotoides; do
  echo "== $t"; xmllint --noout out_final/EJE_DG2018_$t.xml && echo "xml bien formado"
  python3 -I check_landxml.py out_final/EJE_DG2018_$t.xml
done
python3 -I plan.py model_t.pkl out_final/EJE_DG2018_circular_planta.png "Eje corregido DG-2018 (V = 40 km/h), variante circular, sobre el trazo actual"
python3 -I plan.py model_sp_t.pkl out_final/EJE_DG2018_clotoides_planta.png "Eje corregido DG-2018 (V = 40 km/h), variante con clotoides, sobre el trazo actual"
python3 -c "
from PIL import Image
for t in ('circular','clotoides'):
    im=Image.open('out_final/EJE_DG2018_%s_planta.png'%t); im.thumbnail((1900,1900)); im.save('out_final/_small_%s.png'%t)
"
mkdir -p $OUT && cp out_final/EJE_DG2018_* $OUT/ && ls -la $OUT
