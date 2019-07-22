# XRF Parser
 
Take in the files produced by the Bruger Tracer 5i handheld XRF and produce table of compounds.

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

## Description
__Unknown__: Material sample  
__Sample__: One reading from the XRF, concentration will already be a mean of the sample

### Input
- PDZ files, for one or multiple unknowns

### Process
- Select desired compounds (elements, oxides, etc.)
- Select error type (2-sigma, 3-sigma, etc.)

### Output
- Table of percent by weight with error
- Place in diagram, comparing unknowns
