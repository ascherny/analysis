#include <windows.h>

__declspec(dllexport)
PVOID
WINAPI
MyVirtualAllocRw(
    _In_ SIZE_T Size
) {
    return VirtualAlloc(NULL, Size, (MEM_COMMIT | MEM_RESERVE), PAGE_READWRITE);
}

__declspec(dllexport)
PVOID
WINAPI
MyVirtualAllocRo(
    _In_ SIZE_T Size
) {
    return VirtualAlloc(NULL, Size, (MEM_COMMIT | MEM_RESERVE), PAGE_READONLY);
}

__declspec(dllexport)
PVOID
WINAPI
MyVirtualAllocRwx(
    _In_ SIZE_T Size
) {
    return VirtualAlloc(NULL, Size, (MEM_COMMIT | MEM_RESERVE), PAGE_EXECUTE_READWRITE);
}

VOID
WINAPI
AllocateAndWrite(
    VOID
) {
    PVOID Memory = VirtualAlloc(NULL, 0x1000, (MEM_COMMIT | MEM_RESERVE), PAGE_READWRITE);
    if(Memory == NULL)
        return;

    memset(Memory, 0x41, 0x1000);
}

BOOL
APIENTRY
DllMain(
    _In_ HMODULE hModule,
    _In_ DWORD   ul_reason_for_call,
    _In_ LPVOID lpReserved
) {
    switch (ul_reason_for_call) {
            case DLL_PROCESS_ATTACH:
                AllocateAndWrite();
            break;
            case DLL_THREAD_ATTACH:
            case DLL_THREAD_DETACH:
            case DLL_PROCESS_DETACH:
            break;
    }
    return TRUE;
}
