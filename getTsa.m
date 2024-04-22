function [pinTSA, gearTSA, pinAmp, gearAmp] = getTsa(fs, Np, Ng, fPin, inputArray)
    fGear = fPin * Np / Ng; % Gear (Output) shaft frequency (Hz)
    
    fMesh = fPin * Np;    % Gear Mesh frequency (Hz)
    t = 0:1/fs:20-1/fs;
    
    
    inputArray = cell2mat(inputArray); % Convert cell array to numeric array

    
    % Performing Time Synchronous Averaging (TSA) for the Pinion
    tPulseIn = 0:1/fPin:max(t);
    [pinTSA, pinAmp] = tsa(inputArray, fs, tPulseIn, 'NumRotations', 10);
    
    % Performing Time Synchronous Averaging (TSA) for the Gear
    tPulseOut = 0:1/fGear:max(t);
    [gearTSA, gearAmp] = tsa(inputArray, fs, tPulseOut, 'NumRotations', 10);
    

end

