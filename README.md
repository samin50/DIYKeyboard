## Current Design:

<img src="imgs/keyboard-layout.png" width=500>

XC9148 step-up converter is ~95% efficient. (5V @ 400mA)

## Components used:
~~nRF52840:~~
- Abondoned due to difficult-to-solder aQFN73 package, QFN40 loses USB pins.
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

XC9291:
- Takes variable voltage of battery and USB-C and fixes to 3.3V for peripherals and nRF52840.
- ~90% efficient. TPS62840 is ~91-95% efficient. (Vout = 3.3V @ 10mA)

XC9291:
- Takes variable voltage of battery and USB-C and fixes to 5V for LEDs.
- ~95% efficient. (5V @ 400mA)