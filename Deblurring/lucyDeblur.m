function outputImg = lucyDeblur(inputImage)

if nargin ~= 1
    error('Invalid number of input arguments!');
    pause
end

PSF = fspecial('gaussian', 5, 5);

outputImg = deconvlucy(inputImage, PSF, 15);
% outputImg = deconvlucy(inputImage, PSF, 10);
% Third parameter is the number of iterations (10 is the default)