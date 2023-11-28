from machine import Pin, ADC
import utime


# Analog to Digital Convertor Pin allows us to read analog votage value
adc_pin = Pin(26)

# Charging Pin for our capacitor
charging_pin = Pin(17, Pin.OUT, value=0)
adc = ADC(adc_pin)


# Charges and discharges the capacitor for a certain number of cycles, and returns the mean cycle time
def measure_mean_cycle_time(cycles):
    """
    Measure the mean cycle time of charging and discharging a capacitor.

    Parameters:
    - cycles: Number of cycles to perform.

    Returns:
    - The mean cycle time.
    """
    charge_discharge_times = []
    while len(charge_discharge_times) < cycles:
        charging_pin.value(1)
        charge_start_time = utime.ticks_us()        # Begin charge timer
        if adc.read_u16() >= 65535 * .9:            # below 90% of ADC range (0-65535)
            charge_time = utime.ticks_diff(utime.ticks_us(), charge_start_time)
            charging_pin.value(0)
            discharge_start_time = utime.ticks_us() # Begin discharge timer
            while adc.read_u16() >= 65535 * .1:
                pass
            discharge_time = utime.ticks_diff(utime.ticks_us(), discharge_start_time) # Calculate discharge time
            charge_discharge_times.append(charge_time + discharge_time)
            
    if charge_discharge_times:  # Make sure list is not empty to avoid division by zero
        charge_discharge_mean = sum(charge_discharge_times) / len(charge_discharge_times)
        return charge_discharge_mean
    else:
        return 0
    

def calculate_depth(cycle_time):
    """
    Calculate the depth based on the cycle time, and the depth equation
    which we determined based on our calibration data 
    """
    depth = (cycle_time - 470) / 15.37
    return depth

if __name__ == "__main__":
    cycles_to_measure = 100  # Adjust as needed
    # Calculate the mean cycle time
    mean_cycle_time = measure_mean_cycle_time(cycles_to_measure)
    print(f"Mean Cycle Time: {mean_cycle_time:.2f} μs")

    # Calculate depth based on the mean cycle time
    depth = calculate_depth(mean_cycle_time)
    print(f"Calculated Depth: {depth:.2f} cm")
