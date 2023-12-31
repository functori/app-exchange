/* ===========================================================================
 *    Licensed to the Apache Software Foundation (ASF) under one
 *    or more contributor license agreements.  See the NOTICE file
 *    distributed with this work for additional information
 *    regarding copyright ownership.  The ASF licenses this file
 *    to you under the Apache License, Version 2.0 (the
 *    "License"); you may not use this file except in compliance
 *    with the License.  You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 *    Unless required by applicable law or agreed to in writing,
 *    software distributed under the License is distributed on an
 *    "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 *    KIND, either express or implied.  See the License for the
 *    specific language governing permissions and limitations
 *    under the License.
 * ===========================================================================
 *
 *  Original source code taken from
 *  https://svn.apache.org/repos/asf/apr/apr/trunk/encoding/apr_base64.c
 *
 *  Changes by Michel Lang <michellang@gmail.com>:
 *  - Replaced char 62 ('+') with '-'
 *  - Replaced char 63 ('/') with '_'
 *  - Removed padding with '=' at the end of the string
 *  - Changed return type to void for Base64decode and Base64encode
 *
 */

#include "base64.h"

const unsigned char pr2six[256] = {
    64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64,  //
    64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64,  //
    64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 62, 64, 63,  //
    52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 64, 64, 64, 64, 64, 64,  //
    64, 0,  1,  2,  3,  4,  5,  6,  7,  8,  9,  10, 11, 12, 13, 14,  //
    15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 64, 64, 64, 64, 63,  //
    64, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40,  //
    41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 64, 64, 64, 64, 64,  //
    64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64,  //
    64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64,  //
    64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64,  //
    64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64,  //
    64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64,  //
    64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64,  //
    64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64,  //
    64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64   //
};

int base64_decode(unsigned char *bufplain,
                  size_t maxsize,
                  const unsigned char *bufcoded,
                  size_t len) {
    const unsigned char *bufin;
    unsigned char *bufout;
    size_t nprbytes = len;

    bufout = bufplain;
    bufin = bufcoded;

    if (nprbytes % 4 == 1) {
        return -1;
    } else if (nprbytes == 0) {
        return 0;
    }

    if (bufin[nprbytes - 1] == '=') {
        nprbytes--;
    }
    if (bufin[nprbytes - 1] == '=') {
        nprbytes--;
    }

    while (nprbytes > 4) {
        if (maxsize < 3) {
            return -1;
        }
        *(bufout++) = (unsigned char) (pr2six[*bufin] << 2 | pr2six[bufin[1]] >> 4);
        *(bufout++) = (unsigned char) (pr2six[bufin[1]] << 4 | pr2six[bufin[2]] >> 2);
        *(bufout++) = (unsigned char) (pr2six[bufin[2]] << 6 | pr2six[bufin[3]]);
        bufin += 4;
        nprbytes -= 4;
        maxsize -= 3;
    }

    if (nprbytes > 1) {
        if (maxsize < 1) {
            return -1;
        }
        *(bufout++) = (unsigned char) (pr2six[*bufin] << 2 | pr2six[bufin[1]] >> 4);
        maxsize--;
    }

    if (nprbytes > 2) {
        if (maxsize < 1) {
            return -1;
        }
        *(bufout++) = (unsigned char) (pr2six[bufin[1]] << 4 | pr2six[bufin[2]] >> 2);
        maxsize--;
    }

    if (nprbytes > 3) {
        if (maxsize < 1) {
            return -1;
        }
        *(bufout++) = (unsigned char) (pr2six[bufin[2]] << 6 | pr2six[bufin[3]]);
        maxsize--;
    }

    return bufout - bufplain;
}
