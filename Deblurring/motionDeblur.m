function outputImg = motionDeblur(inputImage, LEN, THETA)
% Motion Deblur using Wiener deconvolution
%
% DESCRIPTION:
%     Applies a deconvolution for wiener filter using exact NSR
%     (Noise-to-Signal-power Ratio).
%
% INPUT:
%     inputImg --> Image to be deblurred
%     LEN --> the number of pixels to aproximate the linear motion of a camera
%     THETA --> the angle in a clockwise direction of the simulation
%
% OUTPUT:
%     outputImg --> Blurred image

if nargin == 1
    LEN = 21; %21
    THETA = 11; %11
elseif nargin == 2
    THETA = 11;
elseif nargin > 3 | nargin < 1
    error('Invalid number of input arguments!');
    pause
end

PSF = fspecial('motion', LEN, THETA);
outputImg = deconvwnr(inputImage, PSF, 0);