% Get png file in current folder (should be only one image)
file = dir('*.png');

% Get input image
img = im2double(imread(file.name));

% % Get file name
% name = strsplit(file.name, '.');
% name = name(1);

fprintf('Select the type of blur for %s:\n', file.name);
fprintf('\n  1- Gaussian Blur');
fprintf('\n  2- Motion Blur Simulation');
fprintf('\n  3- Skip blurring step');
answer = input('\n\nAnswer: ');

switch answer
    case 1
        % Gaussian Blur
        blurredImage = gaussianBlur(img);
    case 2
        % Motion Blur
        blurredImage = motionBlur(img);
    otherwise
        goto('NO_BLUR');
end

figure, imshow(blurredImage);
title('Blurred Image');

% LABEL NO_BLUR