% Get png file in current folder (should only be one image)
file = dir('*.png');

% Get input image
img = im2double(imread(file.name));

% BLURRING STEP
[isBlurred, blurredImage] = blurringMenu(file.name, img);

% Number of columns in the figure display
col = 2;
if isBlurred
    col = 3;
    fprintf('Success in blurring image!\n');
    subplot(1,col,1); imshow(img); title('Input');
    subplot(1,col,2); imshow(blurredImage); title('Blurred');
else
    fprintf('No blurring applied!\n');
    subplot(1,col,1); imshow(img); title('Input');
end

fprintf('\n**********************************************\n')

% DEBLURRING STEP
deblurredImage = deblurringMenu(blurredImage);

subplot(1,col,col); imshow(deblurredImage); title('Deblurred');