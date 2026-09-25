import AVFoundation
import Foundation

let status = AVCaptureDevice.authorizationStatus(for: .audio)

print("TCC status = \(status.rawValue)")

AVCaptureDevice.requestAccess(for: .audio) { granted in
    print("granted = \(granted ? 1 : 0)")
    exit(0)
}

RunLoop.current.run()


