# Description of PDZ file
The `*.pdz` files in this directory are binary files produced by the handheld XRF.
Lacking a formal description of the file format, their structure has been inferred by comparison.

A quick preliminary search revealed that only the tests *Glassmajors*, *GeoExploration*, and *GeoMining* are easily decipherable.

## Summary
* The characters of nearly every string are separated by null bytes.
* The first 256 bytes are relatively conserved between all types.
  * Offset 0x06 always contains the string `pdz25`, with each character separated by 0x00 (9 bytes).
* Test type is first indicated at offset 0x12A.
* Most data is stored near the end of the PDZ file:
  * The concentration sections are generally indicated by a sub-test keyword, such as Oxide3phase, OxideConcentrates, etc., or the test name again (GLASSMAJORS). File 174 seems to be the exception.
  * Readings are headed by one of the five following 10-byte hex strings:
    1. `06 00 27 00 00 00 03 00 00 00`
    1. `06 00 25 00 00 00 02 00 00 00`
    1. `06 00 2B 00 00 00 05 00 00 00`
    1. `06 00 29 00 00 00 04 00 00 00`
    1. `06 00 23 00 00 00 01 00 00 00`
  * Readings are ended by a 12-byte string of 0x00.
  * Concentrations are encoded as 32-bit floats and are repeated twice next to each other.
  * Concentration error is also encoded as a 32-bit float, but must be doubled in order to obtain the number given by the "official" application.

### Still need
Items that have remained elusive so far:
* Date
* Calibration check

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

### Reading data

| ID  | Test           | Subtest          |
|-----|----------------|------------------|
| 1   | Glassmajors    | Glassmajors      |
| 206 | Glassmajors    | Glassmajors      |
| 8   | GeoExploration | Oxide3phase      |
| 174 | GeoExploration | GeoExploration   |
| 12  | GeoMining      | OxideConcentrate |

#### Inter-readings
The following 10-byte hex strings appear immediately before the first concentration readings:
```
1    06 00 27 00 00 00 03 00 00 00  MgO
206  06 00 27 00 00 00 03 00 00 00  MgO
8    06 00 25 00 00 00 02 00 00 00  Ti
174  06 00 27 00 00 00 03 00 00 00  MgO
12   06 00 25 00 00 00 02 00 00 00  Ti
```

Prior to subsequent readings, the following examples of similar hex strings appear:
```
1        06 00 2B 00 00 00 05 00 00 00  Al2O3
1        06 00 29 00 00 00 04 00 00 00  SiO2
1        06 00 29 00 00 00 04 00 00 00  P2O5
1        06 00 27 00 00 00 03 00 00 00  SO3
1        06 00 27 00 00 00 03 00 00 00  K2O
1        06 00 27 00 00 00 03 00 00 00  CaO
1        06 00 29 00 00 00 04 00 00 00  TiO2
1        06 00 29 00 00 00 04 00 00 00  V2O5
1        06 00 2B 00 00 00 05 00 00 00  Cr2O3
1        06 00 27 00 00 00 03 00 00 00  MnO
1        06 00 2B 00 00 00 05 00 00 00  Fe2O3
1        06 00 27 00 00 00 03 00 00 00  CoO
1        06 00 27 00 00 00 03 00 00 00  NiO
1        06 00 27 00 00 00 03 00 00 00  CuO
1        06 00 27 00 00 00 03 00 00 00  ZnO
1        06 00 2B 00 00 00 05 00 00 00  Sb2O3
1        06 00 27 00 00 00 03 00 00 00  BaO8
1        06 00 27 00 00 00 03 00 00 00  PbOR  
8        06 00 23 00 00 00 01 00 00 00  V
8        06 00 25 00 00 00 02 00 00 00  C
8        06 00 25 00 00 00 02 00 00 00  Mn
8        06 00 25 00 00 00 02 00 00 00  Fe
8        06 00 25 00 00 00 02 00 00 00  Co
8        06 00 25 00 00 00 02 00 00 00  Ni
8        06 00 25 00 00 00 02 00 00 00  Cu
8        06 00 25 00 00 00 02 00 00 00  Zn
8        06 00 25 00 00 00 02 00 00 00  Ga
8        06 00 25 00 00 00 02 00 00 00  HfH
8        06 00 25 00 00 00 02 00 00 00  TaI
8        06 00 23 00 00 00 01 00 00 00  WJ
8        06 00 25 00 00 00 02 00 00 00  TlQ
174      06 00 23 00 00 00 01 00 00 00  P
174      06 00 23 00 00 00 01 00 00 00  S
174      06 00 25 00 00 00 02 00 00 00  Cl
```

#### Reading packets
Separating the readings into "packets" by using the previous inter-reading strings as breaks yields the following example hex strings.

1 & 206, Al2O3, 39 bytes:
```
00 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D 0E 0F 10 11 12 13 14 15 16 17 18 19 1A 1B 1C 1D 1E 1F 20 21 22 23 24 25 26 27
 A     l     2     O     3                   ( float32  |  float32 ) ( float32 )
41 00 6C 00 32 00 4F 00 33 00 0D 00 00 00 02 FD 2F 2C 41 FD 2F 2C 41 EB 55 6B 3E 00 00 00 00 00 00 00 00 00 00 00 00 00
41 00 6C 00 32 00 4F 00 33 00 0D 00 00 00 02 C8 4B C2 40 C8 4B C2 40 0A 0A D0 3C 00 00 00 00 00 00 00 00 00 00 00 00 00
```

1 & 206, MgO, 34 bytes:
```
00 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D 0E 0F 10 11 12 13 14 15 16 17 18 19 1A 1B 1C 1D 1E 1F 20 21 22
 M     g     O                   ( float32  |  float32 ) ( float32 )
4D 00 67 00 4F 00 0C 00 00 00 02 70 C1 09 40 70 C1 09 40 EC 08 E2 3E 00 00 00 00 00 00 00 00 00 00 00 00
4D 00 67 00 4F 00 0C 00 00 00 02 00 00 00 00 00 00 00 00 AE CE 37 3D 00 00 00 00 00 00 00 00 00 00 00 00
```

8 & 174, Ti, 33 bytes:
```
00 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D 0E 0F 10 11 12 13 14 15 16 17 18 19 1A 1B 1C 1D 1E 1F 20
 T     i                   ( float32  |  float32 ) ( float32 )
54 00 69 00 16 00 00 00 01 24 6D BF 3C 24 6D BF 3C 93 10 D6 3B 00 00 00 00 00 00 00 00 00 00 00 00
54 00 69 00 16 00 00 00 02 36 FA E4 3C 36 FA E4 3C 29 5E 22 3B 00 00 00 00 00 00 00 00 00 00 00 00
```

8 & 174 & 12, V, 31 bytes:
```
00 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D 0E 0F 10 11 12 13 14 15 16 17 18 19 1A 1B 1C 1D 1E
 V                   ( float32  |  float32 ) ( float32 )
56 00 17 00 00 00 01 08 51 2A 3D 08 51 2A 3D 73 BA 15 3C 00 00 00 00 00 00 00 00 00 00 00 00
56 00 17 00 00 00 02 59 43 37 3B 59 43 37 3B 43 BB BF 3A 00 00 00 00 00 00 00 00 00 00 00 00
56 00 17 00 00 00 02 00 00 00 00 00 00 00 00 7B A1 35 39 00 00 00 00 00 00 00 00 00 00 00 00
```

### Footer

| ID  | Test           | Filename                   |
|-----|----------------|----------------------------|
| 1   | Glassmajors    | `00001-GLASSMAJORS.pdz`    |
| 8   | GeoExploration | `00008-GeoExploration.pdz` |
| 12  | GeoMining      | `00012-GeoMining.pdz`      |
| 174 | GeoExploration | `00174-GeoExploration.pdz` |
| 206 | Glassmajors    | `00206-GLASSMAJORS.pdz`    |

The following 54-byte hex strings occur near the end of each PDZ file, immediately preceeding the keyword-apparent `Operator`:
```
1    00 00 07 00 22 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 CD CC 4C 3D 00 00 00 00 00 00 09 00 66 00 00 00 05 00 08 00 00 00
206  00 00 07 00 22 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 CD CC 4C 3D 00 00 00 00 00 00 09 00 7E 00 00 00 05 00 08 00 00 00
8    00 00 07 00 22 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 CD CC 4C 3D 00 00 00 00 00 00 09 00 66 00 00 00 05 00 08 00 00 00
174  00 00 07 00 22 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 CD CC 4C 3D 00 00 00 00 00 00 09 00 7C 00 00 00 05 00 08 00 00 00
12   00 00 07 00 22 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 CD CC 4C 3D 00 00 00 00 00 00 09 00 66 00 00 00 05 00 08 00 00 00
```
Although, in order to keep the 12 bytes of 0x00 at the end of each reading, we should start at 0x07
