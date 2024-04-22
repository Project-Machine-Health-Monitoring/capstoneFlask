fs = 20000;          % Sample Rate (Hz)

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
ipf = fGear;

fImpact = 6000;
tImpact = 0:1/fs:2.5e-4-1/fs; 
xImpact = sin(2*pi*fImpact*tImpact)/3;
xComb = zeros(size(t));

Ind = (0.25*fs/fMesh):(fs/fPin*Np/Ng):length(t);
Ind = round(Ind);
xComb(Ind) = 1;

xPer = 2*conv(xComb,xImpact,'same');

vFault = vNoFault + xPer;

vNoFaultNoisy = vNoFault + randn(size(t))/5;
vFaultNoisy = vFault + randn(size(t))/5;

subplot(2,1,1)
plot(t,vNoFaultNoisy)
xlabel('Time (s)')
ylabel('Acceleration')
xlim([0.0 0.3])
ylim([-2.5 2.5])
title('Noisy Signal for Healthy Gear')


subplot(2,1,2)
plot(t,vFaultNoisy)
xlabel('Time (s)')
ylabel('Acceleration')
xlim([0.0 0.3])
ylim([-2.5 2.5])
title('Noisy Signal for Faulty Gear')
hold on
MarkX = t(Ind(1:3));
MarkY = 2.5;
plot(MarkX,MarkY,'rv','MarkerFaceColor','red')
hold off
