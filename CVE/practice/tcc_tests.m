#import <AVFoundation/AVFoundation.h>

int main(void) {
    @autoreleasepool {
        AVAuthorizationStatus status =
            [AVCaptureDevice authorizationStatusForMediaType:AVMediaTypeAudio];

        NSLog(@"TCC status = %ld", (long)status);

        [AVCaptureDevice requestAccessForMediaType:AVMediaTypeAudio
                                  completionHandler:^(BOOL granted) {
            NSLog(@"granted = %d", granted);
            exit(0);
        }];

        [[NSRunLoop currentRunLoop] run];
    }

    return 0;
}
