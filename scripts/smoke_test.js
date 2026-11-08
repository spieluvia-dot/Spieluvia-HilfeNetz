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
