#include <nss/nss.h>
#include <nss/nssutil.h>
#include <nss/smime.h>
#include <nss/ssl.h>
#include "nss.h"
#include <nss.h>
#include <stdio.h>

int main() {
    SECStatus rv;
    printf("NSS version: %s\n", NSS_GetVersion());
    printf("NSSSMIME version: %s\n", NSSSMIME_GetVersion());
    printf("NSSSSL version: %s\n", NSSSSL_GetVersion());
    printf("NSSUTIL version: %s\n", NSSUTIL_GetVersion());

    rv = NSS_NoDB_Init("./tmp");
    if (rv != SECSuccess){
        printf("NSS_Init failed in directory tmp\n");
        return 1;
    }

    return 0;
}
