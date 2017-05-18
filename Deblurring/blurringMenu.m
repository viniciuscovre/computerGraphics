function [isBlurred, blurredImage] = blurringMenu(fileName, img)
% Menu with the options to blur the input image

fprintf('\n--> BLURRING STEP');
fprintf('\nSelect the type of blur for %s:\n', fileName);
fprintf('\n  1 - Gaussian Blur');
fprintf('\n  2 - Motion Blur Simulation');
fprintf('\n  3 - Skip blurring step');
answer = input('\n\nAnswer: ');

isBlurred = true;
switch answer
    case 1
        % Gaussian Blur
        blurredImage = gaussianBlur(img);
    case 2
        % Motion Blur
        blurredImage = motionBlur(img);
    case 3
        blurredImage = img;
        isBlurred = false;
    otherwise
        fprintf('Invalid option! Choose a valid one...\n');
        [isBlurred, blurredImage] = blurringMenu(fileName, img);
end