# Identicons
## Objectives

* Identicons should be horizontally symmetric and have two colors: background and foreground
* Background color should be consistent, while foreground color should be random and high-contrast to the background
* Identicons should render down as small as 16x16 and remain distinctly legible
* Strings-as-seeds and resulting identicons should have no obvious visual correlation 
* This library should work standalone or be importable in larger projects

## Installation and Usage
`git clone` and `pip install -r requirements`

As a simple cli tool, just call `python generate.py <size> <seed>`, and the resulting identicon will be stored at `<seed>_identicon.png`! 

As an example, `python generate.py 8 absoluteblack` creates <img src="https://github.com/absoluteblack/akkio_identicon/blob/main/absoluteblack_identicon.png?raw=true" height="32" width="32"> at `absoluteblack_identicon.png`, as shown in this repo.
