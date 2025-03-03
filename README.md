## Current Design

<img src="imgs/keyboard-layout.png" width=500>

## Components Used
~~nRF52840:~~
- Abandoned due to difficult-to-solder aQFN73 package, QFN40 loses USB pins.

nRF52833:
- BLE Enabled
- Supports I2C on any pins
- Supports USB data connection 

<img src="imgs/nrf82833%20ref.jpg" width=500>

USB6B1:
- Protects USB C line.

BQ24072:
- Handles switching between USB C power and battery power. Also manages battery charging.
- Handles setting current limit from USB-C; set to 500mA to adhere to standard.

BQ27441:
- Fuel gauge for battery, reports battery level through columb counting.
- Connects to nRF52840 via I2C.

~~XC9291:~~
- Takes variable voltage of battery and USB-C and fixes to 3.3V for peripherals and nRF52840.
- ~90% efficient. TPS62840 is ~91-95% efficient. (Vout = 3.3V @ 10mA)
- Abandoned as far too small (learnt the hard way, used in v1)

XCL240B:
- Step-down converter for 5v rail to 3v3
- Includes inductor, application circuit is very simple
- 85% efficient
- Includes CL discharge feature ensuring known output voltages

XC9248:
- Boost converter for ~3v7 battery to 5V
- ~95% efficient. (5V @ 400mA)

XCL110A
- Boost converter for ~3v7 battery to 5V
- 610mA output current 
- Includes inductor, application circuit is very simple
- 90% efficient

TPS2291
- Load switch
- Slide switch enables/disables this IC rather than actual power rail of the system for better stability

~~74AHCT1G125DCKR:~~ SN74AHCT1G125DCKR
- 4 channel level shifter, replaced for single channel level shifter for space savings
- Used to drive LEDs

~~MCP23018T~~ TCA9537DGSR
- 16 channel GPIO expander, replaced for 4 channel expander for space constraints
- Needed due to nRF528333 QDAA package not having enough GPIOs

## Hardware Used
Segger J-Link:
- Used to program nRF MCUs

## Notes


## Useful Videos
https://www.youtube.com/watch?v=M6_an34wQJk