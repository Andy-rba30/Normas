#!/bin/bash
# Uso: build_memoria.sh <modelo.pkl>   (ruta relativa a scratchpad/aln)
set -e
S=/tmp/claude-0/-home-user-Normas/1d8bfce3-3294-5b1e-ace9-ad5fa4f1a13c/scratchpad
cd $S/rep && python3 -I make_report.py ${1:-model_t.pkl}
pandoc memoria.md -f markdown -t docx --reference-doc=ref_landscape.docx -o memoria.docx
python3 - <<'PY'
import zipfile, shutil
p='/tmp/claude-0/-home-user-Normas/1d8bfce3-3294-5b1e-ace9-ad5fa4f1a13c/scratchpad/rep/memoria.docx'
z=zipfile.ZipFile(p); names=z.infolist(); data={i.filename:z.read(i.filename) for i in names}; z.close()
doc=data['word/document.xml'].decode('utf-8')
sect='<w:sectPr><w:pgSz w:w="16838" w:h="11906" w:orient="landscape"/><w:pgMar w:top="850" w:right="850" w:bottom="850" w:left="850" w:header="400" w:footer="400" w:gutter="0"/><w:cols w:space="708"/><w:docGrid w:linePitch="360"/></w:sectPr>'
if '<w:sectPr />' in doc: doc=doc.replace('<w:sectPr />',sect)
data['word/document.xml']=doc.encode('utf-8')
zout=zipfile.ZipFile(p+'.tmp','w',zipfile.ZIP_DEFLATED)
for i in names: zout.writestr(i,data[i.filename])
zout.close(); shutil.move(p+'.tmp',p); print('memoria.docx apaisada')
PY
cp memoria.docx /home/user/Normas/civil3d/eje/EJE_DG2018_circular_memoria.docx
cp memoria.md /home/user/Normas/civil3d/eje/EJE_DG2018_circular_memoria.md
ls -la /home/user/Normas/civil3d/eje/EJE_DG2018_circular_memoria.*
