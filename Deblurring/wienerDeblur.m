function outputImg = wienerDeblur(inputImage, LEN, THETA)
% Wiener Deblur
%
% DESCRIPTION:
%     Applies a deconvolution for wiener filter using estimated NSR
%     (Noise-to-Signal-power Ratio) and Quantized image.
%     Also good for motion deblur.
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

signal_var = var(inputImage(:));

% % Estimated NSR
% noise_var = 0.0001;
% estimated_NSR = noise_var / signal_var;

% % Quantized image and Estimated NSR
% https://www.mathworks.com/help/images/examples/deblurring-images-using-a-wiener-filter.html %

uniform_quantization_var = (1/256)^2 / 12;
estimated_NSR = uniform_quantization_var / signal_var;

PSF = fspecial('motion', LEN, THETA);
outputImg = deconvwnr(inputImage, PSF, estimated_NSR);