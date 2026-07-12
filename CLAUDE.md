# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

A collection of **PSeInt** pseudocode exercises. PSeInt is an educational tool that
interprets Spanish-language structured pseudocode (`.psc` files). Each file is a
standalone algorithm — there is no build system, package manager, or shared library.

## Running

`.psc` files are meant to be opened and executed in the PSeInt IDE (or its CLI
`pseint`), which handles interpretation, flowchart generation, and interactive
console I/O. There are no tests, linters, or build steps in this repo.

## Language conventions

Code is written in PSeInt's Spanish keyword syntax. Match the existing style when
editing:

- Algorithm wrapper: `Algoritmo <Nombre>` ... `FinAlgoritmo`.
- Declarations: `Definir <var> Como Entero|Real`, arrays via `Dimension nombre[N]`.
- **Array indices are 1-based** (see `array.psc`: loops run `Para i <- 1 Hasta 5`).
- Assignment uses `<-`; I/O uses `Escribir` (print) and `Leer` (read).
- Control flow: `Para`/`FinPara`, `Mientras`/`FinMientras`, `Si`/`FinSi`.
- Body is indented one tab inside the `Algoritmo` block.
- Keep prompts and messages in Spanish, consistent with existing files.
