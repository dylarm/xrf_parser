# Description of PDZ file
The `*.pdz` files in this directory are binary files produced by the handheld XRF.
Lacking a formal description of the file format, their structure has been inferred by comparison.

## Data
### Header
The length of initial similarity between Glassmajors is 128 bytes, while GeoExploration's initial similarity is only 95 bytes.
The three G-tests above have the same initial 246 bytes between each different pairing (Glassmajors-GeoExploration, Glassmajors-GeoMining, etc.).

The first 256 bytes of the following files are compared.

| ID  | Test           | Filename                   |
|-----|----------------|----------------------------|
| 1   | Glassmajors    | `00001-GLASSMAJORS.pdz`    |
| 8   | GeoExploration | `00008-GeoExploration.pdz` |
| 12  | GeoMining      | `00012-GeoMining.pdz`      |
| 174 | GeoExploration | `00174-GeoExploration.pdz` |
| 206 | Glassmajors    | `00206-GLASSMAJORS.pdz`    |

Offset 0x00
```
                   p     d     z     2     5                                               9
19 00 0E 00 00 00 70 00 64 00 7A 00 32 00 35 00 01 00 00 00 01 00 DA 00 00 00 08 00 00 00 39 00    1
```

Offset 0x20
```
 0     0     F     4     5     0     3                 S     K     5     -     4     5     0
30 00 30 00 46 00 34 00 35 00 30 00 33 00 08 00 00 00 53 00 4B 00 35 00 2D 00 34 00 35 00 30 00    1
```

Offset 0x40
```
 3     -  -  -  A  }                 S     D     D                 R     x     B     x
33 00 2D 2D 2D 41 7D 00 03 00 00 00 53 00 44 00 44 00 04 00 00 00 52 00 78 00 42 00 78 00 08 08    1
                                                                                             00    174
```

Offset 0x60
```
             M     o     v     a     b     l     e                                   2
07 00 00 00 4D 00 6F 00 76 00 61 00 62 00 6C 00 65 00 08 00 00 00 01 00 0A 00 00 00 32 00 2E 00    1
```

Offset 0x80
```
 3           4     8           2     6     7                       1     3           0     9
33 00 2E 00 34 00 38 00 2E 00 32 00 36 00 37 00 02 00 05 00 00 00 31 00 33 00 2E 00 30 00 39 00    1
34          35    34                39                                                             206
34          35    34                39                                                             174
```

Offset 0xA0
```
                   6           0     3                       3           0     3
03 00 04 00 00 00 36 00 2E 00 30 00 33 00 04 00 04 00 00 00 33 00 2E 00 30 00 33 00 05 00 04 00    1
```

Offset 0xC0
```
       9           2     F                       1           0     1                       1
00 00 39 00 2E 00 32 00 46 00 06 00 04 00 00 00 31 00 2E 00 30 00 32 00 07 00 04 00 00 00 31 00    1
```

Offset 0xE0
```
       1     1                       1           0     1           V                       Q  ]
2E 00 31 00 31 00 08 00 04 00 00 00 31 00 2E 00 30 00 31 00 02 00 56 00 00 00 01 00 00 00 51 5D    1
                                                                                          9E 98    206
                                                                  5C                      D1 FA    8
                                                                  52                      60 7E    12
                                                                  5C          00          00 00    174
```

