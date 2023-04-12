# thinkfail

A very tiny Python script to prove that Lenovo's P1 Gen 5 and X1 Extreme Edition Gen 5 lose key-presses under certain load situations.

## Usage

Start `thinkfail.py` and keep hitting ENTER at a constant rate. When the fan's state changes, notice that multiple keystrokes are lost. The script will inform you when that happens (determined by the fact that the interval between keystrokes changes).

## Affected Hardware

The affected hardware I know about is using an Intel iGPU.
