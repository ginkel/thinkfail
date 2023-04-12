# thinkfail

A very tiny Python script to prove that Lenovo's ThinkPad P1 Gen 5 and X1 Extreme Edition Gen 5 lose key-presses under certain load situations when using the built-in keyboard.

## Usage

Start `thinkfail.py` and keep hitting ENTER at a constant (rather fast) rate. Aim for a keystroke interval of less than 300 ms.

Eventually, notice that multiple keystrokes are lost. The script will inform you when that happens (determined by the fact that the interval between keystrokes radically changes). this seems to happen correlated to the fan turning on.

## Affected Hardware

The affected hardware I know about is using an Intel iGPU and a Chicony keyboard.
