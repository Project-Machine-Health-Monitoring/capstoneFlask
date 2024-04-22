def isGearFaulty(x, y, z, ffx, ffy, ffz, tsa_data_x, tsa_data_y, tsa_data_z):
    # Check 1: Abnormal vibration
    accel_threshold = 15
    for accel_value in [x, y, z]:
        for value in accel_value:
            if abs(value) > accel_threshold:
                return True
    
    # Check 2: Unusual dominant frequency
    dominant_freq_threshold = 15
    for freq_amplitude in [ffx.items(), ffy.items(), ffz.items()]:
        for frequency, amplitude in freq_amplitude:
            if abs(amplitude) > dominant_freq_threshold:
                return True
    print("tsaddddddddDdddddddd")
    print(tsa_data_x[0].values())
    # Check 3: TSA data analysis for x-axis
    average_amplitude_x = sum(tsa_data_x[0].values()) / len(tsa_data_x)
    threshold_multiplier = 10
    for phase, amplitude in tsa_data_x[0].items():
        if amplitude > average_amplitude_x * threshold_multiplier:
            return True
    
    # Check 4: TSA data analysis for y-axis
    average_amplitude_y = sum(tsa_data_y[0].values()) / len(tsa_data_y)
    for phase, amplitude in tsa_data_y[0].items():
        if amplitude > average_amplitude_y * threshold_multiplier:
            return True
    
    # Check 5: TSA data analysis for z-axis
    average_amplitude_z = sum(tsa_data_z[0].values()) / len(tsa_data_z)
    for phase, amplitude in tsa_data_z[0].items():
        if amplitude > average_amplitude_z * threshold_multiplier:
            return True
    
    # All checks passed, gear is not faulty
    return False