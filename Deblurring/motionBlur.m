function outputImg = motionBlur(inputImg, LEN, THETA)
% Gaussian Blur
%
% DESCRIPTION:
%     Applies a simulation of motion blur in an image.
%
% INPUT:
%     inputImg --> Image to be blurred
%     LEN --> the number of pixels to aproximate the linear motion of a camera
%     THETA --> the angle in a clockwise direction of the simulation
%
% OUTPUT:
%     outputImg --> Blurred image

if nargin == 1
    LEN = 15; %21
    THETA = 11; %11
elseif nargin == 2
    THETA = 11;
elseif nargin > 3 | nargin < 1
    error('Invalid number of input arguments!');
    pause
end

PSF = fspecial('motion', LEN, THETA);
outputImg = imfilter(inputImg, PSF, 'conv', 'circular');