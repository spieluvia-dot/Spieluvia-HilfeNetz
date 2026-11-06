#!/usr/bin/env python3
"""Importiert GeoNames-Postleitzahlen aus DE.zip oder DE.txt (CC BY 3.0)."""
import csv,io,json,pathlib,sys,urllib.request,zipfile
URL="https://download.geonames.org/export/zip/DE.zip"
STATES={"Bavaria":"Bayern","Hesse":"Hessen","Lower Saxony":"Niedersachsen","North Rhine-Westphalia":"Nordrhein-Westfalen","Saxony":"Sachsen","Saxony-Anhalt":"Sachsen-Anhalt","Thuringia":"Thüringen","Mecklenburg-Vorpommern":"Mecklenburg-Vorpommern","Rhineland-Palatinate":"Rheinland-Pfalz"}
def main():
 source=sys.argv[1] if len(sys.argv)>1 else URL
 if source.startswith("https://"):
  req=urllib.request.Request(source,headers={"User-Agent":"Spieluvia-HilfeNetz/1.0 (GeoNames attribution)"})
  with urllib.request.urlopen(req,timeout=60) as response: raw=response.read()
 else:raw=pathlib.Path(source).read_bytes()
 if raw.startswith(b"PK"):
  with zipfile.ZipFile(io.BytesIO(raw)) as z:raw=z.read("DE.txt")
 rows=[];seen=set()
 for row in csv.reader(io.StringIO(raw.decode("utf-8-sig")),delimiter="\t"):
  if len(row)<11 or row[0]!="DE":continue
  try:lat,lon=float(row[9]),float(row[10])
  except ValueError:continue
  if not (47<=lat<=56 and 5<=lon<=16):continue
  plz,city,state=row[1].strip(),row[2].strip(),STATES.get(row[3].strip(),row[3].strip())
  if not(plz.isdigit() and len(plz)==5 and city):continue
  key=(plz,city,state)
  if key in seen:continue
  seen.add(key);rows.append({"postal_code":plz,"city":city,"state":state,"lat":lat,"lon":lon})
 if len(rows)<1000:raise RuntimeError("Import abgebrochen: unerwartet wenige Datensätze; vorhandene Ortsdaten bleiben unverändert")
 rows.sort(key=lambda x:(x["postal_code"],x["city"],x["state"]))
 output=pathlib.Path("data/orte.json");output.parent.mkdir(exist_ok=True)
 output.write_text(json.dumps({"source":"GeoNames Postal Codes DE; CC BY 3.0; https://www.geonames.org/","places":rows},ensure_ascii=False,separators=(",",":"))+"\n",encoding="utf-8")
 print("Import erfolgreich:",len(rows),"PLZ/Ort-Kombinationen")
if __name__=="__main__":main()
