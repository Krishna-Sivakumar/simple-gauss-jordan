# simple-gauss-jordan

A simple Gauss-Jordan Elimination implementation written with rational number types in mind.

#### Directory Structure
```
simple-gauss-jordan
├── LICENSE
├── README.md
├── fraction.py (implements the fraction type)
└── gj.py (implements the GJE algorithm)
```

#### Tests
##### 1. To test the `Fraction` type, run:
```shell
python3 fraction.py
```

##### 2. To test the Gauss-Jordan Elimination algorithm, run:
```shell
python3 gj.py
```
The GJE algorithm is implemented within the `rref()` function. 

### Requirements
1. numpy==1.20.3

#### Motivation
Gauss-Jordan elimination with fractions sounded really cool and convenient, given that floating type errors could rear their ugly head when dealing with the elementary row operations.

So far, I haven't found bugs with the Fraction type. There could be a lot of bugs within the GJE algorithm though, so please do report them to me when you find one!
