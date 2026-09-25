import AVFoundation
import Foundation

@main
struct MicrophoneAccess {
    static func main() async {
        let status = AVCaptureDevice.authorizationStatus(for: .audio)
        print("TCC status = \(status.rawValue)")

        let granted = await AVCaptureDevice.requestAccess(for: .audio)
        print("granted = \(granted ? 1 : 0)")
    }
}
