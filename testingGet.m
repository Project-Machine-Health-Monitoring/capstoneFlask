% Parameters
fs = 20000;  % Sampling frequency (Hz)
Np = 10;    % Number of teeth on the pinion
Ng = 20;    % Number of teeth on the gear
fPin = 100; % Pinion frequency (Hz)

% Create a sample input array (you can modify this based on your requirements)
inputArray = [1, 2, 3, 4, 5];

% Call the getTsa function
[pinTSA, gearTSA, pinAmp, gearAmp] = getTsa(fs, Np, Ng, fPin, inputArray);