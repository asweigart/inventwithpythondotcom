/*
 * ccwd - "Copy Current Working Directory" command
 * Copyright (c) 2008, Albert Sweigart
 * All rights reserved.
 *
 * BSD-style license:
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions are met:
 *     * Redistributions of source code must retain the above copyright
 *       notice, this list of conditions and the following disclaimer.
 *     * Redistributions in binary form must reproduce the above copyright
 *       notice, this list of conditions and the following disclaimer in the
 *       documentation and/or other materials provided with the distribution.
 *     * Neither the name of the ccwd nor the
 *       names of its contributors may be used to endorse or promote products
 *       derived from this software without specific prior written permission.
 *
 * THIS SOFTWARE IS PROVIDED BY Albert Sweigart ``AS IS'' AND ANY
 * EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
 * WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
 * DISCLAIMED. IN NO EVENT SHALL Albert Sweigart BE LIABLE FOR ANY
 * DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
 * (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
 * LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
 * ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
 * (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
 * SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 */

#include "stdafx.h"
#include "windows.h"
#include "string.h"
#include <direct.h>

int main()
{
    LPWSTR cwdBuffer;

    // Get the current working directory:
    if( (cwdBuffer = _wgetcwd( NULL, 0 )) == NULL )
        return 1;

    DWORD len = wcslen(cwdBuffer);
    HGLOBAL hdst;
    LPWSTR dst;

    // Allocate string for cwd
    hdst = GlobalAlloc(GMEM_MOVEABLE | GMEM_DDESHARE, (len + 1) * sizeof(WCHAR));
    dst = (LPWSTR)GlobalLock(hdst);
    memcpy(dst, cwdBuffer, len * sizeof(WCHAR));
    dst[len] = 0;
    GlobalUnlock(hdst);

    // Set clipboard data
    if (!OpenClipboard(NULL)) return GetLastError();
    EmptyClipboard();
    if (!SetClipboardData(CF_UNICODETEXT, hdst)) return GetLastError();
    CloseClipboard();

    free(cwdBuffer);
    return 0;
}