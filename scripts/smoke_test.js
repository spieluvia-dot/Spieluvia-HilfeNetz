'use strict';
const fs = require('node:fs');
const vm = require('node:vm');
const assert = require('node:assert/strict');
const geo = fs.readFileSync('assets/geo.js', 'utf8');
assert.match(geo, /\^\[0-9\]\{5\}\$/);
assert.doesNotMatch(geo, /\^\\\\d\{5\}\$/);
const context = { window: {} };
vm.runInNewContext(fs.readFileSync('assets/contact.js','utf8'), context);
const v = context.window.SpieluviaContact.vcard({
  name: 'Beratung Müller, Nord; Süd',
  address: 'Straße 1; Haus A, 18209 Bad Doberan',
  phone: '038203 12345',
  email: 'hilfe@example.org',
  hours: 'Mo 9–12 Uhr\nDi 10–12 Uhr',
  url: 'https://example.org'
});
assert.ok(v.startsWith('BEGIN:VCARD\r\nVERSION:3.0\r\n'));
assert.ok(v.includes('FN:Beratung Müller\\, Nord\\; Süd'));
assert.ok(v.includes('ADR;TYPE=WORK:;;Straße 1\\; Haus A\\, 18209 Bad Doberan;;;;'));
assert.ok(v.includes('Mo 9–12 Uhr\\nDi 10–12 Uhr'));
assert.ok(v.endsWith('END:VCARD\r\n'));
console.log('PASS: postal-code source check and vCard escaping/CRLF');


async function testRegionalSearch() {
  const elements = new Map();
  function element(id) {
    return { id, value:'', textContent:'', children:[], append(...nodes){this.children.push(...nodes)}, replaceChildren(){this.children=[]}, addEventListener(event,handler){this[event]=handler} };
  }
  for (const id of ['place','radius','state','geo-status','local-results','geo-form']) elements.set(id,element(id));
  const places=[
    {postal_code:'18209',city:'Bad Doberan',state:'Mecklenburg-Vorpommern',lat:54.106,lon:11.900},
    {postal_code:'18055',city:'Rostock',state:'Mecklenburg-Vorpommern',lat:54.086,lon:12.140},
    {postal_code:'18057',city:'Rostock',state:'Mecklenburg-Vorpommern',lat:54.093,lon:12.110}
  ];
  const locations=[{name:'Test Doberan',postal_code:'18209',city:'Bad Doberan',url:'https://example.org/doberan'},
    {name:'Test Rostock',postal_code:'18055',city:'Rostock',url:'https://example.org/rostock'}];
  const document={getElementById:id=>elements.get(id),createElement:tag=>element(tag)};
  const fetch=async path=>({ok:true,json:async()=>path === 'data/orte.json'?{places}:{locations}});
  vm.runInNewContext(geo,{document,fetch,window:{}});
  const submit=(q,r='30')=>{
    elements.get('place').value=q;
    elements.get('radius').value=r;
    elements.get('geo-form').submit({preventDefault(){}});
    return {message:elements.get('geo-status').textContent,items:elements.get('local-results').children};
  };
  assert.match(submit('18209').message,/noch geladen/);
  assert.equal(submit('18209').items.length,0);
  await new Promise(resolve=>setImmediate(resolve));
  assert.match(submit('Rostock').message,/Mehrere Postleitzahlen/);
  assert.equal(submit('18209','5').items.length,1);
  assert.equal(submit('18055','5').items.length,1);
  assert.equal(submit('18057','5').items.length,1);
  assert.equal(submit('99999').items.length,0);
  assert.match(submit('99999').message,/nicht gefunden/);
  console.log('PASS: regional search submits, ambiguous cities, PLZ and radius');
}
testRegionalSearch().catch(e=>{console.error(e);process.exitCode=1});
