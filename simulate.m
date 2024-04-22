function [vFaultNoisy, vNoFaultNoisy] = simulateGearFault()

    fs = 1000;          % Sample Rate (Hz)

    Np = 13;            % Number of teeth on pinion
    Ng = 35;            % Number of teeth on gear

    fPin = 22.5;        % Pinion (Input) shaft frequency (Hz)
    fGear = fPin*Np/Ng; % Gear (Output) shaft frequency (Hz)

    fMesh = fPin*Np;    % Gear Mesh frequency (Hz)
    t = 0:1/fs:20-1/fs;

    vfIn = 0.4*sin(2*pi*fPin*t);    % Pinion waveform     
    vfOut = 0.2*sin(2*pi*fPin*Np/Ng*t);  % Gear waveform

    vMesh = sin(2*pi*fPin*Np*t);      % Gear-mesh waveform

    vNoFault = vfIn + vfOut + vMesh;
    fImpact = 2000
    tImpact = 0:1/fs:2.5e-4-1/fs; 
    xImpact = sin(2*pi*fImpact*tImpact)/3;
    xComb = zeros(size(t));

    Ind = (0.25*fs/fMesh):(fs/fPin*Np/Ng):length(t);
    Ind = round(Ind);
    xComb(Ind) = 1;

    xPer = 2*conv(xComb,xImpact,'same');

    vFault = vNoFault + xPer;

    vNoFaultNoisy = vNoFault + randn(size(t))/5;
    vFaultNoisy = vFault + randn(size(t))/5 + 02.3*sin(2*pi*45*t)+ 07.9*sin(2*pi*200*t) + 01.9*sin(2*pi*430*t) + 07.9*sin(2*pi*450*t);



end