function outputImg = gaussianBlur(inputImg, stdDev)
% Gaussian Blur
%
% DESCRIPTION:
%     Applies gaussian blur in an image with given standard deviation.
%
% INPUT:
%     inputImg --> Image to be blurred
%     stdDev --> Standard deviation for gaussian filter
%
% OUTPUT:
%     outputImg --> Blurred image

if nargin == 1
    stdDev = 2;
elseif nargin > 2 | nargin < 1
    error('Invalid number of input arguments!');
    pause
end

% Blurs the image with gaussian filter (std deviation: 2)
outputImg = imgaussfilt(inputImg, stdDev);
% The greater is the std deviation, the more blurred the image