# thinkfail

A very tiny Python script to prove that Lenovo's ThinkPad P1 Gen {4,5} and X1 Extreme Edition Gen {4,5} lose key-presses under certain load situations when using the built-in keyboard.

## Usage

Start `thinkfail.py` and keep hitting ENTER at a constant (rather fast) rate. Aim for a keystroke interval of less than 300 ms.

Eventually, notice that multiple keystrokes are lost. The script will inform you when that happens (determined by the fact that the interval between keystrokes radically changes).

When a keystroke is missed this will look like this:

```
$ ./thinkfail.py
Hit the ENTER key (or another key of your choice) until eventually a missed keystroke is detected. Aim for at least four keystrokes per second.

Hit Ctrl+C to abort.
16:31:59.976066: Time difference between key presses: 0.72 seconds - did we miss a keystroke?
```

## Prerequisites

Running `thinkfail.py` requires Python 3 to be installed. Running it from a [Kubuntu 22.04 Live USB image](https://cdimage.ubuntu.com/kubuntu/releases/22.04.2/release/kubuntu-22.04.2-desktop-amd64.iso) works just fine and can reliably reproduce the issue with my hardware.

Connecting a power adapter and producing some slight CPU load (just let one or two video streams run in the background in Firefox) seems to be helpful to increase the probability of the issue happening.

## Affected Hardware

The affected hardware seem to be X1E4 and P1G5 with an Intel iGPU and a Chicony keyboard. Chances are high that the issue also applies to P1G4 and X1E5.
