function outputImg = gaussianBlur(inputImg, sigma)
% Gaussian Blur
%
% DESCRIPTION:
%     Applies gaussian blur in an image with given standard deviation.
%
% INPUT:
%     inputImg --> Image to be blurred
%     sigma --> Standard deviation for gaussian filter
%
% OUTPUT:
%     outputImg --> Blurred image

if nargin == 1
    sigma = 5;
elseif nargin > 2 | nargin < 1
    error('Invalid number of input arguments!');
    pause
end

% Blurs the image with gaussian filter (std deviation: 2)

% Create a 5x5 gaussian mask, considering the standard deviation (sigma)
PSF = fspecial('gaussian', 5, sigma);
% The Gaussian filter represents a point-spread function, PSF

% Filters image with the given PSF
outputImg = imfilter(inputImg, PSF, 'symmetric', 'conv');

% The greater is sigma, the more blurred the image (in x-axis)

% Sigma can also be considered in y-axis by adding another parameter. E.g.:
% outputImg = imgaussfilt(inputImg,[sigma_x sigma_y]);