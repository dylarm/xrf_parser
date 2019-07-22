# XRF Parser
 
Take in the files produced by the Bruger Tracer 5i handheld XRF and produce table of compounds.

[![License: Apache 2.0](https://img.shields.io/github/license/dylarm/xrf_parser.svg)](LICENSE)
[![Python 3.7](https://img.shields.io/badge/Python-3.7-blue.svg)](https://python.org/)

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)
[![Maintainability](https://api.codeclimate.com/v1/badges/b5b69702443c7e0986eb/maintainability)](https://codeclimate.com/github/dylarm/xrf_parser/maintainability)
[![codebeat badge](https://codebeat.co/badges/5d6ddbc6-93c4-497b-9624-1a50b17994ec)](https://codebeat.co/projects/github-com-dylarm-xrf_parser-master)

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
