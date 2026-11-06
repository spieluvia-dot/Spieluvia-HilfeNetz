#!/usr/bin/env python3
"""Importiere heruntergeladene GeoNames-Postleitzahlen (DE.txt) lokal, ohne API.
Quelle: https://download.geonames.org/export/zip/DE.zip (CC BY 4.0)
Aufruf: python scripts/import_geonames.py DE.txt
"""
import csv,json,sys,pathlib
p=pathlib.Path(sys.argv[1]); rows=[];seen=set()
with p.open(encoding='utf-8') as f:
 for row in csv.reader(f,delimiter='\t'):
  if len(row)<11 or row[0]!='DE':continue
  try: lat,lon=float(row[9]),float(row[10])
  except ValueError:continue
  k=(row[1],row[2],row[3]);
  if k in seen:continue
  seen.add(k);rows.append({'postal_code':row[1],'city':row[2],'state':row[3],'lat':lat,'lon':lon})
out=pathlib.Path('data/orte.json');out.parent.mkdir(exist_ok=True)
out.write_text(json.dumps({'source':'GeoNames DE postal codes; CC BY 4.0; https://www.geonames.org/','places':rows},ensure_ascii=False,separators=(',',':')),encoding='utf-8')
print(len(rows),'Ortsdatensätze geschrieben')
