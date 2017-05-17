% Get png file in current folder (should only be one image)
file = dir('*.png');

% Get input image
img = im2double(imread(file.name));

% BLURRING STEP
answer = blurringMenu(file.name);
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
        error('Invalid option! Choose a valid one...\n\n');
        answer = blurringMenu(file.name);
end

% Number of columns in the figure display
col = 2;

if isBlurred
    col = 3;
    fprintf('Success in blurring image!');
    subplot(1,col,1); imshow(img); title('Input');
    subplot(1,col,2); imshow(blurredImage); title('Blurred');
else
    subplot(1,col,1); imshow(img); title('Input');
end

% DEBLURRING STEP
answer = deblurringMenu;
switch answer
    case 1
        % Wiener Filter
        deblurredImage = wienerDeblur(blurredImage);
    otherwise
        error('Invalid option! Choose a valid one...\n\n');
        answer = deblurringMenu();
end

subplot(1,col,col); imshow(deblurredImage); title('Deblurred');